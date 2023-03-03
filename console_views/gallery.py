class Gallery: # Return a String with the __str__ method that contains the Gallery Title to continue printing the list of the pokemons.
    def __init__(self):
        self.gallery_text = f'''
        
            GALLERY
---------------------------------
Pokemons:
        '''

    def __str__(self):
        return self.gallery_text

class FavGallery: # Return a String with the __str__ method that contains the Gallery Title to continue printing the list of the favorite pokemons.
    def __init__(self):
        self.favorite_gallery_text = f'''
        FAVORITE GALLERY
---------------------------------

Pokemons:
        '''

    def __str__(self):
        return self.favorite_gallery_text
