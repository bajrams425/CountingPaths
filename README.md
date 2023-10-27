# Counting Paths Problem

## Description

Imagine standing at the origin (0, 0) on a coordinate plane. The goal is to reach the point (X, Y), which is X steps to the east and Y steps to the north. The task is to determine the number of valid paths you can take to reach this point, ensuring you only move either east or north at each step.

### Constraints

* X can range from 0 to 1000 (inclusive).
* Y can range from 0 to 1000 (inclusive).

### Additional Rules

1. At no point should you take three consecutive steps in the same direction. Any number of consecutive steps other than three is valid.
2. The program should also be able to print each valid path.

### Special Cases

1. If the starting and ending points are the same, the solution would be an empty path.
2. If the final three moves in a valid path are in the same direction, it should be disregarded.

## Usage

To execute the program (prefered with python 3.10):

### CMD/BASH only
1. Copy the code from counting_paths_problem_CMD_only.py and put it in an online python compiler like https://www.programiz.com/python-programming/online-compiler/ and hit the Run button, OR;
2. Download the file counting_paths_problem_CMD_only.py and run it via:
   *python \counting_paths_problem_CMD_only.py

### Using tKinter interface
1. Download the file counting_paths_problem_with_interface.py and run it via:
   *python \counting_paths_problem_CMD_only.py
