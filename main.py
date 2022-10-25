#######
# Main file. This is where everything happens since this is a small project
# Written by Kendrick Sharpe on Oct 25, 2022 while on an airplane
#
#####

import random

TWILIO_SECRET = None #Replace ... with your twilio secret for sending texts
PHONE_NUMBER = None #Replace ... with your phone number

#Loads the QUOTES with data from quotes.txt
#Returns array of quotes
def load_quote_array():
    quote_file = open("quotes.txt", "r")
    quote_file_data = quote_file.read()
    quote_list = quote_file_data.split("\n")
    quote_file.close()
    return quote_list

#Randomly selects a quote and returns it as a string
#Honestly, I didn't realize this was a one-liner! Go Python!!
def random_selection(quotes):
    return random.choice(quotes)


if __name__ == "__main__":
    QUOTES = load_quote_array()
    print("-=+=-\n\n" + random_selection(QUOTES) + "\n\n-+-")
