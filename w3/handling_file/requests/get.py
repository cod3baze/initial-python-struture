import requests

def handle_requests_get(url):
    """Nosso Deus é um fogo consumidor, mais os filhos desta vida serão lançados nas estrevas,
        Porque tú es pô e ao pô retornaras, pois este mundo não é sua casa!
    """
    print(f"Initial search for: {url}")
    try:
        x = requests.get(str(url))
        if x:
            print(x.content)
        else:
            print('No result')
    except Exception as e:
        print(f'error: {e.args}')

handle_requests_get('https://google.com')
