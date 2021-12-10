import openpyxl
import json
from collections import OrderedDict
import pprint
import time


# リストに格納するメソッド
def return_dict_name(cell_value):

    title = []
    folder = []
    courseTitle = []
    classroom = []
    teacher = []
    targetGrade = []
    semester = []
    weekdayPeriod = []
    courseClassification = []
    creditClassification = []
    creditTypeOtherInformation = []
    typeClass = []
    credits = []
    precautions = []
    additionalInformation = []
    contactAboutClass = []
    policyAndRelevance = []
    aimLecture = []
    forStudents = []
    courseGoals = []
    courseSchedule = []
    theme1 = []
    homework1 = []
    theme2 = []
    homework2 = []
    theme3 = []
    homework3 = []
    theme4 = []
    homework4 = []
    theme5 = []
    homework5 = []
    theme6 = []
    homework6 = []
    theme7 = []
    homework7 = []
    theme8 = []
    homework8 = []
    theme9 = []
    homework9 = []
    theme10 = []
    homework10 = []
    theme11 = []
    homework11 = []
    theme12 = []
    homework12 = []
    theme13 = []
    homework13 = []
    theme14 = []
    homework14 = []
    theme15 = []
    homework15 = []
    theme16 = []
    homework16 = []
    theme17 = []
    homework17 = []
    theme18 = []
    homework18 = []
    theme19 = []
    homework19 = []
    theme20 = []
    homework20 = []
    theme21 = []
    homework21 = []
    theme22 = []
    homework22 = []
    theme23 = []
    homework23 = []
    theme24 = []
    homework24 = []
    theme25 = []
    homework25 = []
    theme26 = []
    homework26 = []
    theme27 = []
    homework27 = []
    theme28 = []
    homework28 = []
    theme29 = []
    homework29 = []
    theme30 = []
    homework30 = []
    theme31 = []
    homework31 = []
    references = []
    meansOfLearning = []
    evaluation = []
    relatedSubjects = []

    if cell_value == 'title':
        title.append(cell_value)
    elif cell_value == 'folder':
        folder.append(cell_value)
    elif cell_value == 'teacher':
        teacher.append(cell_value)
    elif cell_value == 'grade':
        year_of_eligible_students.append(cell_value)
    elif cell_value == 'semester':
        semester.append(cell_value)


def generation_dict(key):
    f = open('./input/dict_name.txt', 'r')
    dict_name = f.readlines()
    f.close()
    return dict_name[key].rstrip('\n')



def convert_json(excel_path='syllabus.xlsx'):
    excel_path = './input/' + excel_path
    workbook = openpyxl.load_workbook(filename=excel_path, read_only=False)
    # シートのロード
    sheet = workbook['Sheet1']
    f = open('log.txt', 'a')

    for row in sheet.iter_cols():
        for cell in row:
            # print("行:" + str(cell.row), "列:" + str(cell.column))
            # print(cell.value)
            # f.write("行:" + str(cell.row) + "列:" + str(cell.column) + " " + str(cell.value) + '\n')
            if cell.row >= 2:
                f.write("行:" + str(cell.row) + "列:" + str(cell.column) + " " + str(cell.value) + '\n')
                """
                if sheet.cell(row=1, column=cell.column).value == 'subject':
                    print(cell.value)
                """
                print(generation_dict(int(cell.column) - 1))

    f.close()
# convert_json()


# print(generation_dict(0))
convert_json()
