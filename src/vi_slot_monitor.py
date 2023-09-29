from telethon import TelegramClient, events, sync
import os
import dotenv

dotenv.load_dotenv()

# Remember to use your own values from my.telegram.org!
api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
client = TelegramClient('test-session', api_id, api_hash)

@client.on(events.NewMessage(chats='F1_Visa_Slots_Only'))

async def my_event_handler(event):
    text = event.raw_text.lower()
    if "no" not in text and "report" not in text and "?" not in text:
        if "available" in text:
            os.system("open -a 'VLC' ./assets/alarms/high_alarm.mp4")
            with open("high_priority.txt", 'a') as fd:
                fd.write(event.raw_text + "\n")
            os.system("open high_priority.txt")
        else:
            os.system("open -a 'VLC' ./assets/alarms/low_alarm.mp4")
            with open("low_priority.txt", 'a') as fd:
                fd.write(event.raw_text + "\n")
            os.system("open low_priority.txt")
    print(event.raw_text)

client.start()
client.run_until_disconnected()
