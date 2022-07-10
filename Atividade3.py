print("Seja bem-vindo ao sistema eletronico de votacao do condominio")
print("Para votar na chapa Amarelo, digite 1")
print("Para votar na chapa Azul, digite 2")
print("Para votar na chapa Vermelho, digite 3")
print("Para anular o voto, digite 4")

amarelo = 0;
azul = 0;
vermelho = 0;
nulo = 0;
contagem = 0;

for i in range(0, 35):
    voto = int(input("Digite a opcao escolhida: "));
    if voto == 1:
        amarelo += 1;
    elif voto == 2:
        azul += 1;
    elif voto == 3:
        vermelho += 1;
    else:
        nulo += 1;
    
    contagem += 1;

print(f"Resultado da eleicao: ")
print(f"Numero de votos registrados : {contagem}")
print(f"Numero de votos para a chapa Amarelo: {amarelo}")
print(f"Numero de votos para a chapa Azul: {azul}")
print(f"Numero de votos para a chapa Vermelho: {vermelho}")
print(f"Numero de votos nulos: {nulo}")