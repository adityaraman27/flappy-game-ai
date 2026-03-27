import pygame
import neat
import os
import random
import matplotlib.pyplot as plt

WIN_WIDTH = 500
WIN_HEIGHT = 800

PIPE_GAP = 200
PIPE_VEL = 3

GEN = 0
score_history = []

pygame.init()
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Flappy AI")

def load_and_scale(name, size):
    path = os.path.join(os.path.dirname(__file__), name)
    if os.path.exists(path):
        img = pygame.image.load(path)
        return pygame.transform.scale(img, size)
    return None

BIRD_IMG = load_and_scale("bird.png", (40, 30))
PIPE_IMG = load_and_scale("pipe.png", (80, 500))
BG_IMG = load_and_scale("bg.png", (500, 800))

FONT = pygame.font.SysFont("comicsans", 40)

class Bird:
    def __init__(self):
        self.x = 100
        self.y = 350
        self.vel = 0

    def jump(self):
        self.vel = -10

    def move(self):
        self.vel += 1
        self.y += self.vel

    def draw(self, win):
        if BIRD_IMG:
            win.blit(BIRD_IMG, (self.x, self.y))
        else:
            pygame.draw.circle(win, (255, 0, 0), (int(self.x), int(self.y)), 10)


class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(150, 600)
        self.bottom = self.height + PIPE_GAP
        self.passed = False

    def move(self):
        self.x -= PIPE_VEL

    def draw(self, win):
        if PIPE_IMG:
            win.blit(PIPE_IMG, (self.x, self.height - PIPE_IMG.get_height()))
            win.blit(pygame.transform.flip(PIPE_IMG, False, True), (self.x, self.bottom))
        else:
            pygame.draw.rect(win, (0, 255, 0), (self.x, 0, 80, self.height))
            pygame.draw.rect(win, (0, 255, 0), (self.x, self.bottom, 80, WIN_HEIGHT))

    def collide(self, bird):
        bird_rect = pygame.Rect(bird.x, bird.y, 40, 30)
        top_rect = pygame.Rect(self.x, 0, 80, self.height)
        bottom_rect = pygame.Rect(self.x, self.bottom, 80, WIN_HEIGHT)
        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bottom_rect)


def draw_window(win, birds, pipes, score, gen):
    if BG_IMG:
        win.blit(BG_IMG, (0, 0))
    else:
        win.fill((0, 0, 0))

    for pipe in pipes:
        pipe.draw(win)

    for bird in birds:
        bird.draw(win)

    score_text = FONT.render(f"Score: {score}", True, (255, 255, 255))
    gen_text = FONT.render(f"Gen: {gen}", True, (255, 255, 255))

    win.blit(score_text, (10, 10))
    win.blit(gen_text, (10, 50))

    pygame.display.update()

def eval_genomes(genomes, config):
    global GEN, score_history
    GEN += 1

    birds = []
    nets = []
    ge = []

    for _, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        birds.append(Bird())
        g.fitness = 0
        ge.append(g)

    pipes = [Pipe(600)]
    score = 0
    clock = pygame.time.Clock()

    while True:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if len(birds) == 0:
            break

        pipe_ind = 0
        if len(pipes) > 1 and birds[0].x > pipes[0].x + 80:
            pipe_ind = 1

        for i, bird in enumerate(birds):
            bird.move()

            
            ge[i].fitness += 0.1

            pipe = pipes[pipe_ind]

           
            inputs = (
                bird.y / WIN_HEIGHT,
                (pipe.height - bird.y) / WIN_HEIGHT,
                (pipe.bottom - bird.y) / WIN_HEIGHT,
            )

            output = nets[i].activate(inputs)

           
            if output[0] > 0.7:
                bird.jump()

        add_pipe = False
        rem = []

        for pipe in pipes:
            pipe.move()

            for i in reversed(range(len(birds))):
                if pipe.collide(birds[i]):
                    ge[i].fitness -= 1   # ❗ strong penalty
                    birds.pop(i)
                    nets.pop(i)
                    ge.pop(i)

            if pipe.x < -80:
                rem.append(pipe)

            if len(birds) > 0 and not pipe.passed and pipe.x < birds[0].x:
                pipe.passed = True
                add_pipe = True

        if add_pipe:
            score += 1
            for g in ge:
                g.fitness += 5   # ❗ reward passing pipe
            pipes.append(Pipe(600))

        for r in rem:
            pipes.remove(r)

        for i in reversed(range(len(birds))):
            if birds[i].y > WIN_HEIGHT - 10 or birds[i].y < 0:
                birds.pop(i)
                nets.pop(i)
                ge.pop(i)

        draw_window(WIN, birds, pipes, score, GEN)

    # ✅ GRAPH SCORE (NOT FITNESS)
    print(f"Generation {GEN} Score: {score}")
    score_history.append(score)

    plt.clf()
    plt.plot(score_history)
    plt.xlabel("Generation")
    plt.ylabel("Score")
    plt.title("Training Progress")
    plt.pause(0.01)

# -------- RUN --------
def run(config_path):
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path,
    )

    p = neat.Population(config)

    p.run(eval_genomes, 50)

# -------- MAIN --------
if __name__ == "__main__":
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "neat_config.txt")
    run(config_path)