from aiogram import types
from database import models
from loader import dp

@dp.message_handler(commands='start')
async def start(message:types.Message) -> None:
    await message.answer('Hello!')