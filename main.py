import asyncio
import logging
from os import path
from config.loader import dp
from handlers.user import start  # Импорт файла
# python -c "import aiogram; print(aiogram.__version__)" - узнать версию
# python -c "from aiogram.contrib.fsm_storage import MemoryStorage; print('Успех!')"

logging.basicConfig(filename=path.join("data", "log.txt"), level=logging.INFO,
                    format="%(asctime)s %(message)s", filemode="w")


async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())  # Автоматически создает event loop
