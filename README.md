# Remote Pc Telegram Bot

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A Telegram bot that can control your PC through various commands

**GitHub Repo:** [https://github.com/cong34dk/Remote-Pc-Telegram-Bot](https://github.com/cong34dk/Remote-Pc-Telegram-Bot)

## Features

- **Screenshots:**  
  Capture screenshots of any monitor connected to the system and receive the images directly in Telegram.

## Requirements

- **Python:** 3.8 or higher recommended.

- **Telegram Bot Token:** From [BotFather](https://t.me/BotFather).

## Setup Instructions

1. **Clone the Repo:**
   ```bash
   git clone https://github.com/cong34dk/Remote-Pc-Telegram-Bot.git
   cd remote-pc-telegram-bot
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create `.env` File:**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and put your Telegram bot token:
   ```
   TELEGRAM_TOKEN=1234567890:ABC-YourTelegramBotTokenHere
   ```

4. **Run the Bot:**
   ```bash
   python bot.py
   ```

5. **Successfully:**
   Go to telegram app and try it out.

## Example Commands

- `/screenshot`: Capture and receive a screenshot.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
