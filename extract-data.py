import re

#our sample data
data = """
Restaurant and Cuisine:
Deli Delights - Sandwiches
Taste of Italy - Italian
Burger Blitz - Fast Food
Vegan Vibes - Vegan
Sushi Central - Japanese

Ingredient Lists:
Flour, Sugar, Eggs, Butter
Tomatoes, Basil, Mozzarella, Olive Oil, Crabs
Chicken, Lettuce, Mayo, Bread, Tortillas
Rice, Salmon, Avocado, Seaweed, Spinach
Beef, Irish potatoes, Onions, Okra

RGB Colors:
rgb(255, 0, 0)
rgb(0, 255, 0)
rgb(0, 0, 255)
rgb(128, 128, 128)
   
Social Media Usernames:
@johnDoe45
@tech_guru
@codingMaster23
@foodieLover

Product Codes:
XYZ001
ABC789
MNO123
PQR456
   
News Headlines:
Economy on the Rise: Stock Market Hits New Highs
New Species Discovered: Scientists Excited About Findings
Sports Update: Local Team Takes the Championship!
Weather Warning: Heavy Rain Predicted for the Weekend
   
Event Dates/Times:
Oct 12, 2023 - 10:00 AM
Nov 28, 2023 - 03:00 PM
Dec 25, 2023 - 12:00 PM
Oct 31, 2023 - 06:00 PM
   
Email Addresses:
johndoe@email.com
tech.support@webserver.net
sales@mybusiness.org
delights@yahoo.fr
"""

# defining our regex patterns

restaurant_pattern = re.compile(r'^([^\d-]+) -([^\d-]+)$', re.MULTILINE)
ingredient_pattern = re.compile(r'')
rgb_pattern = re.compile(r'rgb\((\d+), (\d+), (\d+)\)', re.MULTILINE')
usernames_pattern = re.compile(r'')
productcode_pattern = re.compile(r'')
headlines_pattern = re.compile(r'')
dates_pattern = re.compile(r'')
email_pattern = re.compile(r'')

# functions to extract data

def extract_restaurants(data):
    return restaurant_pattern.findall(data)

def extract_ingredients(data):
    return ingredient_pattern.findall(data)

def extract_rgb(data):
    return rgb_pattern.findall(data)

def extract_usernames(data):
    return usernames_pattern.findall(data)

def extract_productcodes(data):
    return productcode_pattern.findall(data)

def extract_headlines(data):
    return headlines_pattern.findall(data)

def extract_dates(data):
    return dates_pattern.findall(data)

def extract_emails(data):
    return email_pattern.findall(data)


#testing the functions

print(extract_restaurants(data))

#this is the structure we'll be working with, so we need to just put in our regex patterns to test
