import multiprocessing
import threading
import time



def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())


filenames = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

if __name__ == '__main__':

    print('"Многопроцессное считывание"')
    print('----------------------------')


    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f'Время выполнения: {linear_duration} секунд (линейный)')


    threads = []
    start_time = time.time()
    for filename in filenames:
        thread = threading.Thread(target=read_info, args=(filename,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    multi_thread_duration = time.time() - start_time
    print(f'Время выполнения: {multi_thread_duration} секунд (многопоточный)')



    start_time = time.time()
    processes = []
    for filename in filenames:
        process = multiprocessing.Process(target=read_info, args=(filename,))
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    multi_process_duration = time.time() - start_time
    print(f'Время выполнения: {multi_process_duration} секунд (многопроцессный)')


