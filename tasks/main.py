from .tasklist import TaskList
from logs import configure_logging

import logging

configure_logging()

def display_menu():
    print("\nMenu :")
    print("1. Ajouter une tâche")
    print("2. Supprimer une tâche")
    print("3. Marquer une tâche comme terminée")
    print("4. Afficher la liste des tâches en cours")
    print("5. Afficher la liste des tâches archivées")
    print("6. Quitter")


def main():
    task_list = TaskList()

    while True:
        display_menu()
        choice = input("Entrez le numéro de votre choix : ")

        if choice == "1":
            try:
                name = input("Nom de la tâche : ")
                description = input("Description de la tâche : ")
                task_list.add_task(name, description)
                print(f"Tâche '{name}' ajoutée à la liste.")
            except ValueError as e:
                print(f"Erreur: {e}")
        elif choice == "2":
            task_name = input("Nom de la tâche à supprimer : ")
            task_list.remove_task(task_name)
            print(f"Tâche '{task_name}' supprimée de la liste.")
        elif choice == "3":
            task_name = input("Nom de la tâche à marquer comme terminée : ")
            task_list.mark_task_completed(task_name)
            print(f"Tâche '{task_name}' marquée comme terminée.")
        elif choice == "4":
            print("Liste des tâches en cours :")
            task_list.display_tasks()
        elif choice == "5":
            print("Liste des tâches archivées :")
            task_list.display_archived_tasks()
        elif choice == "6":
            break
        else:
            print("Choix non valide. Veuillez entrer un numéro valide.")


if __name__ == "__main__":
    main()
