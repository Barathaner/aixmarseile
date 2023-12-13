import sys
import random
import matplotlib.pyplot as plt

# Generates a list with N random numbers between [0, 1]
def generate_random_values(N):
    return [random.random() for _ in range(N)]

# Displays three subplots: A line plot of (n, xn), another scatter plot of (xn-1, xn), and a histogram of the random values
def display_subplots(N, values):
    plt.figure(figsize=(12, 4))

    # First subplot - changed to line plot
    plt.subplot(131)
    plt.plot(list(range(N)), values, marker=".")
    plt.title("(n, xn)")
    plt.xlabel("n")
    plt.ylabel("xn")

    # Second subplot
    plt.subplot(132)
    plt.scatter(values[:-1], values[1:], marker=".")
    plt.title("(xn-1, xn)")
    plt.xlabel("xn-1")
    plt.ylabel("xn")

    # Third subplot
    plt.subplot(133)
    plt.hist(values, bins=20, edgecolor="k")
    plt.title("Histogram of xn")
    plt.xlabel("xn")
    plt.ylabel("Count")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 this_file.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be an integer!")
        sys.exit(1)

    values = generate_random_values(N)
    display_subplots(N, values)
