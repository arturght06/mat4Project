from part2 import zadanie2
from tools import get_message_symbols, plot

message = get_message_symbols()

history1 = zadanie2(message, 1/3, 1/3, 1/3)

print("___"*30, "II część", "___"*30, end="\n\n")

print("> Trzykrotnie częściej dla L:")
history2 = zadanie2(message, 3/5, 1/5, 1/5)
print("\n\n\n> Trzykrotnie częściej dla W:")
history3 = zadanie2(message, 1/5, 3/5, 1/5)
print("\n\n\n> Trzykrotnie częściej dla S:")
history4 = zadanie2(message, 1/5, 1/5, 3/5)

print("___"*30, "Rozwiązanie problemu - prezentacja wyniku", "___"*30, end="\n\n")

print(print("___"*10, "ZADANIE 1", "___"*10, end="\n\n"))

plot(history1, "równe prawdopodobieństwa")
plot(history2, "pr-wo Lx3")
plot(history3, "pr-wo Wx3")
plot(history4, "pr-wo Sx3")