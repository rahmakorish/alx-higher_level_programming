#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    result = 0
    try:
        for i in range(0, list_length):
            result = my_list_1[i] / my_list_2[i]
            new.append(result)
    except ZeroDivisionError:
        result = 0
        new.append(result)
        print("division by 0")
    except ValueError:
        print("wrong type")
        result = 0
        new.append(result)
    except IndexError:
        print("out of range")
        result = 0
        new.append(result)
    finally:
        return new
