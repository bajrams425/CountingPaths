'''
Counting Paths Problem

Description:

Imagine you are standing on the point (0, 0) of the coordinate system and you
want to reach the point (X, Y) - that is, the point X steps east and Y steps
north from your current location.
You move by taking steps. Each step must lead either east or north.
Moving east means increasing the x-coordinate value. If you take a step east,
you move to the right on the plane.
Moving north means increasing the y-coordinate value. If you take a step
north, you move upwards on the plane.
Write a program to count all valid ways of reaching the goal.

Optional:
    ● Along your way, you are not allowed to take exactly three steps in a
row in the same direction. Fewer is good, more is also good, only
exactly three is bad.
    ● Along with counting the number of valid ways, print the routes taken
for each valid path.

Constraints:
    ● X will be between 0 and 1000, inclusive.
    ● Y will be between 0 and 1000, inclusive.

NOTE: There are two special solution cases to be handled-
1. If the starting and ending point are the same thus an empty path solution.
2. If the last 3 moves when going to the finish line are the same direction.
'''

# Importing libraries
import tkinter as tk
from tkinter import messagebox

# Solutions will be saved here
valid_routes = []


def find_path(starting_X_coordinate, starting_Y_coordinate, ending_X_coordinate, ending_Y_coordinate, current_path):
    # Recursive function that will find all the possible routes

    # First things first, we need to check if we reached destination
    if starting_X_coordinate == ending_X_coordinate and starting_Y_coordinate == ending_Y_coordinate:
        # We need to check special case number 2:
        if (current_path[-3:] != ['E', 'E', 'E'] and current_path[-3:] != ['N', 'N', 'N']) or (current_path[-4:] == ['E', 'E', 'E', 'E'] or current_path[-4:] == ['N', 'N', 'N', 'N']):
            valid_routes.append(current_path[:])
            return

    # Next we need to check the last 3 moves to ensure we MUST go that way once more
    # But only if we passed 3 times, 4 or more is okay
    if current_path[-3:] == ['E', 'E', 'E'] and current_path[-4:] != ['E', 'E', 'E', 'E']:
        if starting_X_coordinate < ending_X_coordinate:
            find_path(starting_X_coordinate+1, starting_Y_coordinate,
                      ending_X_coordinate, ending_Y_coordinate, current_path + ['E'])
        return

    # We do the same to check if we moved North the last 3 times only:
    if current_path[-3:] == ['N', 'N', 'N'] and current_path[-4:] != ['N', 'N', 'N', 'N']:
        if starting_Y_coordinate < ending_Y_coordinate:
            find_path(starting_X_coordinate, starting_Y_coordinate+1,
                      ending_X_coordinate, ending_Y_coordinate, current_path + ['N'])
        return

    # Now we continue with the regular conditions of moving east/north
    # First we check if we can go East
    if starting_X_coordinate < ending_X_coordinate:
        find_path(starting_X_coordinate+1, starting_Y_coordinate,
                  ending_X_coordinate, ending_Y_coordinate, current_path + ['E'])

    # And then we check if we can go North
    if starting_Y_coordinate < ending_Y_coordinate:
        find_path(starting_X_coordinate, starting_Y_coordinate+1,
                  ending_X_coordinate, ending_Y_coordinate, current_path + ['N'])


def main():
    # Main function that will be executed
    # Clear the field and reset the global array solution
    solution_area.delete(1.0, tk.END)
    global valid_routes
    valid_routes = []
    try:
        # User input
        x = int(x_input.get())
        y = int(y_input.get())
        if 0 <= x <= 1000 and 0 <= y <= 1000:
            find_path(0, 0, int(x), int(y), [])
            if not valid_routes:
                solution_area.insert(tk.END, 'No possible path was found!\n')
            elif not valid_routes[0]:
                solution_area.insert(
                    tk.END, '1 solution found: Take no steps...\n')
            else:
                solution_area.insert(
                    tk.END, f'{len(valid_routes)} solution/s found.\n')
                for indx, path in enumerate(valid_routes, 1):
                    solution_area.insert(
                        tk.END, f'Path {indx}: {"".join(path)}\n')
        else:
            messagebox.showerror(
                "Error", "Coordinates must be between 0 and 1000!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid coordinates!")


# Creating main tkinter window
root = tk.Tk()
root.title("Counting Paths Problem with interface")
# Labels
tk.Label(root, text="X Coordinate (0-1000)").pack(pady=5)
x_input = tk.Entry(root)
x_input.pack(pady=5)

tk.Label(root, text="Y Coordinate (0-1000)").pack(pady=5)
y_input = tk.Entry(root)
y_input.pack(pady=5)

# Button to calculate paths
btn = tk.Button(root, text="Find Paths", command=main)
btn.pack(pady=5)

# Text area to show the solutions
solution_area = tk.Text(root, width=50, height=15)
solution_area.pack(pady=10)

root.mainloop()
