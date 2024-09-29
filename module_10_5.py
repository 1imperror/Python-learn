from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


start = datetime.now()
for i in range(1, 5):
    name = f'./file {i}.txt'
    read_info(name)
end = datetime.now()
print(end - start)  # | 0:00:02.668714


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        all_images = []
        for i in range(1, 5):
            all_images.append(f'./file {i}.txt')
        start = datetime.now()
        pool.map(read_info, all_images)
    end = datetime.now()
    print(end - start)  # | 0:00:01.167148
