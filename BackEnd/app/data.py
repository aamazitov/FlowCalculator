from flask import jsonify
from app.helper import get_min_index_from_list


class Data:
    def __init__(self):
        self.__time = []
        self.__P = []
        self.__r = []
        self.__T = []

    def get_radius(self):
        return self.__r

    def get_time(self):
        return self.__time

    def init_radius(self, r):
        for i in range(len(r)):
            self.__r.append(r[i])

    def append_time(self, time):
        if time in self.__time:
            return

        self.__time.append(time)

    def append_pressure(self, pressure):
        pres = []
        for i in range(len(pressure)):
            pres.append(pressure[i])
        self.__P.append(pres)

    def append_temperature(self, temperature):
        temp = []
        for i in range(len(temperature)):
            temp.append(temperature[i])
        self.__T.append(temp)

    def print_pressure(self):
        for i in range(len(self.__time)):
            print(self.__time[i], " ", self.__P[i])

    def get_der_p_r(self, time, i, h):
        ind = self.__time.index(time)
        return (self.__P[ind][i - 1] - self.__P[ind][i - 2]) / h

    def get_der_p_t(self, time, i, tau):
        ind = self.__time.index(time)
        return (self.__P[ind][i - 1] - self.__P[ind - 1][i - 1]) / tau

    def get_pressure_by_time(self, time: float = None):
        ind = get_min_index_from_list(src_list=self.__time, src_value=time)

        pres = []

        for i in range(len(self.__P[ind])):
            pres.append(self.__P[ind][i])

        return pres

    def get_temperature_by_time(self, time: float = None):
        ind = get_min_index_from_list(src_list=self.__time, src_value=time)

        temp = []

        for i in range(len(self.__T[ind])):
            temp.append(self.__T[ind][i])

        return temp

    def get_pressure_by_radius(self, radius: float = None):
        ind = get_min_index_from_list(src_list=self.__r, src_value=radius)

        pres = []

        for i in range(len(self.__P)):
            pres.append(self.__P[i][ind])

        return pres

    def get_temperature_by_radius(self, radius: float = None):
        ind = get_min_index_from_list(src_list=self.__r, src_value=radius)

        temp = []

        for i in range(len(self.__T)):
            temp.append(self.__T[i][ind])

        return temp

    def save_to_files_by_time(self, time, file_radius_name: str = "", file_pressure_name: str = "",
                              file_temperature_name: str = ""):
        ind = 0

        diff = 1000000000000000000

        for i in range(len(self.__time)):
            if diff > abs(self.__time[i] - time):
                diff = abs(self.__time[i] - time)
                ind = i

        file1 = open("radius.txt" if file_radius_name == "" else file_radius_name, "w")
        file2 = open("pressure.txt" if file_pressure_name == "" else file_pressure_name, "w")
        file3 = open("temperature.txt" if file_temperature_name == "" else file_temperature_name, "w")

        for i in range(len(self.__r)):
            file1.write(str(self.__r[i]).replace(".", ",") + "\n")

        for i in range(len(self.__P[ind])):
            file2.write(str(self.__P[ind][i]).replace(".", ",") + "\n")

        for i in range(len(self.__T[ind])):
            file3.write(str(self.__T[ind][i]).replace(".", ",") + "\n")

        file1.close()
        file2.close()
        file3.close()

    def save_to_files_by_radius(self, radius, file_time_name: str = "", file_pressure_name: str = "",
                                file_temperature_name: str = ""):
        ind = 0

        diff = 1000000000000000000

        for i in range(len(self.__r)):
            if diff > abs(self.__r[i] - radius):
                diff = abs(self.__r[i] - radius)
                ind = i

        file1 = open("time.txt" if file_time_name == "" else file_time_name, "w")
        file2 = open("pressure.txt" if file_pressure_name == "" else file_pressure_name, "w")
        file3 = open("temperature.txt" if file_temperature_name == "" else file_temperature_name, "w")

        for i in range(len(self.__time)):
            file1.write(str(self.__time[i]).replace(".", ",") + "\n")

        for i in range(len(self.__P)):
            file2.write(str(self.__P[i][ind]).replace(".", ",") + "\n")

        for i in range(len(self.__T)):
            file3.write(str(self.__T[i][ind]).replace(".", ",") + "\n")

        file1.close()
        file2.close()
        file3.close()
