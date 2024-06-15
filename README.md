## Same distance simulation

This repository contains the code for the same distance simulation project. It is a simple geometrical idea, and I am playing around, trying
to find effective algorithms to solve it as best as possible.

The efficiency of the algorithm is measured by a score. The score is calculated by the sum of the distances between the points and their partners.
If you have any ideas for good algorithms, please fork the repository and create a pull request.

# General Concept
A number n of points is created, every point has a position x and y. 
Each point chooses freely (randomly) two other points. 
The goal is to move the points in a way, so that they all have the same distance from their partners.

# Future Increments

The project is still in the early stages of development. The following increments are planned for the future:

1. Test different algorithms to find the most efficient one, and implement it.
2. Possibly a simple ML model to predict the best parameters for different algorithms.
3. Make the algorithms race under different conditions (size of the grid, number of points, etc.).

# How to use this project

To use this project, do this:

1. Clone the repository to your local machine.
2. Install the required packages by running the following command in the terminal:
```bash
pip install -r requirements.txt
```
3. Run the __main__.py file to start the simulation. Run the following command in the terminal:
```bash
python3 src\__main__.py
```
4. The simulation will run and the score will be printed to the console. The goal is to have the final score as low as possible.
