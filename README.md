# Analyseur de Complexité Textuelle (FLE) 

## Description du projet
Ce projet est un outil développé en **Python** permettant d'analyser automatiquement la difficulté d'un texte français. Il a été conçu dans le cadre de ma préparation au master **Traitement Automatique des Langues (TAL)**.

L'objectif est d'aider les enseignants ou les linguistes à évaluer rapidement si un texte convient à un niveau A2, B1, B2 ou C1 (selon le CECRL), en se basant sur des statistiques textuelles.

## Fonctionnalités
* **Nettoyage de corpus** : Traitement des caractères spéciaux, normalisation des guillemets et de la ponctuation.
* **Segmentation (Tokenization)** : Utilisation d'expressions régulières (`Regex`) pour découper le texte en phrases et en mots.
* **Calcul de métriques** :
    * Longueur moyenne des phrases.
    * Richesse lexicale.
    * Nombre total de mots et de phrases.
* **Visualisation** : Génération d'un histogramme de distribution des longueurs de phrases avec `Matplotlib`.

## Exemple de résultat
Pour un article de presse analysé (source : *Le Monde* / Texte législatif), l'outil a détecté un niveau **Avancé (C1)** avec une moyenne de **35 mots par phrase**.

![Distribution des phrases](Figure_1.png)
*(Ci-dessus : Distribution de la longueur des phrases générée par l'outil)*

## Technologies utilisées
* **Langage** : Python 3.12
* **Bibliothèques** : `re` (Built-in), `matplotlib`
* **IDE** : PyCharm 2025

---
*Projet réalisé par [你的名字] - 2026*
