import os
from transliterate import translit
import json

renamed = []
original = []
playlists = ['favorite', 'kishlak_afps', 'best_ru_rock', 'old']
print(playlists)
for cur in playlists:
    if '.' not in cur:
        path = cur
        if (len(path.encode("ascii", "ignore")) < len(path)):
            original.append(path)
            os.rename(path, translit(path, reversed=True))
            path = translit(path, reversed=True)
            renamed.append(path)
        authors = os.listdir(path)
        tracks = []
        for author in authors:
            path1 = '/'.join([path, author])
            if (len(path1.encode("ascii", "ignore")) < len(path1)):
                original.append(path1)
                os.rename(path1, translit(path1, reversed=True))
                path1 = translit(path1, reversed=True)
                renamed.append(path1)
            albums = os.listdir(path1)
            for album in albums:
                path2 = '/'.join([path1, album])
                if (len(path2.encode("ascii", "ignore")) < len(path2)):
                    original.append(path2)
                    os.rename(path2, translit(path2, reversed=True))
                    path2 = translit(path2, reversed=True)
                    renamed.append(path2)
                track_list = os.listdir(path2)
                for track in track_list:
                    path3 = '/'.join([path2, track])
                    if (len(path3.encode("ascii", "ignore")) < len(path3)):
                        original.append(path3)
                        os.rename(path3, translit(path3, reversed=True))
                        path3 = translit(path3, reversed=True)
                        renamed.append(path3)
result = {}
for i in range(len(original)):
    result[renamed[i]] = original[i]
with open("ru_en.json", "w") as f:
    json.dump(result, f)