import xlwt
import os
import random


# 既知の条件
Raw_Data_Time = [0, 2, 4, 5, 7, 9, 11]  # 時点
Raw_Data_Displacement = [0, 5, 5, 0, -10, -10, 0]   # 変位
Safe_Maximum_Acceleration = 6   # 安全な最大加速度


def output_excel():
    excel = xlwt.Workbook(encoding='utf-8')
    sheet1 = excel.add_sheet('Sheet1')
    k = 0
    while True:
        sheet1.write(k, 0, Output_Data_Time[k])
        sheet1.write(k, 1, Output_Data_Displacement[k])
        k += 1
        if k == len(Output_Data_Time):
            break
    excel.save(save_path + '/data.xls')


def calculate(start_time, end_time, start_displacement, end_displacement):
    while True:
        time_ = (end_time - start_time) / 2
        displacement_split_point = random.uniform(start_displacement, end_displacement)
        displacement_part_1 = displacement_split_point - start_displacement
        displacement_part_2 = end_displacement - displacement_split_point
        speed_1 = displacement_part_1 / time_
        speed_2 = displacement_part_2 / time_
        acceleration = (speed_2 - speed_1) / time_
        if acceleration < Safe_Maximum_Acceleration:
            break
    return displacement_split_point


def del_list(num):
    if num == 1:
        length_ = len(Temporary_Data_Time)
        while True:
            if length_ == 0:
                break
            del Temporary_Data_Time[length_ - 1]
            length_ -= 1
            if length_ == 0:
                break
    elif num == 2:
        length_ = len(Temporary_Data_Displacement)
        while True:
            if length_ == 0:
                break
            del Temporary_Data_Displacement[length_ - 1]
            length_ -= 1
            if length_ == 0:
                break
    elif num == 3:
        length_ = len(Output_Data_Time)
        while True:
            if length_ == 0:
                break
            del Output_Data_Time[length_ - 1]
            length_ -= 1
            if length_ == 0:
                break
    elif num == 4:
        length_ = len(Output_Data_Displacement)
        while True:
            if length_ == 0:
                break
            del Output_Data_Displacement[length_ - 1]
            length_ -= 1
            if length_ == 0:
                break


def list_append(num):
    if num == 1:
        a = 0
        length_ = len(Output_Data_Time)
        while True:
            Temporary_Data_Time.append(Output_Data_Time[a])
            a += 1
            if a == length_:
                break
    elif num == 2:
        a = 0
        length_ = len(Temporary_Data_Time)
        while True:
            Output_Data_Time.append(Temporary_Data_Time[a])
            a += 1
            if a == length_:
                break
    elif num == 3:
        a = 0
        length_ = len(Output_Data_Displacement)
        while True:
            Temporary_Data_Displacement.append(Output_Data_Displacement[a])
            a += 1
            if a == length_:
                break
    elif num == 4:
        a = 0
        length_ = len(Temporary_Data_Displacement)
        while True:
            Output_Data_Displacement.append(Temporary_Data_Displacement[a])
            a += 1
            if a == length_:
                break


Temporary_Data_Time = []
Temporary_Data_Displacement = []
Output_Data_Time = []
Output_Data_Displacement = []
save_path = os.getcwd()
# output_excel()
print("時点:" + str(Raw_Data_Time))
print("変位:" + str(Raw_Data_Displacement))
print("安全な最大加速度:" + str(Safe_Maximum_Acceleration))
length = len(Raw_Data_Time)
i = 0
while True:
    Output_Data_Time.append(Raw_Data_Time[i])
    i += 1
    if i == length:
        break
length = len(Raw_Data_Displacement)
i = 0
while True:
    Output_Data_Displacement.append(Raw_Data_Displacement[i])
    i += 1
    if i == length:
        break

while True:
    del_list(2)
    j = 0
    _length = len(Output_Data_Displacement)
    while True:
        Temporary_Data_Displacement.append(Output_Data_Displacement[j])
        Temporary_Data_Displacement.append(calculate(Output_Data_Time[j], Output_Data_Time[j + 1], Output_Data_Displacement[j], Output_Data_Displacement[j + 1]))
        j += 1
        if j == _length - 1:
            break
    Temporary_Data_Displacement.append(Output_Data_Displacement[_length - 1])
    del_list(4)
    list_append(4)
    del_list(1)
    j = 0
    _length = len(Output_Data_Time)
    while True:
        Temporary_Data_Time.append(Output_Data_Time[j])
        Temporary_Data_Time.append(Output_Data_Time[j]+(Output_Data_Time[j + 1] - Output_Data_Time[j]) / 2)
        j += 1
        if j == _length - 1:
            break
    Temporary_Data_Time.append(Output_Data_Time[_length - 1])
    del_list(3)
    list_append(2)
    _length_ = len(Output_Data_Time)
    if _length_ > 11000:
        break
print(str(Temporary_Data_Time))
print(str(Output_Data_Time))
print(str(Temporary_Data_Displacement))
print(str(Output_Data_Displacement))
output_excel()