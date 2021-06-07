from telethon import TelegramClient, events, sync

api_id = 'PEGAR_CODIGO_NO_TELEGRAM'
api_hash = 'PEGAR_CODIGO_NO_TELEGRAM'

client = TelegramClient('gthabitacao', api_id, api_hash)

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    async for dialog in client.iter_dialogs():
        if dialog.name.find("GT HabitaAção") != -1:
            print(dialog.name, 'has ID', dialog.id)
            messages = client.iter_messages(dialog.name)
            async for message in messages:
                print(f'\tMensagem: {message}')


with client:
    client.loop.run_until_complete(main())

