import csv
from collections import defaultdict

import requests

api_url = 'https://ru.wikipedia.org/w/api.php'

animals_count = defaultdict(int)

filename = 'beasts.csv'

alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'


def get_animals_data(result_dict: dict):
    """Parse the animals' category from Wiki API and 
    fill in the specified dictionary with the result data.
    """
    params = {
        'action': 'query',
        "cmtitle": "Категория:Животные_по_алфавиту",
        'cmlimit': 500,
        "list": "categorymembers",
        "format": "json",
        "cmcontinue": ''
    }

    while True:
        response = requests.get(url=api_url, params=params).json()
        animals = response['query']['categorymembers']

        for animal in animals:
            first_letter = animal['title'][0]
            if first_letter in alphabet:
                result_dict[first_letter] += 1
            else:
                break

        if 'continue' not in response:
            break

        params.update({'cmcontinue': response['continue']['cmcontinue']})


def write_csv(filename: str, data: dict):
    """Write the provided dictionary into a specified csv-file."""
    with open(filename, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for letter in alphabet:
            if data[letter] > 0:
                writer.writerow([letter, data[letter]])


if __name__ == '__main__':
    get_animals_data(animals_count)
    write_csv(filename, animals_count)
