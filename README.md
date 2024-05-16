# SimpleTelegramBot
This repository contains a simple Python class named `STB` for interacting with the Telegram Bot API. It allows you to send messages, images, and files to a specified user.

## Description

The `STB` class provides an easy interface to send text messages, images, and files to a specified Telegram user. It uses the Telegram Bot API to interact with Telegram and includes methods to handle different types of media.

## Features

- Send text messages
- Send images
- Send files

## Usage

1. Clone the repository.
2. Install the required packages:
    ```bash
    pip install requests pillow
    ```
3. Create an instance of the `STB` class with your bot token and user ID.
4. Use the provided methods to send messages, images, and files.

### Example

```python
from telegram_bot import STB

# Initialize the bot with your token and user ID
bot = STB(token='YOUR_BOT_TOKEN', user_id=YOUR_USER_ID)

# Send a message
bot.send_message('Hello, World!')

# Send an image
bot.send_image('path/to/image.png')

# Send a file
bot.send_file('path/to/file.err')
