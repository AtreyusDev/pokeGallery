class Gallery:
    def __init__(self):
        self.gallery_text = f'''
        
            GALLERY
---------------------------------
Pokemons:
        '''

    def __str__(self):
        return self.gallery_text

class FavGallery:
    def __init__(self):
        self.favorite_gallery_text = f'''
        
        FAVORITE GALLERY
---------------------------------

Pokemons:
        '''

    def __str__(self):
        return self.favorite_gallery_text
