def my_mp4_playlist(file_path, new_song):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    if len(lines) < 3:
        lines += ["\n"] * (3 - len(lines))
    lines[2] = new_song + "\n"
    with open(file_path, 'w') as file:
        file.writelines(lines)
    with open(file_path, 'r') as file:
        print(file.read())


def main():
    file_path = "self/09/utils/songs.txt"
    new_song = "New song;New artist;3:00;"
    my_mp4_playlist(file_path, new_song)


if __name__ == '__main__':
    main()
