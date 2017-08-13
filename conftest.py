import pytest

from users.models import User


@pytest.fixture(scope='function')
def users():
    users = [{
        'username': 'qodot',
        'password': '1234',
    }]

    for user in users:
        new_user = User.objects.create(**user)
        new_user.set_password(user['password'])
        new_user.save()

    yield
    User.objects.all().delete()
