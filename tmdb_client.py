import requests
import os

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")
API_TOKEN2 = "3fd84ea49081758a2fa8e39aa8629db1"


list = ["upcoming","popular","top_rated","now_playing"]

def get_movies_list(list_type):
    end_point = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(end_point, headers=headers)
    response.raise_for_status()
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many] 

def endpoint_single_movie(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    id = str(movie_id)
    endpoint = base_url + id
    return endpoint

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def endpoint_get_single_movie_cast(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    id = str(movie_id)
    cr = "/credits"
    endpoint = base_url + id + cr
    return endpoint

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images" 
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json() 

def endpoint_get_movie_images(movie_id):
    base_url = "https://api.themoviedb.org/3/movie/"
    img = "/images"
    id = str(movie_id)
    endpoint = base_url + id + img
    return endpoint

def search(search_query):
    base_url = "https://api.themoviedb.org/3/"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    endpoint = f"{base_url}search/movie/?query={search_query}"
    response = requests.get(endpoint, headers=headers)
    response = response.json()
    return response['results']

def get_airing_today():
    endpoint = "https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    response = response.json()
    return response['results']

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()