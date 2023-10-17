# Bibliothèque de Gestion de Tâches

Une bibliothèque Python pour la gestion efficace des tâches, des projets et des ressources.

## Table des matières

- [Bibliothèque de Gestion de Tâches](#bibliothèque-de-gestion-de-tâches)
  - [Table des matières](#table-des-matières)
  - [Description du projet](#description-du-projet)
  - [Installation](#installation)
  - [Utilisation](#utilisation)
  - [Exemples d'utilisation](#exemples-dutilisation)
  - [Contributions](#contributions)
  - [Auteurs](#auteurs)


## Description du projet

Créez une application de gestion de tâches en utilisant Python.

L'application doit permettre à l'utilisateur de :
- Ajouter une nouvelle tâche à la liste avec à minima un nom et une description
- Marquer une tâche comme terminée.
- Supprimer une tâche de la liste.
- Afficher la liste des tâches en cours.

## Installation

Pour installer cette bibliothèque, suivez ces étapes :

1. Clonez le dépôt depuis GitHub.
2. Naviguez vers le répertoire du projet : cd nom-du-repertoire-du-projet
3. Créez un environnement virtuel avec la commande : python3 -m venv venv
4. Activez votre environnement avec la commande : source venv/bin/activate
5. Installez les dépendances en exécutant la commande suivante : pip install -r requirements.txt


## Utilisation

Voici comment utiliser cette bibliothèque :

1. Importez la classe `TaskList` dans votre code.
2. Créez une instance de `TaskList`.
3. Utilisez les méthodes de la classe `TaskList` pour ajouter, marquer comme terminée, supprimer des tâches et afficher la liste des tâches en cours.

## Exemples d'utilisation

Voici quelques exemples d'utilisation de la bibliothèque :

```python
# Utilisation de la classe TaskList pour ajouter une tâche
task_list = TaskList()
task_list.add_task("Faire les courses", "Acheter du lait et du pain")
# Utilisation de la classe TaskList pour marquer une tâche comme terminée
task_list.mark_task_completed("Faire les courses")
# Utilisation de la classe TaskList pour supprimer une tâche
task_list.remove_task("Faire les courses")
# Utilisation de la classe TaskList pour afficher la liste des tâches en cours
task_list.display_tasks()
```

## Contributions

Les contributions sont les bienvenues ! Pour contribuer à ce projet, suivez ces étapes :

Fork le projet.
Créez une branche pour votre fonctionnalité (git checkout -b ma-nouvelle-fonctionnalite).
Commit et poussez vos modifications (git commit -m 'Ajout de ma nouvelle fonctionnalité').
Créez une demande d'extraction.

## Auteurs

Alban Pereira - alban.pereira98@gmail.com
Yuchen Xia - xiayuchen35@gmail.com
Aurélien Raulo - aurelien0raulo@gmail.com
Salimatou Traore - tra.salimatou@gmail.com