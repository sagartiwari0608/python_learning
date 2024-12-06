from nested_data import albums

album_name = 0
songs_in_album = 3
year= 2
artist = 1


while True:
    print("Please choose your album ( invalid choice exits):")
    for index, (title,artist,year,songs) in enumerate(albums):
        print("{}:{}, {}, {}".format(index+1, title,artist,year, songs))
    
    choice = int(input())
    if 1<=choice<=len(albums):
        songs_list = albums[choice - 1][3] #to display list of all songs
        # print(songs_list)
        print("your current chosen album is now playing.........")
        for index, (song_number,song_name) in enumerate(songs_list):
            print("{}: {}".format(song_number,song_name))
    else:
        break
