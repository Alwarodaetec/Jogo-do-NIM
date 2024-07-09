# O QUÊ É?
O Jogo do NIM é um clássico jogo de tabuleiro onde dois jogadores se alternam removendo peças de um monte. O jogador que retirar a última peça ganha o jogo. Este projeto implementa o Jogo do NIM em Python, permitindo que um jogador humano desafie o computador, que sempre utilizará uma estratégia vencedora.

# Funcionalidades
Jogador vs Computador: O jogador humano pode jogar contra o computador.
Estratégia Vencedora: O computador segue uma estratégia que garante a vitória, se possível.
Partida Isolada: Jogue uma única partida.
Campeonato: Jogue uma série de três partidas e veja quem é o vencedor geral.

# Regras do Jogo
Configuração Inicial: O jogador escolhe o número inicial de peças (n) e o número máximo de peças que podem ser removidas em uma jogada (m).
Quem Começa: Se n é múltiplo de m+1, o jogador humano começa. Caso contrário, o computador começa.
Turnos Alternados: Os jogadores se alternam removendo entre 1 e "m" peças do monte.
Fim do Jogo: O jogador que retirar a última peça ganha.

# Funções Principais
usuario_escolhe_jogada(n, m): Solicita a jogada do usuário e retorna o número de peças removidas.
computador_escolhe_jogada(n, m): Calcula e retorna a jogada do computador baseada na estratégia vencedora.
partida(): Gerencia uma única partida entre o jogador e o computador.
campeonato(): Realiza três partidas consecutivas e exibe o placar final.
main(): Função principal que inicia o jogo e permite a escolha entre uma partida única e um campeonato.
