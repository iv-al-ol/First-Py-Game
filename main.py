"""
Soundtrack - Fato Shadow
"""

#====================================================================
# Импорт необходимых модулей
#--------------------------------------------------------------------
import pygame as pg
import random as rnd
import os

#====================================================================
# Параметры окна
#--------------------------------------------------------------------
WIDTH = 1600
HEIGHT = 900
FPS = 60

pg.mixer.init()
pg.mixer.music.set_volume(0.1)
pg.display.set_caption("Cat vs Evil Hands")
screen = pg.display.set_mode((WIDTH, HEIGHT))
clock = pg.time.Clock()

#====================================================================
# Работа с файловой системой
#--------------------------------------------------------------------
folder_py = os.path.dirname(__file__)   # Директория .py файла

#####################################################################
# Функции для изображений
#####################################################################
def add_image(add_image_list, folder_img, quantity_img=None):
    """Добавляет изображение в игру.
    
    add_image_list -> tuple: Имена рисунков с расширениями файлов
        (например: ['pic_1.png', 'pic_2.png']);
    Если quantity_img != None:
        add_image_list -> str: Имя типа рисунка без номера и расширения
            (например: 'pic_');
          
    folder_img -> str: Имя папки с изображениями
        (например: 'img\\folder');
    quantity_img -> int: Количество рисунков со схожими названиями;
        (например: при ['pic_1.png', 'pic_2.png'] должно быть 2);
    
    Возвращает сконвертированные изображения в составе списка.
    
    """
    folder_img = os.path.join(folder_py, str(folder_img))   # Определение папки с изображениями
    added_img_list = []
    if (quantity_img != None):
        for num in range(quantity_img):
            filename = ('%s{}.png' % add_image_list).format(num)
            added_img_list.append(pg.image.load(os.path.join(folder_img, filename)).convert_alpha())
    else:
        for img in add_image_list:    
            added_img_list.append(pg.image.load(os.path.join(folder_img, img)).convert_alpha())
        
    return added_img_list

def scale_image(scaling_img, zoom_sise):
    """Масштабирует изображение.
    
    scaling_img: Источник изображения;
    zoom_sise -> float: Величина масштабирования в %
        (например: 50 уменьшит размер изображения в два раза);
    
    """
    transform_img = pg.transform.scale(scaling_img,
                                       (scaling_img.get_width()*zoom_sise // 100,
                                        scaling_img.get_height()*zoom_sise // 100))
    return transform_img

def add_and_scale_image(img_name, folder_img, quantity_img, zoom_sise):
    """Добавляет и масштабирует однотипные изображения циклом.
    
    img_name -> str: Имя типа рисунка без номера и расширения
        (например: 'pic_');
    folder_img -> str: Имя папки с изображениями
        (например: 'img\\folder');
    quantity_img -> int: Количество рисунков со схожими названиями;
        (например: при ['pic_1.png', 'pic_2.png'] должно быть 2);
    zoom_sise -> float: Величина масштабирования в %
        (например: 50 уменьшит размер изображения в два раза);
    
    """
    img_list_name = []
    for num in range(quantity_img):
        filename = ('%s{}.png' % img_name).format(num)
        img = pg.image.load(os.path.join(folder_img, filename)).convert_alpha()
        
        img_transform = pg.transform.scale(img, (img.get_width()*zoom_sise // 100, img.get_height()*zoom_sise // 100))
        img_list_name.append(img_transform)
    return img_list_name

#====================================================================
# Добавление изображений
#--------------------------------------------------------------------
img_cat_player = {}
img_cat_player['move_left'] = add_and_scale_image('cat_', 'img\\cat\\move_left', 4, 200)
img_cat_player['move_right'] = add_and_scale_image('cat_', 'img\\cat\\move_right', 4, 200)
img_cat_player['move_up'] = add_and_scale_image('cat_', 'img\\cat\\move_up', 4, 200)
img_cat_player['move_down'] = add_and_scale_image('cat_', 'img\\cat\\move_down', 4, 200)

img_cat_player_lives = add_image(['cat_0.png'], 'img\\cat\\move_right')
img_cat_player_lives = img_cat_player_lives[0]
img_cat_player_lives = scale_image(img_cat_player_lives, 70)

img_bullets = add_image('bullet_', 'img\\bullets', 5)

img_evil_hand = add_image(['evil_hand.png'], 'img')
img_evil_hand = img_evil_hand[0]

img_background = add_image(['darkPurple.png'], 'img')
img_background = img_background[0]

img_blood_anim_1 = {}
img_blood_anim_1['small'] = add_and_scale_image('1_', 'img\\blood\\anim_1', 21, 100)
img_blood_anim_1['medium'] = add_and_scale_image('1_', 'img\\blood\\anim_1', 21, 200)
img_blood_anim_1['large'] = add_and_scale_image('1_', 'img\\blood\\anim_1', 21, 300)
img_blood_anim_2 = {}
img_blood_anim_2['small'] = add_and_scale_image('1_', 'img\\blood\\anim_2', 21, 100)
img_blood_anim_2['medium'] = add_and_scale_image('1_', 'img\\blood\\anim_2', 21, 200)
img_blood_anim_2['large'] = add_and_scale_image('1_', 'img\\blood\\anim_2', 21, 300)
img_blood_anim_3 = {}
img_blood_anim_3['small'] = add_and_scale_image('1_', 'img\\blood\\anim_3', 21, 100)
img_blood_anim_3['medium'] = add_and_scale_image('1_', 'img\\blood\\anim_3', 21, 200)
img_blood_anim_3['large'] = add_and_scale_image('1_', 'img\\blood\\anim_3', 21, 300)
img_blood_anim_4 = {}
img_blood_anim_4['small'] = add_and_scale_image('1_', 'img\\blood\\anim_4', 21, 100)
img_blood_anim_4['medium'] = add_and_scale_image('1_', 'img\\blood\\anim_4', 21, 200)
img_blood_anim_4['large'] = add_and_scale_image('1_', 'img\\blood\\anim_4', 21, 300)
img_blood_anim_5 = {}
img_blood_anim_5['small'] = add_and_scale_image('1_', 'img\\blood\\anim_5', 21, 100)
img_blood_anim_5['medium'] = add_and_scale_image('1_', 'img\\blood\\anim_5', 21, 200)
img_blood_anim_5['large'] = add_and_scale_image('1_', 'img\\blood\\anim_5', 21, 300)

#####################################################################
# Функции для звуков
#####################################################################
def add_sound(add_sound_list, folder_snd):
    """Добавляет звуки в игру.
    
    add_sound_list -> tuple: Имена звуков с расширениями файлов
        (например: ['sound_1.mp3', 'sound_2.wav']);
    folder_snd -> str: Имя папки со звуками;
        (например: 'snd\\folder');
        
    Возвращает добавленные звуки в составе списка.
    
    """
    folder_snd = os.path.join(folder_py, str(folder_snd))   # Определение папки со звуками
    added_sound_list = []
    for snd in add_sound_list:    
        added_sound_list.append(pg.mixer.Sound(os.path.join(folder_snd, snd)))
    return added_sound_list

def add_music(add_music_list, folder_snd):
    """Добавляет музыку в игру.
    
    add_music_list -> tuple: Имена музыки с расширениями файлов
        (например: ['music_1.mp3', 'music_2.wav']);
    folder_snd -> str: Имя папки c музыкой;
        (например: 'snd\\folder');
        
    Возвращает добавленную музыку в составе списка.
    
    """
    folder_snd = os.path.join(folder_py, str(folder_snd))   # Определение папки с музыкой
    added_music_list = []
    for mus in add_music_list:    
        added_music_list.append(pg.mixer.music.load(os.path.join(folder_snd, mus)))
    return added_music_list

#====================================================================
# Добавление звуков
#--------------------------------------------------------------------
soundtrack_1 = add_music(['soundtrack_1.mp3'], 'snd')
soundtrack_1 = soundtrack_1[0]

snd_shoot = add_sound(['shoot_1.wav', 'shoot_2.wav', 'shoot_3.wav'], 'snd')

snd_explosion = add_sound(['explosion_1.wav',
                           'explosion_2.wav', 'explosion_3.wav'], 'snd')

#====================================================================
# Задание цветов
#--------------------------------------------------------------------
WHITE         = (255, 255, 255)
BLACK         = (  0,   0,   0)
RED           = (255,   0,   0)
GREEN         = (  0, 255,   0)
BLUE          = (  0,   0, 255)
YELLOW        = (255, 255,   0)
JADE          = (  0, 168, 107)
DARK_BROWN    = (101,  67,  33)

#####################################################################
# Функции для игрового цикла
#####################################################################
def draw_ground():
    """Закрашивает фон экрана рисунком"""
    background_rect = img_background.get_rect()
    
    ground_limit_x = WIDTH // background_rect.width + 1
    ground_limit_y = HEIGHT // background_rect.height + 1
    
    for line_y in range (ground_limit_y):
        for line_x in range(ground_limit_x):
            screen.blit(img_background, (0 + line_x*(background_rect.height),
                                         0 + line_y*(background_rect.height)))

def debug_hits(self):
    """Рисует круг для проверки столкновений"""
    self.rect = self.image.get_rect()
    self.radius = self.image.get_height() // 2 - int(self.image.get_height() * 0.1)
    pg.draw.circle(self.image, RED, self.rect.center, self.radius)

def draw_text(surf, text, size, x, y):
    """Выводит текст на поверхности с заданными параметрами.
    
    surf: Поверхность отображения текста;
    text: Отображаемый текст;
    size: Размер шрифта;
    x: Координата середины блока текста по x;
    y: Координата верха блока текста по y;
    
    """
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def add_hands():
    """Добавляет врагов."""
    evil_h = EvilHand()
    all_sprites.add(evil_h) # Добавляем спрайт в группу all_sprites
    hands.add(evil_h)    # Добавляем спрайт в группу hands

def draw_health_bar(surf, x, y, filling, color):
    """Выводит полоску на поверхности.
    
    surf: Поверхность отображения полоски;
    x: Координата середины полоски по x;
    y: Координата верха блока текста по y;
    filling: Величина заливки полоски;
    clor: Цвет заливки;
    
    """
    if filling < 0:
        filling = 0
    BAR_LENGTH = WIDTH // 4
    BAR_HEIGHT = HEIGHT // 20
    fill = (filling / 100) * BAR_LENGTH
    x = x - (BAR_LENGTH // 2)
    y = y + (BAR_HEIGHT // 2)
    outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
    pg.draw.rect(surf, color, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)

def draw_lives(surf, x, y, lives, image):
    for i in range(lives):
        img_rect = image.get_rect()
        img_rect.x = x + 30 * i
        img_rect.y = y
        surf.blit(image, img_rect)
    
#####################################################################
# ОБЪЕКТЫ
#####################################################################
#====================================================================
# Объект игрока
#--------------------------------------------------------------------
class Cat(pg.sprite.Sprite):
    """Объект игрока. Выводит спрайт кота."""

    def __init__(self):
        pg.sprite.Sprite.__init__(self)  
        self.direction = 'move_down'
        self.image = img_cat_player[self.direction][1]
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2

        self.speed_x = 0
        self.speed_y = 0
        
        self.move_speed_x = 6
        self.move_speed_y = 6

        self.last_center = self.rect.center
        
        self.health = 100
        self.lives = 3
        self.hidden = False
        self.rebirth_time = 3000
        self.hidden_time = pg.time.get_ticks()
        
        self.shoot_delay = 200
        self.last_shot = pg.time.get_ticks()
        self.shoot_speed_x = 0
        self.shoot_speed_y = 0

        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = 60

    def hide(self):
        self.hidden = True
        self.hidden_time = pg.time.get_ticks()
        self.rect.x = WIDTH*2
        self.rect.y = HEIGHT*2
    
    def shoot(self):
        """Выводит спрайт снаряда."""
        now = pg.time.get_ticks()
        if self.direction == 'move_left':
            bullet = Bullet(self.rect.left - 10, self.rect.centery - 10, self.shoot_speed_x, self.shoot_speed_y)
        if self.direction == 'move_right':
            bullet = Bullet(self.rect.right + 10, self.rect.centery - 10, self.shoot_speed_x, self.shoot_speed_y)
        if self.direction == 'move_up':
            bullet = Bullet(self.rect.centerx, self.rect.top - 10, self.shoot_speed_x, self.shoot_speed_y)
        if self.direction == 'move_down':
            bullet = Bullet(self.rect.centerx, self.rect.bottom + 10, self.shoot_speed_x, self.shoot_speed_y)
                        
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            all_sprites.add(bullet)
            bullets.add(bullet)
            rnd.choice(snd_shoot).play()
    
    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pg.key.get_pressed()
        
        if self.hidden and pg.time.get_ticks() - self.hidden_time > self.rebirth_time:
            self.hidden = False
            self.health = 100
            self.rect.center = self.last_center
        
        def shoot_speed_calc(self):
            """Определяет направление полета снарядов."""
            if (keystate[pg.K_LEFT]):
                self.shoot_speed_x = -10
                self.shoot_speed_y = 0
                self.direction = 'move_left'
            elif keystate[pg.K_RIGHT]:
                self.shoot_speed_x = 10
                self.shoot_speed_y = 0
                self.direction = 'move_right'
            elif keystate[pg.K_UP]:
                self.shoot_speed_x = 0
                self.shoot_speed_y = -10
                self.direction = 'move_up'
            elif keystate[pg.K_DOWN]:
                self.shoot_speed_x = 0
                self.shoot_speed_y = 10
                self.direction = 'move_down'
            return self.shoot_speed_x, self.shoot_speed_y, self.direction
        shoot_speed_calc(self)
        
        def shoot_direction():
            """Вызывает функцию выстрела при нажатии клавиш стрельбы."""
            if ((keystate[pg.K_LEFT] or keystate[pg.K_RIGHT] or 
                keystate[pg.K_UP] or keystate[pg.K_DOWN]) and (not self.hidden)):
                    self.shoot()
        shoot_direction()
                
        def move(self):
            """Описывает движения объекта."""
            now = pg.time.get_ticks()
            
            def frame_updater():
                """Отрисовывает кадры изображения."""
                if (keystate[pg.K_LEFT] or keystate[pg.K_RIGHT] or 
                    keystate[pg.K_UP] or keystate[pg.K_DOWN]):
                        shoot_speed_calc(self)

                if now - self.last_update > self.frame_rate:
                    self.last_update = now
                    if self.frame == len(img_cat_player[self.direction]):
                        self.frame = 0
                    else:
                        center = self.rect.center
                        self.image = img_cat_player[self.direction][self.frame]
                        self.rect = self.image.get_rect()
                        self.rect.center = center
                        self.frame += 1

            # Движение по x
            if keystate[pg.K_a]:
                if keystate[pg.K_RIGHT]:
                    self.speed_x = -self.move_speed_x / 1.4
                    frame_updater()
                else:    
                    self.speed_x = -self.move_speed_x
                    self.direction = 'move_left'
                    frame_updater()
                    
            if keystate[pg.K_d]:
                if keystate[pg.K_LEFT]:
                    self.speed_x = self.move_speed_x / 1.4
                    frame_updater()
                else:    
                    self.speed_x = self.move_speed_x
                    self.direction = 'move_right'
                    frame_updater()
            self.rect.x += self.speed_x
            
            # Движение по y
            if keystate[pg.K_w]:
                if keystate[pg.K_DOWN]:
                    self.speed_y = -self.move_speed_y / 1.4
                    frame_updater()
                else:    
                    self.speed_y = -self.move_speed_y
                    self.direction = 'move_up'
                    frame_updater()
                    
            if keystate[pg.K_s]:
                if keystate[pg.K_UP]:
                    self.speed_y = self.move_speed_y / 1.4
                    frame_updater()
                else:    
                    self.speed_y = self.move_speed_y
                    self.direction = 'move_down'
                    frame_updater()
            self.rect.y += self.speed_y

            # Отображает изображение стойки при отсутствии нажатий;
            if ((keystate[pg.K_a] or keystate[pg.K_d] or 
                keystate[pg.K_w] or keystate[pg.K_s]) != True):
                    center = self.rect.center
                    self.image = img_cat_player[self.direction][1]
                    self.rect = self.image.get_rect()
                    self.rect.center = center
            
            def limit_coord(self):
                """Определяет ограничения по осям координат."""
                if self.rect.right > WIDTH:
                    self.rect.right = WIDTH
                if self.rect.left < 0:
                    self.rect.left = 0
                    
                if self.rect.bottom > HEIGHT - HEIGHT // 15:
                    self.rect.bottom = HEIGHT - HEIGHT // 15
                if self.rect.top < HEIGHT // 20:
                    self.rect.top = HEIGHT // 20
            if not self.hidden:  # Если не скрыт, то учитывать ограничения координат;
                limit_coord(self)
        move(self)
        
#====================================================================
# Объект противника
#--------------------------------------------------------------------
class EvilHand(pg.sprite.Sprite):
    """Объект противника. Выводит спрайт злых рук."""
    
    def evil_hand_pos(self):
        """Определяет начальную позицию и скорость злых рук."""
        self_rect_x = rnd.randrange(3*(-self.rect.width),
                                    WIDTH + 3*(self.rect.width))
        if self_rect_x > WIDTH // 2:
            self.rect.x = rnd.randrange(WIDTH + self.rect.width,
                                        WIDTH + 3*(self.rect.width))
        else:
            self.rect.x = rnd.randrange(3*(-self.rect.width),
                                        (-self.rect.width))
        self.rect.y = rnd.randrange(3*(-self.rect.height),
                                    HEIGHT + 3*(self.rect.height))
        
        self_speed_x = rnd.randrange(-8, 8)
        if self_speed_x > -1:
            self.speed_x = rnd.randrange(1, 8)
        if self_speed_x < 1:
            self.speed_x = rnd.randrange(-8, -1)

        self_speed_y = rnd.randrange(-8, 8)
        if self_speed_y > -1:
            self.speed_y = rnd.randrange(1, 8)
        if self_speed_y < 1:
            self.speed_y = rnd.randrange(-8, -1)
    
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image_orig = img_evil_hand
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        EvilHand.evil_hand_pos(self)
        
        self.rot = 0
        self.rot_speed = rnd.randrange(-10, 10)
        self.last_update = pg.time.get_ticks()
    
    def rotate(self):
        """Задает вращение."""
        now = pg.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now  
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pg.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center
        
    def update(self):
        self.rotate()
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.left > WIDTH + 3*self.rect.width:
            EvilHand.evil_hand_pos(self)
            
        if self.rect.right < 0 - 3*self.rect.width:
            EvilHand.evil_hand_pos(self)
            
        if self.rect.top > HEIGHT + 3*self.rect.height:
            EvilHand.evil_hand_pos(self)

        if self.rect.bottom < 0 - 3*self.rect.height:
            EvilHand.evil_hand_pos(self)

#====================================================================
# Объект кровавых взрывов
#--------------------------------------------------------------------
class BloodExplosion(pg.sprite.Sprite):
    """Объект кровавых взрывов. Выводит на экран кровавый взрыв.
    
    center: Центральная точка появления взрыва;
    size: Размер взрыва;
    frame_rate: Время до следующего кадра;
    anim_type: Тип загруженной анимации взрыва крови (от 1 до 5);
    
    """
    
    def __init__(self, center, size, frame_rate, anim_type):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.anim_type = anim_type
        self.image = img_blood_anim_1[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pg.time.get_ticks()
        self.frame_rate = frame_rate
        
    def update(self):
        def anim_choice(len_calc, frame):
            """Добавляет выбор анимации взрыва крови.
            
            len_calc: Выбирается при необходимости расчета числа кадров
                (True - считать кадры, False - не считать кадры);
            frame: Выбор кадра анимации;
            
            """
            if len_calc == False:    
                if self.anim_type == 1:
                    self.image = img_blood_anim_1[self.size][frame]
                elif self.anim_type == 2:
                    self.image = img_blood_anim_2[self.size][frame]
                elif self.anim_type == 3:
                    self.image = img_blood_anim_3[self.size][frame]
                elif self.anim_type == 4:
                    self.image = img_blood_anim_4[self.size][frame]
                elif self.anim_type == 5:
                    self.image = img_blood_anim_5[self.size][frame]
                else:
                    self.image = img_blood_anim_1[self.size][frame]
                return self.image
            elif len_calc == True:
                if self.anim_type == 1:
                    image = img_blood_anim_1[self.size]
                elif self.anim_type == 2:
                    image = img_blood_anim_2[self.size]
                elif self.anim_type == 3:
                    image = img_blood_anim_3[self.size]
                elif self.anim_type == 4:
                    image = img_blood_anim_4[self.size]
                elif self.anim_type == 5:
                    image = img_blood_anim_5[self.size]
                else:
                    image = img_blood_anim_1[self.size]
                return image
        
        now = pg.time.get_ticks()
        
        def frame_updater():
            """Отрисовывает кадры изображения."""
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                if self.frame == len(anim_choice(True, 0)):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = anim_choice(False, self.frame)
                    self.rect = self.image.get_rect()
                    self.rect.center = center
                    self.frame += 1
        frame_updater()
        
#====================================================================
# Объект выстрелов
#--------------------------------------------------------------------
class Bullet(pg.sprite.Sprite):
    """Объект снарядов. Выводит спрайт снарядов.
    
    x: Положение вывода снаряда по x;
    y: Положение вывода снаряда по y;
    shoot_speed_x: Скорость снаряда по x;
    shoot_speed_y: Скрость сняряда по y;
    
    """
    
    def __init__(self, x, y, shoot_speed_x, shoot_speed_y):
        pg.sprite.Sprite.__init__(self)
        self.image = rnd.choice(img_bullets)
        self.rect = self.image.get_rect()

        self.rect.centerx = x
        self.rect.centery = y

        self.speed_x = shoot_speed_x
        self.speed_y = shoot_speed_y
        
        self.radius = self.image.get_height() // 2 - int(self.image.get_height() * 0.05)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
                 
        # Удалить спрайт, если вышел за границу окна
        if self.rect.bottom < 0:
            self.kill()
        if self.rect.top > HEIGHT:
            self.kill()
        if self.rect.right < 0:
            self.kill()
        if self.rect.left > WIDTH:
            self.kill()

#====================================================================
# Создаем окно игры
#--------------------------------------------------------------------
pg.init()
#--------------------------------------------------------------------

#====================================================================
# Создание групп спрайтов
#--------------------------------------------------------------------
all_sprites = pg.sprite.Group()
hands        = pg.sprite.Group()
bullets     = pg.sprite.Group()
#--------------------------------------------------------------------

#====================================================================
# Добавление спрайтов в группы спрайтов
#--------------------------------------------------------------------
player_cat = Cat()
all_sprites.add(player_cat) # Добавляем спрайт в группу all_sprites

for i in range(rnd.randrange(10, 35)):
    add_hands()   # Добавить врагов
#--------------------------------------------------------------------

#====================================================================
# Подсчет очков
#--------------------------------------------------------------------
score = 0

#====================================================================
# Цикл игры
#--------------------------------------------------------------------
pg.mixer.music.play(loops=-1)   # Запуск музыки

running = True
while running:
    clock.tick(FPS) # Держим цикл на правильной скорости

    #----------------------------------------------------------------
    # Проверка событий
    #----------------------------------------------------------------
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    #----------------------------------------------------------------

    all_sprites.update()    # Обновление всех спрайтов
    
    #----------------------------------------------------------------
    # Проверка касания групп СНАРЯД - РУКИ
    #----------------------------------------------------------------
    hits_bullets_hands = pg.sprite.groupcollide(bullets, hands, True, True,
                                  pg.sprite.collide_rect_ratio(0.95))
    for hit in hits_bullets_hands:
        score += 1
        rnd.choice(snd_explosion).play()
        blood_explosion = BloodExplosion(hit.rect.center, 'medium', 20, rnd.randint(1, 5))
        all_sprites.add(blood_explosion)
        for i in range(rnd.randrange(1, 3)):
            add_hands()
    #----------------------------------------------------------------
    # Проверка касания спрайта ИГРОК с РУКИ
    #----------------------------------------------------------------
    if player_cat.alive():
        hits_player_hands = pg.sprite.spritecollide(player_cat, hands, True,
                                    pg.sprite.collide_rect_ratio(0.95))
        for hit in hits_player_hands:
            player_cat.health -= abs(hit.rot_speed) + abs(hit.speed_x) + abs(hit.speed_y)
            blood_explosion = BloodExplosion(hit.rect.center, 
                                             'small', 20, rnd.randint(1, 5))
            all_sprites.add(blood_explosion)
            for i in range(rnd.randrange(3, 5)):
                add_hands()
            if player_cat.health <= 0:
                player_cat.last_center = player_cat.rect.center
                player_cat.hide()
                player_cat.health = 0
                player_cat.lives -= 1
                player_death_explpsion = BloodExplosion(player_cat.last_center, 
                                                                'large', 100, rnd.randint(1, 5))
                all_sprites.add(player_death_explpsion)
    if player_cat.lives <= 0:
        running = False
    
    #----------------------------------------------------------------
    draw_ground()   # Закрасить фон
    
    all_sprites.draw(screen)    # Отрисовка всех спрайтов
    
    draw_text(screen, str('Уничтожено рук: %s' % score), 30, WIDTH // 2, HEIGHT // 90)
    draw_health_bar(screen, WIDTH // 2, HEIGHT - HEIGHT // 11, player_cat.health, RED)
    draw_text(screen, str('Здоровье: %s' % player_cat.health), 
              30, WIDTH // 2, HEIGHT - HEIGHT // 16)
    draw_lives(screen, WIDTH // 1.4, HEIGHT - HEIGHT // 19, player_cat.lives, img_cat_player_lives)
    
#--------------------------------------------------------------------
    pg.display.flip()   # После отрисовки всего, переворачиваем экран
#--------------------------------------------------------------------

pg.quit()
