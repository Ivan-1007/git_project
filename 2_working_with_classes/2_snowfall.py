import simple_draw as sd

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    fallen_flakes = 0

    def __init__(self, color=sd.COLOR_WHITE):
        self.x = sd.randint(40, sd.resolution[0] - 40)
        self.y = 610
        self.len = sd.randint(15, 35)
        self.start_rays = sd.randint(5, 10) / 10
        self.len_rays = sd.randint(5, 10) / 10
        self.angle_rays = sd.randint(30, 160)
        self.color = color

    def move(self):
        step_x = sd.randint(-15, 15)
        self.x = self.x + step_x
        self.y = self.y - sd.randint(5, 20)

    def draw(self, color='default'):
        if color == 'default':
            color = self.color
        start_point = sd.get_point(self.x, self.y)
        sd.snowflake(center=start_point, length=self.len, color=color, factor_a=self.start_rays,
                     factor_b=self.len_rays, factor_c=self.angle_rays)

    def clear_previous_picture(self):
        self.draw(color=sd.background_color)

    def can_fall(self):
        return self.y > -15

    def create_new_center(self):
        self.x = sd.randint(40, 560)
        self.y = 610


flake = Snowflake(color=sd.COLOR_CYAN)

print(flake.color)

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        flake.clear_previous_picture()
        flake.create_new_center()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
