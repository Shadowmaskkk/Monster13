import telebot
import random
import time
from datetime import datetime

# --- CONFIGURATION ---
API_TOKEN = '8899407339:AAH-Rj2KbuT3dsFFBuXPuazH48njku4dyi0'
GROUP_ID = '-1003759123387'

bot = telebot.TeleBot(API_TOKEN)

# --- GENUINE DATA POOLS ---
data = {
    "Crunchyroll": {"plans": ["Fan Tier", "Mega Fan", "Ultimate Fan"], "prices": ["$9.99", "$13.99", "$17.99"]},
    "Netflix": {"plans": ["Standard", "Premium 4K", "Standard with Ads"], "prices": ["$15.49", "$24.99", "$7.99"]},
    "Adobe": {"plans": ["Creative Cloud Pro", "Photography Plan", "Student Bundle"], "prices": ["$69.99", "$19.99", "$22.99"]},
    "Xbox": {"plans": ["Game Pass Ultimate", "PC Game Pass", "Core Membership"], "prices": ["$22.99", "$13.99", "$9.99"]},
    "Spotify": {"plans": ["Premium Individual", "Premium Family", "Premium Duo"], "prices": ["$12.99", "$21.99", "$18.99"]},
    "ChatGPT": {"plans": ["Plus Subscription", "Team Plan"], "prices": ["$20.00", "$30.00"]},
    "Amazon Prime": {"plans": ["Monthly Membership", "Annual Membership"], "prices": ["$14.99", "$139.00"]}
}

statuses = ["account received", "subscription renewed for", "payment confirmed for", "plan activated:"]

def generate_instant_message():
    """Generates a unique message on the fly"""
    service = random.choice(list(data.keys()))
    plan = random.choice(data[service]["plans"])
    price = random.choice(data[service]["prices"])
    status = random.choice(statuses)
    rand_id = random.randint(1000000, 9999999) # 7-digit ID for a real feel
    
    return f"{service} {status} {plan}, Price {price} (Ref: {rand_id})"

def start_monster_alert():
    print(f"🚀 Monster Alert System: Live on Group {GROUP_ID}")
    
    while True:
        try:
            # 1. Generate the message instantly
            msg_content = generate_instant_message()
            current_time = datetime.now().strftime('%Y-%m-%d | %H:%M:%S')

            # 2. Ultra-Realistic UI
            professional_ui = (
                "💳 **PAYMENT GATEWAY ALERT**\n"
                "────────────────────\n"
                f"📝 **Details:** `{msg_content}`\n"
                f"📊 **Status:** 🟢 `SUCCESS` \n"
                f"📡 **Network:** `Mainnet-V2` \n"
                "────────────────────\n"
                f"Timestamp: `{current_time}`"
            )
            
            # 3. Send to Group
            bot.send_message(
                GROUP_ID, 
                professional_ui, 
                parse_mode='Markdown'
            )
            print(f"✅ Sent to Group: {msg_content}")

            # 4. Random Delay (Aiming for 50-70 messages a day)
            # Waits between 10 and 25 minutes
            delay = random.randint(600, 1500)
            print(f"⏳ Waiting {delay // 60} minutes...")
            time.sleep(delay)

        except Exception as e:
            print(f"⚠️ Error: {e}")
            time.sleep(30)

if __name__ == "__main__":
    start_monster_alert()
