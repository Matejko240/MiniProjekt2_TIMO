import numpy as np
from scipy.optimize import minimize

def objective_function(p):
    """
    Oblicza ujemną wartość zysku całkowitego.
    Minimalizujemy tę funkcję, aby zmaksymalizować zysk.

    Args:
        p (list): Lista zawierająca ceny produktów [p1, p2, p3].

    Returns:
        float: Ujemna wartość zysku.
    """
    p1, p2, p3 = p
    
    # Popyt i zysk jednostkowy dla każdego produktu
    demand1 = 6000 - 3*p1 + 0.5*p2
    unit_profit1 = p1 - 300
    
    demand2 = 25000 - 7.5*p2 + 0.3*p1 + 0.5*p3
    unit_profit2 = p2 - 140
    
    demand3 = 30000 - 15*p3 + 2.5*p2
    unit_profit3 = p3 - 60
    
    # Zysk całkowity
    total_profit = (demand1 * unit_profit1) + \
                   (demand2 * unit_profit2) + \
                   (demand3 * unit_profit3)
                   
    # Zwracamy wartość ujemną, ponieważ `minimize` szuka minimum
    return -total_profit

# --- Definicje Ograniczeń ---
# Optymalizator `scipy.optimize.minimize` z metodą SLSQP
# wymaga, aby ograniczenia nierównościowe były w postaci g(x) >= 0.

def constraint_demand1(p):
    """
    Reprezentuje ograniczenie: Popyt1 <= 5000.
    Przekształcone do formy: 5000 - Popyt1 >= 0.
    """
    demand1 = 6000 - 3*p[0] + 0.5*p[1]
    return 5000 - demand1

def constraint_demand2(p):
    """
    Reprezentuje ograniczenie: Popyt2 <= 15000.
    Przekształcone do formy: 15000 - Popyt2 >= 0.
    """
    demand2 = 25000 - 7.5*p[1] + 0.3*p[0] + 0.5*p[2]
    return 15000 - demand2

def constraint_demand3(p):
    """
    Reprezentuje ograniczenie: Popyt3 <= 18000.
    Przekształcone do formy: 18000 - Popyt3 >= 0.
    """
    demand3 = 30000 - 15*p[2] + 2.5*p[1]
    return 18000 - demand3

# Uruchomienie skryptu
if __name__ == "__main__":
    # Punkt startowy dla algorytmu optymalizacyjnego
    # Wybieramy ceny równe kosztom jednostkowym, co jest dobrym punktem startowym
    initial_guess = [300, 140, 60]

    # Granice dla zmiennych (cen)
    # Cena musi być co najmniej równa kosztowi jednostkowemu, aby zysk jednostkowy był nieujemny.
    # p1 >= 300, p2 >= 140, p3 >= 60
    bounds = [(300, None), (140, None), (60, None)]

    # Lista ograniczeń w formacie wymaganym przez scipy
    constraints = [
        {'type': 'ineq', 'fun': constraint_demand1},
        {'type': 'ineq', 'fun': constraint_demand2},
        {'type': 'ineq', 'fun': constraint_demand3}
    ]

    # Uruchomienie optymalizacji
    result = minimize(objective_function, 
                      initial_guess, 
                      method='SLSQP', 
                      bounds=bounds, 
                      constraints=constraints)

    # Prezentacja wyników
    if result.success:
        p1_opt, p2_opt, p3_opt = result.x
        max_profit = -result.fun
        
        # Obliczenie popytów dla optymalnych cen w celu weryfikacji
        final_demand1 = 6000 - 3*p1_opt + 0.5*p2_opt
        final_demand2 = 25000 - 7.5*p2_opt + 0.3*p1_opt + 0.5*p3_opt
        final_demand3 = 30000 - 15*p3_opt + 2.5*p2_opt

        print("Optymalizacja zakończona sukcesem.")
        print("-" * 40)
        print(f"Optymalna cena dla produktu 1 (p1): {p1_opt:.2f} PLN")
        print(f"Optymalna cena dla produktu 2 (p2): {p2_opt:.2f} PLN")
        print(f"Optymalna cena dla produktu 3 (p3): {p3_opt:.2f} PLN")
        print("-" * 40)
        print(f"Maksymalny zysk: {max_profit:,.2f} PLN")
        print("-" * 40)
        print("Wynikowy popyt (weryfikacja ograniczeń):")
        print(f"  Popyt na produkt 1: {final_demand1:.0f} (Ograniczenie: <= 5000)")
        print(f"  Popyt na produkt 2: {final_demand2:.0f} (Ograniczenie: <= 15000)")
        print(f"  Popyt na produkt 3: {final_demand3:.0f} (Ograniczenie: <= 18000)")
        print("-" * 40)
    else:
        print("Nie udało się znaleźć rozwiązania.")
        print("Komunikat błędu:", result.message)