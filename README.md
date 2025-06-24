NLP5 – Optymalizacja cen 3 produktów w celu maksymalizacji zysku
📌 Treść zadania
Menadżer w pewnej firmie chce ustalić ceny trzech produktów, tak aby zmaksymalizować zysk. Produkty różnią się jakością, kosztem produkcji i wzajemnie wpływają na siebie nawzajem w zakresie sprzedaży.

Całkowity zysk przedsiębiorstwa opisany jest funkcją:

Kopiuj
Edytuj
f(p1, p2, p3) =
  (6000 − 3p1 + 0.5p2)(p1 − 300) +
  (25000 − 7.5p2 + 0.3p1 + 0.5p3)(p2 − 140) +
  (30000 − 15p3 + 2.5p2)(p3 − 60)
gdzie:

pi – cena i-tego produktu,

pierwszy nawias – popyt na produkt,

drugi nawias – jednostkowy zysk z produktu.

Ograniczenia technologiczne:
Popyt na produkt 1 nie może przekroczyć 5000 sztuk.

Popyt na produkt 2 nie może przekroczyć 15000 sztuk.

Popyt na produkt 3 nie może przekroczyć 18000 sztuk.

🧠 Podejście do rozwiązania
Zadanie zostało sformułowane jako nieliniowy problem optymalizacji z ograniczeniami (NLP). Użyto biblioteki SciPy i metody SLSQP, ponieważ:

Obsługuje nieliniową funkcję celu,

Pozwala na uwzględnienie ograniczeń nierównościowych,

Umożliwia określenie przedziałów cenowych.

Funkcja celu
W pliku main.py funkcja objective_function(p) reprezentuje ujemny całkowity zysk, ponieważ algorytm minimize minimalizuje wartość – a naszym celem jest maksymalizacja zysku.

Ograniczenia
Zdefiniowano trzy funkcje constraint_demandX(p), które odpowiadają warunkom:

Popyt_i <= wartość maksymalna,

Przekształcone do formy g(x) >= 0, wymaganej przez scipy.optimize.minimize.

⚙️ Jak uruchomić
Upewnij się, że masz zainstalowany Python 3 i bibliotekę SciPy:

nginx
Kopiuj
Edytuj
pip install numpy scipy
Uruchom skrypt:

css
Kopiuj
Edytuj
python main.py
Wynik zostanie wyświetlony w terminalu i będzie zawierał:

Optymalne ceny produktów,

Maksymalny możliwy zysk,

Weryfikację spełnienia ograniczeń na popyt.

✅ Przykładowy wynik
Optymalizacja zakończona sukcesem.
----------------------------------------       
Optymalna cena dla produktu 1 (p1): 1414.83 PLN
Optymalna cena dla produktu 2 (p2): 2038.45 PLN
Optymalna cena dla produktu 3 (p3): 1231.52 PLN
----------------------------------------       
Maksymalny zysk: 42,979,734.78 PLN
----------------------------------------
Wynikowy popyt (weryfikacja ograniczeń):
  Popyt na produkt 1: 2775 (Ograniczenie: <= 5000)
  Popyt na produkt 2: 10752 (Ograniczenie: <= 15000)
  Popyt na produkt 3: 16623 (Ograniczenie: <= 18000)
----------------------------------------
❓ Najczęstsze pytania (FAQ)
Dlaczego użyto minimize, skoro celem jest maksymalizacja?
Ponieważ minimize minimalizuje funkcję, maksymalizację zysku osiągamy poprzez minimalizację ujemnej wartości funkcji celu.

Dlaczego ceny produktów nie mogą być niższe niż [300, 140, 60]?
Są to koszty jednostkowe. Cena sprzedaży musi być wyższa, aby firma mogła osiągnąć zysk. Zatem ceny zostały ograniczone od dołu przez granice (bounds).

Czy funkcja celu uwzględnia wpływ jednego produktu na drugi?
Tak. Każdy składnik popytu (np. demand1) zależy nie tylko od p1, ale także od pozostałych cen (p2, p3), co odzwierciedla efekt kanibalizacji lub komplementarności produktów.

Czy rozwiązanie spełnia ograniczenia?
Tak. Po optymalizacji skrypt dodatkowo oblicza i wypisuje wartości popytu, by upewnić się, że nie przekraczają dozwolonych limitów produkcyjnych.