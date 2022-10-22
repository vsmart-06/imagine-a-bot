import nextcord as discord
from nextcord.ext import commands
import os

bot = commands.Bot()
token = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print("Ready to build some bots!")
    await bot.change_presence(activity = discord.Game(name = "Imagine-A-Bot!"))
    my_user = await bot.fetch_user(706855396828250153)
    await my_user.send("The sky is the limit for your imagination!")

@bot.event
async def on_guild_join(guild: discord.Guild):
    my_user = await bot.fetch_user(706855396828250153)
    await my_user.send(f"New server: {guild}")

@bot.event
async def on_guild_remove(guild: discord.Guild):
    my_user = await bot.fetch_user(706855396828250153)
    await my_user.send(f"Removed from: {guild}")

@bot.slash_command(name = "about", description = "Get to know about the initiative!")
async def about(interaction: discord.Interaction):
    about_embed = discord.Embed(title = "About us!", description = "Thanks a lot for showing your interest in us! Imagine-A-Bot is an initiative by a [budding freelancer](https://discord.com/users/706855396828250153/) wherein he will build a custom Discord bot in python for just $5! Not just that, all the money collected through this initiative will be given to charity, through a non-profit organization named [Sewa International](https://www.sewainternational.org/)!", colour = discord.Colour.blue())
    about_embed.add_field(name = "Details",  value = "With this offer, I will give you a personalized Discord bot which will ideally have 5-10 commands, both traditional text commands and the new slash commands. However, the number of commands is open to discussion! A team will be made on the Discord Developers Portal so that you can access the bot's application page in order to customize it to your preferences. Throughout the duration of the bot's creation, you will have private access to a GitHub repository that will be created for the bot. After the bot is created, I will also guide you on how to host this bot so that it can run 24/7, ready to respond to your commands at any time!", inline = False)
    about_embed.add_field(name = "TL;DR", value = '''With this package, you will essentially get:
1. A custom Discord bot
2. Complete access to the codebase for the bot
3. A hands-on guide on how to host the bot
4. A $5 donation to Sewa International!

**Link to get started**: https://www.fiverr.com/share/xj8RXZ''', inline = False)
    about_embed.set_image(url = "https://media.discordapp.net/attachments/852578295967121443/1032627676139237476/fiverr_banner.png?width=841&height=473")
    await interaction.send(embed = about_embed)

@bot.slash_command(name = "start", description = "Get the link to hire the freelancer to build your bot!")
async def start(interaction: discord.Interaction):
    view = discord.ui.View(timeout = None)
    view.add_item(discord.ui.Button(label = "Imagine A Bot!", style = discord.ButtonStyle.url, url = "https://www.fiverr.com/share/xj8RXZ"))
    await interaction.send(view = view)

@bot.slash_command(name = "avatar")
async def avatar():
    pass

@avatar.subcommand(name = "bot", description = "View the bot's avatar")
async def bot_avatar(interaction: discord.Interaction):
    await interaction.send("https://media.discordapp.net/attachments/852578295967121443/1032627676139237476/fiverr_banner.png?width=841&height=473")

@avatar.subcommand(name = "user", description = "View a user's avatar")
async def user_avatar(interaction: discord.Interaction, user: discord.Member = discord.SlashOption(name = "user", description = "The user who's avatar you wish to see", required = False)):
    if user:
        url = user.display_avatar
    else:
        url = interaction.user.display_avatar
    await interaction.send(url)

@bot.slash_command(name = "contact", description = "Send a message to the freelancer!")
async def contact(interaction: discord.Interaction, message: str = discord.SlashOption(name = "message", description = "The message you would like to send", required = True)):
    contact_embed = discord.Embed(title = "New message", description = f'''**User**: {interaction.user} ({interaction.user.mention})
**Server**: {interaction.guild.name}

**Message**: {message}
''', colour = discord.Colour.blue())
    channel = await bot.fetch_channel(1032630602328977449)
    my_user = await bot.fetch_user(706855396828250153)
    msg = await channel.send(embed = contact_embed)
    await my_user.send(f"New message! {msg.jump_url}")
    await interaction.send("Message sent! You will receive a response via DMs!", ephemeral = True)

@bot.slash_command(name = "reply", description = "Reply to a message", guild_ids = [852578295967121438])
async def reply(interaction: discord.Interaction, user: str = discord.SlashOption(name = "user", description = "The ID of the user you wish to reply to", required = True), message: str = discord.SlashOption(name = "message", description = "The message you wish to send")):
    try:
        user = int(user)
        reply_user = await bot.fetch_user(user)
    except:
        await interaction.send("Invalid user ID", ephemeral = True)
        return
    reply_embed = discord.Embed(title = "Reply from the freelancer!", description = message, colour = discord.Colour.blue())
    await reply_user.send(embed = reply_embed)
    await interaction.send(embed = reply_embed)

@bot.slash_command(name = "strength", description = "View the bot's server count", guild_ids = [852578295967121438, 835448058656587777])
async def strength(interaction: discord.Interaction):
    await interaction.send(f"I'm in {len(bot.guilds)} servers!")

bot.run(token)