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
    if key <= 20 or key >= 83:
        return dict_name[key].rstrip('\n')
    elif key % 2 != 0:
        return "theme"
    elif key % 2 == 0:
        return "homework"

def convert_json(excel_path='syllabus.xlsx'):
    excel_path = './input/' + excel_path
    workbook = openpyxl.load_workbook(filename=excel_path, read_only=False)
    # シートのロード
    sheet = workbook['Sheet1']
    f = open('log.txt', 'a')

    json_list = []
    first_counter = True
    for row in sheet.iter_rows():
        theme = []
        homework = []

        if first_counter:
            first_counter = False
            continue
        else:
            data = OrderedDict()
        for cell in row:
            # print("行:" + str(cell.row), "列:" + str(cell.column))
            # print(cell.value)
            # f.write("行:" + str(cell.row) + "列:" + str(cell.column) + " " + str(cell.value) + '\n')
            if cell.row >= 2:
                # print("行:" + str(cell.row) + "列:" + str(cell.column) + " " + str(cell.value) + '\n')
                # print(generation_dict(int(cell.column) - 1))
                if generation_dict(int(cell.column) - 1) == "theme":
                    theme.append(cell.value)
                    data[generation_dict(int(cell.column) - 1)] = theme
                elif generation_dict(int(cell.column) - 1) == "homework":
                    homework.append(cell.value)
                    data[generation_dict(int(cell.column) - 1)] = homework
                else:
                    data[generation_dict(int(cell.column) - 1)] = cell.value
                
        json_list.append(data)
    output_name = './test_data.json'
    with open(output_name, 'w') as file:
        json.dump(json_list, file, indent=4, ensure_ascii=False)

    print("Success!!")

convert_json()

