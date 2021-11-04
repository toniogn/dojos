# Dojos

## Introduction

This repository is dedicated to dojos. To each dojo correspond two python files, a template for writing solution with integrated tests and my solution.

## Avoid credit (≈20min): about list

The aim of this dojo is to ensure your bank account to never be in credit delaying a minimum of expanses. Knowing the chronological list of expanses (negative values) and incomes (positive values) you have, find the minimum expanses relocation number you should do to never be in credit (i.e. the accumulated amount of expanses and incomes is always positive or zero). You can only relocate expanses and only to the end of the chronological list.

### Example

```python
operations = [3, 2, 7, -5, 1, -9, 6, -1, -2, 2]
```

In the flow of opérations when the -9 operation occurs, the accumulated sum goes to -1, relocating -9 or -5 at the end is enough to avoid credit at any time.

```python
result = 1
```

## Clean the grid (≈1h): logic object-oriented empowered

The aim of this dojo is to count the number of different squares of a given grid that a robot can clean. The squares could be occupied by an obstacle. Once the robot meets a grid border or an obstacle it can only turn 90° right. The robot initial position is at the top left square of the grid, which isn't cleaned yet, looking to the right.

### Example

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

## :anchor: Climb the lighthouse (≈15min): recursivity

This dojo challenge you to find the exact number of different paths to climb a lighthouse stairway. The only rule is that you can climb either one or two steps and you begin right before the first step and you finish on the last one.

### Example

```python
stairs_number = 3
```

With three steps you can climb each steps one by one, you can do #1 then #3 and you can do #2 then #3.

```python
results = 3
```
