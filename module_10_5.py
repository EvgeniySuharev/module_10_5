import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='cp1251') as file:
        all_data += file.readlines()


if __name__ == '__main__':
    file_list = []
    for i in range(1, 5):
        file_list.append(f'file {i}.txt')

    start = time.time()
    for file in file_list:
        read_info(file)
    stop = time.time()
    print(f'{round(stop - start, 3)} сек. - линейный')

    with multiprocessing.Pool(processes=4) as pool:
        start = time.time()
        pool.map(read_info, file_list)
    stop = time.time()
    print(f'{round(stop - start, 3)} сек. - мультипроцессный')
