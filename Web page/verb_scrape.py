# Import dependencies
from bs4 import BeautifulSoup as bs
import requests

def get_verb_info():
    # Set variable to hold URL
    verb_url = "http://127.0.0.1:5000/"

    # Retrieve page with the requests module
    response = requests.get(verb_url)

    # Create BeautifulSoup object; parse with 'html'
    soup = bs(response.text, 'html')

    # Retrieve the parent div for the grid containing the input verb
    results = soup.find_all('select', class_='person')


    ## verb = input
    ## person = input
    ## tense = input
    ## mood = input