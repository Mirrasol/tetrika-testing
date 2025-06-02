from collections import defaultdict
from unittest.mock import patch

import lxml
import pytest

from task2.solution_webpage import get_animals_data, write_csv


def test_get_animals_data_single_page(mock_general_response):
    with patch('requests.get', return_value=mock_general_response):
        animals_count = defaultdict(int)
        get_animals_data('https://mocked_url', animals_count)

    assert animals_count == {'А': 2, 'Б': 1}


def test_get_animals_data_ignores_non_russian(mock_nonrussian_response):
    with patch('requests.get', return_value=mock_nonrussian_response):
        animals_count = defaultdict(int)
        get_animals_data('https://mocked_url', animals_count)

    assert animals_count == {}


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
