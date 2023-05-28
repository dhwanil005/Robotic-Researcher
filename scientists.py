from datetime import datetime

'''
This class represents individual Scientists
'''


class Scientist:
    '''
    Constructor for the Scientist Class
    Args: 
        name(str): name of the scientist
        birth_date(str): Birth Date of the Scientist
        death_date(str): Death Date of the Scientist
        introduction(str): The content of first paragraph from the wikipedia page of the scientist
    '''

    def __init__(self, name: str, birth_date: str, death_date: str, introduction: str):
        self.name = name
        self.birth_date = birth_date
        self.death_date = death_date
        self.introduction = introduction

    '''
    getter method for the name of the scientist
    Returns:
        name(str): name of the scientist
    '''

    def get_name(self) -> str:
        return self.name if self.name else "Unavialable"

    '''
    getter method for the birth_date of the scientist
    Returns:
        birth_date(str): Birth date of the scientist
    '''

    def get_birth_date(self) -> str:
        return self.birth_date if self.birth_date else "Unavailable"

    '''
    getter method for the death_date of the scientist
    Returns:
        death_date(str): Death date of the scientist
    '''

    def get_death_date(self) -> str:
        return self.death_date if self.death_date else "Unavailable"

    '''
    getter method for the intrduction of the scientist
    Returns:
        introduction(str): The content of first paragraph from the wikipedia page of the scientist
    '''

    def get_introduction(self) -> str:
        return self.introduction if self.introduction else "Unavailable"

    '''
    This method calculates age of the Scientist based on birthdate and deathdate
    Returns:
        age(int): The actual age of the Scientist
    '''

    def calculate_age(self) -> int:
        if (not self.birth_date or not self.death_date):
            return -1
        try:
            birth_date = datetime.strptime(self.birth_date, "%d %B %Y")
            death_date = datetime.strptime(self.death_date, "%d %B %Y")
            age = death_date.year - birth_date.year
            if death_date.month < birth_date.month or (death_date.month == birth_date.month and death_date.day < birth_date.day):
                age -= 1
            return age
        except ValueError:
            return None
