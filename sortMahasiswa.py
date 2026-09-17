import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    
    # Kerjakan disini
    column = maps[index]
    for current_index in range(len(data) -1):
        selected_index = current_index
        for next_index in range(current_index + 1, len(data)):
            selected_value = data[selected_index] [column]
            next_value = data[next_index] [column]

            if (not rev and next_value < selected_value) or (rev and next_value > selected_value):
                selected_index = next_index

        data[current_index], data[selected_index] = (
            data[selected_index], data[current_index]
        )
    # Jangan Dihapus
    show_data(data)

sort_by(data)


    
