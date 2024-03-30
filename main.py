from context import getRoomLink, isRoomComplete, getRoomId
from telebot.async_telebot import AsyncTeleBot
import os

token = os.environ.get("TOKEN_KONTEKSTNO")
rooms = {}
bot = AsyncTeleBot(token)

@bot.message_handler(commands=['го', 'start'])
async def send_welcome(message):
    try:
        msgText = ""
        pinMsg = False
        if str(message.chat.id) in rooms.keys() and not isRoomComplete(rooms[str(message.chat.id)]):
            msgText = "Вам необходимо закончить комнату - " + getRoomLink(rooms[str(message.chat.id)])
        else:
            roomId = getRoomId()
            rooms[str(message.chat.id)] = roomId
            msgText = "Ваша комната - " + getRoomLink(roomId)
            pinMsg = True
            
        sm = await bot.send_message(message.chat.id, msgText)
        if pinMsg:
            await bot.pin_chat_message(message.chat.id, sm.message_id)
    except:
        pass

async def f():
    while True:
        try:
            await asyncio.sleep(5)
            for key in rooms:
                if isRoomComplete(rooms[key]):
                    await bot.unpin_all_chat_messages(key)
                    await bot.send_message(key, "Комната " + rooms[key] + " успешно завершена")
                    roomId = getRoomId()
                    rooms[key] = roomId
                    sm = await bot.send_message(key, "Ваша комната - " + getRoomLink(roomId))
                    await bot.pin_chat_message(key, sm.message_id)

                    
        except:
            pass


import asyncio        
async def main():
    task1 = asyncio.create_task(f())
    task2 = asyncio.create_task(bot.polling())

    await task1
    await task2
asyncio.run(main())
