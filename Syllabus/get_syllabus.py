import openpyxl
import json
from collections import OrderedDict
import pprint
import time

# エクセルファイルのロード
excel_path = './syllabus.xlsx'
workbook = openpyxl.load_workbook(filename=excel_path)

# シートのロード
sheet = workbook['Sheet1']

"""
for rows in sheet.iter_rows(min_row=1, min_col=1):
    for cell in rows:
        print(cell.value)
"""

"""
instructor	grade	semester	day	A	B	C	D	E	F	G	H	I	J	K	L	M	N	O	P	Q	R	S	T	U	V	W	X	Y	Z	AA	AB	AC	AD	AE	AF	AG	AH	AI	AJ	AK	AL	AM	AN	AO	AP	AQ	AR	AS	AT	AU	AV	AW	AX	AY	AZ	BA	BB	BC	BD	BF	BG	BH	BI	BJ	BK	BL	BM	BN	BO	BP	BQ	BR	BS	BT	BU	BV	BW	BX	BY	BZ	CA	CB
"""

title_list = []
folder_list = []
subject_list = []
class_list = []
instructor_list = []
grade_list = []
semester_list = []
day_list = []
A_list = []
B_list = []
C_list = []
D_list = []
E_list = []
F_list = []
G_list = []
H_list = []
I_list = []
J_list = []
K_list = []
L_list = []
M_list = []
N_list = []
O_list = []
P_list = []
Q_list = []
R_list = []
S_list = []
T_list = []
U_list = []
V_list = []
W_list = []
X_list = []
Y_list = []
Z_list = []
AA_list = []
AB_list = []
AC_list = []
AD_list = []
AE_list = []
AF_list = []
AG_list = []
AH_list = []
AI_list = []
AJ_list = []
AK_list = []
AL_list = []
AM_list = []
AN_list = []
AO_list = []
AP_list = []
AQ_list = []
AR_list = []
AS_list = []
AT_list = []
AU_list = []
AV_list = []
AW_list = []
AX_list = []
AY_list = []
AZ_list = []
BA_list = []
BB_list = []
BC_list = []
BD_list = []
BE_list = []
BF_list = []
BG_list = []
BH_list = []
BI_list = []
BJ_list = []
BK_list = []
BL_list = []
BM_list = []
BN_list = []
BO_list = []
BP_list = []
BQ_list = []
BR_list = []
BS_list = []
BT_list = []
BU_list = []
BV_list = []
BW_list = []
BX_list = []
BY_list = []
BZ_list = []
CA_list = []
CB_list = []

for colum in range(1, 88):
    for cell in list(sheet.columns)[colum]:
        print(colum)
        if cell.row >= 2:
            if colum == 1:
                title_list.append(cell.value)
            elif colum == 2:
                title_list.append(cell.value)
            elif colum == 3:
                folder_list.append(cell.value)
            elif colum == 4:
                subject_list.append(cell.value)
            elif colum == 5:
                class_list.append(cell.value)
            elif colum == 6:
                instructor_list.append(cell.value)
            elif colum == 7:
                grade_list.append(cell.value)
            elif colum == 8:
                semester_list.append(cell.value)
            elif colum == 9:
                day_list.append(cell.value)
            elif colum == 10:
                A_list.append(cell.value)
            elif colum == 11:
                B_list.append(cell.value)
            elif colum == 12:
                C_list.append(cell.value)
            elif colum == 13:
                D_list.append(cell.value)
            elif colum == 14:
                E_list.append(cell.value)
            elif colum == 15:
                F_list.append(cell.value)
            elif colum == 16:
                G_list.append(cell.value)
            elif colum == 17:
                H_list.append(cell.value)
            elif colum == 18:
                I_list.append(cell.value)
            elif colum == 19:
                J_list.append(cell.value)
            elif colum == 20:
                K_list.append(cell.value)
            elif colum == 21:
                L_list.append(cell.value)
            elif colum == 22:
                M_list.append(cell.value)
            elif colum == 23:
                N_list.append(cell.value)
            elif colum == 24:
                O_list.append(cell.value)
            elif colum == 25:
                P_list.append(cell.value)
            elif colum == 26:
                Q_list.append(cell.value)
            elif colum == 27:
                R_list.append(cell.value)
            elif colum == 28:
                S_list.append(cell.value)
            elif colum == 29:
                T_list.append(cell.value)
            elif colum == 30:
                U_list.append(cell.value)
            elif colum == 31:
                V_list.append(cell.value)
            elif colum == 32:
                W_list.append(cell.value)
            elif colum == 33:
                X_list.append(cell.value)
            elif colum == 34:
                Y_list.append(cell.value)
            elif colum == 35:
                Z_list.append(cell.value)
            elif colum == 36:
                AA_list.append(cell.value)
            elif colum == 37:
                AB_list.append(cell.value)
            elif colum == 38:
                AC_list.append(cell.value)
            elif colum == 39:
                AD_list.append(cell.value)
            elif colum == 40:
                AE_list.append(cell.value)
            elif colum == 41:
                AF_list.append(cell.value)
            elif colum == 42:
                AG_list.append(cell.value)
            elif colum == 43:
                AH_list.append(cell.value)
            elif colum == 44:
                AI_list.append(cell.value)
            elif colum == 45:
                AJ_list.append(cell.value)
            elif colum == 46:
                AK_list.append(cell.value)
            elif colum == 47:
                AL_list.append(cell.value)
            elif colum == 48:
                AM_list.append(cell.value)
            elif colum == 49:
                AN_list.append(cell.value)
            elif colum == 50:
                AO_list.append(cell.value)
            elif colum == 51:
                AP_list.append(cell.value)
            elif colum == 52:
                AQ_list.append(cell.value)
            elif colum == 53:
                AR_list.append(cell.value)
            elif colum == 54:
                AS_list.append(cell.value)
            elif colum == 55:
                AT_list.append(cell.value)
            elif colum == 56:
                AU_list.append(cell.value)
            elif colum == 57:
                AV_list.append(cell.value)
            elif colum == 58:
                AW_list.append(cell.value)
            elif colum == 59:
                AX_list.append(cell.value)
            elif colum == 60:
                AY_list.append(cell.value)
            elif colum == 61:
                AZ_list.append(cell.value)
            elif colum == 62:
                BA_list.append(cell.value)
            elif colum == 63:
                BB_list.append(cell.value)
            elif colum == 64:
                BC_list.append(cell.value)
            elif colum == 65:
                BD_list.append(cell.value)
            elif colum == 66:
                BE_list.append(cell.value)
            elif colum == 67:
                BF_list.append(cell.value)
            elif colum == 68:
                BG_list.append(cell.value)
            elif colum == 69:
                BH_list.append(cell.value)
            elif colum == 70:
                BI_list.append(cell.value)
            elif colum == 71:
                BJ_list.append(cell.value)
            elif colum == 72:
                BK_list.append(cell.value)
            elif colum == 73:
                BL_list.append(cell.value)
            elif colum == 74:
                BM_list.append(cell.value)
            elif colum == 75:
                BN_list.append(cell.value)
            elif colum == 76:
                BO_list.append(cell.value)
            elif colum == 77:
                BP_list.append(cell.value)
            elif colum == 78:
                BQ_list.append(cell.value)
            elif colum == 79:
                BR_list.append(cell.value)
            elif colum == 80:
                BS_list.append(cell.value)
            elif colum == 81:
                BT_list.append(cell.value)
            elif colum == 82:
                BU_list.append(cell.value)
            elif colum == 83:
                BV_list.append(cell.value)
            elif colum == 84:
                BW_list.append(cell.value)
            elif colum == 85:
                BX_list.append(cell.value)
            elif colum == 86:
                BY_list.append(cell.value)
            elif colum == 87:
                BZ_list.append(cell.value)
            elif colum == 88:
                CA_list.append(cell.value)
            elif colum == 89:
                CB_list.append(cell.value)
