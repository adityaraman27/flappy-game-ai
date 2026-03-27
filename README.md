
#  Flappy Bird AI 

##  Project Overview

This project is an implementation of an Artificial Intelligence agent that learns to play the Flappy Bird game using the NEAT (NeuroEvolution of Augmenting Topologies) algorithm.

Instead of manually coding rules, the AI evolves over generations and improves its performance by learning how to avoid obstacles and maximize score.



##  Problem Statement

Flappy Bird is a simple yet challenging game that requires precise timing and decision-making. The problem addressed in this project is:

Can an AI agent learn to play Flappy Bird efficiently without being explicitly programmed?

This project explores how machine learning, specifically neuroevolution, can be applied to solve real-time decision-making problems.



##  Solution Approach

The solution uses the NEAT algorithm to evolve neural networks that control the bird's actions.

### Key Concepts Used:

* Neural Networks
* Genetic Algorithms
* Reinforcement Learning (reward-based learning)
* Game Simulation using Pygame

### How it Works:

1. A population of birds is created.
2. Each bird is controlled by a neural network.
3. Birds receive inputs like:

   * Bird's vertical position
   * Distance from pipe gap
4. Based on outputs, the bird decides whether to jump.
5. Fitness is assigned based on:

   * Survival time
   * Pipes successfully passed
6. The best-performing birds evolve into the next generation.

---

## 🧠 Features

* ✅ AI learns automatically (no hardcoding)
* 📈 Live training graph (Score vs Generation)
* 🎮 Real-time game simulation
* ⚡ Lightweight and fast training
* 🧬 Evolution-based learning using NEAT

---

## 🛠️ Technologies Used

* Python
* Pygame
* NEAT-Python
* Matplotlib

---

## 📂 Project Structure

```
FLAPPY/
│── train.py          # Main training script
│── neat_config.txt   # NEAT configuration file
│── bird.png          # Bird image
│── pipe.png          # Pipe image
│── bg.png            # Background image
│── README.md         # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flappy-ai.git
cd flappy-ai
```

### 2. Install Dependencies

```bash
pip install pygame neat-python matplotlib
```

### 3. Run the Project

```bash
python train.py
```

---

## ▶️ How to Use

* Run the script and the training will start automatically.
* A game window will open showing birds playing.
* A graph window will display training progress.
* Over time, the AI improves and achieves higher scores.

---

## 📊 Output

* Real-time gameplay window
* Training graph showing improvement
* Console logs of generation-wise scores

---

## 🚧 Challenges Faced

* Initial AI behavior was random and ineffective
* Fitness function tuning was required
* Graph visualization issues during training
* Balancing game difficulty for learning

---

## 📈 Learning Outcomes

* Understanding of NEAT algorithm
* Practical implementation of AI in games
* Experience with real-time training visualization
* Debugging and optimizing ML systems

---

## 🔮 Future Improvements

* Save and replay the best trained model
* Add sound effects and better UI
* Optimize training speed
* Deploy as a web-based game

---

## 📌 Conclusion

This project demonstrates how AI can learn complex behaviors through evolution rather than explicit programming. It highlights the power of combining machine learning with game development.

---

## 👨‍💻 Author

Aditya Raman

---

## ⭐ Acknowledgment

This project was developed as part of the **Bring Your Own Project (BYOP)** under the course *Fundamentals of AI and ML*.
