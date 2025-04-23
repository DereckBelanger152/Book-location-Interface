from livre import Livre
from revue import Revue
from utilisateur import Utilisateur

def charger_livres(fichier):
    """Charge les livres à partir d'un fichier texte.

    Args:
        fichier (str): Chemin vers le fichier contenant les informations des livres.

    Returns:
        list[Livre]: Liste des objets Livre créés.
    """
    livres = []
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                # Format attendu : titre;auteur;annee;code_unique;nb_pages
                titre, auteur, annee, code_unique, nb_pages = ligne.strip().split(";")
                livre = Livre(titre, auteur, int(annee), code_unique, int(nb_pages))
                livres.append(livre)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier} est introuvable.")
    return livres


def charger_revues(fichier):
    """Charge les revues à partir d'un fichier texte.

    Args:
        fichier (str): Chemin vers le fichier contenant les informations des revues.

    Returns:
        list[Revue]: Liste des objets Revue créés.
    """
    revues = []
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                # Format attendu : titre;auteur;annee;code_unique;numero;frequence
                titre, auteur, annee, code_unique, numero, frequence = ligne.strip().split(";")
                revue = Revue(titre, auteur, int(annee), code_unique, int(numero), frequence)
                revues.append(revue)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier} est introuvable.")
    return revues


def charger_utilisateurs(fichier):
    """Charge les utilisateurs à partir d'un fichier texte.

    Args:
        fichier (str): Chemin vers le fichier contenant les informations des utilisateurs.

    Returns:
        list[Utilisateur]: Liste des objets Utilisateur créés.
    """
    utilisateurs = []
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            for ligne in f:
                # Format attendu : nom;prenom;id_utilisateur
                nom, prenom, id_utilisateur = ligne.strip().split(";")
                utilisateur = Utilisateur(nom, prenom, id_utilisateur)
                utilisateurs.append(utilisateur)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {fichier} est introuvable.")
    return utilisateurs