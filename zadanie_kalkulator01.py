import logging

def dodawanie(a, b):
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b != 0:
        return a / b
    else:
        logging.error("Dzielenie przez zero!")
        return None

def main():
    logging.basicConfig(level=logging.INFO)
    
    dzialanie = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    
    if dzialanie not in ['1', '2', '3', '4']:
        logging.error("Podano nieprawidłową opcję.")
        return

    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))
    
    if dzialanie == '1':
        operacja = 'Dodawanie'
        wynik = dodawanie(a, b)
    elif dzialanie == '2':
        operacja = 'Odejmowanie'
        wynik = odejmowanie(a, b)
    elif dzialanie == '3':
        operacja = 'Mnożenie'
        wynik = mnozenie(a, b)
    else:
        operacja = 'Dzielenie'
        wynik = dzielenie(a, b)

    logging.info(f"{operacja} {a:.2f} i {b:.2f}")
    print(f"Wynik to {wynik:.2f}")

if __name__ == '__main__':
    main()