from time import sleep


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def __contains__(self, other):
        if isinstance(other, str):
            return any(user.nickname == other for user in self.users)

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break

    def register(self, nickname, password, age):
        if nickname in ur:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = User(nickname, password, age)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for video in args:
            self.videos.append(video)

    def get_videos(self, title):
        videos_list = []
        for video in self.videos:
            if title.lower() in video.title.lower():
                videos_list.append(video.title)
        return videos_list

    def watch_video(self, title):
        if self.current_user is not None:
            for video in self.videos:
                if video.title == title:
                    if video.adult_mode is True and ur.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                        break
                    else:
                        for i in range(video.time_now + 1, video.duration + 1):
                            print(i, end=' ')
                            sleep(1)
                        print('Конец видео')
                        video.time_now = 0
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


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

    def __str__(self):
        return self.nickname


if __name__ == '__main__':
    ur = UrTube()

    v1 = Video('Лучший язык программирования 2024 года', 200)

    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео

    ur.add(v1, v2)

    # Проверка поиска

    print(ur.get_videos('лучший'))

    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение

    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('vasya_pupkin', 'lolkekcheburek', 13)

    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт

    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео

    ur.watch_video('Лучший язык программирования 2024 года!')
