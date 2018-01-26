# coding=utf-8
# 生产者将任务分批发送，降低CPU负载
import math
import time


if __name__ == "__main__":

    # task list
    elements = range(1, 998)
    #
    section_count = 100
    total_time = 10  # second
    print("len:", len(elements))

    elements_each_section = len(elements) / (section_count * 1.0)
    elements_each_section = int(math.ceil(elements_each_section))
    time_each_section = total_time / (section_count * 1.0)

    print("elements_each_section:", elements_each_section)
    print("section_count:", elements_each_section)
    print("time_each_section:", time_each_section)

    start_time = time.time()
    for i in range(section_count):
        start_index = i * elements_each_section
        n = i + 1
        end_index = n * elements_each_section
        print(start_index, end_index)
        print(elements[start_index: end_index])

        #############
        # TODO
        # YourTaskToConsumeCPU()
        #############

        # time compensation
        now = time.time()
        if now - start_time < n * time_each_section:
            duration = n * time_each_section - (now - start_time)
            print("sleep:", duration)
            time.sleep(duration)

    end_time = time.time()
    print(end_time - start_time)




