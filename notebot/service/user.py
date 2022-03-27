from notebot.models.user import User


class UserAlreadyExists(Exception):
    pass


async def create(user_id, username, full_name, language_code) -> User:
    is_exist = await User.exists(id=user_id)

    if is_exist:
        raise UserAlreadyExists("User already exists")

    user = await User.create(
        id=user_id,
        username=username,
        full_name=full_name,
        language=language_code,
    )

    return user
