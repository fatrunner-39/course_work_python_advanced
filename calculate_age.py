from datetime import date



def calculate_age(born):
    today = date.today()
    return today.year - int(born[2]) - ((today.month, today.day) < (int(born[1]), int(born[0])))


if __name__ == '__main__':
    print(calculate_age(['6', '2', '1991']))
