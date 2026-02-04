import matplotlib.pyplot as plt

def analyser_texte_debutant(chemin_fichier):

    print(f" Lecture du fichier : {chemin_fichier} ...")

    # 1. Lecture du fichier (Lecture du corpus)
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        texte = f.read()

    # 2. Nettoyage des données
    # Suppression des sauts de ligne
    texte = texte.replace('\n', ' ')
    # Normalisation de la ponctuation
    texte = texte.replace("«", " ")
    texte = texte.replace("»", " ")
    texte = texte.replace("’", "'")

    # 3. Segmentation (Découpage en phrases)
    # je remplace ? et ! par . pour couper facilement
    texte = texte.replace("?", ".")
    texte = texte.replace("!", ".")

    # Découpage du texte en liste de phrases
    phrases_brutes = texte.split(".")

    # 4. Traitement et Analyse
    phrases_finales = []
    longueurs = []

    # Boucle pour analyser chaque phrase
    for p in phrases_brutes:
        p_clean = p.strip()

        if len(p_clean) > 0:
            phrases_finales.append(p_clean)
            mots = p_clean.split()
            nb_mots = len(mots)
            longueurs.append(nb_mots)

    # 5. Calcul des statistiques (Métriques)
    total_phrases = len(phrases_finales)

    if total_phrases > 0:
        total_mots = sum(longueurs)
        moyenne = total_mots / total_phrases
    else:
        moyenne = 0

    # Affichage du rapport
    print(f"\n RÉSULTATS DE L'ANALYSE :")
    print(f"   - Nombre de phrases : {total_phrases}")
    print(f"   - Moyenne de mots par phrase : {moyenne:.2f}")

    # Verdict sur le niveau
    print(f"\n⚖️ ESTIMATION DU NIVEAU :")
    if moyenne > 25:
        print("   Niveau : Avancé (C1/C2)")
        print("   Analyse : Les phrases sont longues et complexes.")
    elif moyenne > 18:
        print("   Niveau : Intermédiaire (B2)")
        print("   Analyse : Niveau standard pour la presse.")
    else:
        print("   Niveau : Élémentaire (A1/A2/B1)")
        print("   Analyse : Les phrases sont plutôt courtes.")

    # 6. Visualisation (Graphique)
    print("\n Génération de l'histogramme...")

    plt.figure(figsize=(10, 6))
    plt.hist(longueurs, bins=10, color='#87CEEB', edgecolor='black', alpha=0.8)

    plt.title("Distribution de la longueur des phrases", fontsize=14)
    plt.xlabel("Nombre de mots par phrase")
    plt.ylabel("Fréquence")
    plt.axvline(moyenne, color='red', linestyle='--', label=f'Moyenne : {moyenne:.1f}')
    plt.legend()
    plt.show()


# Point d'entrée
if __name__ == '__main__':
    analyser_texte_debutant("news.txt")