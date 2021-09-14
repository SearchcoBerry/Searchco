from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

import json
from collections import OrderedDict
from tqdm import tqdm


def output(PATH):
    fp = open("./pdf/" + PATH, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)

    subject_list = []
    subject_teacher_list = []
    subject_schedule_list = []
    subject_period_list = []
    subject_contact_list = []

    print("Getting PDF...")
    for page in tqdm(pages):
        # print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        index_1 = 0
        index_2 = 0
        index_3 = 0
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                print('At %r is text: %s' % ((x, y), text))
                f = open('myfile.txt', 'a')
                f.write('At %r is text: %s' % ((x, y), text))

                word = text

                # 曜日・日限を取得
                if x == 458.46 or x == 453.96 or x == 449.46:
                    word = word.replace('\n', '')
                    subject_schedule_list.append(word)
                    index_1 += 1

                # 担当者を取得
                elif "担当者" in text and x == 31.86 and len(text) < 30:
                    word = word.replace('-', '')
                    word = word.replace('\u3000', '')
                    word = word.replace('担当者', '')
                    word = word.replace('\n', '')
                    subject_teacher_list.append(word)
                    index_2 += 1
                # 科目名を取得
                elif "科目名" in text and x == 31.86:
                    index_3 += 1
                    word = word.replace('科目名', '')
                    word = word.replace('\u3000', '')
                    word = word.replace('\n', '')
                    subject_list.append(word)
                    # print("index_checked:" + str(index_1 + ", " + index_2))

                # 期別を取得
                elif x == 341.82 and y == 791.3249999999999:
                    subject_period_list.append(word)

                # 問い合わせを取得
                elif x == 399.24 and y == 754.965:
                    subject_period_list.append(word)

        print("----------")
        f.write('------------------------------\n')

    json_list = []
    print(len(subject_schedule_list), len(subject_teacher_list), len(subject_list))
    for i in tqdm(range(len(subject_list))):
        data = OrderedDict()
        data["subject_name"] = subject_list[i]
        data["subject_teacher"] = subject_teacher_list[i]
        data["subject_schedule"] = subject_schedule_list[i]
        data["subject_period"] = subject_period_list[i]

        json_list.append(data)

    output_name = './output/' + PATH[:-4] + '.json'
    output_name = output_name.replace('./pdf/', '')
    with open(output_name, 'w') as file:
        json.dump(json_list, file, indent=4, ensure_ascii=False)

    print("Success!!")


output("industrial_industrialinformation2021.pdf")
