def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in',
             'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translation = (words[word] for word in sentence.split())
    for word in translation:
        print(word, end=' ')


def main():
    translate('el gato esta en la casa')


if __name__ == '__main__':
    main()
