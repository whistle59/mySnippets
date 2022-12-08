# https://www.freecodecamp.org/espanol/news/como-combinar-multiples-archivos-csv-con-solo-8-lineas-de-codigo/

# Paso 1: Importa los paquetes y selecciona el directorio de trabajo
# Cambia "/midir" por tu directorio de trabajo o carpeta deseada.

import os
import glob
import pandas as pd
os.chdir("/midir")

# Paso 2: Usa la función glob para encontrar el patrón 'csv'
# Encuentra el patrón ('csv') y guarda la lista de los nombres de los archivos 
# en la variable 'todos_los_archivos'. Puedes revisar este link para aprender más sobre expresiones regulares (RegEx).

extension = 'csv'
todos_los_archivos = [i for i in glob.glob('*.{}'.format(extension))]

# Paso 3: Combina todos los archivos en la lista y expórtalos como CSV
# Usa la librería 'pandas' para concatenar todos los archivos en la lista y exportarlos como CSV. 
# El nombre del archivo resultante será 'combined_csv.csv' y podrás encontrarlo en tu directorio de trabajo o carpeta seleccionada previamente.

#combina todos los archivos de la lista
combinado_csv = pd.concat([pd.read_csv(f) for f in todos_los_archivos ])

#exporta a csv
combinado_csv.to_csv( "combinado_csv.csv", index=False, encoding='utf-8-sig')
# El encoding = ‘utf-8-sig’ se agregó para solucionar el problema al exportar idiomas 'Non-English'.

# ¡Y eso es todo!
