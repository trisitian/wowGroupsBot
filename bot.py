
import discord
from discord import app_commands,ui
from datetime import datetime
import os
TOKEN = os.environ['DISCORD_TOKEN']
ID = os.environ["GUILD_ID"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


class test_modal(ui.Modal, title ="Example Modal"):
    answer = ui.TextInput(label = "New Label",style = discord.TextStyle.short, default = "foo", required = True, max_length=1000)

    async def on_submit(self, interaction):
        embed = discord.Embed(
            title=self.title,
            description=f"User's Input: {self.answer.value}",
            timestamp=datetime.now()
        )
        await interaction.response.send_message(embed=embed)


@tree.command(name = "foo", description = "My first application Command", guild=discord.Object(id=ID))
async def first_command(interaction):
    await interaction.response.send_message("YOU JUST DID A SLASH COMMAND")

@tree.command(name = "modal", description = "Ecample modal", guild=discord.Object(id=ID))
async def modal(interaction):
    await interaction.response.send_modal(test_modal())



@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=ID))
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(TOKEN)