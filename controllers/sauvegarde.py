import sqlite3

class Sauvegarde:
    def __init__(self, db_path="data/sauvegarde.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.creer_tables()

    def creer_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS plantes (
            nom TEXT,
            eau INTEGER,
            lumiere INTEGER,
            croissance INTEGER,
            fertilite INTEGER
        )
        """)
        self.conn.commit()

    def sauvegarder_jardin(self, jardin):
        self.cursor.execute("DELETE FROM plantes")
        for plante in jardin.plantes:
            self.cursor.execute("""
            INSERT INTO plantes (nom, eau, lumiere, croissance, fertilite)
            VALUES (?, ?, ?, ?, ?)
            """, (plante.nom, plante.eau, plante.lumiere, plante.croissance, plante.fertilite))
        self.conn.commit()

    def charger_jardin(self, jardin, classes_plantes):
        self.cursor.execute("SELECT * FROM plantes")
        lignes = self.cursor.fetchall()
        jardin.plantes.clear()
        for ligne in lignes:
            nom, eau, lumiere, croissance, fertilite = ligne
            if nom.lower() in classes_plantes:
                plante = classes_plantes[nom.lower()]()
                plante.eau = eau
                plante.lumiere = lumiere
                plante.croissance = croissance
                plante.fertilite = fertilite
                jardin.ajouter_plante(plante)

    def reinitialiser_sauvegarde(self):
        self.cursor.execute("DELETE FROM plantes")
        self.conn.commit()

    def fermer(self):
        self.conn.close()
