"""
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police(булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
"""


class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} started moving'.format(self.name))

    def stop(self):
        print('{} is stopped'.format(self.name))

    def turn(self, direction):
        print('{} is turning to {}'.format(self.name, direction))

    def show_speed(self):
        print('speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Slow down!')
        super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Slow down!')
        super().show_speed()


class PoliceCar(Car):
    def show_speed(self):
        super().show_speed()


sportcar = SportCar(240, 'red', 'BMW', False)
policecar = PoliceCar(62, 'blue', 'lada', True)
workcar = WorkCar(45, 'white', 'mercedes', False)
towncar = TownCar(65, 'yellow', 'audi', False)
sportcar.show_speed()
policecar.go()
towncar.stop()
workcar.turn('right')

