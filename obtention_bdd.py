import pandas as pd

df = pd.read_csv('Census_2016_2021.csv') # On charge le fichier

def afficher_dataframe():
    municipalites = df[df['Type'] == 'MÉ'].reset_index(drop=True)  # Filtrage des éléments de type MÉ
    print(f'Le nombre de municipalités est : {municipalites.shape[0]}\n')
    print(municipalites.head())
    return municipalites

afficher_dataframe()
