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
    subject_credits_list = []
    subject_grade_list = []
    subject_purpose_list = []
    subject_message_list = []
    subject_goal_list = []
    subject_theme_list = []
    subject_contents_list = []
    subject_references_list = []
    subject_documents_list = []
    subject_points_list = []
    subject_related_list = []

    print("Getting PDF...")
    for page in tqdm(pages):
        subject_theme_sublist = []
        subject_contents_sublist = []
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
                # f = open('myfile.txt', 'a')
                # f.write('At %r is text: %s' % ((x, y), text))

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

                # 単位数を取得
                elif x == 557.28 and y == 791.3249999999999:
                    subject_credits_list.append(word)

                # 対象年次を取得
                elif x == 339.84 and y == 754.965:
                    subject_grade_list.append(word)

                # 問い合わせを取得
                elif x == 399.24 and y == 754.965:
                    subject_contact_list.append(word)

                # ねらいを取得
                elif x == 31.86 and y == 24.725:
                    subject_purpose_list.append(word)

                # メッセージを取得
                elif x == 308.34 and y == 724.725:
                    subject_message_list.append(word)

                # 到達目標を取得
                elif x == 31.86 and y == 653.805:
                    subject_goal_list.append(word)

                # テーマを取得
                # No.1
                elif x == 47.16 and y == 533.0331:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 533.0331:
                    subject_contents_sublist.append(word)

                # No.2
                elif x == 47.16 and y == 518.8131:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 533.0331:
                    subject_contents_sublist.append(word)
                # No.3
                elif x == 47.16 and y == 518.8131:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 518.8131:
                    subject_contents_sublist.append(word)
                # No.4
                elif x == 47.16 and y == 490.5531:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 490.5531:
                    subject_contents_sublist.append(word)
                # No.5
                elif x == 47.16 and y == 476.3331:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 476.3331:
                    subject_contents_sublist.append(word)
                # No.6
                elif x == 47.16 and y == 462.1131:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 462.1131:
                    subject_contents_sublist.append(word)
                # No.7
                elif x == 47.16 and y == 447.8931:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 447.8931:
                    subject_contents_sublist.append(word)
                # No.8
                elif x == 47.16 and y == 433.6731:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 433.6731:
                    subject_contents_sublist.append(word)
                # No.9
                elif x == 47.16 and y == 419.63309999999996:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 419.63309999999996:
                    subject_contents_sublist.append(word)
                # No.10
                elif x == 47.16 and y == 405.4131:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 405.4131:
                    subject_contents_sublist.append(word)
                # No.11
                elif x == 47.16 and y == 391.19309999999996:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 391.19309999999996:
                    subject_contents_sublist.append(word)
                # No.12
                elif x == 47.16 and y == 376.9731:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 376.9731:
                    subject_contents_sublist.append(word)
                # No.13
                elif x == 47.16 and y == 405.4131:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 405.4131:
                    subject_contents_sublist.append(word)
                # No.14
                elif x == 47.16 and y == 348.7131:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 348.7131:
                    subject_contents_sublist.append(word)
                # No.15
                elif x == 47.16 and y == 334.49309999999997:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 334.49309999999997:
                    subject_contents_sublist.append(word)
                # No.16
                elif x == 47.16 and y == 320.2731:
                    subject_theme_sublist.append(word)
                elif x == 436.14 and y == 320.2731:
                    subject_contents_sublist.append(word)

                # 参考文献を取得
                elif x == 49.68 and y == 287.145:
                    subject_references_list.append(word)

                # 学びの手立てを取得
                elif x == 49.68 and y == 216.225:
                    subject_documents_list.append(word)

                # 評価を取得
                elif x == 49.68 and y == 122.445:
                    subject_points_list.append(word)

                # 次のステージ・関連科目を取得
                elif x == 49.68 and y == 53.325:
                    subject_related_list.append(word)

                """
                elif subject_period_list[-1] == '集中':
                """
            subject_theme_list.append(subject_theme_sublist)
            subject_contents_list.append(subject_contents_sublist)

            if len(subject_schedule_list) < len(subject_teacher_list):
                subject_schedule_list.append("")
            if len(subject_purpose_list) < len(subject_teacher_list):
                subject_contact_list.append("")
                subject_purpose_list.append("")
                subject_message_list.append("")
                subject_goal_list.append("")
                subject_theme_list.append("")
                subject_contents_list.append("")
                subject_references_list.append("")
                subject_documents_list.append("")
                subject_points_list.append("")
                subject_related_list.append("")

        print("----------")
        # f.write('------------------------------\n')

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
