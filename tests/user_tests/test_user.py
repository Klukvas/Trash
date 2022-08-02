from UsersData.main import Users
from ..src.response import Response
from ..src.response_validator import User


def test_getting_all_users():
    all_users_response = Users().get_all_users()
    resp_obj = Response(all_users_response)
    resp_obj.\
        check_status_code().\
        check_schema(User)