#-*- coding: utf-8 -*-

def avarage_temps(temps):
    sum_of_temps = 0

    for t in temps:
        sum_of_temps += float(t)

    return sum_of_temps / len(temps)



if __name__ == "__main__":

    temps = [21, 24, 24, 22, 20, 23, 24]

    average = avarage_temps(temps)

    print('La temperatura promedio es: {}'.format(average))