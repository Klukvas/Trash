from requests import get


class Users:
    
    def __init__(self):
        self.main_url = "https://gorest.co.in/"

    def get_all_users(self):
        response = get(self.main_url + "public/v2/users")
        return response
    
    def get_user_data(self, usr_id):
        response = get(self.main_url + f"/public/v2/users/{usr_id}")
        return response
    
    def get_posts_of_user(self, usr_id):
        response = get(self.main_url + f"/public/v2/users/{usr_id}/posts")
        return response



if __name__ == "__main__":
    o = Users()
    print(o.get_posts_of_user(1).json())