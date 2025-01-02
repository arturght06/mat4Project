from collections import Counter
from matplotlib import pyplot as plt

def calc_probabilities(filename):
    symbols, probs = [], []
    with open(f"files/{filename}", "r") as f:
        next(f)
        symbols.extend(line.split('"')[3] for line in f)
        total = sum(Counter(symbols).values())
        probs = {key: round(value / total, len(str(total))) for key, value in Counter(symbols).items()}
        return symbols, probs


def get_message_symbols() -> list:
    message = []
    with open("files/message 25.txt", "r") as f:
        next(f)
        message.extend(line.split('"')[3] for line in f)
        # total = sum(Counter(message).values())
        # pmessage = {key: round(value / total, len(str(total))) for key, value in Counter(message).items()}
        return message

def plot(history, filename):
    x = range(len(history["L"]))
    plt.plot(x, history["L"], label="L (Latverian)", color="blue")
    plt.plot(x, history["W"], label="W (Wakandan)", color="green")
    plt.plot(x, history["S"], label="S (Symkarian)", color="red")

    # Dodanie legendy
    plt.legend()

    # Opis osi
    plt.xlabel("Iteracja")
    plt.ylabel("Prawdopodobieństwo")

    # Tytuł wykresu
    plt.title("Zmiana prawdopodobieństw dla języków")

    plt.savefig(f"plot_results/{filename}.png")
    plt.clf()