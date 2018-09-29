# quantumutils documentation

So quantumutils is my first attempt at making a library that everyone can use, and it includes several of the utilities that I use to make my bot.

### Installation
`python -m pip install quantumutils`

### Contents
- Basic functions 
  - tdm()
  - find()
  - getjson()
- Some better utilities
  - Pages
  - FieldPages
  - A sample HelpPaginator
  - SimplePaginator

### Usage

Some sample code outlining some of the functions of my bot.
```python
import quantumutils
print(quantumutils.find("Lorem","Lorem Ipsum Lorem"))
>>> [0,12]
print(await quantumutils.getjson("www.randomjsonreturner.com"))
>>> {
        "some":{
                 "structured":"JSON",
                 "result":"returned",
                  "as","a"
             },
         "dictionary":"."
     }

#discordbotapp.py
import quantumutils
import discord
from discord.ext import commands
bot = commands.Bot(prefix=".",description="A sample bot")
@bot.command()
async def paginatedcommand(ctx):
    embeds=[discord.Embed(title="One",description="1"),discord.Embed(title="Two",description="2"),discord.Embed(title="Three",description="3")]
    await quantumutils.SimplePaginator(extras=embeds).paginate(ctx)
```

### Notes
Quite a bit of the code in the module are from other external sources, which I copied (and modified to add some of my own effort).
I understand that I should not be doing this technically. But, I find it useful if all those scattered utilities are compiled into
one utility module, plus some of my own utilities, then everyone can use.