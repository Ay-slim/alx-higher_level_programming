#!/usr/bin/python3
import hidden_4


def print_hidden_names():
    hidden_names = dir(hidden_4)
    for i in range(0, len(hidden_names)):
        if hidden_names[i][0] == '_' and hidden_names[i][1] == '_':
            continue
        print(hidden_names[i])


if __name__ == "__main__":
    print_hidden_names()
