class Pokemon_data: # Return a String with the __str__ method that contains the data of the selected pokemon.
    def __init__(self, poke_data):
        self.text = f'''
        Name = {poke_data['name']}.
        '''

    def __str__(self):
        return self.text