
import configparser

config=configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class Read_Config:
    @staticmethod
    def get_url():
        website=config.get('admin_login_info','url')
        return website

    @staticmethod
    def get_username():
        username = config.get('admin_login_info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('admin_login_info', 'password')
        return password

    @staticmethod
    def get_invalid_username():
        invalid_username = config.get('admin_login_info', 'invalid_username')
        return invalid_username
