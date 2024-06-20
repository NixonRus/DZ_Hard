import time


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, login, password):
        self.login = login
        self.password = password



class Video:
    def __init__(self, title: str, duration: time.ctime(secs=), time_now: time.ctime(secs=0), adult_mode: bool):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode



class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

user = User('Batman', 123456, 23)
print(user)