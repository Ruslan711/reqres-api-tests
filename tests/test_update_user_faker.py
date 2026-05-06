from faker import Faker

from services.reqres_in.users.patch_update import UpdateUser
from services.reqres_in.users.models.user import UpdateUserRequest, UpdateUserResponse

fake = Faker()


def test_update_user_faker(env_config):
    name = fake.name()
    job = fake.job()

    user_request = UpdateUserRequest(
        name=name,
        job=job,
    )

    response, updated_user = UpdateUser(env_config).update(
        user_id=2,
        request=user_request,
    )

    assert response.status_code == 200
    assert isinstance(updated_user, UpdateUserResponse)

    assert updated_user.name == user_request.name
    assert updated_user.job == user_request.job
    assert updated_user.updatedAt is not None