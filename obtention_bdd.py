# Programme d'analayse d'un fichier CSV sur les recensements de 2021 et 2016 par municipalité au Canada

import pandas as pd
import matplotlib.pyplot as plt

def creer_dataframe():
    df = pd.read_csv('Census_2016_2021.csv')  # On charge le fichier csv grace au script de preprocessing
    municipalites = df[df['Type'] == 'MÉ'].reset_index(drop=True)  # Filtrage des éléments de type MÉ à partir du csv
    municipalites.head() # Création de la df
    return municipalites

def afficher_nb_municipalites(municipalites):
    print(f'\nLe nombre de municipalités est de : {municipalites.shape[0]}\n')  # On extrait le nombre de lignes de la df
    return

def calculer_population_moyenne(municipalites):

    population_moyenne_2016 = municipalites['Pop16'].mean()
    population_moyenne_2021 = municipalites['Pop21'].mean()
    print(f'Population moyenne en 2016 : {population_moyenne_2016}')
    print(f'Population moyenne en 2021 : {population_moyenne_2021}')
    return

def tracer_nuage_points(municipalites):

    municipalites['PctAcc'] = 100 * (municipalites['Pop21'] - municipalites['Pop16']) / municipalites['Pop16'] # Calcul du pourcentage d'accroissement de la population de 2016 à 2021 et créer une nouvelle colonne dans la df
    municipalites.head()

    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['font.size'] = 14
    plt.rcParams['figure.figsize'] = (12, 6)

    plt.scatter(municipalites['Pop21'],municipalites['PctAcc'])
    plt.title('Pourcentage d’accroissement de la population de 2016 à 2021 par rapport à la population en 2021')
    plt.xlabel('Population des municipalités en 2021')
    plt.ylabel('Pourcentage d’accroissement en %')
    plt.show()
    return
def classer_et_tracer_municipalites(municipalites):

    # Calcul du nombre de municipalités dans chaque catégorie de population demandée avec la fct 'sum()'
    inf2000 = (municipalites['Pop21'] < 2000).sum()
    b2000_9999 = ((municipalites['Pop21'] >= 2000) & (municipalites['Pop21'] <= 9999)).sum()
    b10000_24999 = ((municipalites['Pop21'] >= 10000) & (municipalites['Pop21'] <= 24999)).sum()
    b25000_99999 = ((municipalites['Pop21'] >= 25000) & (municipalites['Pop21'] <= 99999)).sum()
    sup100000 = (municipalites['Pop21'] >= 100000).sum()

    # Création d'une nouvelle df pour faciliter l'extraction des données
    categories = pd.DataFrame([['inférieur à 2000', inf2000], ['entre 2000 et 9999', b2000_9999], ['entre 10000 et 24999', b10000_24999],
    ['entre 25000 et 99999', b25000_99999],['supérieur à 100000', sup100000]], columns=['Catégories', 'Nombre'])
    print(f'\n{categories.head()}')

    # Traçage du diagramme en barres horizontales comme présenté dans le cours
    plt.rcParams['figure.autolayout'] = True
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['font.size'] = 14
    plt.rcParams['figure.figsize'] = (12, 6)
    categories.plot(kind='barh', y='Nombre', x='Catégories')
    plt.xlabel('Nombre de municipalités')
    plt.title('Nombre de municipalités par catégorie de population en 2021')
    plt.show()
    return

# Appel des fonctions dans l'ordre
municipalites = creer_dataframe()
afficher_nb_municipalites(municipalites)
calculer_population_moyenne(municipalites)
tracer_nuage_points(municipalites)
classer_et_tracer_municipalites(municipalites)