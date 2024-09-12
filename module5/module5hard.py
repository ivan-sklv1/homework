import time


class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode 

    def __str__(self):
        return f"{self.title}"

class User:
    
    
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age
    
    def __str__(self):
        return f"{self.nickname}"
    
    def __eq__(self, other):
        return self.nickname == other.nickname
    
    def __hash__(self):
        return hash(self.password)


class UrTube:
    
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
    
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
    
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует.')
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)
    
    def log_out(self):
        self.current_user = None
        
    def add(self, *args):
        for video in args:
            self.videos.append(video)
    
    def get_videos(self, text):
        result = []
        for video in self.videos:
            if text.lower() in video.title.lower():
                result.append(video.title)
        return result

    def watch_video(self, movie):
        if self.current_user and self.current_user.age < 18:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(1, video.duration + 1):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')
            
        def __str__(self):
            return f'Текущий пользователь: {self.current_user}' if self.current_user else 'Аккаунт не авторизован'


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
