import json
import re

def for_discord_messages(messages):
    messages_content = []

    for message in messages:
        if message[0] != "ID": # This is a CSV header, ignore it then...
            text = message[2]
            
            messages_content.append(text)
    
    return messages_content


def parse_messages_json(messages_json_file, messages_text_file):
    contents = []

    with open(messages_json_file, 'r') as file:
        contents = json.load(file)

    messages_text = []
    if contents["message-source"] == "discord":
        messages_text = for_discord_messages(contents["messages"])
    
    with open(messages_text_file, 'a') as file:
        for line in messages_text:
            file.write(f"{line}\n")

if __name__ == "__main__":
    parse_messages_json("discord-messages.json", "messages")