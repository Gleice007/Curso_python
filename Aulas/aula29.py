"""
COSTANTE = "Variáveis" que não vão mudar 
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim) 
"""
velocidade = 61 # velocidade atual do carro 
local_carro = 101 # local em que o carro está na estrada 
   
RADAR_1 = 60 # velocidade máxima do radar 1 
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGER = 1  # A distância onde o radar pega

carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGER)
local_carro <= (LOCAL_1 + RADAR_RANGER)

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if carro_passou_radar_1:
    print('Carro passou radar')

if local_carro >= (LOCAL_1 - RADAR_RANGER) and \
        local_carro <= (LOCAL_1 + RADAR_RANGER) and \
             velocidade > RADAR_1:
    print('carro multado em radar 1')
