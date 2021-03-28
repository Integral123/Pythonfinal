#importa pandas
import pandas as pd

# Crea una Serie de los numeros 10, 20 and 10.
lista = [10,20,30]

# Crea una Serie con tres objetos: 'rojo', 'verde', 'azul'
lista2 = ['rojo', 'verde', 'azul']

# Crea un dataframe vacío llamado 'df'
df = pandas.DataFrame()

# Crea una nueva columna en el dataframe, y asignale la primera serie que has creado
df = pandas.DataFrame(lista)
df

# Crea otra columna en el dataframe y asignale la segunda Serie que has creado
df = pandas.DataFrame(lista2) 
df

# Lee el archivo llamado 'avengers.csv" localizado en la carpeta "data" y crea un DataFrame, llamado 'avengers'. 
# El archivo está localizado en "data/avengers.csv"
avengers = pd.read_csv('./data/pandas/avengers.csv')
avengers

# Muestra las primeras 5 filas del DataFrame.
avengers.head(5)

# Muestra las primeras 10 filas del DataFrame. 
avengers.head(10)

# Muestra las últimas 5 filas del DataFrame.
avengers.tail(5)

# Muestra el tamaño del DataFrame
avengers.count

# Muestra los data types del dataframe
avengers.dtypes

# Cambia el indice a la columna "fecha_inicio".
av = avengers.set_index("fecha_inicio")
av.head()

# Ordena el índice de forma descendiente
avengers.head(173)

# Resetea el índice
avengers=avengers.reset_index(drop=True)