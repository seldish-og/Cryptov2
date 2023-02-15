# ищем 3 делителя кроме 1, 0, и самого number
def task(number: int):
    count = 0
    for i in range(2, number // 2):
        if number % i == 0:
            print(i)
            count += 1
            if count >= 3:
                return True
    if count < 3:
        return False


# print(task(5))/
# print(task(10))
# print(task(15002300))
