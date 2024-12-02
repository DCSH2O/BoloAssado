# BoloAssado
Exemplo simples:

def fazer_bolo(ingredientes, tempo_de_forno):
    # Verificar o tipo de bolo
    if ingredientes < 3:
        tipo_bolo = "Bolo Simples"
    else:
        tipo_bolo = "Bolo Complexo"
        tempo_de_forno += 10  # Aumentar 10 minutos para Bolo Complexo
    
    # Imprimir o tipo de bolo e o tempo de forno
    print(f"Tipo de Bolo: {tipo_bolo}")
    print(f"Tempo de Forno: {tempo_de_forno} minutos")
    
    # Imprimir a mensagem final
    print("Bolo Assado")

# Testando a função
fazer_bolo(2, 20)  # Bolo Simples com 20 minutos de forno
fazer_bolo(5, 25)  # Bolo Complexo com 25 minutos de forno