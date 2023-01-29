class Title:
    def __init__(self):
        self.title_text = '''
        ¡WELCOME TO POKEMON GALLERY!'''.center(15,'*')

    def __str__(self):
        return self.title_text

class Menu:
    def __init__(self):
        self._version = '1.0.0'
        self.menu_text = f'''
           POKE-MENU
-------------------------------
        1. View Gallery
        2. View Favorites
        3. Exit 
        -----------------
        Version : {self.version}
        '''

    @property
    def version(self):
        return self._version

    def __str__(self):
        return self.menu_text

