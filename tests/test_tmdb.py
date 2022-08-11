import tmdb_client
from unittest.mock import Mock
import pytest
from main import app

def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

def test_get_movie_images():
    movies_image = tmdb_client.get_movie_images(movie_id="")
    assert movies_image is not None

def test_get_single_movie_cast(monkeypatch):
   mock_movies_list = ['Cast 1', 'Cast 2']

   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_single_movie_cast(movie_id="")
   assert movies_list == mock_movies_list

@pytest.mark.parametrize('name, code',(
    ('/', 200),
    ('/popular/', 200),
))

def test_homepage(name, code, monkeypatch):
    api_mock = Mock(return_value={'results': []})
    monkeypatch.setattr("main.popular", api_mock)
    with app.test_client() as client:
       response = client.get('/')
       assert response.status_code == 200