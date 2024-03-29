# The_Doomed_Dice_Challenge

This project implements solutions to the Doomed Dice Challenge, which involves manipulating the configurations of two six-sided dice, Die A and Die B, while maintaining certain constraints and probabilities.

## Problem Statement

You are given two six-sided dice, Die A and Die B, each with faces numbered from 1 to 6. The challenge consists of two parts:

### Part A:
1. Calculate the total number of combinations possible when rolling both Die A and Die B together.
2. Calculate and display the distribution of all possible combinations that can be obtained when rolling both Die A and Die B together.
3. Calculate the probability of each possible sum occurring when rolling both Die A and Die B together.

### Part B:
Modify the configurations of Die A and Die B while ensuring the following conditions:
- Die A cannot have more than 4 spots on a face.
- Die A may have multiple faces with the same number of spots.
- Die B can have as many spots on a face as necessary, even more than 6.
- The probability of obtaining each sum when rolling both dice must remain the same.

## Solution Overview

### Part A:
- Implemented functions to calculate the total number of combinations, generate the distribution of combinations, and calculate probabilities for each sum.
- Utilized nested loops and data structures to represent the combinations and sums.

### Part B:
- Developed the `undoom_dice` function to redistribute spots on Die A and Die B while maintaining the same probabilities for each sum.
- Utilized scaling factors and rounding to achieve the desired configurations for Die A and Die B.
