from classes import Client, Computer, Session
from base import Database
from datetime import datetime

class ComputerClub:
    def __init__(self, name, address, phone_number):
        """
        Initializes a new instance of the ComputerClub class.

        Args:
            name (str): The name of the computer club.
            address (str): The address of the computer club.
            phone_number (str): The phone number of the computer club.

        Returns:
            None
        """
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.db = Database()
        self.clients = self.load_clients()
        self.computers = self.load_computers()
        self.sessions = self.load_sessions()

    def __str__(self):
        return f"Клуб: {self.name}, Адрес: {self.address}, Телефон: {self.phone_number}"

    # clients
    def manage_clients(self):
        while True:
            print("\n1. Просмотреть список клиентов")
            print("2. Добавить нового клиента")
            print("3. Редактировать информацию о клиенте")
            print("4. Удалить клиента")
            print("5. Вернуться в главное меню")
            choice = input("Выберите действие: ")
            if choice == "1":
                self.show_clients()
            elif choice == "2":
                self.add_client()
            elif choice == "3":
                self.edit_client()
            elif choice == "4":
                self.delete_client()
            elif choice == "5":
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите существующий вариант.")

    def add_client(self):
        full_name = input("Введите ФИО клиента: ")
        phone_number = input("Введите номер телефона клиента: ")
        self.db.cursor.execute("INSERT INTO clients (full_name, phone_number) VALUES (?, ?)", (full_name, phone_number))
        self.db.connection.commit()
        print("Информация о клиенте добавлена в базу данных.")

    def delete_client(self):
        self.show_clients()
        client_id = int(input("Выберите ID клиента: "))
        if client_id in [client.id for client in self.clients]:
            self.db.cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
            self.db.connection.commit()
            print("Клиент успешно удален из базы данных.")
        else:
            print("Такого клиента нет в базе данных.")

    def edit_client(self):
        self.show_clients()
        client_id = int(input("Выберите ID клиента: "))
        if client_id in [client.id for client in self.clients]:
            full_name = input("Введите новое ФИО клиента: ")
            phone_number = input("Введите новый номер телефона клиента: ")
            self.db.cursor.execute("UPDATE clients SET full_name = ?, phone_number = ? WHERE id = ?", (full_name, phone_number, client_id))
            self.db.connection.commit()
            print("Информация о клиенте обновлена в базе данных.")
        else:
            print("Такого клиента нет в базе данных.")

    def show_clients(self):
        self.clients = self.load_clients()
        print("Список клиентов:")
        for client in self.clients:
            print(f"ID: {client.id}, ФИО: {client.full_name}, Телефон: {client.phone_number}")

    #computers

    def manage_computers(self):
        while True:
            print("\n1. Просмотреть список компьютеров")
            print("2. Добавить новоый компьютер")
            print("3. Редактировать информацию о компьютере")
            print("4. Удалить компьютер")
            print("5. Вернуться в главное меню")
            choice = input("Выберите действие: ")
            if choice == "1":
                self.show_computers()
            elif choice == "2":
                self.add_computer()
            elif choice == "3":
                self.edit_computer()
            elif choice == "4":
                self.delete_computer()
            elif choice == "5":
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите существующий вариант.")

    def add_computer(self):
        configuration = input("Введите конфигурацию компьютера: ")
        last_service_date = input("Введите дату последнего сервисного обслуживания (гггг-мм-дд): ")
        self.db.cursor.execute("INSERT INTO computers (configuration, last_service_date) VALUES (?, ?)", (configuration, last_service_date))
        self.db.connection.commit()
        print("Информация о компьютере добавлена в базу данных.")

    def show_computers(self):
        self.computers = self.load_computers()
        self.update_computer_status()
        print("Список компьютеров:")
        for computer in self.computers:
            print(computer)

    def show_available_computers(self):
        self.computers = self.load_computers()
        self.update_computer_status()
        print("Свободные компьютеры:")
        for computer in self.computers:
            if not computer.is_busy:
                print(computer)
    
    def edit_computer(self):
        self.show_computers()
        computer_id = int(input("Выберите ID компьютера: "))
        if computer_id in [computer.id for computer in self.computers]:
            configuration = input("Введите новую конфигурацию компьютера: ")
            last_service_date = input("Введите новую дату последнего сервисного обслуживания (гггг-мм-дд): ")
            self.db.cursor.execute("UPDATE computers SET configuration = ?, last_service_date = ? WHERE id = ?", (configuration, last_service_date, computer_id))
            self.db.connection.commit()
            print("Информация о компьютере обновлена в базе данных.")
        else:
            print("Такого компьютера нет в базе данных.")
    
    def delete_computer(self):
        self.show_computers()
        computer_id = int(input("Выберите ID компьютера: "))
        if computer_id in [computer.id for computer in self.computers]:
            self.db.cursor.execute("DELETE FROM computers WHERE id = ?", (computer_id,))
            self.db.connection.commit()
            print("Компьютер успешно удален из базы данных.")
        else:
            print("Такого компьютера нет в базе данных.")

    def update_computer_status(self):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        for computer in self.computers:
            for session in self.sessions:
                if session.computer_id == computer.id and session.start_time <= current_time <= session.end_time:
                    computer.is_busy = True
                    break
            else:
                computer.is_busy = False

    #sessions

    def manage_sessions(self):
        while True:
            print("\n1. Просмотреть список сессий")
            print("2. Добавить новую сессию")
            print("3. Редактировать сессию")
            print("4. Удалить сессию")
            print("5. Вернуться в главное меню")
            choice = input("Выберите действие: ")
            if choice == "1":
                self.show_session_history()
            elif choice == "2":
                self.create_session()
            elif choice == "3":
                self.edit_session()
            elif choice == "4":
                self.delete_session()
            elif choice == "5":
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите существующий вариант.")

    def create_session(self):
        self.show_clients()
        client_id = int(input("Выберите ID клиента: "))
        if client_id in [client.id for client in self.clients]:
            self.show_available_computers()
            computer_id = int(input("Выберите ID компьютера: "))
            if computer_id in [computer.id for computer in self.computers]:
                start_time = input("Введите время начала сессии (гггг-мм-дд чч:мм): ")
                end_time = input("Введите время окончания сессии (гггг-мм-дд чч:мм): ")

                for session in self.sessions:
                    if session.computer_id == computer_id:
                        if (start_time <= session.start_time <= end_time) or (start_time <= session.end_time <= end_time):
                            print("Ошибка: новая сессия пересекается с существующей.")
                            return

                self.db.cursor.execute("INSERT INTO sessions (computer_id, client_id, start_time, end_time) VALUES (?, ?, ?, ?)",
                                    (computer_id, client_id, start_time, end_time))
                self.db.connection.commit()
                print("Сессия успешно создана.")
                self.update_computer_status()
            else:
                print("Некорректный выбор компьютера.")
        else:
            print("Некорректный выбор клиента.")


    def edit_session(self):
        self.show_session_history()
        session_id = int(input("Выберите ID сессии: "))
        if session_id in [session.id for session in self.sessions]:
            computer_id = int(input("Выберите ID компьютера: "))
            client_id = int(input("Выберите ID клиента: "))
            start_time = input("Введите время начала сессии (гггг-мм-дд чч:мм): ")
            end_time = input("Введите время окончания сессии (гггг-мм-дд чч:мм): ")
            self.db.cursor.execute("UPDATE sessions SET computer_id = ?, client_id = ?, start_time = ?, end_time = ? WHERE id = ?",
                                   (computer_id, client_id, start_time, end_time, session_id))
            self.db.connection.commit()
            print("Сессия успешно обновлена.")
        else:
            print("Некорректный выбор сессии.")
        
    def delete_session(self):
        self.show_session_history()
        session_id = int(input("Выберите ID сессии: "))
        if session_id in [session.id for session in self.sessions]:
            self.db.cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
            self.db.connection.commit()
            print("Сессия успешно удалена.")
        else:
            print("Некорректный выбор сессии.")

    def show_session_history(self):
        self.sessions = self.load_sessions()
        if self.sessions:
            print("История сессий:")
            for session in self.sessions:
                print(session)
        else:
            print("История сессий пуста.")

    #loaders

    def load_clients(self):
        clients = []
        rows = self.db.get_clients()
        for row in rows:
            client = Client(row[0],row[1], row[2])
            clients.append(client)
        return clients

    def load_computers(self):
        computers = []
        rows = self.db.get_computers()
        for row in rows:
            computer = Computer(row[0], row[1], row[2])
            computers.append(computer)
        return computers

    def load_sessions(self):
        sessions = []
        rows = self.db.get_sessions()
        for row in rows:
            session = Session(row[0], row[1], row[2], row[3], row[4])
            sessions.append(session)
        return sessions