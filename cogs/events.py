import discord
from discord.ext import commands
listener = commands.Cog.listener


class events(commands.Cog):

	def __init__(self, client):
		self.client = client

	@listener()
	async def on_member_ban(self, server, user):
		channel = self.client.get_channel(869134199855149056)
		await channel.send(f'Пользователь {user.mention} был забанен')

	@listener()
	async def on_message_unban(self, server, user):
		channel = self.client.get_channel(869134199855149056)
		await channel.send(f'Пользователь {user.mention} был разбанен')


	@listener()
	async def on_member_join(self, member):
		channel = self.client.get_channel(869134199855149056)
		role1 = member.guild.get_role(870347664116551771)
		await member.add_roles(role1)
		await channel.send(f"Добро пожаловать в клан 'Берлога', {member.mention}!")
	@listener()
	async def on_member_remove(self, member):
		channel = self.client.get_channel(869134199855149056)
		await channel.send(f"{member.mention} Покинул нас!")

	@listener()
	async def on_button_click(self, res):
		await res.respond(type=6)
	@listener()
	async def on_voice_state_update(self,member,before,after):
		if after.channel.id == 870945646507610122:
			mainCategory = discord.utils.get(member.guild.categories, id=870945493985923123)
			channel2 = await member.guild.create_voice_channel(name=f"Комната {member.display_name}",category=mainCategory)
			await member.move_to(channel2)
			await channel2.set_permissions(member,mute_members=True,move_members=True,manage_channels=True)
			def check(a,b,c):
				return len(channel2.members) == 0
			await self.client.wait_for('voice_state_update', check=check)
			await channel2.delete()

def setup(client):
	client.add_cog(events(client))