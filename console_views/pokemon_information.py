class Pokemon_data:
    def __init__(self, poke_data):
        self.text = f'''
        Name = {poke_data['name']}.
        '''

    def __str__(self):
        return self.text