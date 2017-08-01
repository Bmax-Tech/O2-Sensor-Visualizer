import matplotlib.pyplot as plt

sensor_data_set_x_1 = []
sensor_data_set_y_1 = []

with open('dataset\\O2sensor.txt') as file:
    for line in file:
        inner_list = [elt.strip() for elt in line.split('\t')]
        sensor_data_set_x_1.append(inner_list[0])
        sensor_data_set_y_1.append(inner_list[1])
    print(sensor_data_set_y_1)

    plt.plot(sensor_data_set_x_1, sensor_data_set_y_1, linewidth=1.0)
    plt.show()
