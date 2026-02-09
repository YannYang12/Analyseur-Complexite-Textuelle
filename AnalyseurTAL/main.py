import matplotlib.pyplot as plt


def analyser_texte_étudiant(chemin_fichier):
    # Lancement de l'analyse
    print(f"--- Début de l'analyse du fichier : {chemin_fichier} ---")

    # 1. Lecture du fichier (Chargement du corpus)
    # J'utilise 'utf-8' pour être sûr de bien lire les accents français
    with open(chemin_fichier, 'r', encoding='utf-8') as f:
        texte = f.read()

    # 2. Nettoyage des données (Méthode manuelle)
    # Je remplace les sauts de ligne par des espaces pour ne pas couper les mots
    texte = texte.replace('\n', ' ')
    # Je remplace les caractères spéciaux courants par des versions simples
    texte = texte.replace("«", " ")
    texte = texte.replace("»", " ")
    texte = texte.replace("’", "'")
    texte = texte.replace("...", ".")  # Pour éviter les phrases vides avec les points de suspension

    # 3. Segmentation (Découpage en phrases)
    # "笨方法" : Je remplace ? et ! par des points pour utiliser un seul séparateur
    texte = texte.replace("?", ".")
    texte = texte.replace("!", ".")

    # Découpage du texte en une liste de phrases
    phrases_brutes = texte.split(".")

    # 4. Traitement et Analyse statistique
    phrases_finales = []
    longueurs_mots = []

    # Je parcours chaque phrase pour compter les mots
    for p in phrases_brutes:
        phrase_nettoyée = p.strip()  # Enlever les espaces inutiles au début et à la fin

        # Je vérifie que la phrase n'est pas vide
        if len(phrase_nettoyée) > 0:
            phrases_finales.append(phrase_nettoyée)
            # Je coupe la phrase en mots en utilisant les espaces
            mots = phrase_nettoyée.split()
            nombre_de_mots = len(mots)
            longueurs_mots.append(nombre_de_mots)

    # 5. Calcul des métriques (Moyenne)
    total_phrases = len(phrases_finales)

    if total_phrases > 0:
        total_mots = sum(longueurs_mots)
        moyenne = total_mots / total_phrases
    else:
        moyenne = 0

    # Affichage des résultats dans la console
    print(f"\n[RÉSULTATS STATISTIQUES]")
    print(f"Nombre total de phrases : {total_phrases}")
    print(f"Moyenne de mots par phrase : {moyenne:.2f}")

    # 6. Évaluation du niveau selon le CECRL (Heuristique)
    # J'utilise la longueur moyenne des phrases comme indicateur de complexité
    print(f"\n[ESTIMATION DU NIVEAU]")
    if moyenne > 25:
        verdict = "Niveau Avancé (C1/C2)"
        commentaire = "Structure complexe avec des phrases longues."
    elif moyenne > 18:
        verdict = "Niveau Intermédiaire (B2)"
        commentaire = "Structure standard, typique de la presse française."
    else:
        verdict = "Niveau Élémentaire (A1/A2/B1)"
        commentaire = "Structure simple avec des phrases courtes."

    print(f"Verdict : {verdict}")
    print(f"Analyse : {commentaire}")

    # 7. Visualisation (Histogramme avec Matplotlib)
    print("\n[INFO] Génération de l'histogramme de distribution...")

    plt.figure(figsize=(10, 6))
    plt.hist(longueurs_mots, bins=10, color='#87CEEB', edgecolor='black', alpha=0.7)

    plt.title("Distribution de la longueur des phrases", fontsize=12)
    plt.xlabel("Nombre de mots")
    plt.ylabel("Fréquence (Nombre de phrases)")
    # Ajouter une ligne rouge pour la moyenne
    plt.axvline(moyenne, color='red', linestyle='dashed', linewidth=2, label=f'Moyenne : {moyenne:.1f}')
    plt.legend()
    plt.show()


# Lancement du programme principal
if __name__ == '__main__':
    # Remplacez "news.txt" par le nom de votre fichier texte
    try:
        analyser_texte_étudiant("news.txt")
    except FileNotFoundError:
        print("Erreur : Le fichier 'news.txt' est introuvable.")