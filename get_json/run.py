import get_syllabus
import os

if __name__ == '__main__':
    # get_syllabus.get_files()
    print("---------------------")
    # get_syllabus.get_files_dict()
    path = "./pdf"
    files = os.listdir(path)
    for name in files:
        print(name)
        if "pdf" in name:
            get_syllabus.output(name)
    # get_syllabus.output("econo_economics2021.pdf")
    # get_syllabus.output("qualification_tp2021.pdf")
