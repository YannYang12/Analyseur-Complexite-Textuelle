import re
import matplotlib.pyplot as plt

def analyser_complexite_textuelle(chemin_fichier):
    """
    Fonction principale pour analyser la complexité d'un texte français.
    Étapes : Lecture, Nettoyage, Segmentation, Calculs statistiques et Visualisation.
    """
    print(f"📂 Lecture du fichier en cours : {chemin_fichier} ...")

    try:
        # 1. Lecture du fichier (Gestion des entrées/sorties)
        # Utilisation de 'with' pour une fermeture automatique du fichier
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            texte = f.read()

        # 2. Prétraitement et Nettoyage du corpus (Pre-processing)
        # Suppression des sauts de ligne pour obtenir un texte continu
        texte_clean = texte.replace('\n', ' ')
        
        # Normalisation de la ponctuation :
        # - Remplacement des guillemets français (« ») par des espaces
        # - Uniformisation des apostrophes (’) vers l'apostrophe standard (')
        texte_clean = texte_clean.replace("«", " ").replace("»", " ").replace("’", "'")

        # 3. Segmentation en phrases (Tokenization des phrases)
        # Utilisation d'une expression régulière (Regex) pour couper sur . ? !
        phrases = re.split(r'[.?!]', texte_clean)
        # Filtrage : suppression des chaînes vides générées par le split
        phrases = [p.strip() for p in phrases if p.strip() != ""]
        
        # 4. Extraction des caractéristiques (Feature Extraction)
        # Calcul de la longueur de chaque phrase (en nombre de mots)
        longueurs = [] 
        for p in phrases:
            # Segmentation en mots basée sur les espaces
            mots = p.split()
            longueurs.append(len(mots))

        # 5. Calcul des métriques globales
        total_phrases = len(phrases)
        if total_phrases > 0:
            moyenne = sum(longueurs) / total_phrases
        else:
            moyenne = 0

        # Affichage du rapport d'analyse dans la console
        print(f"\n📊 RAPPORT D'ANALYSE LINGUISTIQUE :")
        print(f"   - Nombre total de phrases : {total_phrases}")
        print(f"   - Moyenne de mots par phrase : {moyenne:.2f}")
        print(f"   - Phrase la plus longue : {max(longueurs)} mots")

        # 6. Visualisation des données (Data Visualization)
        print("🎨 Génération du graphique de distribution...")
        
        plt.figure(figsize=(10, 6))
        
        # Création de l'histogramme
        plt.hist(longueurs, bins=10, color='#87CEEB', edgecolor='black', alpha=0.8)
        
        # Configuration des labels en français
        plt.title("Distribution de la longueur des phrases (Corpus Journalistique)", fontsize=14, fontweight='bold')
        plt.xlabel("Nombre de mots par phrase", fontsize=12)
        plt.ylabel("Fréquence", fontsize=12)
        
        # Ajout de la ligne verticale indiquant la moyenne
        plt.axvline(moyenne, color='red', linestyle='dashed', linewidth=1.5, label=f'Moyenne : {moyenne:.1f}')
        
        plt.legend()
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        
        # Affichage de la fenêtre graphique
        plt.show()

    except FileNotFoundError:
        print("❌ Erreur critique : Le fichier spécifié est introuvable.")
        print("-> Vérifiez que le fichier se trouve bien dans le dossier du projet.")
    except Exception as e:
        print(f"❌ Une erreur inattendue est survenue : {e}")

# Point d'entrée du script
if __name__ == '__main__':
    analyser_complexite_textuelle("news.txt")
