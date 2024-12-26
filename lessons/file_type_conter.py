from pathlib import Path
from pprint import pprint
import sys

print(sys.argv)
try:
    print()
    # Создаем объект Path для указанной директории
    path = Path(sys.argv[1])

    file_counter = 0
    files = path.iterdir()
    contents = len(list(filter(lambda x: sys.argv[2] in x.suffix, files)))
    # contents = [(lambda files, file_counter: file_counter += 1)()
    #             for item in]  # Список с именами
    pprint(contents)
except FileNotFoundError:
    print(f"Папка '{sys.argv[1]}' не найдена.")
except Exception as e:
    print(f"Произошла ошибка: {e}")
