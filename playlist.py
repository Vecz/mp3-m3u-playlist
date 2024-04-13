import os
playlists = ['favorite', 'kishlak_afps', 'best_ru_rock', 'old']
print(playlists)
for cur in playlists:
    if '.' not in cur:
        path = cur
        authors = os.listdir(path)
        tracks = []
        for author in authors:
            if '.' not in author:
                path1 = '/'.join([path, author])
                albums = os.listdir(path1)
                for album in albums:
                    path2 = '/'.join([path1, album])
                    track_list = os.listdir(path2)
                    for track in track_list:
                        temp = '/'.join([path2, track])
                        temp = temp.replace('/', '\\')
                        tracks.append(temp)
        filename = cur + ".m3u"
        f = open(filename, "w")
        f.write("#EXTM3U\r\n")
        for i in tracks:
            f.write(i +'\r\n')
        f.close()