#######
# Main file. This is where everything happens since this is a small project
# Written by Kendrick Sharpe on Oct 25, 2022 while on an airplane
#
#####

import random
from twilio.rest import Client #You can comment this out if you don't have twilio installed

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

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

def send_text(quote):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to="", #replace with target phone number
        from_="", #replace with twilio number
        body=quote)

if __name__ == "__main__":
    QUOTES = load_quote_array()
    quote = random_selection(QUOTES)
    print("-=+=-\n\n" + quote + "\n\n-+-\n")
    send_text(quote)
