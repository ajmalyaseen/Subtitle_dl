from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn




@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        text="Hello ๐๐ป {}!\n\n๐ ๐๐ฆ ๐ฌ๐ข๐ฆ๐ฉ๐ฅ๐ ๐ฒ๐๐ญ ๐ฉ๐จ๐ฐ๐๐ซ๐๐ฎ๐ฅ ๐๐จ๐ญ ๐ญ๐จ ๐๐จ๐ฐ๐ง๐ฅ๐จ๐๐ ๐๐จ๐ง๐ ๐ฌ ๐๐ฎ๐๐ข๐จ ๐๐ง๐ ๐๐ข๐๐๐จ \n\n๐๐ญ๐ช๐ค๐ฌ /help ๐๐ฐ๐ณ ๐๐ฐ๐ณ๐ฆ ๐๐ฆ๐ญ๐ฑ ๐๐ฏ ๐๐บ ๐๐ด๐ข๐จ๐ฆ โค".format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("๐ซUPDATES", url="https://t.me/CoderzHEX"),
            InlineKeyboardButton("๐ตโโCREATOR", url="https://t.me/DIAGO_X")
            ],[
            InlineKeyboardButton("๐ABOUT", callback_data= "about"),
            InlineKeyboardButton("๐ CLOSE", callback_data= "close")
            ]]
        ),
        disable_web_page_preview=True
    )



@Client.on_callback_query()
async def cb_handler(client, query):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b><u>About Me</u></b>\n\nโข ๐๐๐ฆ๐ : แดแด๊ฑษชแด แดส \n\nโข ๐๐๐ง๐ ๐ฎ๐๐ ๐ : แดแดสแดแดษด \n\nโข ๐๐ข๐๐ซ๐๐ซ๐ฒ : แดสสแดษขสแดแด \n\nโข ๐๐๐ซ๐ฏ๐๐ซ :  สแดสแดแดแด \n\nโข ๐๐ญ๐๐ญ๐ฎ๐ฌ :  V 1.0 \n\nโข ๐๐ซ๐๐๐ญ๐จ๐ซ : <b><a href='https://t.me/diago_x'>แดษชแดษขแด</a></b>\n\n<b>แดแดแดแดแดแดแด แดษด 22-5-21 ษชษดแดษชแดษด แดษชแดแด 11:00 แดแด</b>\n\n<b><a href='https://t.me/coderzHex'>ยฉแดแดแดแดสแดขสแดx</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("๐CLOSE", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start", "start@GroupMusicPlayBot"]) & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text(
          text="**Music Bot Is Online โ**",
          reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="๐๏ธ Support Group ๐๏ธ", url="https://t.me/MusicBotSupports")
              ]]
          )
      )


@Client.on_message(filters.command(["help", "start@GroupMusicPlayBot"]) & filters.private & ~filters.channel)
async def help(_, message: Message):
    await message.reply_text(
        text="""๐๐ค๐ฌ ๐๐ค ๐ฟ๐ค๐ฌ๐ฃ๐ก๐ค๐๐ ๐๐ค๐ฃ๐

๐ก /song ๐๐จ๐ง๐  ๐๐๐ฆ๐ : แดแดแดกษดสแดแดแด สแดแดส ๊ฑแดษดษข แดแด แดแดแดษชแด

๐ก /vid ๐ฌ๐จ๐ง๐  ๐๐๐ฆ๐ : แดแดแดกษดสแดแดแด สแดแดส ๊ฑแดษดษข แดแด แด ษชแดแดแด

โข๐๐๐๐ซ๐๐ก ๐ฌ๐จ๐ง๐  ๐๐จ๐ฎ๐๐ฎ๐๐ ๐ฅ๐ข๐ง๐ค

๐ก /search ๐ฌ๐จ๐ง๐  ๐ง๐๐ฆ๐ : ษขแดแด สแดแดส ๊ฑแดษดษข สแดแดแดแดสแด สษชษดแด


@CoderzHex
 """,
        reply_markup=InlineKeyboardMarkup(
              [[
              InlineKeyboardButton(text="๐ซUPDATES", url="https://t.me/CoderzHEX"),
              InlineKeyboardButton("๐CLOSE", callback_data = "close")
              ]]
          )
      )
