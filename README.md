
# Discord Bot for Tokens Information

A Discord bot that provides detailed information about cryptocurrency tokens using data from the DexScreener API. This bot allows users to query for specific tokens and get real-time information such as price, liquidity, market cap, and more.

## Features

- Fetches and displays information about tokens from the DexScreener API.
- Shows price (USD and native), volume, liquidity, and market cap.
- Provides direct links to external resources like BirdEye and DEX page.
- Displays additional information such as highest and lowest prices in the last 24 hours, social media links, and more.

## Prerequisites

Before you begin, ensure you have the following:

- [Python 3.8+](https://www.python.org/downloads/)
- [Discord Bot Token](https://discord.com/developers/applications) (you'll need to create a bot in the Discord Developer Portal and get a token).
- Install the required libraries:

```bash
pip install discord.py requests python-dotenv
```

## Setup

1. Clone this repository to your local machine:

```bash
git clone https://github.com/icyjkk/Discord-bot-token-info.git
```

2. Navigate to the project directory:

```bash
cd discord-bot-token-info
```

3. Create a `.env` file in the root directory to store your bot token securely:

```bash
touch .env
```

4. Open the `.env` file and add your bot token:

```
DISCORD_BOT_TOKEN=your-discord-bot-token-here
```

5. Replace the placeholder in `bot.py` for `bot.run`:

```python
import os
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
bot.run(TOKEN)
```

6. Run the bot:

```bash
python bot.py
```

## Usage

Once the bot is running and connected to your Discord server, use the command `!token <token-address>` in the channel where the bot has permissions to interact. The bot will respond with an embedded message displaying the token's details, including price, market cap, and social media links.

![image](https://github.com/user-attachments/assets/2f1d1437-7ae3-4ed1-ae49-faf9a53ad2c6)
