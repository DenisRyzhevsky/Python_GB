# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный)
# — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение
# и завершать скрипт.

from time import sleep
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self.__color = (('red', 7), ('yellow', 2), ('green', 5))

    def running (self):
        for color, time in cycle(self.__color):
            print(color)
            sleep(time)

TrafficLight = TrafficLight()
TrafficLight.running()
