import time

class User:
    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

user = User('Batman', 123456, 23)


class Video:
    def __init__(self, title: str, duration: time.ctime(secs=), time_now: time.ctime(secs=0), adult_mode: bool):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, login, password):
        self.login = login
        self.password = password
        if # пользователь найден в Users, то current_user меняется на найденного
            pass

    def register(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        if # пользователя нет в списке, добавляет его

        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        current_user = none

    def add(self):
        videos += 1

    def get_videos(self):
        pass

    def watch_video(self):
        pass







