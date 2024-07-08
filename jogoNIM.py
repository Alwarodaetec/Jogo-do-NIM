def usuario_escolhe_jogada(n,m):
    x=int(input("Quantas peças deseja tirar? "))
    while x > n or x < 1 or x > m:
        print  ("Ooops! Jogada Inválida, Tente novamente!")
        x=int(input("Quantas peças deseja tirar? "))
    n-=x
    return x
    
def computador_escolhe_jogada(n, m):
    for quantidade in range(1, m + 1):
        if (n - quantidade) % (m + 1) == 0:
            m=quantidade
            n-=m
            print(f"Computador retirou {quantidade} peças.")
            return quantidade
    n-=m
    return f"Computador retirou {m} peças."


def partida():
    n=int(input("quantas peças? "))
    m=int(input("limite de peças? "))
    
    if (n%(m+1)==0):
        print("Você começa!")
        vezComputador=False
    else:
        print("Computador começa!")
        vezComputador=True
        
    while n>0:
        if vezComputador:
            n-=computador_escolhe_jogada(n,m)
            vezComputador=False
        else:
            n-=usuario_escolhe_jogada(n,m)
            vezComputador=True
        print(f"restam {n} peças")
            
    if vezComputador:
        print("Você ganhou, Parabéns!")
        return 0
    else:
        print("Computador ganhou!")
        return 1
    
def campeonato():
    vitoria_j=0
    vitoria_c=0
    rodada=1
    while rodada<=3:
        print(f"**** Rodada {rodada}****")
        resultado=partida()       
        if resultado==0:
            vitoria_j+=1
        else:
            vitoria_c+=1
        rodada+=1
    
    print(f"Placar: Você {vitoria_j}x{vitoria_c} Computador")
    if vitoria_c>vitoria_j:
        print("Computador venceu o campe")
        
def main():
    print("Bem Vindo ao Jogo do NIM!")
    x=int(input("para começarmos digite 1 para partida única, ou 2 para campeonato com três rodadas "))
    if x==1:
        partida()
    elif x==2:
        campeonato()
    else:
        print("Valor inserido inválido")
        main()
    

if __name__ == '__main__':
    main()