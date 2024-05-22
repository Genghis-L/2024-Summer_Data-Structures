# Copyright 2024 Genghis, 骆可瀚(Luo Kehan), kl4747@nyu.edu

class Car:
    """Car Class"""

    def __init__(self, year_model, make, speed) -> None:
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed


def main():
    car_1 = Car("2004", "Toyota", 100)
    for _ in range(5):
        car_1.accelerate()
        print(f"Current Speed: {car_1.get_speed()} km/h")

    for _ in range(5):
        car_1.brake()
        print(f"Current Speed: {car_1.get_speed()} km/h")


if __name__ == "__main__":
    main()
