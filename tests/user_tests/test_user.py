from UsersData.main import Users
from ..src.response import Response
from ..src.response_validator import User, UserNotExists, Post
import pytest


@pytest.mark.all_users
def test_getting_all_users():
    all_users_response = Users().get_all_users()
    resp_obj = Response(all_users_response)
    resp_obj.\
        check_status_code().\
        check_schema(User)

@pytest.mark.one_user
@pytest.mark.parametrize("user_id,existing", [(3336, True), (1, False)])
def test_getting_user_data(user_id, existing):
    user_data_response = Users().get_user_data(user_id)
    if existing:
        resp_obj = Response(user_data_response)
        resp_obj.\
            check_status_code().\
            check_schema(User)
    else:
        resp_obj = Response(user_data_response)
        resp_obj.\
            check_status_code(404).\
            check_schema(UserNotExists)


@pytest.mark.user_posts
@pytest.mark.parametrize("user_id,existing", [(3327, True), (1, False)])
def test_getting_user_post(user_id, existing):
    user_data_response = Users().get_posts_of_user(user_id)
    if existing:
        resp_obj = Response(user_data_response)
        resp_obj.\
            check_status_code().\
            check_schema(Post)
    else:
        resp_obj = Response(user_data_response)
        resp_obj.\
            check_status_code().\
            check_value_type_of_response