from collections import defaultdict

import pytest  # noqa: F401

from task2.solution_api import get_animals_data, write_csv


def test_get_animals_data(mock_api_get):
    animals_count = defaultdict(int)
    get_animals_data(animals_count)

    assert animals_count['А'] == 2
    assert animals_count['Б'] == 1
    assert animals_count['В'] == 1
    assert animals_count['Г'] == 0
    assert 'Д' not in animals_count


def test_write_csv(tmp_path):
    animals_data = {'А': 10, 'Б': 13, 'В': 2, 'Г': 0, 'Д': 0, 'Е': 0, 'Ё': 0,
               'Ж': 0, 'З': 0, 'И': 0, 'Й': 0, 'К': 0, 'Л': 0, 'М': 0,
               'Н': 0, 'О': 0, 'П': 0, 'Р': 0, 'С': 0, 'Т': 0, 'У': 0,
               'Ф': 0, 'Х': 0, 'Ц': 0, 'Ч': 0, 'Ш': 0, 'Щ': 0, 'Ъ': 0,
               'Ы': 0, 'Ь': 0, 'Э': 0, 'Ю': 0, 'Я': 6}
    file_path = tmp_path / 'test_beasts.csv'
    
    write_csv(file_path, animals_data)

    with open(file_path, encoding='utf-8') as f:
        lines = f.read().splitlines()

    assert lines == ['А,10', 'Б,13', 'В,2', 'Я,6']
