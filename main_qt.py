import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

def main():
    app = QApplication(sys.argv)

    # Charger le fichier .ui
    loader = QUiLoader()
    ui_file = QFile("main.ui")  # Remplacez "main.ui" par le chemin de votre fichier .ui
    ui_file.open(QFile.ReadOnly)

    window = loader.load(ui_file)
    ui_file.close()

    if window is None:
        print("Erreur lors du chargement de la fenêtre.")
        sys.exit(-1)

    # Afficher la fenêtre
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()