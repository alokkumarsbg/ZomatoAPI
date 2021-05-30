import logging
import requests
from bs4 import BeautifulSoup
import json
import re

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'}

# Read the URL using request
def get_restaurant_details(url):
    """ Response restaturant details in json format 
    url = https://www.zomato.com/pune/rajmandir-ice-cream-1-shivaji-nagar/order
    Explore json file to get all details for a restaurants
    """
    try:
        logging.info(f"Reading Restaurant: {url}")
        
        response = requests.get(url,headers=headers)
        logging.info(f"Response code {response.status_code}")
        
        if response.status_code != 200:
            return False
        

        # Get the script value
        soup = BeautifulSoup(response.content,'html.parser')
        for txt in soup(text=re.compile(r'JSON.parse')):
            json_str = json.loads(str(txt[51:-11]))#.strip())
            rest_result=json.loads(json_str)
            
        return rest_result
        
    except Exception as e:
        logging.info("Failed to Extract data")


def get_popularlocation_bycity(cityurl):
        """ Get details of popular locations of the city and its URL
        This URL will further be used to extract the Restaurants
        """
        response = requests.get(cityurl,headers=headers)
        print(f"Response code {response.status_code}")
        
        # Get the script value
        soup = BeautifulSoup(response.content,'html.parser')
        for txt in soup(text=re.compile(r'JSON.parse')):
            json_str = json.loads(str(txt[51:-11]))#.strip())
            rest_result=json.loads(json_str)
        
        return rest_result['pages']['city']['5']['sections']['SECTION_POPULAR_LOCATIONS']['locations']