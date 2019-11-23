from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()

#   Discord.py required, made by Dragons of Demons | contact me over Discord for support

import os

import discord
token = os.environ.get('API_KEY')
import asyncio
bot = discord.Client()
sendmsg = discord.abc.Messageable.send 
import json
from discord.ext import commands
embed = bot.event

@embed
async def on_ready():
    print("Online")

async def playStatus():
    await bot.wait_until_ready()
    await bot.change_presence(game=discord.Game(name="use '=help=' to begin"))

@embed
async def on_message(message):
    received = message.content.startswith
    reply = message.channel

    if received("=Lineage="):
        embed = discord.Embed(title="Lineage", colour=discord.Colour(0xd6680e), description="Overview on Lineage")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="About Lineage", value="A strange and unique power passed down through generations.  Some are passed down through historical figure's descendents, certain rich and/or powerful families(very few), families descended from magic beings/creatures, and a handful of families that received them randomly.  The \"Lineage\" (power) are all one of a kind, each with their own name, appearance, and powers(s) they give their user(A Lineage's powers fall under 7 types: Support, Offense, Defense, Mobility, Enhancement, Deception, or Creation.  A Lineages can have 1-3 types, the less powers they have, the more potent the abilities are, the more powers, the less potent they are).  ")
        embed.add_field(name="Lenderization", value="With enough training, a Lineage holder can utilize a technique called Lenderization.  Lenderization makes the user's Lineage materialize, also allowing the user to control them with a thought, the Lineage usualy floats around the user.  Once the Lineage materializes, it gains a small level of sentience, and can function on its own, only to the extent of protect Lineage holder+the holder's allies, and attack/intercept threats to holder+holder's eneimes(withouth much training, the user can partially Lenderize, temporarily gaining control over one or more extra appendages and/or tools, and/weapons).  ")
        embed.add_field(name="Lenderization (cont)", value="Lenderization can be taken a step further, and after enough experience using it allows the holder to access a form similar to a anime mode or video game power, up known as Power Lenderization, which causes the Lineage holder and their Lineage to fuse, merging physical appearances, increasing all abilities and attributes for the both of them")
        
        await sendmsg(reply, embed=embed)

        embed = discord.Embed(title="Lineage", colour=discord.Colour(0xd6680e), description="List of Lineage Categories")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="Descendants of historical figures(DHL)", value="Their signifact historical ancestor would be their Lineage.")
        embed.add_field(name="Random bloodlines(RBL)", value="Their Lineage can be animals, types of warriors, certain job occupations, and in rare cases, elemental golems")
        embed.add_field(name="Aether Elves(AEs) and Dark Elves(DEs)", value="Look like humans, long pointed ears, angled/gaunt features, usually tall and skinny, Aether Elves have metallic bronze skin, Dark Elves have metallic silver skin, both have either ginger or black hair,  Elves are slightly stronger/sturdier then humans, but much faster then them, but are more Susceptible to illusions and elemental damage.")
        embed.add_field(name="Wealthy/powerful families(WPL)", value="Same as random bloodlines, plus the addition of magic and/or mythological beings and creatures")
        embed.add_field(name="Descendants of magic beings(DML)", value="magical ancestor, or creature closely related to magical ancestor would be their Lineage")

        await sendmsg(reply, embed=embed)

        
    elif received("=Species="):
        embed = discord.Embed(title="Species", colour=discord.Colour(0xd6680e), description="List of Species")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="Fae", value="Dividided into two subraces, Pixies and Goblon, Fae are the race capable of using Faetech.  Fae cannot recieve Blessings upon birth.  Pixies look very similar to humans, the differences being they are all very short blue or green skin, pointed ears, extreme resistance to cold, and retractable insect-like wings(wings can only be used for 30 seconds, upon activation wings create a powerful gust of cold air.  Pixies cacreate the strong gusts at will, starting temp is mildy chilly, eventually the temp becomes cold enough to freeze almost anything upon contact)")
        embed.add_field(name="Fae (cont)", value="Pixies are usually very rude, cruel, self-centered, and analyzing.  Goblins are bipedal lizard humanoids, like Faery, they are all very short, extreme resistance to fire, unlike the Pixies, they cannot fly, instead they have sharp claws useful for climbing, and can raise the temperature of their skin(at first only lukewarm temp is available, eventually Goblins can heat their skin so much it catches fire), Goblins are usually kind, humorous, jovial, and understanding")
        embed.add_field(name="Aether Elves(AEs) and Dark Elves(DEs)", value="Look like humans, long pointed ears, angled/gaunt features, usually tall and skinny, Aether Elves have metallic bronze skin, Dark Elves have metallic silver skin, both have either ginger or black hair,  Elves are slightly stronger/sturdier then humans, but much faster then them, but are more Susceptible to illusions and elemental damage.")
        embed.add_field(name="Beastkin", value="Sometimes indistinguishable from humans, and are fundamentally the same, but have animal features/body parts, slightly better physical attributes than humans, and can see in the dark.  Beastkin's animal features can range from just animal ears, to taking on the body types of animals.  (examples: Sleek skin, gills, and shark teeth.  8 orb eyes, mandibles.  Bunny ears and bunny tail.  Wings on arms, talons.  Slimy body, stalk eyes, lumpy tail.  etc)")
        embed.add_field(name="Kitsune", value="Closely related to Beastkin, they either look human, with multiple fox tails(1-9) and fox ears, or are humanoid and covered in fox fur and have a muzzle, in addition to tails and ears.  Kitsune are slightly faster then humans and can shapeshift")


        await sendmsg(reply, embed=embed)

    elif received("=Magic="):
        embed = discord.Embed(title="~~Magic/Alchemy~~ Currently Locked", colour=discord.Colour(0xd6680e), description="Overview on Magic/Alchemy")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="About Magic/Alchemy", value="Only people with certain diseases, disabilities, ailments, and other conditions that set them apart from others can use magic, the worse/more impactful the condition is, the stronger the magic is.  Without preparation or timing of any sort, the most a magic user can do is create smart car-sized three dimensional shapes of elemental energy.  However, if certain rituals, potions, chemical blends, injuries, experiences, or other situations are put into play, various more powerful techniques become available.")
        embed.add_field(name="Bonuses and Buffs", value="If magic is used on the second day of any month, the day before new year, during quakes, during floods, under certain constellations, or during auspicious moments, magic users gain widly powerful abilities, abilities that caused  earlier inhabitants of both Earth and Rellstruck to mistake magic users as gods.  Any race can use magic, if the aforementioned conditions are met. Items made up of certain objects that went through certian rituals can also contain/conduct magic")

        await sendmsg(reply, embed=embed)

    elif received("=FaeTech="):
        embed = discord.Embed(title="FaeTech", colour=discord.Colour(0xd6680e), description="Overview on FaeTech")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="About FaeTech", value="A strange mystical kind of technology that only Fae can use.  Faetech is made of either black, brown, tan, or light grey stone with different colored runes.  Potency of Faetech is determined by the stone color; tier 1. grey, tier 2 tan, tier 3 brown, tier 4 black.  Grey and tan are common, brown is slightly rarer and harder to use, black is usually considered impossible to use to its fullest extent, and barely any Fae can actually use them.")
        embed.add_field(name="Abilities", value="Faetech, for the most part, can be categorized as either technical, offense, or defense.  Defense being shields, armor, and forcefields,  offensive being weapons and explosives, technical being all others.  Faetech can shoot lasers, use hard light constructs, utilize elemental abilities, summon objects, activate automated entities, grow, and many other things perceived as \"magic\" ")

        await sendmsg(reply, embed=embed)

    elif received("=Invite="):
        embed = discord.Embed(title="Invite your friends!", colour=discord.Colour(0xd6680e), description="Everything is better with friends, so come invite some!")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="Invite Link", value="https://discord.gg/eqZrU8M")

        await sendmsg(reply, embed=embed)

    elif received("=Blessings="):
        embed = discord.Embed(title="Blessings", colour=discord.Colour(0xd6680e), description="Some blessings come with restrictions, these are \n First Blessing: Restricted to all \n Unique Blessings: Staff Only \n Rare: Staff and Trusted only \n Common: Open to all")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="Unobtainable Blessings", value="Death Blessing \nLife Blessing \nGale Blessing \nEarth Blessing \nFlame Blessing \nAqua Blessing \nSolar Blessing \nLunar Blessing", inline=False)
        embed.add_field(name="Rare", value="Time+Space: Acceleration Blessing \n  User can accelerate their body, effectively gaining super speed, as well as accelerate objects forwards.  User can also run up walls and on water \n\nTime+Life: Bio Blessing \n  User can temporarily grow animal body parts as well as gain animal senses.  User is also strengthened when around nature \n\nDeath+Life: Toxic Blessing \n   User can create and manipulate a hazardous purple and green water like substance, or a hazardous purple and green gas.  The substance can have many effects, such as temporary loss of one or more senses, draining energy, a “lifesteal” effect, corrode weak metals\n\nGale+Life: Weather Blessing \n  User can manipulate and create weather phenomenons\n\nGale+Aqua: Frost Blessing \n    User can create and control Ice\n\nGale+Flame: Tesla Blessing \n   User can create and control electricity\n\nSpace+Earth: Gravity Blessing \n    Can control and redirect the gravitational pull/ personal gravity of people and objects", inline=False)
        embed.add_field(name="Rare (cont)", value="Life+Earth: Environment Blessing \n User can create a environment or parts of a environment \n\nGale+Earth: Sand Blessing \n    User can create and manipulate sand \n\nAqua+Earth: Mud Blessing \n    User can create and manipulate mud \n\nFlame+Earth: Magma Blessing \n  User can create and manipulate magma \n\nLunar+Earth: Shadow Blessing \n User can manipulate and solidify shadows \n\nSolar+Lunar: Celestial Blessing \n  User can create and in some cases manipulate celestial energies/bodies", inline=False)
        embed.add_field(name="Uncommon", value="Earth+Tesla: Magnet Blessing\n  User can create and manipulate metals, as well as manipulate magnetic energies\n\nAcceleration+Gale: Jet Blessing\n  User can create jets of wind from and around their body, used for propulsion, enhancement, and diffusion of damage\n\nFlame+Tesla: Esp Blessing\n  User gains telekinetic and telepathic abilities\n\nFlame+Toxic: Smog Blessing\n  User can create and manipulate smoke, to the point where it becomes solid\n\nGravity+Celestial: Black hole\n  User can create black holes, however it is just a gravitational pull, and will not crush matter\n\nMagma+Sand: Glass Blessing\n  User can create and control any kind of glass\n\nSolar+Bio: Bio-luminescence Blessing\n  User gains Bio-luminescence, as well as the ability to project solid and/or concussive light\n\nMagma+Mud: Slime Blessing\n  User can secrete and manipulate a orange slimy substance", inline=False)
        embed.add_field(name="Rarity: Common x1", value="Space+Esp: Portal Blessing \nUser can create portals in the shape of discs or orbs\n \nLife+Esp: Cleanse Blessing\nUser can heal injuries, purify certain things, create barriers, and nullify the negative effects  \n \nDeath+Esp: Spirit Blessing\nUser can commune with the dead, as well as float and become invisible for a time\n \nBio+Gale: Sound Blessing\nUser can magnify sound, increase hearing, and vibrate their bodies using sound\n \nBio+Esp: Clairvoyance Blessing\nUser can see a few seconds into the future, as well as see the breaking points, pressure points, how much force something needs to break, and see through illusions.\n \nSlime+Aqua: Absorption blessing\nUser can absorb kinetic energy, and either redirect it or strengthen themselves temporarily\n \nEnvironment+Toxic: Fungi Blessing\nUser can create and manipulate fungi", inline=False)
        embed.add_field(name="Rarity: Common x1 (cont)", value="Smog+Esp: Mirage Blessing\nUser can create illusions, however the illusions are broken upon contact\n \nSmog+Sand: Dust Blessing\nUser can create and manipulate dust\n \nCrystal+Esp: Energy Blessing\nUser can generate, transform, and transfer energy\n \nGlass+Esp: Reflection Blessing\nThe user can reflect solids, liquids, gases, and other things around their bodies", inline=False)
        embed.add_field(name="Rarity: Common x2", value="Fungi+Time: Regeneration Blessing\nUser can regenerate body parts and heal themselves\n \nReflection+Earth: Crystal Blessing\nUser can create and manipulate crystals\n \nSound+Portal: Phase Blessing\nUser can phase through people and objects, as well as cause items and people they are holding to phase\n \nEnergy+Flame: Plasma Blessing\nUser can create and control plasma\n \nEnergy+Bio: Strength Blessing\nUser can strengthen themselves at the cost of stamina\n \nBio+Portal: Clone Blessing\nUser can clone themselves\n \nBio+Spirit: Civilization Blessing\nUser can create almost any man-made constructs/objects not made for transportation or attack\n \nSolar+Spirit: Holy Blessing\nUser can project holy concussive or defensive energies\n \nEnergy+Magnet: Mechanical Blessing\nUser can “speak” to machines, has increased mechanical skill, and can control machines almost telepathically\n \nMirage+Reflection: Mimic Blessing\nUser can mimic sounds, body parts, and appearances of any living or non-living thing\n", inline=False)
        
        await sendmsg(reply, embed=embed)

        embed = discord.Embed(title="Blessings", colour=discord.Colour(0xd6680e), description="Some blessings come with restrictions, these are \n First Blessing: Restricted to all \n Unique Blessings: Staff Only \n Rare: Staff and Trusted only \n Common: Open to all")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")


        embed.add_field(name="Rarity: Common x2 (cont)", value="Fungi+Spirit: Rot Blessing\nUser can cause skin, plants, and other related materials rot temporarily", inline=False)
        embed.add_field(name="Rarity: Common x3", value="Clairvoyance+Holy: Luck Blessing\nUser randomly increases positive and negative luck for themselves and others\n \nRot+Holy: Corruption Blessing\nUser can “corrupt” plants, animals, and objects, temporarily changing and/or controlling them\n \nCivilization+Earth: Rubber Blessing\nUser can stretch their bodies to extreme lengths, heights, and widths, while retaining control of their bodies\n \nCivilization+Toxic: Pollution Blessing\nUser can manipulate all forms of pollution, user also becomes stronger near pollution\n \nCivilization+Tesla: Data Blessing\nUser can store and transfer digital data, interface digital devices, systems, and databases without outside help\n \nCivilization+Magnet: Weapon Blessing\nUser can create weapons and control them\n \nEarth+Slime: Oil Blessing\nUser can create and manipulate oil", inline=False)
        embed.add_field(name="Rarity: Common x4", value="Flame+Weapon: Explosion Blessing\nUser can create explosions explosions around themselves and objects they’ve touched\n \nPollution+Bio: Chemical Blessing\nUser can create and manipulate chemicals, and also cause chemical reactions\n \nPollution+Spirit: Phantom Blessing\nUser can possess objects, plants, and animals.  User can also become intangible for a few seconds\n \nRubber+Space: Size Blessing\nUser can shrink and grow themselves or individual body parts", inline=False)
        embed.add_field(name="Rarity: Common x5", value="Corruption+Phantom: Infernal Blessing\nUser can create and manipulate infernal concussive or defensive energies\n \nExplosion+Reflection: Implosion Blessing\nThe user can cause plants and objects to implode", inline=False)

        await sendmsg(reply, embed=embed)

    elif message.content.lower().find("=help=") == 0:
        embed = discord.Embed(title="Information Commands", colour=discord.Colour(0xd6680e), description="All information commands")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="=Lineage=", value="Presents Lineage Information", inline=False)
        embed.add_field(name="=Species=", value="Presents Species Information", inline=False)
        embed.add_field(name="=Magic=", value="Presents Magic/Alchemy Information", inline=False)
        embed.add_field(name="=FaeTech=", value="Presents FaeTech Information", inline=False)
        embed.add_field(name="=Blessings=", value="Lists Blessings Information", inline=False)

        await sendmsg(reply, embed=embed)

        embed = discord.Embed(title="Assistance Commands", colour=discord.Colour(0xd6680e), description="All bot commands")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="=help=", value="Shows this card", inline=False)
        embed.add_field(name="=Bot=", value="Presents Creator Information and Message", inline=False)
        embed.add_field(name="=Invite=", value="An invite code to the Mirai RP server is shown", inline=False)

        await sendmsg(reply, embed=embed)

    elif received("=Bot="):
        
        creator = message.server.get_member("474551359140528128")
        pichash = creator.avatar
        embed = discord.Embed(title="Thanks for using me!", colour=discord.Colour(0x2d8ce2), url="https://discordapp.com/oauth2/authorize?client_id=499948714337763329&permissions=2146958847&scope=bot", description="This took my creator some time to make")

        print(pichash)
        embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/HfR2VUvbtgDrYRhtJYtbVRG8ptOUXl0szXSCAOAiC_8/https/discordapp.com/assets/ee7c382d9257652a88c8f7b7f22a994d.png?width=800&height=420")
        embed.set_footer(text="Made by Dungeons of Dragons", icon_url="https://cdn.discordapp.com/avatars/474551359140528128/" + pichash + ".png")


        await sendmsg(reply, embed=embed)

    elif received("=How="):
        embed = discord.Embed(title="Designs", colour=discord.Colour(0xd6680e), description="If you'd like to help out, you can use the [embed visualizer!](https://leovoel.github.io/embed-visualizer/) then export the code using the generate code button as Discord.py. I recommend using [pastebin](https://pastebin.com) and sending Dragons of Demons the link")

        embed.set_thumbnail(url="https://cdn.discordapp.com/icons/499487329635794945/3de65d781670e4dcc713eca8cfc95f11.png")
        embed.set_author(name="Mirai RP Server")
        embed.set_footer(text="I got bored okay?")

        embed.add_field(name="Example", value="Here's an example of the then incomplete [Blessings List](https://pastebin.com/vWUCQXJX)", inline=False)

        await sendmsg(reply, embed=embed)

    elif message.content.lower().find("=profit=") == 0:
        idhash = message.author.id
        await sendmsg(reply, str(idhash))
        # Your idea was to create a JSON file listing the necessary stuff
        # You'll need three JSON files
        # One will store the IDs of the user
        # The other two will store the amount of money they have
        # and the last time they claimed the daily
        # for now, I'm going to bed, see ya after
        
        
bot.loop.create_task(playStatus())
bot.run(token)
