class Client:
    def __init__(self, id, full_name, phone_number):
        """
        Initializes a new instance of the Client class.

        Args:
            id (int): The unique identifier of the client.
            full_name (str): The full name of the client.
            phone_number (str): The phone number of the client.

        Returns:
            None
        """
        self.id = id
        self.full_name = full_name
        self.phone_number = phone_number

    def __str__(self):
        return f"Клиент ID: {self.id}, ФИО: {self.full_name}, Телефон: {self.phone_number}"

class Computer:
    def __init__(self, id, configuration, last_service_date):
        """
        Initializes a new instance of the Computer class.

        Args:
            id (int): The unique identifier of the computer.
            configuration (str): The configuration of the computer.
            last_service_date (str): The date of the last service performed on the computer.

        Returns:
            None
        """
        self.id = id
        self.configuration = configuration
        self.last_service_date = last_service_date
        self.is_busy = False

    def __str__(self):
        return f"Компьютер ID: {self.id} (Конфигурация: {self.configuration}, Последнее обслуживание: {self.last_service_date}, Занят: {'да' if self.is_busy else 'нет'})"

class Session:
    def __init__(self, id, computer_id, client_id, start_time, end_time):
        """
        Initializes a new instance of the Session class.

        Args:
            id (int): The unique identifier of the session.
            computer_id (int): The unique identifier of the computer associated with the session.
            client_id (int): The unique identifier of the client associated with the session.
            start_time (str): The start time of the session.
            end_time (str): The end time of the session.

        Returns:
            None
        """
        self.id = id
        self.computer_id = computer_id
        self.client_id = client_id
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"Сессия ID: {self.id} (Компьютер: {self.computer_id}, Клиент: {self.client_id}, Время начала: {self.start_time}, Время окончания: {self.end_time})"