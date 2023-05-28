import re
from RPA.Browser.Selenium import Selenium
from datetime import datetime
from scientists import Scientist

SCIENTISTS = ["Albert Einstein", "Isaac Newton",
              "Marie Curie", "Charles Darwin"]

URL_PREFIX = "https://en.wikipedia.org/wiki/"

br = Selenium()

'''
This class is responsible for everything that the robot is supposed to do
'''


class Robot:
    '''
    Initialising the Robot class
        Args: 
            name (str): Name of the Robot
    '''

    def __init__(self, name):
        self.name = name

    '''
    This method is responsible for the Robot greeting and introducing itself
    '''

    def say_hello(self) -> None:
        print("Hello, my name is " + self.name)

    '''
    This method is responsible for the robot explaining the steps it is going to take
    '''

    def robot_steps(self) -> None:
        print("I will navigate to the Scientist's wikipedia page, fetch a short introduction, birth dates and death dates. I will also calculate their age and display it to you! :) ")

    '''
    This method is responsible for saying goodbye after it has performed the above mentioned steps
    '''

    def say_goodbye(self) -> None:
        print("Goodbye, my name is " + self.name)

    '''
    This method is responsible for opening the webpage, wikipedia page in our case
    Args:
        webpage(str): the desired wikipedia page URL
    '''

    def open_webpage(self, webpage):
        br.open_available_browser(webpage)

    '''
    This method is responsible for closing the webpage after the robot has fetched the desired data
    '''

    def close_webpage(self):
        br.close_all_browsers()

    '''
    This method is responsible for manipulating the list items(SCIENTISTS) to fit the desired URL criteria and fetching the necessary information.
    '''

    def retrieve_scientist_data(self) -> None:
        for scientist_name in SCIENTISTS:
            url_suffix = scientist_name.replace(" ", "_")
            webpage = URL_PREFIX + url_suffix
            scientist_data = self.fetch_scientist_data(webpage, scientist_name)
            if scientist_data:
                print(f"Lets see some Information about {scientist_name}.")
                self.print_scientist_details(scientist_data)
        self.close_webpage()

    '''
    This method is a helper function to retrieve_scientist_data
    Args:
        webpage(str): the desired wikipedia page URL
        scientist_name(str): the name of the scientist whose data we want to fetch
    Returns:
        Scientist(obj): of type Scientist
    '''

    def fetch_scientist_data(self, webpage, scientist_name) -> Scientist:
        self.open_webpage(webpage)
        try:
            birth_date = self.extract_birth_date()
            death_date = self.extract_death_date()
            introduction = self.extract_introduction()
            scientist = Scientist(
                scientist_name, birth_date, death_date, introduction)
            return scientist
        except Exception as e:
            print(e)
            return None

    '''
    This method is responsible for extracting the birth date from the birth details blob of data
    Returns:
        birth_date(str): Birth date of scientist
    '''

    def extract_birth_date(self) -> str:
        try:
            birth_date = br.get_text("xpath://td[@class='infobox-data'][1]")
            birth_date = re.search(r'\d+\s+\w+\s+\d+', birth_date).group()
            return birth_date
        except Exception as e:
            print("Sorry! I could not fetch the scientist's birth date.")
            return None
    '''
    This method is responsible for extracting the death date from the death details blob of data
    Returns:
        death_date(str): Death date of scientist
    '''

    def extract_death_date(self) -> str:
        try:
            death_details = br.get_text(
                "xpath://tr[th[contains(text(), 'Died')]]/td[@class='infobox-data']")
            death_data = death_details.split('(')
            death_date = death_data[0].strip()
            return death_date
        except Exception as e:
            print("Sorry! I could not fetch the scientist's death date.")
            return None

    '''
    This method is responsible for extracting the first paragraph from the scientist's wikipedia page.
    Returns:
    introduction(str): the introduction of scientist
    '''

    def extract_introduction(self) -> str:
        try:
            introduction = br.find_element("xpath://p[2]").text
            if not introduction:
                introduction = br.find_element("xpath://p[3]").text
            return introduction
        except Exception as e:
            print("Sorry! I could not fetch the scientist's Introduction.")
            return None

    '''
    The sole purpose of this method is to print the details of the scientists in a user-friendly manner
    '''

    def print_scientist_details(self, scientist_data) -> None:
        print("-------------------------------------------------------------------------")
        print(f"Name: {scientist_data.get_name()}"
              )
        print(f"Birth Date: {scientist_data.get_birth_date()}"
              )
        print(f"Death Date: {scientist_data.get_death_date()}"
              )
        print(f"Age: {str(scientist_data.calculate_age())}"
              ) if scientist_data.calculate_age() >= 0 else print("Age Unavailable")
        print(f"Introduction: {scientist_data.get_introduction()}"
              )
        print("-------------------------------------------------------------------------")
