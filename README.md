# Discord Bot using OpenAI's GPT-3 API

This is a Python Discord Bot that uses OpenAI's GPT-3 API to generate responses to messages in Discord. It uses the `discord.py` library to interact with the Discord API.

## Dependencies

- `openai`: A Python library for accessing the OpenAI API.
- `discord`: A Python library for interacting with the Discord API.

## Installation

To install and run this bot, follow these steps:

1. Clone the repository using Git:

```git
git clone https://github.com/tr3xxx/simple-discord-ai-bot.git
```

2. Navigate to the directory where the repository was cloned:

```git
cd simple-discord-ai-bot
```

3. Install the required dependencies using `pip`:
```git
pip install openai discord.py
```


## Configuration

To run this bot, you will need to provide the following information:

- An OpenAI API key, stored in the `OPENAI_API_KEY` environment variable.
- A Discord bot token, stored in the `DISCORD_TOKEN` environment variable.

## How it works

The bot listens for messages in private chat channels and sends a "Thinking about it..." message while it is generating a response. It then edits the message with the generated response, which is obtained using the `openai.Completion.create` method with the `text-davinci-003` model.

## License

This code is provided under the tr3x © 2022 license.
