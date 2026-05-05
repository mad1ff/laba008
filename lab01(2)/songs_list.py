violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

time1 = 0
for song in violator_songs_list:
    if song[0] in ['Halo', 'Enjoy the Silence', 'Clean']:
        time1 += song[1]

time_total= round(time1, 2)



violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}


time2 = 0

for song2 in ['Sweetest Perfection', 'Policy of Truth', 'Blue Dress']:
    if song2 in violator_songs_dict:
        time2 += violator_songs_dict[song2]

total_time2 = int(time2)



def pesnia():
    print(f"Три песни звучат {time_total} минут")
    print(f"А другие три песни звучат {total_time2} минут")
