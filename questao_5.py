def inverte_string(string):
    invertida = ""
    for i in range(len(string)-1, -1, -1):
        invertida += string[i]
    return invertida

# Definindo uma string para inverter
string = "Exemplo de string"

print("String original:", string)
print("String invertida:", inverte_string(string))
