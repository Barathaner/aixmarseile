import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

maxgen = 10

def convertfiletogrid(filepath):
    with open(filepath, "r") as my_file:
        initialstate = my_file.read().split('\n')
    return [[int(cell) for cell in line] for line in initialstate]

def printgrid(grid):
    for line in grid:
        print(''.join(map(str, line)))

def outputtext(population):
    with open('output.txt', 'w') as file:
        for line in population:
            file.write(''.join(map(str, line)) + '\n')

def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[x])

def countaliveneighbours(grid, x, y):
    count = 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if is_valid(grid, i, j) and not (i == x and j == y) and grid[i][j] == 1:
                count += 1
    return count

def evolve(population):
    new_population = [row[:] for row in population]
    for i in range(len(population)):
        for j in range(len(population[i])):
            alive_neighbours = countaliveneighbours(population, i, j)
            if population[i][j] == 1:
                if alive_neighbours < 2 or alive_neighbours > 3:
                    new_population[i][j] = 0
            else:
                if alive_neighbours == 3:
                    new_population[i][j] = 1
    return new_population

def update(frame):
    global population
    im.set_data(population)
    population = evolve(population)
    return [im]

if __name__ == "__main__":
    while True:
        input('Press enter to start')
        option = input('Load file [l], generate [r] random grid, or exit [q]? ')
        
        if option == 'l':
            path = input('Enter file path: ')
            population = convertfiletogrid(path)
            maxgen = int(input('Enter number of generations: '))
            
        elif option == 'r':
            x, y = map(int, input('Enter the size of the grid: x,y ').split(','))
            maxgen = int(input('Enter number of generations: '))
            population = [[random.randint(0, 1) for _ in range(y)] for _ in range(x)]
            
        elif option == 'q':
            break

        # Create a matplotlib plot for animation
        fig, ax = plt.subplots()
        im = ax.imshow(population, animated=True)
        ani = FuncAnimation(fig, update, frames=maxgen, repeat=False)
        plt.show()
