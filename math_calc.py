from tools import *

def get_probabilities(message: list, pL, pW, pS):
    # Oblicz prawdopodobieństwa dla każdego języka
    # dlatver: lista symboli dla języka L
    # pdlatver: rozkład prawdopodobieństwa dla języka L
    dlatver, pdlatver = calc_probabilities("dlatver 25.txt")
    dsymk, pdsymk = calc_probabilities("dsymk 23.txt")
    dwak, pdwak = calc_probabilities("dwak 26.txt")

    # Wyświetl symbole i rozkłady prawdopodobieństwa
    print("Symbole w języku L:", dlatver[:30], "...")
    print("Prawdopodobieństwa literek w języku L:", pdlatver)
    print("\nSymbole w języku S:", dsymk[:30], "...")
    print("Prawdopodobieństwa literek w języku S:", pdsymk)
    print("\nSymbole w języku W:", dwak[:30], "...")
    print("Prawdopodobieństwa literek w języku W:", pdwak)

    # I ... Szukamy P(W|m), P(L|m), P(Z|m)

    # Prawdopodobieństwa a priori dla języków
    print(f"\nPrawdopodobieństwa języków:\nJęzyk W: {pW}\nJęzyk S: {pS}\nJęzyk L: {pL}")

    # Pobierz symbole wiadomości
    print("Symbole wiadomości:", message)

    history = {"L": [], "W": [], "S": []}

    # Obliczamy prawdopodobieństwa wiadomości dla każdego języka
    p_ML = p_MW = p_MS = 1
    for i in message:
        if i != "N":
            p_ML = p_ML * pdlatver[i]
            p_MW = p_MW * pdwak[i]
            p_MS = p_MS * pdwak[i]

        # Całkowite prawdopodobieństwo wiadomości (normalizacja)
        pM = (p_MS * pS) + (p_MW * pW) + (p_ML * pL)

        # Posteriori: P(W|M), P(S|M), P(L|M)
        p_WM = (p_MW * pW) / pM
        p_SM = (p_MS * pS) / pM
        p_LM = (p_ML * pL) / pM
        history["W"].append(p_WM)
        history["S"].append(p_SM)
        history["L"].append(p_LM)

    p_WM = history["W"][-1]
    p_SM = history["S"][-1]
    p_LM = history["L"][-1]

    # Wyświetl prawdopodobieństwa wiadomości dla każdego języka
    print(f"Prawdopodobieństwo wiadomości od L: {p_ML}")
    print(f"Prawdopodobieństwo wiadomości od W: {p_MW}")
    print(f"Prawdopodobieństwo wiadomości od S: {p_MS}")

    print(f"Prawdopodobieństwa posteriori (hipotezą jest prawdopodobieństwo że język został użyty w tej wiadomości \nP(W użyty w message|message) albo P(S użyty w message|message)):\nJęzyk W: {p_WM}\nJęzyk S: {p_SM}\nJęzyk L: {p_LM}")

    # Sprawdzenie poprawności sumy
    print(f"Suma: {p_WM + p_SM + p_LM}")
    return history

