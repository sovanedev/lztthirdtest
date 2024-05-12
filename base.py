import sqlite3

class Database:
    def __init__(self, db_name="computer_club.db"):
        """
        Initializes a new instance of the Database class.

        Parameters:
            db_name (str): The name of the database file. Defaults to "computer_club.db".

        Returns:
            None
        """
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """
        Creates the necessary tables in the database if they do not already exist.

        Parameters:
        - self: The current instance of the Database class.

        Returns:
        - None
        """
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
                                id INTEGER PRIMARY KEY,
                                full_name TEXT NOT NULL,
                                phone_number TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS computers (
                                id INTEGER PRIMARY KEY,
                                configuration TEXT NOT NULL,
                                last_service_date TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS sessions (
                                id INTEGER PRIMARY KEY,
                                computer_id INTEGER NOT NULL,
                                client_id INTEGER NOT NULL,
                                start_time TEXT NOT NULL,
                                end_time TEXT NOT NULL,
                                FOREIGN KEY (computer_id) REFERENCES computers(id),
                                FOREIGN KEY (client_id) REFERENCES clients(id))''')

        self.connection.commit()

    def get_clients(self):
        self.cursor.execute("SELECT * FROM clients")
        return self.cursor.fetchall()

    def get_computers(self):
        self.cursor.execute("SELECT * FROM computers")
        return self.cursor.fetchall()

    def get_sessions(self):
        self.cursor.execute("SELECT * FROM sessions")
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()