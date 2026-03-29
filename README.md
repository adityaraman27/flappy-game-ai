
#  Flappy Bird AI 

##  Project Overview
This project entails the development of a program that incorporates an Artificial Intelligence agent that can learn how to play the Flappy Bird game using the NEAT algorithm.

The AI agent does not require any rules to be hardcoded. The AI agent learns how to play the Flappy Bird game by improving its performance through evolution.


##  Problem Statement

The Flappy Bird game is a simple game, but it requires a good level of intelligence to be played. The problem being solved by this project is as follows:

Can an AI agent learn how to play the Flappy Bird game efficiently without being explicitly programmed?

This project is focused on showing how a machine learning, specifically 

##  Solution Approach

The solution for this problem is the use of the NEAT algorithm, which can be used for evolving a neural network.

### Key Concepts Used:

* Neural Networks
* Genetic Algorithms
* Reinforcement Learning (Reward-Based Learning)
* Game Simulation using Pygame
  
### How it Works:

1. Population of birds is created.
2. Each bird is controlled by a neural network.
3. Each bird receives a set of inputs:
   * Bird's vertical position
   * Distance from pipe gap
     
4. Based on this information, the bird decides to jump or not.
   
5. Each bird is given fitness points based on:
   * Survival time
   * Number of pipes passed



## Features

*   AI learns by itself (No Hard Coding)
*   Live Training Graph (Score vs Generation)
*   Real Time Game Simulation
*   Lightweight and Fast Training
*   Evolutionary Learning using NEAT



##  Technologies Used

*   Python
*   Pygame
*   NEAT-Python
*   Matplotlib



##  Project Structure

###FLAPPY
─ train.py          
─ neat_config.txt   
─ bird.png          
─ pipe.png          
─ bg.png            
─ README.md        



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

* Ability to save and replay the best trained model
* Sound effects and better UI
* Optimization of training speed


##  Conclusion

This project demonstrates how AI can learn complex behaviors through evolution rather than explicit programming. It highlights the power of combining machine learning with game development.


