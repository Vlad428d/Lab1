import matplotlib.pyplot as plt
def save_simple_plot(filename="plot.png"):
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.title("Тестовий графік")
    plt.savefig(filename)
    plt.close()
    return f"Графік збережено у {filename}"
