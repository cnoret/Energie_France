"""
Création de la page "Introduction" de l'application Énergie_France
"""

import streamlit as st

def preparation():
    "Contenu de la page de data-prep"
    st.title("Préparation des données : DF (Eco2Mix)")
    st.header("Traitement des valeurs manquantes")

    st.info("Notre jeu de données est très propre, les NaNs présents correspondent uniquement à une \
            production ou consommation nulle. Nous avons procédé en découpage par étage afin de traiter \
            séparément ces valeurs. Nous n'avons pas de duplicatas", icon = '✨')

    st.header("Modification et ajout de nouvelles colonnes")

    st.write(" - Ajout de colonnes temporelles avec DateTime ('Date - Heure', 'Jour', 'Jour_mois', 'Mois', 'Année').\n - Création d'une colonne booléenne 'Week-end'. \n - Nous avons supprimé l'année 2022 du scope, car elle n'était pas complète dans l'étude. \n - Création d'une colonne qui somme toute la 'Production (MW)'. \n - Création d'une colonne 'Côtier' pour observer les tendances des régions qui sont sur la côte. \n - Création d'une fonction qui sépare les régions du Nord de la France, de celle du Sud.")

    st.header("Création de nos jeux de données")

    st.write("Notre stratégie a été de créer des jeux de données depuis DF, pour faciliter la suite de l'étude et les visualisations : \n - 'consommation' = Toutes les données sans les données de production. \n - 'production' = Toutes les données sans la consommation. \n - 'yearly' = Un groupby sur 'Année' et 'Région', avec SUM de Consommation. \n 'tco_tch' = Nous avons traité toutes ces valeurs dans leur propre DataFrame.")

    st.header("Préparation des données de l'INSEE")

    st.write("Les données étaient sur un fichier Excel, nous avons donc du utiliser 'XLRD' et la méthode GLOBALS() ainsi que des boucles pour extraire ces données dans un DataFrame exploitable. \n \n Par la suite, les données de la population des différentes régions par années ont été ajoutées à notre DF 'yearly', puis nous avons créé le ratio 'Consommation per Capita', bâptisé 'ratio' dans ce DataFrame.")

    st.header("Préparation des données de EUROSTAT")

    st.write("Le fichier récupéré auprès de EUROSTAT était très formaté, il a donc nécessité un certain nombre de transformations pour être exploitable : \n - Une fonction pour déterminer le 'type' (Entre consommation, production, imports, etc...' \n - Une fonction pour déterminer la 'class' (Type d'énergie). \n - Un renommage complet des colonnes, \n - Une fonction pour convertir tous les noms des pays d'Europe du format ISO2, au format toutes lettres. \n - Enfin, une séparation en deux DataFrames, EUROP_CONS et EUROPE_PROD.")

    st.header("Nos codes couleurs")

    st.write("Nous avons créé deux dictionnaires, pour garder des couleurs constantes dans les visualisations : ")

    colors = {
        'Thermique (MW)': 'red',
        'Nucléaire (MW)': '#F7E237',
        'Eolien (MW)': 'lightblue',
        'Solaire (MW)': 'orange',
        'Hydraulique (MW)': 'darkblue',
        'Bioénergies (MW)': 'green'}

    st.code(colors, language= 'python' )

    colors_euro = {
    'Bioénergie': '#FF0000',  # Rouge
    'Déchets municipaux renouvelables': '#00FF00',  # Vert
    'Éolien': '#ADD8E6',  # Bleu clair
    'Solaire Photovoltaique': '#FFA500',  # Orange
    'Solaire Thermique': '#FFFF00',  # Jaune
    'Hydraulique': '#00008B',  # Bleu foncé
    'Biogaz': '#808080',  # Gris
    'Biocarburants': '#800080',  # Violet
    'Pompe à chaleur': '#FF0000',  # Rouge
    'Océan': '#0000FF',  # Bleu
    'Geothermique': '#D076FF'  # Violet
    }

    st.code(colors_euro, language= 'python')
