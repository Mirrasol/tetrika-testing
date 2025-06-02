import csv
from collections import defaultdict

import lxml
import requests
from bs4 import BeautifulSoup

starting_url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

animals_count = defaultdict(int)

filename = 'beasts.csv'

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def get_animals_data(url: str, result_dict: dict):
    """Parse the provided Wiki page and 
    fill in the specified dictionary with the result data.
    """
    alphabet_end_flag = 'Continue'

    while alphabet_end_flag == 'Continue':
        response = requests.get(url=url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'lxml')

        animals_on_page = soup.find('div', id='mw-pages').find_all('div', class_='mw-category-group')
        animal_categories = [category for category in animals_on_page]
        
        for category in animal_categories:
            first_letter = category.h3.text
            if first_letter in alphabet:
                for animal in category.find_all('li'):
                    result_dict[first_letter] += 1
            else:
                alphabet_end_flag = 'End'
                break
        
        next_page = [link['href'] for link in soup.find_all('a', title='Категория:Животные по алфавиту')
                     if link.text == 'Следующая страница'][0]
        url = f'https://ru.wikipedia.org{next_page}'


def write_csv(filename: str, data: dict):
    """Write the provided dictionary into a specified csv-file."""
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for letter in alphabet:
            if data[letter] > 0:
                writer.writerow([letter, data[letter]])


if __name__ == '__main__':
    get_animals_data(starting_url, animals_count)
    write_csv(filename, animals_count)
