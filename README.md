# examen : Projet Final
# **Introduction**
Ce projet représente une collaboration intensive entre les 3 membres de notre team, axée sur l'application de techniques avancées de clustering et de réduction de dimensionnalité à un ensemble de données textuelles. L'objectif principal était d'évaluer et de comparer la performance de diverses méthodes de réduction de dimensionnalité, telles que l'ACP, TSNE, et UMAP, couplées au clustering avec HDBSCAN. Un aspect clé de ce projet a été l'utilisation efficace des outils de développement collaboratif modernes. En particulier, Git et GitHub ont été employés pour la gestion du code et la collaboration entre les membres de l'équipe, tandis que Docker a été utilisé pour garantir un environnement de développement cohérent et reproductible. Cette approche a permis une intégration fluide du travail, malgré la complexité des tâches et la diversité des techniques utilisées. Les résultats, évalués par les scores NMI et ARI, ont non seulement fourni des insights précieux sur les techniques de clustering dans le traitement de données textuelles, mais ont également démontré l'efficacité de notre méthodologie de travail collaboratif dans le contexte d'un projet de science des données complexe.

# **Méthodologie**

## *Gestion du Projet et Collaboration*
Le projet a été géré en utilisant une approche collaborative moderne, s'appuyant sur des outils de développement de pointe pour faciliter la communication, la coordination et le suivi des progrès entre les membres de l'équipe.


*   **Utilisation de Git et GitHub :**  Pour la gestion de version et la collaboration, nous avons utilisé Git avec GitHub. Cela nous a permis de maintenir un historique clair des modifications, de gérer efficacement les contributions simultanées des membres de l'équipe et de résoudre les conflits de manière structurée. Des branches distinctes ont été créées pour chaque fonctionnalité majeure, assurant ainsi une organisation claire et évitant les interférences dans le code principal.

*   **Développement avec Docker :** Docker a été utilisé pour créer un environnement de développement uniforme pour tous les membres de l'équipe. Cela a assuré la cohérence et la reproductibilité des résultats, indépendamment des configurations de machines individuelles. Les conteneurs Docker ont été configurés pour inclure toutes les dépendances nécessaires, permettant ainsi une installation et une mise en route aisées pour tous les développeurs.


## *Techniques de Réduction de Dimensionnalité et de Clustering*
Le cœur du projet consistait à appliquer des méthodes de réduction de dimensionnalité et de clustering sur un ensemble de données textuelles, avec l'objectif de comparer leur efficacité.
*   **Réduction de Dimensionnalité :** Nous avons exploré trois techniques différentes :

  * ***Analyse en Composantes Principales (ACP) :*** Utilisée pour transformer les données en un espace de dimension inférieure tout en conservant le maximum de variance.
  * ***t-distributed stochastic neighbor embedding (TSNE) :*** Appliquée pour analyser et réduire les dimensions des données .
  * ***Uniform Manifold Approximation and Projection (UMAP) :*** Employée pour la réduction de dimension non linéaire, adaptée aux structures complexes des données.

* **Clustering avec HDBSCAN :** Après la réduction de dimension, nous avons utilisé HDBSCAN, un algorithme de clustering basé sur la densité, pour regrouper les données. Contrairement à k-means, HDBSCAN ne nécessite pas de spécifier le nombre de clusters à l'avance et est capable d'identifier les points de bruit.

*   **Validation des Modèles :** Pour évaluer de manière approfondie l'efficacité de nos méthodes de clustering, nous avons adopté une approche similaire à une cross-validation. Cette approche impliquait d'itérer sur l'apprentissage en modifiant à chaque fois le nombre de clusters (K) pour chaque méthode de réduction de dimension (ACP, TSNE, UMAP). À chaque itération, nous avons sauvegardé les valeurs des scores NMI et ARI. Cette méthode nous a permis de comprendre non seulement la performance de chaque combinaison de réduction de dimension et de clustering pour un nombre spécifique de clusters, mais aussi de voir comment cette performance varie avec différents nombres de clusters.
À la fin de ces itérations, nous avons calculé la moyenne des scores NMI et ARI pour chaque méthode, fournissant ainsi une évaluation quantitative globale de leur efficacité.

## Évaluation des Performances
Pour évaluer la performance des différents modèles de clustering, nous avons utilisé deux métriques principales :
*   **Normalized Mutual Information (NMI) :** Mesure l'information partagée entre les clusters prédits et les véritables étiquettes des données.
*   **Adjusted Rand Index (ARI) :** Fournit une mesure de la similarité entre les clusters prédits et les véritables étiquettes, corrigée pour le hasard.

# **Développement**
## *Processus de Développement*
Le développement de notre projet a été structuré en plusieurs phases clés, chacune nécessitant une attention particulière à différents aspects de la science des données et de l'ingénierie logicielle.
*   **Initialisation et Configuration de l'Environnement :** Nous avons commencé par configurer notre environnement de développement, en mettant l'accent sur Docker pour assurer une uniformité entre les machines de tous les développeurs. Les conteneurs Docker ont été configurés pour inclure toutes les dépendances nécessaires, ce qui a permis à chaque membre de l'équipe de travailler dans un environnement cohérent et contrôlé.

* **Gestion du Code avec Git et GitHub :** Pour gérer efficacement le code source, nous avons utilisé Git avec des branches dédiées pour chaque grande fonctionnalité. Cela nous a permis de travailler sur différents aspects du projet simultanément sans perturber le code de base. Les pull requests et les revues de code sur GitHub ont joué un rôle clé dans notre processus de collaboration, assurant la qualité et la cohérence du code.
## *Gestion et Préparation des Données*
Une partie intégrante de notre développement a impliqué la mise en œuvre de stratégies efficaces pour la gestion des données. En particulier, nous avons pris les mesures suivantes :

* **Stockage et Sérialisation des Données :** Afin d'optimiser l'efficacité du processus de développement, nous avons stocké le dataset 20 Newsgroups sous forme d'objet pickle dans notre image Docker. Cela nous a permis de charger les données de manière plus rapide et fiable, en les lisant directement à partir du système de fichiers local de l'image, réduisant ainsi la nécessité de téléchargements répétitifs.

* **Chargement Conditionnel des Données :** Nous avons mis en place une logique de chargement des données qui tente d'abord de charger le dataset à partir de la cache locale. Si le chargement échoue, par exemple en cas de fichier manquant ou corrompu, le système est conçu pour récupérer le dataset à distance. Cette approche garantit la disponibilité continue des données nécessaires pour l'apprentissage et l'évaluation des modèles sans interruption.

* **Intégration des Données avec Docker :** La sérialisation et le stockage des données dans Docker ont été essentiels pour assurer la portabilité et la reproductibilité du projet. Cela a facilité la mise en place d'un environnement de développement cohérent pour tous les membres de l'équipe et a permis de gagner un temps précieux lors des itérations de développement.

