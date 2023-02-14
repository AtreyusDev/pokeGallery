class FavoritePokemons:
    def __init__(self, pokemons):
        try:
            index_searched = int(input('Please, write the index of the pokemon that you want to add to favorites: '))
        except:
            print('Please, make sure that you are entering just integer digits.')

        for pokemon in pokemons:
            if index_searched == pokemon['index']:
                self.fav_pokemons.append(pokemon)
                print(f'''Pokemon added to favorite list succesfully!
                
                Current List:
                ''')
                for data in self.fav_pokemons:
                    print(f'''Id: {data['index']} | Name: {data['name']}''')
            else:
                print('pokemon already added to favorite.')

        # HAY QUE AGREGAR UNA VALIDACIÓN PARA EVITAR QUE EL USUARIO AGREGUE UN POKEMON QUE YA FUE
        # AGREGADO A FAVORITOS.