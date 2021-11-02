# Dojos

## Introduction

This repository is dedicated to dojos, each python file correspond to my solution for each dojos.

## Clean the grid

The aim of this dojo is to count the number of different squares of a given grid that a robot can clean. The squares could be occupied by an obstacle. Once the robot meets a grid border or an obstacle it can only turn 90° right. The robot initial position is at the top left square of the grid, which isn't cleaned yet, looking to the right.

### Test examples

```python
grid = [
  "......", 
  "....xx", 
  "......"
]
```

The robot cleans the 6 top squares, reaches the right border, tries to turn right but meets an obstacle so turn right again. On its way back it cleans no more square 'cause everything is already clean. It reaches the left border and turn two times to get back to it's exact same position. The robot will not be able to clean more tha 6 squares in that case.

```python
result = 6
```
