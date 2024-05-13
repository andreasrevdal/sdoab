# SDOAB: Simple Discord OpenAI Bot

Integrate OpenAI's ChatGPT into your Discord bot. Customize this bot to behave exactly as you like.

## Getting Started

### Prerequisites
1. **OpenAI API Key**: Obtain your API key [here](https://platform.openai.com/api-keys).
2. **Discord Bot Token**: Create a Discord bot and get its token [here](https://discord.com/developers/applications/).
3. **Python 3+**: Download Python from [here](https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe).

### Setup Instructions

1. **Install Python and PIP**:
   - Download and install Python 3+ from the link above.
   - Open PowerShell and run:
     ```powershell
     curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
     python get-pip.py
     ```

2. **Install Dependencies**:
   - Run the following command in PowerShell to install the necessary dependencies:
     ```powershell
     pip install py-cord openai==0.28
     ```

3. **Download and Run the Bot**:
   - Download the `bot.py` file.
   - Open PowerShell in the directory where the file is stored.
   - Run the bot with:
     ```powershell
     py .\bot.py
     ```

### Customization
- **Bot Token and API Key**: Replace `"discord bot token"` and `"api_key"` in the `bot.py` file with your actual keys.
- **Bot Persona**: Modify the line `"You are NAME, a smart and fun bot..."` to create a unique persona for your bot.

## Support

If you find this project helpful and want to support its development, consider buying me a coffee! Your support is greatly appreciated.

[Buy Me A Coffee](https://www.buymeacoffee.com/revdal)

## Join the Community

Stay updated and discuss the project by joining our Discord community:

[Discord](https://discord.gg/zmYFvR8vT8)

## Contributions

Feel free to open an issue or submit a pull request if you have any suggestions or improvements. Your contributions are welcome!
