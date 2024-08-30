def verifica_letra_a(string):    
    count_a = string.lower().count('a')
    
    if count_a > 0:
        print(f"A letra 'a' aparece {count_a} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

string = input("Informe uma string: ")
verifica_letra_a(string)
