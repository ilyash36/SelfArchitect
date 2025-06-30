def clean_and_format(text: str) -> str:
    """
    Убирает пробелы по краям и приводит первую букву к верхнему регистру, остальные — к нижнему.
    """
    return text.strip().capitalize()

def normalize_email(email: str) -> str:
    """
    Удаляет пробелы по краям и приводит email к нижнему регистру.
    """
    return email.strip().lower()

def smart_clean(text: str) -> str:
    """
    Убирает пробелы и приводит текст к нижнему регистру.
    """
    return text.strip().lower()
