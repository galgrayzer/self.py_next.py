def stop_iteration():
    raise StopIteration


def zero_division_error():
    raise ZeroDivisionError


def assertion_error():
    raise AssertionError


def import_error():
    raise ImportError


def key_error():
    raise KeyError


def syntax_error():
    raise SyntaxError


def identation_error():
    raise IndentationError


def type_error():
    raise TypeError


def main():
    try:
        stop_iteration()
    except StopIteration as e:
        print(f'StopIteration: {e}')

    try:
        zero_division_error()
    except ZeroDivisionError as e:
        print(f'ZeroDivisionError: {e}')

    try:
        assertion_error()
    except AssertionError as e:
        print(f'AssertionError: {e}')

    try:
        import_error()
    except ImportError as e:
        print(f'ImportError: {e}')

    try:
        key_error()
    except KeyError as e:
        print(f'KeyError: {e}')

    try:
        syntax_error()
    except SyntaxError as e:
        print(f'SyntaxError: {e}')

    try:
        identation_error()
    except IndentationError as e:
        print(f'IndentationError: {e}')

    try:
        type_error()
    except TypeError as e:
        print(f'TypeError: {e}')


if __name__ == '__main__':
    main()
