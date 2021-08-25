from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

import json
from collections import OrderedDict
from tqdm import tqdm
import requests
from bs4 import BeautifulSoup
import re


def get_files():
    print("test")

    # スクレイピング対象の URL にリクエストを送り HTML を取得する
    res = requests.get('https://www.okiu.ac.jp/academic/lecture/syllabus/sy2021')

    # レスポンスの HTML から BeautifulSoup オブジェクトを作る
    soup = BeautifulSoup(res.text, 'html.parser')

    #elems = soup.find_all(data-block-id=re.compile(""))
    elems = soup.find("div",attrs={"data-block-id":"641847"})
    link = elems.find_all(href=re.compile("https://www2.okiu.ac.jp/syllabus"))

    #print(*elems)

    url = {link[i].get('href') for i in range(len(link))}

    print(len(url))

    #print(url + ":" + len(url))



def output(PATH):
    fp = open(PATH, 'rb')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pages = PDFPage.get_pages(fp)

    subject_list = []
    subject_teacher_list = []
    subject_schedule_list = []

    print("Getting PDF...")
    for page in tqdm(pages):
        #print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        for lobj in layout:
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                #print('At %r is text: %s' % ((x, y), text))

                word = text

                # 曜日・日限を取得
                if x == 458.46 or x == 453.96:
                    #print('At %r is text: %s' % ((x, y), text))
                    word = word.replace('\n', '')
                    subject_schedule_list.append(word)
                # 担当者を取得
                elif "担当者" in text and x == 31.86 and len(text) < 30:
                    word = word.replace('-', '')
                    word = word.replace('\u3000', '')
                    word = word.replace('担当者', '')
                    word = word.replace('\n', '')
                    subject_teacher_list.append(word)
                # 科目名を取得
                elif "科目名" in text and x == 31.86:
                    word = word.replace('科目名', '')
                    word = word.replace('\u3000', '')
                    word = word.replace('\n', '')
                    subject_list.append(word)

    json_list = []
    for i in tqdm(range(len(subject_list))):
        data = OrderedDict()
        data["subject_name"] = subject_list[i]
        data["subject_teacher"] = subject_teacher_list[i]
        data["subject_schedule"] = subject_schedule_list[i]

        json_list.append(data)

    output_name = './output/' + PATH[:-4] + '.json'
    with open(output_name, 'w') as file:
        json.dump(json_list, file, indent=4, ensure_ascii=False)

    print("Success!!")
