magiczna_liczba = 42  # Możesz tu wpisać dowolną magiczną liczbę

while True:
    try:
        liczba = int(input("Podaj liczbę całkowitą: "))

        if liczba < magiczna_liczba:
            print("Podana liczba jest mniejsza od magicznej.")
        elif liczba > magiczna_liczba:
            print("Podana liczba jest większa od magicznej.")
        else:
            print("Gratulacje! Trafiłeś magiczną liczbę.")
            break
    except ValueError:
        print("To nie jest prawidłowa liczba całkowita. Spróbuj ponownie.")
