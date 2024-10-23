import yaml

class AuthProvider:
    def __init__(self):
        with open('config/config.yaml', 'r') as file:
            config = yaml.safe_load(file)
            self.username = config['auth']['username']
            self.password = config['auth']['password']

    def get_auth_data(self):
        return {
            "username": self.username,
            "password": self.password
        }
