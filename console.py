from console_views.menu import Title, Menu
from console_views.instructions import Instructions
from console_views.gallery import Gallery
from api.request_api import Request

class Navile(Request):
    def __init__(self, url):
        super().__init__(url)
        print(Title())
        print(Instructions())
        self.user = input('¿What is your name?: ')
        print(f'''
        ¡Hi {self.user}!''')
        print(Menu())
        self.MenuOptions()

    def MenuOptions(self):
        choice = 0
        while choice != 1 or choice != 2 or choice != 3:
            try: 
                choice = int(input('¿What you wanna do?: '))
            except:
                print('Please, make sure that you are entering just int digits.')
            if choice < 1 and choice > 3:
                print('Available options: 1 | 2 | 3 . Please, check your input.')
            else:
                if choice == 1:
                    self.Gallery_Options()
                elif choice == 2:
                    break
                elif choice == 3:
                    print(f'¡See you later {self.user}!')

    def Gallery_Options(self):
        choice = 0
        data = Request.get_api(self)
        self.pokemons = data['results']
        print(Gallery())
        index = 0
        for pokemon in self.pokemons:
            print(f"{index} - {pokemon['name'].capitalize()}")
            index += 1
        print('''
        1. Show pokemon.
        2. Get back.
        ''')


if __name__ == '__main__':
    Navile('https://pokeapi.co/api/v2/pokemon')
    