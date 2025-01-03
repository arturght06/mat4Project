## Podstawy teoretyczne
> **Zadanie:** zdefiniuj badane hipotezy:

Hipotezą w danym problemie jest "użycie języka $X$ w wiadomości $M$", danymi znanymi natomiast przyjmujemy symbole tekstu wiadomości.
Zatem wzorem na P(*język X został użyty* | *symbole wiadomości*) jest:

>$P(X|M) = \frac{P(M|X)P(X)}{P(M)}$

Gdzie:

- $P(M|X) =$ *przmnożone prawdopodobieństwa występowania w języku każdego symbolu z wiadomości*
- $P(X) =$ *prawdopodobieństwo wyboru konkretnego języka z możliwych*
- $P(M) =$ *suma prawdopodobieństw występowanie języka w wiadomości P(X|M), P(Y|M), P(Z|M) razy prawdopodobieństwo wyboru tego języka P(X), P(Y), P(Z). 
Czyli tak zwane całkowite prawdopodobieństwo albo normalizacja*

> **Zadanie:** Wyjaśnij pojęcie prawdopodobieństwa a priori i a posteriori.

**a priori** - proces oszacowania prawdopodobieństwa zdarzenia na podstawie wcześniejszej wiedzy teoretycznej lub założeń, bez uwzględniania danych z rzeczywistych obserwacji lub eksperymentów.

**a posteriori** - proces oszacowania prawdopodobieństwa zdarzenia na podstawie danych zebranych w wyniku eksperymentu lub obserwacji. To prawdopodobieństwo jest aktualizowane po uwzględnieniu nowych informacji, często w oparciu o analizę statystyczną (np. w ramach statystyki bayesowskiej).

> Zdefiniuj funkcję wiarogodności, jaka jest jej interpretacja?

$P(L|Message) =$ iloczyn prawdopodobieństw pojawiania się każdego z symboli w języku ($P(M_i|L_k)$).
Funkcja wiarogodności mierzy zgodność obserwowanych danych (wiadomości M) z założeniem, że wiadomość została napisana w języku $L_k$.

>  Czy przyjęte początkowo rozkłady a priori mają wpływ na ostateczną klasyfikację?

Tak, zmiana charakterystyk początkowych a priori wprost zmienia różnicę między prawdopodobieństwami L, S, które nie są charakterystyczne dla danej wiadomości. Ale po odpowiedniej ilości rund prawdopodobieństwo tego wiadomość została napisana w języku W zwiększa się blisko 1. Więc a priori nie zmienia znacząco odpowiedzi funkcji wiarygodności.

> Zaproponuj i uzasadnij sensowną metodę stopu umożliwiającą zakończenie procedury aktualzacji bez
czytania całej wiadomości message

Jeżeli po wystarczającej ilości rund przemnożenia prawdopodobieństw literek wiadomości w języku odpowiedż funkcji wiarygodności zbliża się wartości granicznej 1, możemy uznać że taka wiadomośc została napisana w tym języku.

>  4 zadanie 
> > Opisz uzyskane wnioski i spostrzeżenia.

Wybraliśmy symbole C oraz D. Teraz oceniamy tylko prawdopodobieństwa pojawiania się tych symboli w językach i po narysowaniu wykresów widzimy że zależy wynik wprost od prawdopodobieństwa wybrania konkretnego języka, zatem wynika z tego równość prawdopodobieństwa pojawiania się tych wybranych symboli we wszystkich językach. 

___
