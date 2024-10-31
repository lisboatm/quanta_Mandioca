# Função para calcular a quantidade total de mandioca
def calcular_mandioca(curupira_porcoes, boitata_porcoes, boto_porcoes, mapinguari_porcoes, iara_porcoes):
    # Definindo o tamanho das porções
    porcoes = {
        "Curupira": 300,
        "Boitatá": 1500,
        "Boto": 600,
        "Mapinguari": 1000,
        "Iara": 150,
        "Dona Chica": 225  # Dona Chica sempre come 225g
    }
    
    # Calculando a quantidade total
    total_mandioca = (
        curupira_porcoes * porcoes["Curupira"] +
        boitata_porcoes * porcoes["Boitatá"] +
        boto_porcoes * porcoes["Boto"] +
        mapinguari_porcoes * porcoes["Mapinguari"] +
        iara_porcoes * porcoes["Iara"] +
        porcoes["Dona Chica"]  # Adicionando a quantidade de Dona Chica
    )
    
    return total_mandioca

# Leitura das porções de mandioca
curupira_porcoes = int(input())
boitata_porcoes = int(input())
boto_porcoes = int(input())
mapinguari_porcoes = int(input())
iara_porcoes = int(input())

# Chamando a função e imprimindo o resultado
total = calcular_mandioca(curupira_porcoes, boitata_porcoes, boto_porcoes, mapinguari_porcoes, iara_porcoes)
print(total)
