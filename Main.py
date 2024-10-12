


import telebot
import random

# Initialize bot with your token
TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)

# JJK Characters and quotes
characters = {
    "Yuji Itadori": "I'm not alone. I have my friends.",
    "Satoru Gojo": "No matter how many allies you have, it doesn't matter.",
    "Megumi Fushiguro": "I'm not a hero, I'm a jujutsu sorcerer.",
    "Nobara Kugisaki": "I don't care about logic. My emotions are what drive me!"
}

# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the Jujutsu Kaisen Bot! Type /fight to battle or /quote for a random JJK quote.")

# Fight command (Random battle outcome)
@bot.message_handler(commands=['fight'])
def fight(message):
    fighter = random.choice(list(characters.keys()))
    outcome = random.choice(["won", "lost"])
    bot.reply_to(message, f"{fighter} fought bravely and {outcome}!")

# Quote command (Random character quote)
@bot.message_handler(commands=['quote'])
def quote(message):
    character = random.choice(list(characters.keys()))
    quote = characters[character]
    bot.reply_to(message, f"{character} says: \"{quote}\"")

# Polling the bot
bot.polling()
