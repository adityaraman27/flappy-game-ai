import pygame
import random

W, H = 500, 800
PIPE_GAP = 250
PIPE_VEL = 4
BIRD_X = 100

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE  = (135, 206, 235)
YELLOW = (255, 255, 0)

pygame.font.init()
FONT = pygame.font.SysFont("arial", 30)


class Bird:
    GRAVITY = 0.3
    JUMP = -7

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vel = 0
        self.width = 30
        self.height = 30

    def jump(self):
        self.vel = self.JUMP

    def move(self):
        self.vel += self.GRAVITY
        self.vel = min(self.vel, 10)
        self.y += self.vel

    def draw(self, win):
        pygame.draw.ellipse(win, YELLOW,
                            (self.x, self.y, self.width, self.height))

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)


class Pipe:
    def __init__(self, x):
        self.x = x
        self.width = 70
        self.height = random.randrange(100, H - PIPE_GAP - 100)
        self.top = self.height
        self.bottom = self.height + PIPE_GAP

    def move(self):
        self.x -= PIPE_VEL

    def draw(self, win):
        pygame.draw.rect(win, GREEN, (self.x, 0, self.width, self.top))
        pygame.draw.rect(win, GREEN, (self.x, self.bottom, self.width, H - self.bottom))

    def collide(self, bird):
        bird_rect = bird.get_rect()
        top_rect = pygame.Rect(self.x, 0, self.width, self.top)
        bot_rect = pygame.Rect(self.x, self.bottom, self.width, H - self.bottom)
        return bird_rect.colliderect(top_rect) or bird_rect.colliderect(bot_rect)


class FlappyGame:
    def __init__(self, birds):
        self.birds = birds
        self.pipes = [Pipe(600)]
        self.scores = [0] * len(birds)
        self.alive = [True] * len(birds)

    def run_step(self, actions):
        rewards = [0] * len(self.birds)

       
        if len(self.pipes) == 0 or self.pipes[-1].x < W - 250:
            self.pipes.append(Pipe(W))

        for pipe in self.pipes:
            pipe.move()

        self.pipes = [p for p in self.pipes if p.x + p.width > 0]

        for i, bird in enumerate(self.birds):
            if not self.alive[i]:
                continue

            if actions[i]:
                bird.jump()

            bird.move()
            rewards[i] += 0.02

            # Collision
            for pipe in self.pipes:
                if pipe.collide(bird):
                    self.alive[i] = False
                    rewards[i] = -1

            # Ground/ceiling
            if bird.y + bird.height >= H or bird.y <= 0:
                self.alive[i] = False
                rewards[i] = -1

            # Score
            for pipe in self.pipes:
                if pipe.x + pipe.width < bird.x and not hasattr(pipe, f"passed_{i}"):
                    setattr(pipe, f"passed_{i}", True)
                    self.scores[i] += 1
                    rewards[i] = 1

        game_over = not any(self.alive)
        return rewards, game_over, self.scores


def draw_window(win, birds, pipes, scores, gen, alive, best_score):
    win.fill(BLUE)

    for pipe in pipes:
        pipe.draw(win)

    for i, bird in enumerate(birds):
        if alive[i]:
            bird.draw(win)

    pygame.draw.rect(win, (0, 0, 0), (0, 0, 210, 160))
    pygame.draw.rect(win, WHITE, (0, 0, 210, 160), 2)

    gen_text = FONT.render(f"Gen    : {gen}", True, WHITE)
    alive_text = FONT.render(f"Alive  : {sum(alive)}", True, WHITE)
    best_text = FONT.render(f"Best   : {best_score}", True, WHITE)
    curr_text = FONT.render(f"Score  : {max(scores)}", True, WHITE)

    win.blit(gen_text, (10, 10))
    win.blit(alive_text, (10, 45))
    win.blit(best_text, (10, 80))
    win.blit(curr_text, (10, 115))

    pygame.display.update()