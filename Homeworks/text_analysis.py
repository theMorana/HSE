import re
from collections import Counter

def load_data(filename):
    """
    Загружает текстовый файл и возвращает его содержимое как строку.
    
    Args:
        filename (str): Путь к текстовому файлу.
    
    Returns:
        str: Содержимое файла.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

def clean_text(text):
    """
    Очищение текста
    
    Args:
        text (str): Текст для обработки
    
    Returns:
        str: Изменённый текст
    """
    # Очищение от тегов
    text = re.sub(r'<.*?>', '', text)
    return text

def tokenize_text(text):
    """
    Токенизация текста
    
    Args:
        text (str): Исходный текст
    
    Returns:
        str: Очищенный и нормализованный текст
    """
    text = text.lower()
    # Оставляет только буквы, знаки препинания и пробелы
    text = re.sub(r'[^а-яёa-z0-9.,!?;: -]', ' ', text)
    # Удаление повторяющихся пробелов
    text = re.sub(r'\s+', ' ', text).strip()
    # Приведение к нижнему регистру
    
    return text

def create_frequency_dict(text):
    """
    Преобразует текст в очищенный список слов и возвращает частотный словарь.
    
    Args:
        text (str): Исходный текст
        
    Returns:
        Counter: Частотный словарь слов
    """
    # Очистка текста от знаков препинания
    cleaned = re.sub(r'[^\w\s]', ' ', text)
    words = cleaned.split()
    freq_dict = Counter(words)
    
    return freq_dict

# Основной код
text = load_data("Avengers_dialogue_dataset.txt")
print(f"Длина файла: {len(text)}")
print("Первые 10 символов:", text[:50])

tokens = tokenize_text(text)
print("После токенизации:", tokens[:200])

cleaned_text = clean_text(text)
freq_dict = create_frequency_dict(tokens)
print("Самые частые слова:", freq_dict.most_common(5))
