# Aquí crearemos un entorno donde podemos probar las estrategias

# En cada periodo de tiempo nos vamos a parar en un dato real del símbolo que estemos utilizando
# el periodo de timepo viene definido por la periodicidad de los datos que tengamos, 1m, 5m, etc
# un periodo de tiempo termina cuando empieza el siguiente, 
# en cada periodo de tiempo la estrategia tiene dos opciones; entrar al mercado o no hacerlo
 # si decide entrar al mercado tomará una posición, sea compra o venta dependiento de la estrategia
 # si decide no entrar al mercado no pasa nada
# cada periodo de tiempo sin importar si entra o no al mercado se actualizará la cuenta que puede:
 # permanecer igual si la estrategia no entró al mercado
 # puede recibir una recompensa positiva si el precio de cierre del siguiente periodo es positiva
 # de igual manera si el precio de cierre del siguiente periodo no le conviene recibirá un castigo

import pandas as pd

#importamos los datos del simbolo que usaremos
data = pd.read_csv('datos\EURUSD1.csv', header=None)
data.columns = ['date', 'time', 'open', 'high', 'low', 'close', 'volume']

periodos = 2000                 # Asegurarse que haya datos para cada uno de los periodos
valor_inical = 200

class tiempo:

    def __init__(self, date, open, high, low, close, volume): 
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume


t1 = tiempo(data['date'][1], data['open'][1], data['high'][1], data['low'][1], data['close'][1], data['volume'][1])

print(t1)
