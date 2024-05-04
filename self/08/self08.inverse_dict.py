def inverse_dict(my_dict):
    out = {value: [] for value in my_dict.values()}
    [out[value].append(key) for key, value in my_dict.items()]
    return out

def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))

if __name__ == '__main__':
    main()
