class Instructions:
    def __init__(self) -> None:
        self.instructions_text = '''
    I´m Navile. Your assistant in this app.

How to use: First, write your name to meet you, then, 
            I´m going to ask you what you want to do.
            For to answer, I read just integers (1,2,3...).
            I will show you the options, so you
            will know which options you have.
        '''

    def __str__(self):
        return self.instructions_text