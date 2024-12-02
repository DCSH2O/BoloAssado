# Solicitar ao usuário os ingredientes, separados por vírgulas
ingredientes = input("Digite os ingredientes separados por vírgulas: ").split(',')

# Função para fazer o bolo
def fazer_bolo(ingredientes, tempo_de_forno):
    # Contar a quantidade de ingredientes
    quantidade_ingredientes = len(ingredientes)

    # Verificar o tipo de bolo com base na quantidade de ingredientes
    if quantidade_ingredientes < 3:
        tipo_bolo = "Bolo Simples"
    else:
        tipo_bolo = "Bolo Complexo"
        tempo_de_forno += 10  # Aumentar 10 minutos para Bolo Complexo
    
    # Imprimir o tipo de bolo e o tempo de forno
    print(f"Tipo de Bolo: {tipo_bolo}")
    print(f"Tempo de Forno: {tempo_de_forno} minutos")
    
    # Imprimir a quantidade de ingredientes
    print(f"Quantidade de ingredientes: {quantidade_ingredientes}")
    
    # Imprimir a mensagem final
    print("Bolo Assado")

# Chamar a função após o usuário fornecer os ingredientes
fazer_bolo(ingredientes, 20)  # Passa a lista de ingredientes e o tempo de forno inicial
