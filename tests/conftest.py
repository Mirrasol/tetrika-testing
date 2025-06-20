from unittest.mock import Mock, patch

import pytest

html_russian = '''
<div id="mw-subcategories">
  <h2>Подкатегории</h2>
  <div class="mw-category">
    <div class="mw-category-group">
      <h3>П</h3>
      <ul>
        <li><a href="/wiki/Категория:Породы_по_алфавиту">Породы по алфавиту</a></li>
      </ul>
      </div>
    </div>
  </div>
<div id="mw-pages">
  <div class="mw-category-group">
    <h3>А</h3>
    <ul>
      <li><a href="/wiki/Аардоникс">Аардоникс</a></li>
      <li><a href="/wiki/Абелизавр">Абелизавр</a></li>
    </ul>
  </div>
  <div class="mw-category-group">
    <h3>Б</h3>
    <ul>
      <li><a href="/wiki/Бабакотии">Бабакотии</a></li>
    </ul>
  </div>
  <div class="mw-category-group">
    <h3>A</h3>
    <ul>
      <li><a href="/wiki/Aardonyx">Aardonyx</a></li>
    </ul>
  </div>
</div>
<a href="/w/index.php?title=%D1%82D1%83&pagefrom=%D1%87D0%BA%D0%B8#mw-pages" title="Категория:Животные по алфавиту">Следующая страница</a>
'''

html_non_russian = '''
    <div id="mw-pages">
      <div class="mw-category-group">
        <h3>A</h3>
        <ul>
          <li><a href="/wiki/Aardonyx">Aardonyx</a></li>
        </ul>
      </div>
    </div>
    <a href="/w/index.php?title=%D1%82D1%83&pagefrom=%D1%87D0%BA%D0%B8#mw-pages" title="Категория:Животные по алфавиту">Следующая страница</a>
    '''

mock_api_page_1 = {
    "batchcomplete": "",
    "continue": {
        "cmcontinue": "page|123456",
        "continue": "-||"
    },
    "query": {
        "categorymembers": [
            {"title": "Аардоникс"},
            {"title": "Абелизавр"},
            {"title": "Бабакотии"},
        ]
    }
}

mock_api_page_2 = {
    "batchcomplete": "",
    "query": {
        "categorymembers": [
            {"title": "Виваксия"},
            {"title": "Aardonyx"},
            {"title": "Zuchos"},
        ]
    }
}


@pytest.fixture(scope='module')
def mock_general_response():
    mock = Mock()
    mock.status_code = 200
    mock.text = html_russian
    mock.encoding = 'utf-8'
    return mock


@pytest.fixture(scope='module')
def mock_nonrussian_response():
    mock = Mock()
    mock.status_code = 200
    mock.text = html_non_russian
    mock.encoding = 'utf-8'
    return mock


@pytest.fixture
def mock_api_get():
    with patch('requests.get') as mock_get:
        mock_get.side_effect = [
            Mock(status_code=200, json=lambda: mock_api_page_1),
            Mock(status_code=200, json=lambda: mock_api_page_2),
        ]
        yield mock_get
