
#  Flappy Bird AI 

##  Project Overview
This project involves the implementation of an Artificial Intelligence agent that is able to learn how to play the Flappy Bird game using the NEAT algorithm.

The AI agent does not require any rules to be hardcoded; instead, it uses evolution to improve its performance by learning how to avoid obstacles and maximize scores.



## Problem Statement

The Flappy Bird game is a simple game but requires a good level of intelligence to be played. The problem being solved in this project is:

Can an AI agent learn how to play Flappy Bird efficiently without being explicitly programmed?

This project focuses on how machine learning, specifically 

##  Solution Approach

The solution involves using the NEAT algorithm to evolve neural networks that control the bird's actions.

### Key Concepts Used:

* Neural Networks
* Genetic Algorithms
* Reinforcement Learning (Reward-Based Learning)
* Game Simulation using Pygame
  
### How it Works:

1. Population of birds is created.
2. Each bird is controlled using a neural network.
3. Each bird receives inputs such as:
   * Bird's vertical position
   * Distance from pipe gap
     
4. Based on this information, the bird determines whether to jump or not.
   
5. Each bird is assigned fitness points based on:
   * Survival time
   * Number of pipes passed



## Features

*   AI learns by itself (no hardcoding)
*   Live training graph (Score vs Generation)
*   Real-time game simulation
*   Lightweight and fast training
*   Evolutionary learning using NEAT



##  Technologies Used

* Python
* Pygame
* NEAT-Python
* Matplotlib



##  Project Structure

FLAPPY/
│── train.py          
│── neat_config.txt   
│── bird.png          
│── pipe.png          
│── bg.png            
│── README.md        



## Installation & Setup

 1. Clone the Repository

git clone https://github.com/your-username/flappy-ai.git
cd flappy-ai

 2. Install Dependencies

pip install pygame neat-python matplotlib

3. Run the Project 

python train.py

##  How to Use

* Run the script and the training will start automatically.
* A game window will open showing birds playing.
*  A graph window will open showing training progress.
* Over time, the AI improves and achieves higher scores.


## Output

* Real-time game play window
* Training graph indicating improvement
* Console output for generation-wise scores


##  Challenges Faced

* Initial AI behavior was random and ineffective
* Tuning of fitness function
* Problems in graph visualization
* Difficulty in balancing game difficulty for AI to learn



##  Learning Outcomes

* Knowledge of NEAT algorithm
* Practical experience in implementing AI in games
* Real-time training visualization
* Debugging and optimizing AI systems


##  Future Improvements

* Save and replay the best trained model
* Add sound effects and better UI
* Optimize training speed
* Deploy as a web-based game


##  Conclusion

This project demonstrates how AI can learn complex behaviors through evolution rather than explicit programming. It highlights the power of combining machine learning with game development.


