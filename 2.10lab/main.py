if __name__ == "__main__":
    pass
class HeightError(Exception): pass
class WeightError(Exception): pass
class TemperatureError(Exception): pass

try:
    height = float(input("Введите рост (см): "))
    if not 0 <= height <= 300:
        raise HeightError("Некорректный рост")
    print("Рост введен корректно")
except HeightError as e:
    print(e)

try:
    weight = float(input("Введите вес (кг): "))
    if not 0 <= weight <= 500:
        raise WeightError("Некорректный вес")
    print("Вес введен корректно")
except WeightError as e:
    print(e)

try:
    temp = float(input("Введите температуру (°C): "))
    if temp < -273.15:
        raise TemperatureError("Некорректная температура")
    print("Температура введена корректно")
except TemperatureError as e:
    print(e)
