COTACAO_DOLAR = 5
def dolar_real (dolar):
    reais = dolar * COTACAO_DOLAR
    return reais

def real_dolar (real):
    dolares = real / COTACAO_DOLAR
    return dolares

opcao = input("calculadora monetaria\n"
"[1 - converter de dolar para real]\n" \
"[2 - converter de real para dolar]\n" \
"digite sua opção: ")

if opcao == "1" :
    dolares = float(input("digite quantos dolares deseja converter para real:"))
    reais = dolar_real(dolares)
    print(f"os seus dolares equivalem R$ {reais:.2f}")

elif opcao == "2" :
    reais = float(input("digite quantos reais deseja converter para dolares:"))
    dolar = real_dolar(reais)
    print(f"os seus reais equivalem $ {dolar:.1f}")

else:
    print("opcao invalida")