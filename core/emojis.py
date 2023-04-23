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
