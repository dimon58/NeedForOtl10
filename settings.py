import os

from pygame.constants import USEREVENT

# Разрешение экрана
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

# скорость, ниже которой модули всех скоростей считются нулём
critical_speed = 1e-2

# косинус угола между реакцией опоры(которая не равна 0) и нормалью, при которой считается устройчивая опора для ног
# Коэффициент трения = sqrt(1/critical_ground_collision**2 - 1)
critical_ground_collision = 0.35

# Максимальная скорость отскока от земли, при которой не засчитывается полёт
# Не должна быть слишком большой, иначе не будет ощущения, что игрок сразу начинает падать, при отсутствии опоры для ног
# Не должна быть маленькой, иначе будуь засчитываться ложные смены статуса на полёт
bounce_correction_speed = 1

# Критический уровень перезарядки, при котором уже можно снова ипользовать способность
critical_reloading = 0.01

# отклонение от угла, при котором не происоходит перерисовывание
no_rotate_delta = 0.1

# Ускорение свободного падения
g = 9.81

# Режим разработчика по умолчанию
DEVMODE = True

# Путь до папки с конфигарациями персонажей
person_configs_path = os.path.join('src', 'configs', 'persons')

# Путь до папки с конфигарациями статичных объектов
game_objects_configs_path = os.path.join('src', 'configs', 'game_objects')

# Путь до папки с фоновой музыкой для меню
menu_music_path = os.path.join('Resources', 'Music', 'Menu')

# Путь до папки с фоновой музыкой для игры
game_music_path = os.path.join('Resources', 'Music', 'Fight')

# Путь до папки со звуками для игры
game_sounds_path = os.path.join('Resources', 'Music', 'States_of_player')

# Событие конца музыки
SONG_END = USEREVENT + 1

# Уровень громкости фоновой музыки в меню
menu_music_volume = 0.1
# Уровень громкости фоновой музыки в игре
game_music_volume = 0.1

# Громкость звуков
sounds_volume = 1.0

# Громкость звуков персонажей
persons_volume = 1.0

# Громкость музыки
music_volume = 1.0

# Глобальная громкость звуков
global_volume = 1.0

# Шаг регулировки громкости
volume_delta = 0.1

# Дефолтные звуки
default_sounds_path = os.path.join('Resources', 'Music', 'States_of_player', '_default_sounds.yaml')

# ДЕфолтный персонаж
default_person_path = os.path.join('src', 'configs', 'persons', '_default_person.yaml')
