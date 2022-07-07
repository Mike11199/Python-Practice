import math


def distance(one_x, one_y, two_x, two_y):
    # distance = sqrt{  (x2 - x1)^2 + (y2 - y1)^2  }
    distance_val = math.sqrt((two_x-one_x)**2+(two_y-one_y)**2)
    return distance_val


def main():
    distance1 = distance(3, 5, -1, 2)
    distance2 = distance(0, 0, 0, 0)
    print(distance1, distance2)


if __name__ == '__main__':
    main()

