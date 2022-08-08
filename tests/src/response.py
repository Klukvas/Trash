from hamcrest import *

class Response:

    def __init__(self, response) -> None:
        self.response = response

    def check_status_code(self, expected_status=200):
        assert_that(self.response.status_code, is_(expected_status))
        return self
    
    def check_schema(self, schema):
        if isinstance(self.response.json(), list):
            for item in self.response.json():
                schema.parse_obj(item)
        else: 
            print(self.response.json())
            schema.parse_obj(self.response.json())
        return self
    
    def check_value_type_of_response(self, excpected_type):
        assert_that(self.response.json(), is_(excpected_type))
        return self