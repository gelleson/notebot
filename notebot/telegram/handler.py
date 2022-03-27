from notebot.telegram import dispatcher
from aiogram import types

from notebot.models import User, Role, Note
from notebot.models import notes
from notebot.service import user

from aiogram.dispatcher.filters import Regexp

from .app import bot

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class TextNote(StatesGroup):
    note = State()


@dispatcher.message_handler(commands='start')
async def start(message: types.Message, user: User):
    await message.answer(f'Hello, {user.full_name}!')


@dispatcher.message_handler(commands='note')
async def note(message: types.Message, user: User):
    await TextNote.note.set()
    await message.answer('Send your note')


@dispatcher.message_handler(state=TextNote.note)
async def note(message: types.Message, user: User, state: FSMContext):
    n = await Note.create(
        owner=user,
        note=message.text,
        note_type=notes.NoteType.TEXT,
    )

    for i in message.entities:
        if i.type == 'hashtag':
            await notes.TagNote.create(
                note=n,
                tag=(await notes.Tag.get_or_create(
                    name=i.get_text(message.text)
                ))[0]
            )
    await message.answer(f'Note saved #{n.id}!')
    await message.delete()
    await state.finish()


@dispatcher.message_handler(
    Regexp("((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]+\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&\/\?\:@\-_=#])*"))
async def url(message: types.Message, user: User):
    await notes.Note.create(
        owner=user,
        note=message.text,
        note_type=notes.NoteType.URL,
    )

    await message.delete()
    await message.answer('URL saved!')


@dispatcher.message_handler(Regexp('^#[a-zA-Z0-9_]+$'))
async def tag_note(message: types.Message, user: User):
    n = await notes.Note.filter(
        tags__tag=message.text
    )

    if len(n) == 0:
        await message.answer('No notes found!')

    for i in n:
        await message.answer(i.note)


@dispatcher.message_handler(commands='iamadmin')
async def i_am_admin(message: types.Message, user: User):
    count = await User.filter(role=Role.ADMIN).count()

    if count == 0:
        user.role = Role.ADMIN
        await user.save(
            update_fields=['roles']
        )
        await message.answer('Yes, you are admin!')
    elif user.role == Role.ADMIN:
        await message.answer('You are already admin!')
    else:
        await message.answer('Sorry, but there is already an admin!')
