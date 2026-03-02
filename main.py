import os

mensagens = []

nome = input("Nome: ")

while True:
    
    os.system("cls" if os.name == "nt" else "clear")

    if len(mensagens) > 0:
        for m in mensagens:
            print(f"{m['nome']} - {m['texto']}")
        print("________________")

    texto = input("Mensagem (ou 'fim' para sair): ")

    if texto.lower() == "fim":
        break


    mensagens.append({
        "nome": nome,
        "texto": texto
    })  
    
