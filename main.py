import discord
import asyncio
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

async def main():
    token = input("Enter your bot token: ")
    message_to_send = input("Enter the message to send: ")

    intents = discord.Intents.default()
    intents.members = True
    bot = discord.Client(intents=intents)

    @bot.event
    async def on_ready():
        print(f"{Fore.CYAN}Bot connected as {bot.user}")
        for guild in bot.guilds:
            print(f"{Fore.YELLOW}Sending messages to members of the server: {guild.name}")
            for member in guild.members:
                if not member.bot:
                    try:
                        await member.send(message_to_send)
                        print(f"{Fore.GREEN}Message sent to {member.name}")
                    except Exception as e:
                        print(f"{Fore.RED}Failed to send message to {member.name}: {e}")
        await bot.close()

    await bot.start(token)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        input("\nPress Enter to exit...")
