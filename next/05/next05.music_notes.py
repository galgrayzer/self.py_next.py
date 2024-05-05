class MusicNotes:
    def __init__(self):
        self.start = 0
        self.notes = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]

    def __iter__(self):
        while True:
            if self.start == len(self.notes):
                self.notes = list(map(lambda x: x * 2, self.notes))
                self.start = 0
            if self.notes[self.start] > 1600:
                break
            yield self.notes[self.start]
            self.start += 1


def main():
    music = iter(MusicNotes())
    for freq in music:
        print(freq)


if __name__ == '__main__':
    main()
