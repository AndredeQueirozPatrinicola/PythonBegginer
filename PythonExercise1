#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
#No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
#O seu resultado fica sendo a média dos três valores restantes. 
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a 
#descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). 
#Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. 


lista = []
n = 1
atleta = input("Nome: ")
while n <= 5:
    saltos = float(input(f"Salto {n}: "))
    lista.append(saltos)
    n += 1
print('\n')
print(f"Atleta: {atleta}")
print('\n')
print(f"Primeiro salto: {lista[0]} m")
print(f"Segundo salto: {lista[1]} m")
print(f"Terceiro salto: {lista[2]} m")
print(f"Quarto salto: {lista[3]} m")
print(f"Quinto salto: {lista[4]} m")
print('\n')
lista.sort()
melhor = lista[4]
pior = lista[0]
media = (lista[1] + lista[2] + lista[3]) / 3


print(f"Melhor salto: {melhor} m")
print(f"Pior salto: {pior} m")
print(f"Média dos demais saltos: {media:.2f} m")

print(f"Resultado final: {media:.2f} m /n Atleta: {atleta} ")
