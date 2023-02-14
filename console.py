from console_views.menu import Title, Menu
from console_views.instructions import Instructions
from console_views.gallery import Gallery, FavGallery
from console_views.pokemon_information import Pokemon_data
from api.request_api import Request

class Navile(Request):
    def __init__(self, url):
        super().__init__(url)
        self.fav_pokemons = []
        print(Title())
        print(Instructions())
        self.user = input('¿What is your name?: ')
        print(f'''
        ¡Hi {self.user}!''')
        self.MenuOptions()
        
    def MenuOptions(self):
        print(Menu())
        choice = 0
        while choice != 1 or choice != 2:
            try: 
                choice = int(input('¿What you wanna do?: '))
            except:
                print('Please, make sure that you are entering just int digits.')
            if choice < 1 and choice > 3:
                print('Available options: 1 | 2 | 3 . Please, check your input.')
            else:
                if choice == 1:
                    self.Gallery_Options()
                    break
                elif choice == 2:
                    if len(self.fav_pokemons) < 1:
                        print('''
Favorite gallery empty. You can add pokemons to favorite in the Gallery menu.
                        ''')
                        print(Menu())
                    else:
                        print(FavGallery())
                        for data in self.fav_pokemons:
                            print(f'''Id: {data['index']} | Name: {data['name']}''')
                        print(Menu())
                elif choice == 3:
                    print(f'¡See you later {self.user}!')
                    break

    def Gallery_Options(self):
        pokemon_choice = 0
        data = Request.get_api(self)
        self.pokemons = data['results']
        print(Gallery())
        index = 0
        for pokemon in self.pokemons:
            pokemon['index'] = index
            print(f"{pokemon['index']} - {pokemon['name'].capitalize()}")
            index += 1

        while pokemon_choice != 3:
            print('''
            1. Show pokemon.
            2. Add to favorite.
            3. Get back.
            ''')
        
            try:
                pokemon_choice = int(input('What do you want to do?: '))
            except:
                print('Please, make sure that you are entering just int digits.')
            if pokemon_choice == 1:
                try:
                    index_searched = int(input('Please, write the index of the pokemon that you want to view: '))
                except:
                    print('Please, make sure that you are entering just integer digits.')

                for pokemon in self.pokemons:
                    if index_searched == pokemon['index']:
                        print(Pokemon_data(pokemon))
            elif pokemon_choice == 2:
                try:
                    index_searched = int(input('Please, write the index of the pokemon that you want to add to favorites: '))
                except:
                    print('Please, make sure that you are entering just integer digits.')

                for pokemon in self.pokemons:
                    if index_searched == pokemon['index']:
                        if pokemon in self.fav_pokemons:
                            print('Pokemon already added.')
                        else:
                            self.fav_pokemons.append(pokemon)
                            print(f'''Pokemon added to favorite list succesfully!
                            
                            Current List:
                            ''')
                            for data in self.fav_pokemons:
                                print(f'''Id: {data['index']} | Name: {data['name']}''')

            elif pokemon_choice == 3:
                print('''

Returning to the menu...
                ''')
                self.MenuOptions()
            elif pokemon_choice < 1 or pokemon_choice > 2:
                print()
                print('Available options: 1 | 2. Please, check your input.')
            
if __name__ == '__main__':
    try:
        Navile('https://pokeapi.co/api/v2/pokemon')
    except:
        print(f'Error triying to connect with the API. Please check your connection and try again.')
        exit()
    