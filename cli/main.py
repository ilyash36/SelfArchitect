
from pathlib import Path

from core.user import User
from modules.text_tools.cleaner import clean_and_format, normalize_email
from utils.storage import load_users, save_users


DATA_FILE = Path("data/data.json")


def _load_users() -> list[User]:
    return [User.from_dict(u) for u in load_users(DATA_FILE)]


def _save_users(users: list[User]) -> None:
    save_users([u.to_dict() for u in users], DATA_FILE)


def add_user() -> None:
    name = clean_and_format(input("Введите имя: "))
    email = normalize_email(input("Введите email: "))
    users = _load_users()
    users.append(User(name=name, email=email))
    _save_users(users)
    print(f"Пользователь {name} добавлен.")


def list_users() -> None:
    users = _load_users()
    if not users:
        print("Список пользователей пуст.")
        return
    for idx, user in enumerate(users, 1):
        print(f"{idx}. {user.name} <{user.email}>")


def main() -> None:
    while True:
        print("\n1. Добавить пользователя")
        print("2. Список пользователей")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            add_user()
        elif choice == "2":
            list_users()
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда.")

if __name__ == "__main__":
    main()
