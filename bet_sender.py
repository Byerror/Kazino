from pyrogram import Client
from pyrogram.types import Message
import asyncio
from config import CHANNEL_ID

api_id = "20668090"#сюда свой апи ид
api_hash = "19dc666390d73b98aae44b77d4d8d25c"#а сюда апи хеш

app = Client('bot', api_id=api_id, api_hash=api_hash)

async def send_bet(username, summa, bet_type) -> int:
    await app.start()

    message_text = (
        "**[<emoji id=5282939632416206153>⛈</emoji>] Новая ставка!\n\n"
        f"> <emoji id=5258011929993026890>👤</emoji> Никнейм игрока: {username}\n\n"
        f"> <emoji id=5443038326535759644>💬</emoji> Игрок ставит на: {bet_type}\n\n"
        f"> <emoji id=5375296873982604963>💰</emoji> Сумма ставки: {summa}$**"
    )

    try:
        message: Message = await app.send_message(
            chat_id=CHANNEL_ID,
            text=message_text
        )

        return message.id
    finally:
        await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(send_bet('testusername', 100, 'больше'))
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        try:
            loop.run_until_complete(app.stop())
        except Exception as e:
            print(f"An error occurred while stopping the client: {e}")
