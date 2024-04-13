import os
import json

with open("ru_en.json", "r") as f:
    data = json.load(f)

playlists = ['favorite', 'kishlak_afps', 'best_ru_rock', 'old']
print(playlists)
for cur in playlists:
    if '.' not in cur:
        path = cur
        authors = os.listdir(path)
        tracks = []
        for author in authors:
            path1 = '/'.join([path, author])
            albums = os.listdir(path1)
            for album in albums:
                path2 = '/'.join([path1, album])
                track_list = os.listdir(path2)
                for track in track_list:
                    path3 = '/'.join([path2, track])
                    if (path3 in data.keys()):
                        os.rename(path3, data[path3])
                        path3 = data[path3]
                if (path2 in data.keys()):
                    os.rename(path2, data[path2])
                    path2 = data[path2]
            if (path1 in data.keys()):
                os.rename(path1, data[path1])
                path1 = data[path1]
        if (path in data.keys()):
            os.rename(path, data[path])
            path = data[path]