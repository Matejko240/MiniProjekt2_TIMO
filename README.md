
# NLP5 – Optymalizacja cen trzech produktów

## 📌 Treść zadania

Menadżer w firmie chce ustalić ceny trzech produktów (`p1`, `p2`, `p3`), tak aby zmaksymalizować **zysk całkowity** przedsiębiorstwa. Produkty mają różną jakość i koszt wytworzenia, a także wpływają wzajemnie na swoją sprzedaż.

Funkcja zysku jest zdefiniowana jako:
```
f(p1, p2, p3) =
  (6000 − 3p1 + 0.5p2)(p1 − 300) +
  (25000 − 7.5p2 + 0.3p1 + 0.5p3)(p2 − 140) +
  (30000 − 15p3 + 2.5p2)(p3 − 60)
```
gdzie:
- pierwszy nawias to model popytu,
- drugi nawias to jednostkowy zysk.

### Ograniczenia produkcyjne (na popyt):
- Produkt 1: ≤ 5000 szt.
- Produkt 2: ≤ 15000 szt.
- Produkt 3: ≤ 18000 szt.

---

## 🧠 Teoria i metody optymalizacji zastosowane w kodzie

Problem sformułowano jako **nieliniowy problem programowania matematycznego (NLP)** z ograniczeniami. Rozwiązanie wykorzystuje metodę **SLSQP** z biblioteki `scipy.optimize`.

### 1. Funkcja celu

```python
def objective_function(p):
    ...
    return -total_profit
```

Zwracana jest **ujemna wartość zysku**, ponieważ funkcja `minimize` szuka minimum, a my chcemy zmaksymalizować zysk.

Funkcja jest ciągła i różniczkowalna, co umożliwia jej wykorzystanie w SLSQP.

### 2. Ograniczenia nierównościowe

Zdefiniowane są jako funkcje:

```python
def constraint_demand1(p): return 5000 - (6000 - 3*p[0] + 0.5*p[1])
```

co odpowiada warunkowi: `popyt1 ≤ 5000`. Funkcja zwraca wyrażenie `g(x) ≥ 0`, zgodne z wymaganiami metody SLSQP.

### 3. Granice na zmienne (bounds)

```python
bounds = [(300, None), (140, None), (60, None)]
```

Są to **ograniczenia dolne** – ceny muszą być większe lub równe kosztom jednostkowym, aby nie generować strat.

### 4. Punkt startowy

```python
initial_guess = [300, 140, 60]
```

To realistyczne wartości początkowe – równe kosztom jednostkowym.

### 5. Rozwiązanie optymalizacyjne

```python
result = minimize(...)
```

Metoda iteracyjna szuka minimum funkcji celu z uwzględnieniem ograniczeń i warunków brzegowych. W wyniku otrzymujemy:

- optymalne ceny `p1`, `p2`, `p3`,
- maksymalny zysk (`-result.fun`),
- końcowe wartości popytu dla weryfikacji ograniczeń.

---

## ✅ Jak uruchomić

### Wymagania:
```bash
pip install numpy scipy
```

### Uruchomienie:
```bash
python main.py
```

W terminalu zostaną wyświetlone:
- Optymalne ceny,
- Maksymalny zysk,
- Sprawdzenie ograniczeń popytu.

---

## 💡 Przykładowy wynik

```
Optymalizacja zakończona sukcesem.
Optymalna cena dla produktu 1 (p1): 1414.83 PLN
Optymalna cena dla produktu 2 (p2): 2038.45 PLN
Optymalna cena dla produktu 3 (p3): 1231.52 PLN
Maksymalny zysk: 42,979,734.78 PLN
Popyt: [2775, 10752, 16623]
```

Wszystkie ograniczenia zostały spełnione.

---

## ❓ Najczęstsze pytania

**Dlaczego minimalizujemy funkcję, skoro chcemy maksymalizować zysk?**  
Ponieważ `scipy.optimize.minimize` znajduje minimum – więc minimalizujemy `-zysk`.

**Skąd dolne granice 300, 140, 60?**  
Są to koszty jednostkowe. Cena musi być co najmniej równa kosztowi.

**Czy produkty wpływają na siebie wzajemnie?**  
Tak – każda funkcja popytu zależy od więcej niż jednej zmiennej (np. `p1` wpływa na `popyt2`).

**Czy rozwiązanie zawsze spełnia ograniczenia?**  
Tak – wartości popytu są weryfikowane po znalezieniu optimum.

---

**Autor: Jan Rybarz**  
**Przedmiot: Teoria i metody optymalizacji**  
**Data: Czerwiec 2025**
