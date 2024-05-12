import threading
import time
from club import ComputerClub

from datetime import datetime

def main_menu(club: ComputerClub) -> None:
    """
    Displays a menu for managing sessions, computers, and clients of a computer club.

    Parameters:
        club (ComputerClub): The computer club to manage.

    Returns:
        None
    """
    while True:
        print(club)
        print(datetime.now().strftime("%Y-%m-%d %H:%M"))
        print("\n1. Управление сессиями")
        print("2. Управление компьютерами")
        print("3. Управление клиентами")
        print("4. Выход")
        choice = input("Выберите действие: ")
        if choice == "1":
            club.manage_sessions()
        elif choice == "2":
            club.manage_computers()
        elif choice == "3":
            club.manage_clients()
        elif choice == "4":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите существующий вариант.")

def update_computer_status(club: ComputerClub):
    """
    Updates the status of all computers in the club every minute.

    Args:
        club (ComputerClub): An instance of the ComputerClub class.

    Returns:
        None
    """
    while True:
        club.update_computer_status()
        time.sleep(60)

def main():
    club = ComputerClub("Имя", "street", "number")

    update_thread = threading.Thread(target=update_computer_status, args=(club,))
    update_thread.daemon = True
    update_thread.start()

    main_menu(club)

if __name__ == "__main__":
    main()
