

"""
Ce module contient le hook de post-génération pour Cookiecutter.
Il s'exécute après la génération du projet pour initialiser Git et installer les dépendances.
"""
import subprocess
import sys


def run_command(command):
    """
    Exécute une commande shell et affiche un message d'erreur en cas d'échec.

    Args:
        command (str): La commande à exécuter.
    """
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError:
        print(f"[!] Erreur lors de l'exécution de : {command}")



if __name__ == "__main__":
    print("\n[+] Initialisation du dépôt Git...")
    run_command("git init")
    run_command("git add .")
    run_command("git commit -m 'feat: Initial commit from template'")

    print("\n[+] Installation des dépendances avec uv...")
    run_command("uv sync")

    print("\n[v] Projet prêt ! Tape 'cd {{ cookiecutter.project_slug }}'")