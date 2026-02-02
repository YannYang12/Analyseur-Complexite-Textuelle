import re
import matplotlib.pyplot as plt


def analyser_texte_final(chemin_fichier):
    """
    Analyse de la complexité textuelle et visualisation des données.
    (文本复杂度分析与数据可视化)
    """
    print(f"📂 Lecture du fichier (正在读取文件): {chemin_fichier} ...")

    try:
        # 1. Lecture du fichier (读取文件)
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            texte = f.read()

        # 2. Nettoyage des données (数据清洗)
        # Remplacer les sauts de ligne par des espaces (去掉换行符)
        texte_clean = texte.replace('\n', ' ')
        # Traitement des guillemets et apostrophes (处理引号和撇号)
        texte_clean = texte_clean.replace("«", " ").replace("»", " ").replace("’", "'")

        # 3. Segmentation en phrases (句子切分)
        # Utilisation d'expressions régulières (使用正则表达式)
        phrases = re.split(r'[.?!]', texte_clean)
        # Filtrer les phrases vides (过滤空句子)
        phrases = [p.strip() for p in phrases if p.strip() != ""]

        # 4. Calcul de la longueur des phrases (计算句长)
        longueurs = []
        for p in phrases:
            mots = p.split()
            longueurs.append(len(mots))

        # 5. Calcul des statistiques (计算统计指标)
        total_phrases = len(phrases)
        if total_phrases > 0:
            moyenne = sum(longueurs) / total_phrases
        else:
            moyenne = 0

        print(f"\n📊 RÉSULTATS (结果):")
        print(f"   - Nombre total de phrases (总句数): {total_phrases}")
        print(f"   - Moyenne mots/phrase (平均句长): {moyenne:.2f}")

        # 6. Visualisation (可视化)
        print("🎨 Génération du graphique...")

        plt.figure(figsize=(10, 6))

        # Histogramme (直方图)
        plt.hist(longueurs, bins=10, color='#87CEEB', edgecolor='black', alpha=0.8)

        # Titres et labels en Français (全法语标签)
        plt.title("Distribution de la longueur des phrases", fontsize=14, fontweight='bold')
        plt.xlabel("Nombre de mots par phrase", fontsize=12)
        plt.ylabel("Fréquence (Nombre de phrases)", fontsize=12)

        # Ligne de moyenne (平均线)
        plt.axvline(moyenne, color='red', linestyle='dashed', linewidth=1.5, label=f'Moyenne: {moyenne:.1f}')

        plt.legend()
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()

        # 显示图表
        plt.show()

    except FileNotFoundError:
        print("❌ Erreur: Fichier introuvable.")
    except Exception as e:
        print(f"❌ Erreur inconnue: {e}")


if __name__ == '__main__':
    analyser_texte_final("news.txt")