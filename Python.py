 

import sqlite3

# Connect to the database
conn = sqlite3.connect('bot_users.db')
cursor = conn.cursor()

# Create a table for user stats
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                  (user_id INTEGER PRIMARY KEY, wins INTEGER, losses INTEGER)''')
conn.commit()

def update_stats(user_id, result):
    # Check if user exists
    cursor.execute('SELECT * FROM users WHERE user_id=?', (user_id,))
    user = cursor.fetchone()

    if user:
        wins, losses = user[1], user[2]
        if result == "won":
            wins += 1
        else:
            losses += 1
        cursor.execute('UPDATE users SET wins=?, losses=? WHERE user_id=?', (wins, losses, user_id))
    else:
        if result == "won":
            cursor.execute('INSERT INTO users (user_id, wins, losses) VALUES (?, 1, 0)', (user_id,))
        else:
            cursor.execute('INSERT INTO users (user_id, wins, losses) VALUES (?, 0, 1)', (user_id,))

    conn.commit()

# Usage in the fight function
@bot.message_handler(commands=['fight'])
def fight(message):
    fighter = random.choice(list(characters.keys()))
    outcome = random.choice(["won", "lost"])
    
    # Update the user's stats in the database
    update_stats(message.from_user.id, outcome)

    bot.reply_to(message, f"{fighter} fought bravely and {outcome}!")
