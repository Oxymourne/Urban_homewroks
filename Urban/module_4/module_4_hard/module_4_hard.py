class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, other):
        if isinstance(other, str):
            return any(user.nickname == other for user in self.users)
        elif isinstance(other, list):
            return any(user.nickname == other[0] and user.password == hash(other[1]) for user in self.users)

    def log_in(self, nickname, password):
        if [nickname, password] in ur:
            self.current_user = nickname

    def register(self, nickname, password, age):
        if nickname in ur:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, hash(password), age))
            self.current_user = nickname

    def add(self, *args):
        for video in args:
            self.videos.append(video)



class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


if __name__ == '__main__':
    ur = UrTube()
    print(ur.current_user)
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    print(ur.current_user)
    print()
    ur.log_in('vasya_pupkin', 'lolkekcheburek')
    print(ur.current_user)
