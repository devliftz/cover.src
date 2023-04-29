import json

# Load emoji data from a JSON file
with open('./config/emojis.json', 'r') as f:
    emoji_data = json.load(f)

# Define emojis as global variables
check = emoji_data['check']
warning = emoji_data['warning']
locked = emoji_data['locked']
unlocked = emoji_data['unlocked']
plus = emoji_data['plus']
channel = emoji_data['channel']
reply = emoji_data['reply']
up = emoji_data['up']
down = emoji_data['down']
giveaway = emoji_data['giveaway']
ticket = emoji_data['ticket']
ban = emoji_data['ban']
economy = emoji_data['economy']
home = emoji_data['home']
cpu = emoji_data['cpu']
fm = emoji_data['fm']
btc = emoji_data['btc']
eth = emoji_data['eth']
github = emoji_data['github']