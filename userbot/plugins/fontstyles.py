""" .weeb a text By :- @PhycoNinja13b
 .downside by @sn12384"""
import re
import time
import requests
from telethon import events
from userbot import CMD_HELP, fonts
from userbot.utils import register, admin_cmd
import asyncio
import random



@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    if not vpr.text[0].isalpha() and vpr.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await vpr.get_reply_message()
        message = vpr.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
            return

        for charac in message:
            if 0x21 <= ord(charac) <= 0x7F:
                reply_text.append(chr(ord(charac) + 0xFEE0))
            elif ord(charac) == 0x20:
                reply_text.append(chr(0x3000))
            else:
                reply_text.append(charac)

        await vpr.edit("".join(reply_text))

@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    if not stret.text[0].isalpha() and stret.text[0] not in ("/", "#", "@", "!"):
        textx = await stret.get_reply_message()
        message = stret.text
        message = stret.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
            return

        count = random.randint(3, 10)
        reply_text = re.sub(
            r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])",
            (r"\1"*count),
            message
        )
        await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    if not zgfy.text[0].isalpha() and zgfy.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await zgfy.get_reply_message()
        message = zgfy.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await zgfy.edit(
                "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
            )
            return

        for charac in message:
            if not charac.isalpha():
                reply_text.append(charac)
                continue

            for _ in range(0, 3):
                randint = random.randint(0, 2)

                if randint == 0:
                    charac = charac.strip() + \
                        random.choice(fonts.ZALG_LIST[0]).strip()
                elif randint == 1:
                    charac = charac.strip() + \
                        random.choice(fonts.ZALG_LIST[1]).strip()
                else:
                    charac = charac.strip() + \
                        random.choice(fonts.ZALG_LIST[2]).strip()

            reply_text.append(charac)

        await zgfy.edit("".join(reply_text))

    
@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    if not cp_e.text[0].isalpha() and cp_e.text[0] not in ("/", "#", "@", "!"):
        textx = await cp_e.get_reply_message()
        message = cp_e.pattern_match.group(1)

        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
            return

        reply_text = random.choice(fonts.EMOJIS)
        b_char = random.choice(
            message
        ).lower()  # choose a random character in the message to be substituted with 🅱️
        for owo in message:
            if owo == " ":
                reply_text += random.choice(fonts.EMOJIS)
            elif owo in fonts.EMOJIS:
                reply_text += owo
                reply_text += random.choice(fonts.EMOJIS)
            elif owo.lower() == b_char:
                reply_text += "🅱️"
            else:
                if bool(random.getrandbits(1)):
                    reply_text += owo.upper()
                else:
                    reply_text += owo.lower()
        reply_text += random.choice(fonts.EMOJIS)
        await cp_e.edit(reply_text)

        
@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    if not mock.text[0].isalpha() and mock.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await mock.get_reply_message()
        message = mock.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
            return

        for charac in message:
            if charac.isalpha() and random.randint(0, 1):
                to_app = charac.upper() if charac.islower() else charac.lower()
                reply_text.append(to_app)
            else:
                reply_text.append(charac)

        await mock.edit("".join(reply_text))
        
        
        
@borg.on(admin_cmd(pattern="weeb ?(.*)"))
async def weebify(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text   
    if not args:
        await event.edit("`What I am Supposed to Weebify `")
        return
    string = '  '.join(args).lower()
    for normiecharacter in string:
        if normiecharacter in fonts.normiefont:
            weebycharacter = fonts.weebyfont[fonts.normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)
    await event.edit(string)        

   

@borg.on(admin_cmd(pattern="downside ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for upsidecharacter in string:
        if upsidecharacter in fonts.upsidefont:
            downsidecharacter = fonts.downsidefont[fonts.upsidefont.index(upsidecharacter)]
            string = string.replace(upsidecharacter, downsidecharacter)
    await event.edit(string)   
    
    
    
@borg.on(admin_cmd(pattern="smothtext ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smothtextcharacter = fonts.smothtextfont[fonts.normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, smothtextcharacter)
    await event.edit(string)  
 
@borg.on(admin_cmd(pattern="blackbubbles ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblesblackcharacter = fonts.bubblesblackfont[fonts.normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, bubblesblackcharacter)
    await event.edit(string)  
 
@borg.on(admin_cmd(pattern="bubbles ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            bubblescharacter = fonts.bubblesfont[fonts.normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, bubblescharacter)
    await event.edit(string) 
 
@borg.on(admin_cmd(pattern="subscript ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            subscriptcharacter = fonts.subscriptfont[fonts.normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, subscriptcharacter)
    await event.edit(string)  
 
@borg.on(admin_cmd(pattern="superscript ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            superscriptcharacter = fonts.superscriptfont[fonts.normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, superscriptcharacter)
    await event.edit(string) 
 
@borg.on(admin_cmd(pattern="smallcaps ?(.*)"))
async def stylish_generator(event):
    args = event.pattern_match.group(1)
    if not args:
        get = await event.get_reply_message()
        args = get.text 
    if not args:    
        await event.edit("What I am Supposed to change give text")
        return
    string = '  '.join(args).lower()
    for normaltextcharacter in string:
        if normaltextcharacter in fonts.normaltext:
            smallcapscharacter = fonts.smallcapsfont[fonts.normaltext.index(normaltextcharacter)]
            string = string.replace(normaltextcharacter, smallcapscharacter)
    await event.edit(string) 
  
CMD_HELP.update({
    "fontstyles": ".cp (text) or .cp reply to message \
\nUsage: inserts some emojis in between the texts\
\n\n.vapor (text) or .vapor reply to message \
\nUsage: Vaporize the given text. \
\n\n.str (text) or .str reply to message \
\nUsage: Stretchs the given message.\
\n\n.zal (text) or .zal reply to message \
\nUsage: Invoke the feeling of chaos.\
\n\n.mock (text) or .mock reply to message \
\nUsage: random capital and small letters in given text.\
\n\n.weeb (text) or .weeb reply to message \
\nUsage: a different style of alphabets .\
"
})
        
    
