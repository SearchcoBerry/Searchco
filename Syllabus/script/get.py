import openpyxl
import json
from collections import OrderedDict
import pprint
import time
from tqdm import tqdm

# 辞書を生成するときに使用する関数

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

    json_list = []
    first_counter = True
    # tqdm(sheet.iter_rows(), total=len(len(sheet.iter_rows())))
    # sheet.iter_rows()
    print(sheet.max_row, sheet.max_column)
    sheet_len = sheet.max_row
    for row in tqdm(sheet.iter_rows(), total=sheet_len):
        theme = []
        homework = []

        if first_counter:
            first_counter = False
            continue
        else:
            data = OrderedDict()
        for cell in row:
            if cell.row >= 2:
                value = str(cell.value).replace('\n', '')
                if generation_dict(int(cell.column) - 1) == "theme":
                    theme.append(value)
                    data[generation_dict(int(cell.column) - 1)] = theme
                elif generation_dict(int(cell.column) - 1) == "homework":
                    homework.append(value)
                    data[generation_dict(int(cell.column) - 1)] = homework
                else:
                    data[generation_dict(int(cell.column) - 1)] = value
                
        json_list.append(data)
    output_name = './output/syllabus.json'
    with open(output_name, 'w') as file:
        json.dump(json_list, file, indent=4, ensure_ascii=False)

    print("Success!!")


def main():
    convert_json()


if __name__ == "__main__":
    main()

