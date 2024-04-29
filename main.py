import discord
import time
from discord import app_commands
import random

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync()
            self.synced = True
        print(f"We have logged in as {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(name='mines', description='Mines game mode')
async def mines(interaction: discord.Interaction, tile_amt: int, round_id: str):
    if len(round_id) == 36:
        start_time = time.time()
        grid = ['❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌','❌']
        already_used = []

        count = 0
        while tile_amt > count:
            a = random.randint(0, 24)
            if a in already_used:
                continue
            already_used.append(a)
            grid[a] = '✅'
            count += 1
        
        chance = random.randint(45,95)
        if tile_amt < 4:
            chance = chance - 15

        em = discord.Embed(color=0xFFFFFF)
        em.add_field(name='Grid', value="\n" + "```"+grid[0]+grid[1]+grid[2]+grid[3]+grid[4]+"\n"+grid[5]+grid[6]+grid[7]+grid[8]+grid[9]+"\n"+grid[10]+grid[11]+grid[12]+grid[13]+grid[14]+"\n"+grid[15]+grid[16]+grid[17] \
            +grid[18]+grid[19]+"\n"+grid[20]+grid[21]+grid[22]+grid[23]+grid[24] + "```\n" + f"**Accuracy**\n```{chance}%```\n**Round ID**\n```{round_id}```\n")
        em.set_footer(text='Modded by AzurTDM')
        await interaction.response.send_message(embed=em)
    else:
        em = discord.Embed(color=0xff0000)
        em.add_field(name='Error', value="Invalid round id")
        await interaction.response.send_message(embed=em)

@tree.command(name='towers', description='Towers game mode')
async def towers(interaction: discord.Interaction, round_id: str, tile_amount: int):
    if len(round_id) == 36:
        start_time = time.time()
        grid = [['❓', '❓', '❓'] for _ in range(8)]  # Simplified grid initialization

        for count in range(tile_amount):
            a = random.randint(0, 2)
            grid[count][a] = '✅'

        chance = random.randint(45, 95)
        if tile_amount < 4:
            chance -= 15

        grid_str = "\n".join("".join(row) for row in reversed(grid))  # Convert grid to string
        em = discord.Embed(color=0xFFFFFF)
        em.add_field(name="Grid", value=f"```{grid_str}```\n**Accuracy**\n```{chance}%```\n**Round ID**\n```{round_id}```\n")
        em.set_footer(text='Modded by AzurTDM')
        await interaction.response.send_message(embed=em)
    else:
        em = discord.Embed(color=0xff0000)
        em.add_field(name='Error', value="Invalid round id")
        
        await interaction.response.send_message(embed=em)

@tree.command(name='roulette', description='Roulette game mode')
async def roulette(interaction: discord.Interaction, round_id: str):
    round_length = len(round_id)
    if round_length < 36:
        await interaction.response.send_message("Invalid round id")
    elif round_length == 36:
        predictions = ['gold', 'red', 'purple']
        prediction = random.choice(predictions)
        accuracy = random.randint(60, 99)
        if prediction == 'gold':
            prediction_color = "```YELLOW! 🟨```"
            color = 0xF0FF00
        elif prediction == 'red':
            prediction_color = "```RED! 🟥```"
            color = 0xFF0000
        elif prediction == 'purple':
            prediction_color = "```PURPLE! 🟪```"
            color = 0xFF00B9
        em = discord.Embed(color=color)
        em.add_field(name="AzurTDM COMPILER", value=prediction_color)
        em.add_field(name="Accuracy", value=f"```{accuracy}%```", inline=False)
        em.set_footer(text="Modded by AzurTDM")
        await interaction.response.send_message(embed=em)
    

client.run('put_your_token_here') # SEU TOKEN AQUI POR FAVOR!!!!!