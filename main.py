from collections import Counter

from math_calc import get_probabilities
from tools import get_message_symbols, plot

message = get_message_symbols()

history1 = get_probabilities(message, 1 / 3, 1 / 3, 1 / 3)

print("___"*30, "II część", "___"*30, end="\n\n")

print("> Trzykrotnie częściej dla L:")
history2 = get_probabilities(message, 3 / 5, 1 / 5, 1 / 5)
print("\n\n\n> Trzykrotnie częściej dla W:")
history3 = get_probabilities(message, 1 / 5, 3 / 5, 1 / 5)
print("\n\n\n> Trzykrotnie częściej dla S:")
history4 = get_probabilities(message, 1 / 5, 1 / 5, 3 / 5)

print("___"*30, "Rozwiązanie problemu - prezentacja wyniku", "___"*30, end="\n\n")

print("___"*10, "ZADANIE 1", "___"*10, end="\n\n")

print("Wykresy do zadania nr.1 zapisane do folderu plot_results")
plot(history1, "równe prawdopodobieństwa")
plot(history2, "pr-wo Lx3")
plot(history3, "pr-wo Wx3")
plot(history4, "pr-wo Sx3")

print("___"*10, "ZADANIE 4", "___"*10, end="\n\n")

print(Counter(message))
chosentwo = ["C", "D"]
message = ["N" if i not in chosentwo else i for i in message]
print(Counter(message))

history1 = get_probabilities(message, 1 / 3, 1 / 3, 1 / 3)
history2 = get_probabilities(message, 3 / 5, 1 / 5, 1 / 5)
history3 = get_probabilities(message, 1 / 5, 3 / 5, 1 / 5)
history4 = get_probabilities(message, 1 / 5, 1 / 5, 3 / 5)

plot(history1, "zad2_równe prawdopodobieństwa")
plot(history2, "zad2_pr-wo Lx3")
plot(history3, "zad2_pr-wo Wx3")
plot(history4, "zad2_pr-wo Sx3")