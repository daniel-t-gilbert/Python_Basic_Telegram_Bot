# Telegram Bot

This is a simple Telegram bot created using Python and the `python-telegram-bot` library.

## Getting Started

1. **Create a Telegram Bot:**
   - Go to Telegram and search for "BotFather".
   - Select the account with the verification tick and click on "Start".
   - Type `/newbot` to create a new bot.
   - Follow the instructions to give your bot a name and username.
   - You will receive an Access Token. Copy this token for use in your Python code.

2. **Setting Up the Bot:**
   - Clone this repository:
     ```
     git clone https://github.com/yourusername/telegram-bot.git
     cd telegram-bot
     ```
   - Install dependencies:
     ```
     pip install python-telegram-bot
     ```
   - Replace `YOUR_TELEGRAM_BOT_TOKEN` in the code with the token obtained from BotFather.


3. **Running the Bot:**
   - Run the bot using Python:
     ```
     python telegram-bot.py
     ```
   - The bot should now be running and responding to commands on Telegram.

## Bot Commands

- `/start`: Start the bot and see the welcome message.
- `/help`: View available commands and usage instructions.
- `/about`: Learn more about this bot.
- `/english`: Get Daniel's favorite English song link.
- `/malayalam`: Get Daniel's favorite Malayalam song link.
- `/hindi`: Get Daniel's favorite Hindi song link.
- `/contact`: Get contact information.

## Customization

Feel free to modify the Python functions (`telegram-bot.py`) to add more commands or customize the bot's behavior as per your needs.

## Contributing

If you have suggestions or improvements, feel free to open an issue or pull request.
