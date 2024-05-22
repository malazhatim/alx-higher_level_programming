import requests
import sys

def get_movie_title(movie_id):
    response = requests.get(f'https://swapi.dev/api/films/{movie_id}/')
    if response.status_code == 200:
        data = response.json()
        return data['title'], data['characters']
    else:
        return None, []

def get_character_name(character_url):
    response = requests.get(character_url)
    if response.status_code == 200:
        data = response.json()
        return data['name']
    else:
        return None

def main(movie_id):
    title, character_urls = get_movie_title(movie_id)
    if title is None:
        print(f"Movie with ID {movie_id} not found.")
        return

    print(f"Characters in '{title}':")
    for url in character_urls:
        name = get_character_name(url)
        if name:
            print(name)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python star_wars_characters.py <Movie ID>")
    else:
        try:
            movie_id = int(sys.argv[1])
            main(movie_id)
        except ValueError:
            print("Movie ID must be an integer.")

