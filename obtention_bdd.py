import pandas as pd

df_cleaned = pd.read_csv('Census_2016_2021.csv') # On charge le fichier
municipalites = df_cleaned[df_cleaned['Type'] == 'MÉ'] # Filtrage des éléments de type MÉ

nombre_municipalites = municipalites.shape[0]
print(f'Le nombre de municipalités est : {nombre_municipalites}')

print(municipalites.head())
print(municipalites.head())