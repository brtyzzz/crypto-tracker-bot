import requests
import streamlit as st

# Your Telegram Bot Token and Chat ID
TELEGRAM_BOT_TOKEN = "7612091247:AAHdPIkvy8x9pxvnZwfzn9dIDgOZcIn0fYY"
TELEGRAM_CHAT_ID = "6218032056"

def send_telegram_alert(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    return response.json()
