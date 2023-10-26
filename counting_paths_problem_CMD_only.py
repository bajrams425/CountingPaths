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

# Solutions will be saved here
valid_routes = []


def get_coordinate(axis):
    # Function that gets the input coordinates
    while True:
        coordinate = input(
            f'Enter the {axis}-coordinate (0 to 1000, or Enter to cancel): ')
        if (coordinate.isdigit() and 0 <= int(coordinate) <= 1000) or coordinate == '':
            return coordinate
        print(f'Invalid input! Please type an integer between 0 and 1000, or press Enter to cancel.')


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
    # First we get the coordinates as an input
    x = get_coordinate("X")
    if x == '':
        print('Operation canceled, thank you and have a nice day!')
        return
    y = get_coordinate("Y")
    if y == '':
        print('Operation canceled, thank you and have a nice day!')
        return

    # Start finding the paths
    find_path(0, 0, int(x), int(y), [])

    if not valid_routes:
        print('No possible path was found!')
    # Special case 1: Empty path solution
    elif not valid_routes[0]:
        print('1 solution found: Take no steps...')
    else:
        print(f'{len(valid_routes)} solution/s found.')
        for indx, path in enumerate(valid_routes, 1):
            print(f'Path {indx}: {"".join(path)}')


# Execute main function
main()
