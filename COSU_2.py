import pygame #Импартирование библиотеки Pygame
import random #Импортирование библиотеки random для случайных чисел
import os #Импортирование библиотеки os для работы с файловой системой

pygame.init() #Инициализация Pygame

music_file = "Secret.mp3"

if os.path.isfile(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(-1)
    print("Музыка найдена и играет.")
else:
    print("Файл музыки не найден. Играем без музыки.")

run = True #Это просто переменная для управления циклом игры
take = 0 #Счётчик столкновений
#Экраны и цвета
width, height = 800, 600 #Размер экрана
screen = pygame.display.set_mode((width, height))  # Экран
BLACK = (0, 0, 0) #Чёрный
WHITE = (255, 255, 255) #Белый
RED = (255, 0, 0) #Красный
BLUE = (0, 255, 255) #Синий
tick = pygame.time.Clock() #Это просто объект для управления частотой кадров 

#Рандомные позиции для игрока и препятствия
obs_pos_x = random.randint(0, width-50) #Рандомная позиция по X для препятствия
obs_pos_y = random.randint(0, height-50) #Рандомная позиция по Y для препятствия
random_pos_x = random.randint(0, width-50) #Рандомная позиция по X, чтобы игрок не выходил за границы экрана
random_pos_y = random.randint(0, height-50) #Рандомная позиция по Y, чтобы игрок не выходил за границы экрана


#Игрок
player_width, player_height = 30, 30 #Ширина и высота игрока
player = pygame.Rect(random_pos_x, random_pos_y, player_width, player_height) #Прямоугольник игрока (x, y, ширина, высота)
block_width, block_height = 20, 20 #Ширина и высота блока
block = pygame.Rect(height - block_height, width - block_width, block_width, block_height) #Прямоугольник блока (x, y, ширина, высота)
BOSS_width, BOSS_height = 50, 50 #Ширина и высота босса
BOSS_random_pos_x = random.randint(0, width - BOSS_width) #Рандомная позиция по X для босса
BOSS_random_pos_y = random.randint(0, height - BOSS_height) #Рандомная позиция по Y для босса
BOSS = pygame.Rect(BOSS_random_pos_x, BOSS_random_pos_y, BOSS_width, BOSS_height) #Прямоугольник босса (x, y, ширина, высота)

space_pressed = False  # флаг для отслеживания одиночного нажатия

while run: #Цикл игры
    screen.fill(WHITE) #Пакраска экрана белым цветом
    pygame.draw.rect(screen, BLACK, player)
    pygame.draw.rect(screen, RED, block) #Отрисовка блока

    mouse_x, mouse_y = pygame.mouse.get_pos() #Получение позиции мыши
    block = pygame.Rect(mouse_x -7, mouse_y -5, block_width, block_height) #Создание прямоугольника куба по позиции мыши
    block.clamp_ip(screen.get_rect()) #Ограничение блока в пределах

    if block.colliderect(player): #Проверка на столкновение между игроком и блоком
        # Если столкновение произошло, перемещаем игрока в случайную позицию
        obs_pos_x = random.randint(0, width - player_width)
        obs_pos_y = random.randint(0, height - player_height)
        player = pygame.Rect(obs_pos_x, obs_pos_y, player_width, player_height)

        take += 1 #Увеличение счётчика столкновений
        print(f"Было столкновений: {take} раз(а)")

        # Обновление заголовка окна с количеством столкновений
        pygame.display.set_caption(f"Было столкновений: {take} раз(а)")
        
        
    for event in pygame.event.get(): #Проверка событий
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): #Проверка клавишь
            print(f"Сколько вообщем было столкновений: {take} раз(а)")
            run = False  
    if take >= 50: #Проверка на количество столкновений  
        pygame.draw.rect(screen, BLUE, BOSS) #Отрисовка босса   
        if block.x < BOSS.x:
            BOSS.x = BOSS.x - 3
        if block.x > BOSS.x:
            BOSS.x = BOSS.x + 3
        if block.y < BOSS.y:
            BOSS.y = BOSS.y - 3
        if block.y > BOSS.y:
            BOSS.y = BOSS.y + 3
        if block.colliderect(BOSS):
            print(f"Вы дотронулись до босса!\n"f"Сколько вообщем было столкновений: {take} раз(а)")
            run = False
    
    pygame.display.update() #Обновление экрана
    tick.tick(60) #ФПС (60 кадров в секунду)
pygame.quit() # Выход
