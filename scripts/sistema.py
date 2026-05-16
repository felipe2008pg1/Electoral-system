import tools as to
import time
import json
import os

candidatos = to.carregar_dados()

to.limpar_tela()
to.escrever_menu("-- ELEIÇÕES 2026 --", pular_linha=False)
time.sleep(0.4)
to.escrever_lento(' By @dlv.gonzalezz')

to.escrever_lento("\n⚠️  AVISO: Este projeto está em fase de desenvolvimento. Futuramente, " /
"atualizarei esse sistema para votação por número do candidato.")

time.sleep(1.5)
print("="*10)

input("Digite ENTER para continuar:")
print("Iniciando...")
time.sleep(0.6)
to.limpar_tela()

votos_disponiveis = 1 

while True:
    if votos_disponiveis <= 0:
        print("\n=== VOTAÇÃO ENCERRADA (Limite de votos atingido) ===")
        for t, c in enumerate(candidatos, start=1):
            print(f"{t} - {c['candidato']:<14} | Nº de votos: {c['votos']}")
        to.encerrar()
        break

    print(f"\n== TELA INICIAL == {to.mostrar_hora()} - Horário de Brasília")

    try:
        menu = int(input("\n1 - Votar \n2 - Sair \n - ESCOLHA SUA OPÇÃO: ").strip())
        to.limpar_tela()

        if menu == 1:
            while True:
                print("\n-- Opções de candidatos --")
                for t, c in enumerate(candidatos, start=1):
                    print(f"{t} - {c['candidato']:<14} | Nº de votos: {c['votos']}")
                print('='*10)

                opcao_voto = input("Digite o NOME do candidato: ").strip().upper()
                encontrado = False
                    
                for c in candidatos:
                    if opcao_voto == c['candidato']:
                        c['votos'] += 1
                        votos_disponiveis -= 1
                        encontrado = True
                        
                        to.salvar_dados(candidatos)
                        
                        print('\nVoto realizado e gravado com sucesso.')
                        time.sleep(1)
                        to.limpar_tela()
                        break 

                if encontrado:
                    break 
                
                print("\n[ERRO] Nome inválido. Tente novamente.")
                time.sleep(2)
                to.limpar_tela()

        elif menu == 2:
            to.encerrar()
            break

        else:
            print("[ERRO] Digite uma opção válida (1 ou 2).")
            time.sleep(1)
            to.limpar_tela()

    except ValueError:
        print("[ERRO] Entrada inválida. Digite um número inteiro.")
        time.sleep(1)
        to.limpar_tela()
