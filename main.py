import discord
from discord.ext import commands

try:
    import settings
except Exception as e:
    print("settings.py does not exist")
    print(e)
    quit()


if __name__ == "__main__":
    def get_prefix(bot, message):
        prefixes = settings.bot.prefixes
        return commands.when_mentioned_or(*prefixes)(bot, message)
    """   Get all prefixes, and mention   """

    bot = commands.Bot(command_prefix=get_prefix)
    bot.remove_command('help')
    """   Create bot variable, remove default help command """

    try:
        for extension in settings.extensions.initial_extensions:
            bot.load_extension(extension)
            print(f"Loaded module: \"{extension}\"")
    except commands.ExtensionNotFound as e:
        print(e)
        quit()
    else:
        print(f"Loaded all modules")
    """   Load all modules   """

    bot.run(settings.login.token)
    """   Run the bot   """