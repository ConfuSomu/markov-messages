# Read messages from a Discord data export
# They are written to a discord-messages.json file if run alone
# Code taken from https://old.reddit.com/r/discordapp/comments/8t97ka/i_made_a_script_that_analyzes_your_discord_data/ or https://gist.github.com/kittenswolf/0c4f42303aa9498066e6a0e57b972201 and highly modified.
import os
import csv
import json
import sys

def parse_csv(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        readCSV = csv.reader(f, delimiter=',')
        return list(readCSV)

def export(root_dir, messages_text_file):
    messages_dir = os.path.join(root_dir, "messages")
    message_channels = [x[0] for x in os.walk(messages_dir) if not os.path.split(x[0])[1] == "messages"]
    print("{} channels".format(len(message_channels)))

    all_messages = []
    for channel in message_channels:
        all_messages += parse_csv(os.path.join(channel, "messages.csv"))

    print("{} messages".format(len(all_messages)))

    # Create the list of messages
    messages_content = []
    for message in all_messages:
        if message[0] != "ID": # This is a CSV header, ignore this element then...
            text = message[2]
            messages_content.append(text)
    
    # Append the messages to a text file that contains every message
    with open(messages_text_file, 'a') as file:
        for line in messages_content:
            file.write(f"{line}\n")

if __name__ == "__main__":
    try:
        root_dir = sys.argv[1]
        messages_file = sys.argv[2]
    except IndexError:
        sys.exit("Provide root Discord data export directory and messages file as arguments.")
    export(root_dir, messages_file)