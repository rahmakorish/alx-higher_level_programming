#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for item in range(0, len(dir(hidden_4))):
        if dir(hidden_4)[item].startswith('_'):
            pass
        else:
            print(dir(hidden_4)[item])
