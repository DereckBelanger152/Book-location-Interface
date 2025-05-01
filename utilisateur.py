class Utilisateur:
    """Classe représentant un utilisateur de la bibliothèque.

    Attributes:
        nom (str): Nom de famille de l'utilisateur
        prenom (str): Prénom de l'utilisateur
        id_utilisateur (str): Identifiant unique de l'utilisateur
        documents_empruntes (list): Liste des documents empruntés par l'utilisateur (liste vide par défaut)
    """

    def __init__(self, nom, prenom, id_utilisateur):
        """Initialise un nouvel utilisateur.

        Args:
            nom (str): Nom de famille
            prenom (str): Prénom
            id_utilisateur (str): Identifiant unique
        """
        self.nom = nom
        self.prenom = prenom
        self.id_utilisateur = id_utilisateur
        self.documents_empruntes = []

    def emprunter_document(self, document):
        """Permet à l'utilisateur d'emprunter un document.

        Args:
            document (Document): Le document à emprunter

        Returns:
            bool: True si l'emprunt a réussi, False sinon
        """
        if document.disponible:
            document.emprunter()
            self.documents_empruntes.append(document)
            return True
        return False

    def retourner_document(self, document):
        """Permet à l'utilisateur de retourner un document.

        Args:
            document (Document): Le document à retourner

        Returns:
            bool: True si le retour a réussi, False sinon
        """
        if document in self.documents_empruntes:
            document.retourner()
            self.documents_empruntes.remove(document)
            return True
        return False

    def __str__(self):
        """Retourne une représentation textuelle de l'utilisateur.

        Returns:
            str: Description de l'utilisateur
        """
        return f"{self.prenom} {self.nom} (ID: {self.id_utilisateur})"


from document import Document
from utilisateur import Utilisateur

def test_emprunter_document():
    """Teste l'emprunt d'un document par un utilisateur."""
    utilisateur = Utilisateur("Doe", "John", "U12345")
    document = Document("Titre Test", "Auteur Test", 2023, "CODE-TEST")

    # Test emprunt d'un document disponible
    assert utilisateur.emprunter_document(document) == True, "L'emprunt d'un document disponible devrait réussir"
    assert document in utilisateur.documents_empruntes, "Le document devrait être ajouté à la liste des documents empruntés"
    assert document.disponible == False, "Le document ne devrait plus être disponible après emprunt"

    # Test emprunt d'un document non disponible
    assert utilisateur.emprunter_document(document) == False, "L'emprunt d'un document non disponible devrait échouer"

    print("Test de l'emprunt de document réussi!")


def test_retourner_document():
    """Teste le retour d'un document par un utilisateur."""
    utilisateur = Utilisateur("Doe", "John", "U12345")
    document = Document("Titre Test", "Auteur Test", 2023, "CODE-TEST")

    # Ajouter le document à la liste des emprunts
    utilisateur.emprunter_document(document)

    # Test retour d'un document emprunté
    assert utilisateur.retourner_document(document) == True, "Le retour d'un document emprunté devrait réussir"
    assert document not in utilisateur.documents_empruntes, "Le document devrait être retiré de la liste des documents empruntés"
    assert document.disponible == True, "Le document devrait être disponible après retour"

    # Test retour d'un document non emprunté
    assert utilisateur.retourner_document(document) == False, "Le retour d'un document non emprunté devrait échouer"

    print("Test du retour de document réussi!")


def test_str_utilisateur():
    """Teste la méthode __str__ de la classe Utilisateur."""
    utilisateur = Utilisateur("Doe", "John", "U12345")
    assert str(utilisateur) == "John Doe (ID: U12345)", "La méthode __str__ ne retourne pas la bonne représentation"
    print("Test de la méthode __str__ réussi!")


# Exécution des tests
if __name__ == "__main__":
    print("Début des tests pour la classe Utilisateur")
    test_emprunter_document()
    test_retourner_document()
    test_str_utilisateur()
    print("Tous les tests pour la classe Utilisateur ont été passés avec succès!")
