import os
import threading
import time

playlist = {}
playlist['favorite'] = "https://music.yandex.ru/users/veczez/playlists/3"
playlist['kishlak_afps'] = "https://music.yandex.ru/users/veczez/playlists/1009"
playlist['best_ru_rock'] = "https://music.yandex.ru/users/veczez/playlists/1008"
playlist['old'] = "https://music.yandex.ru/users/veczez/playlists/1000"

def main(argu:int):
    pattern = 'yandex-music-downloader --browser "firefox" --hq --url {} --skip-existing --embed-cover --path-pattern "#album-artist/#album/#title" --dir "{}"'
    i = [*playlist.keys()]
    i = i[argu]
    os.system(pattern.format(playlist[i], i))


threads = []
for i in range(len(playlist)):
    threads.append(threading.Thread(target=main, args= [i]))
    threads[-1].start()
print(f"{len(playlist)} threads started work")