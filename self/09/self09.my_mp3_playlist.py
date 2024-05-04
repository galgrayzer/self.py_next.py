from functools import reduce


def my_mp3_playlist(file_path):
    longest_song = ""
    longest_song_length = 0
    num_of_songs = 0
    artist_dict = {}
    with open(file_path, 'r') as file:
        for line in file.readlines():
            song, artist, length, garbage = line.split(";")
            num_of_songs += 1
            if float(length.replace(":", ".")) > longest_song_length:
                longest_song = song
                longest_song_length = float(length.replace(":", "."))
            artist_dict[artist] = artist_dict.get(artist, 0) + 1
    artist_with_most_songs = reduce(
        lambda x, y: x if artist_dict[x] > artist_dict[y] else y, artist_dict.keys())
    return (longest_song, num_of_songs, artist_with_most_songs)


def main():
    file_path = "self/09/utils/songs.txt"
    print(my_mp3_playlist(file_path))


if __name__ == '__main__':
    main()
