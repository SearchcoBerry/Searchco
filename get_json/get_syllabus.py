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
import re, time, os
import urllib.request as req
import urllib
from urllib.parse import urljoin
import random
import glob
import mojimoji

def get_files(year = 2021):

    # スクレイピング対象の URL にリクエストを送り HTML を取得する
    res = requests.get('https://www.okiu.ac.jp/academic/lecture/syllabus/sy' + str(year))

    # レスポンスの HTML から BeautifulSoup オブジェクトを作る
    soup = BeautifulSoup(res.text, 'html.parser')

    #elems = soup.find_all(data-block-id=re.compile(""))
    elems = soup.find("div",attrs={"data-block-id":"641847"}).select('li')

    print("link----------------")

    urls = []

    for elem in elems:
        try:
            link = elem.find("a", href=re.compile("https://www2.okiu.ac.jp/syllabus"))
            print(link)
            urls.append(str(link.get('href')))
        except AttributeError:
            print("None")

    print("check_list:" + str(len(urls)))

    print("url///")
    #print(urls)

    filename_list = []
    for download_url in urls:
        temp_list = download_url.split("/")
        filename_list.append(temp_list[-1])
    #print(filename_list)

    # スリープ
    #time.sleep(2)

    target_dir = "./pdf"
    savepath_list = []
    for filename in filename_list:
        savepath_list.append(os.path.join(target_dir, filename))
    #print(savepath_list)

    print("Download Files...")

    for (pdflink, savepath) in zip(urls, savepath_list):
        urllib.request.urlretrieve(pdflink, savepath)
        print(pdflink,savepath)
        time.sleep(random.randint(3, 6))

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

    print("Getting PDF...")
    index_0 = 0
    index_1 = 0
    index_2 = 0
    index_3 = 0
    for page in tqdm(pages):
        index_0 += 1
        #print('Processing next page...')
        interpreter.process_page(page)
        layout = device.get_result()
        """
        for i in range(len(layout)):
            print()
        """
        
        for lobj in layout:
            
            if isinstance(lobj, LTTextBox):
                x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
                #print('At %r is text: %s' % ((x, y), text))

                word = text

                f = open('myfile.txt', 'a')
                f.write('At %r is text: %s' % ((x, y), text))

                # 曜日・日限を取得
                if (x == 458.46 or x == 453.96 or x == 449.46 or x == 444.96) and y == 791.3249999999999:
                    index_1 += 1
                    word = word.replace('\n', '')
                    word = mojimoji.zen_to_han(word, kana=False, ascii=False) 
                    subject_schedule_list.append(word)
                
                # 担当者を取得
                elif "担当者" in text and x == 31.86 and y == 774.405:
                    index_2 += 1
                    word = word.replace('-', '')
                    word = word.replace('\u3000', '')
                    word = word.replace('担当者', '')
                    word = word.replace('\n', '')
                    subject_teacher_list.append(word)
                    #print(word)
                # 科目名を取得
                elif "科目名" in text and x == 31.86 and y == 809.865:
                    index_3 += 1
                    word = word.replace('科目名', '')
                    word = word.replace('\u3000', '')
                    word = word.replace('\n', '')
                    subject_list.append(word)
                    #print(word)

            # print(len(subject_schedule_list),len(subject_teacher_list), len(subject_list))
        if len(subject_schedule_list) < len(subject_teacher_list):
            subject_schedule_list.append("")
        
        f = open('index_check.txt', 'a')
        f.write("index_checked:" + str(index_0) + ", " + str(index_1) + ", " + str(index_2) + ", " + str(index_3) + " / ")
        f.write(str(len(subject_schedule_list)) + ", " + str(len(subject_teacher_list)) + ", " + str(len(subject_list)) + "\n")

        """
        f = open('index_check.txt', 'a')
        f.write("index_checked:" + str(index_0) + ", " + str(index_1) + ", " + str(index_2) + ", " + str(index_3) + " / ")
        f.write(str(len(subject_schedule_list)) + ", " + str(len(subject_teacher_list)) + ", " + str(len(subject_list)) + "\n")
        print("index_checked:" + str(index_0) + ", " + str(index_1) + ", " + str(index_2) + ", " + str(index_3))
        """

    json_list = []
    print(len(subject_schedule_list),len(subject_teacher_list), len(subject_list))
    for i in tqdm(range(len(subject_list))):
        data = OrderedDict()
        data["subject_name"] = subject_list[i]
        data["subject_teacher"] = subject_teacher_list[i]
        data["subject_schedule"] = subject_schedule_list[i]

        json_list.append(data)

    output_name = './output/' + PATH[:-4] + '.json'
    output_name = output_name.replace('./pdf/','')
    with open(output_name, 'w') as file:
        json.dump(json_list, file, indent=4, ensure_ascii=False)

    print("Success!!")

def get_pdf_names():
    files = glob.glob("./pdf/*.pdf")
    for f in files:
        print(f[6:])
        output(f)

def get_files_dict(year = 2021):

    # スクレイピング対象の URL にリクエストを送り HTML を取得する
    res = requests.get('https://www.okiu.ac.jp/academic/lecture/syllabus/sy' + str(year))

    # レスポンスの HTML から BeautifulSoup オブジェクトを作る
    soup = BeautifulSoup(res.text, 'html.parser')

    #elems = soup.find_all(data-block-id=re.compile(""))
    elems = soup.find("div",attrs={"data-block-id":"641847"}).select('li')

    print("link----------------")

    urls = []
    title = []
    tag_list = []

    for elem in elems:
        try:
            link = elem.find("a", href=re.compile("https://www2.okiu.ac.jp/syllabus"))
            #print(link)
            url = str(link.get('href'))
            url_split = url.split("/")
            url = url_split[-1]
            urls.append(url)
            title.append(str(link.get_text()))
        except AttributeError:
            print("None")
    
    for i in tqdm(range(len(title))):
        data = OrderedDict()
        data["label"] = title[i]
        data["code"] = urls[i]

        tag_list.append(data)

    output_name = './output/rakusitai.json'
    with open(output_name, 'w') as file:
        json.dump(tag_list, file, indent=4, ensure_ascii=False)

    print("Success!!")

    print("check_list:" + str(len(urls)))
