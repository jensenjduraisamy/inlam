def skriv_nummers_mellan_2_and_n(n):
        if isinstance(n, int) and 2 <= n <= 99:
            for number in range(2, n + 1):
               print(number)
        else:
                print("Invalid value for n. Vänligen Ange ett heltal mellan 2 och 99.")
n = int(input("Ange ett heltal mellan 2 och 99: "))
skriv_nummers_mellan_2_and_n(n)