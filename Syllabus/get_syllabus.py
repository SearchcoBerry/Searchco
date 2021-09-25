import pandas
import csv
import json


def output(filename):
    name = filename.replace('.xlsx', '')
    excel_path = './input/' + name + '.xlsx'
    df = pandas.read_excel(excel_path, sheet_name=0)
    csv_path = "./output/" + name + ".csv"
    df.to_csv(csv_path, index=False)

    json_list = []

    # CSV ファイルの読み込み
    with open(csv_path, 'r') as f:
        for row in csv.DictReader(f):
            json_list.append(row)

    # JSON ファイルへの書き込み
    with open('./output/' + name + '.json', 'w') as f:
        json.dump(json_list, f, ensure_ascii=False)


output("syllabus.xlsx")
