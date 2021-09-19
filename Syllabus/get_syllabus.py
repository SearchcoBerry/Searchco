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
        # print(cell.value)
        if cell.row >= 2:
            if (cell.column - 1) == 1:
                title_list.append(cell.value)
            elif (cell.column - 1) == 2:
                folder_list.append(cell.value)
            elif (cell.column - 1) == 3:
                subject_list.append(cell.value)
            elif (cell.column - 1) == 4:
                class_list.append(cell.value)
            elif (cell.column - 1) == 5:
                instructor_list.append(cell.value)
            elif (cell.column - 1) == 6:
                grade_list.append(cell.value)
            elif (cell.column - 1) == 7:
                semester_list.append(cell.value)
            elif (cell.column - 1) == 8:
                day_list.append(cell.value)
            elif (cell.column - 1) == 9:
                A_list.append(cell.value)
            elif (cell.column - 1) == 10:
                B_list.append(cell.value)
            elif (cell.column - 1) == 11:
                C_list.append(cell.value)
            elif (cell.column - 1) == 12:
                D_list.append(cell.value)
            elif (cell.column - 1) == 13:
                E_list.append(cell.value)
            elif (cell.column - 1) == 14:
                F_list.append(cell.value)
            elif (cell.column - 1) == 15:
                G_list.append(cell.value)
            elif (cell.column - 1) == 16:
                H_list.append(cell.value)
            elif (cell.column - 1) == 17:
                I_list.append(cell.value)
            elif (cell.column - 1) == 18:
                J_list.append(cell.value)
            elif (cell.column - 1) == 19:
                K_list.append(cell.value)
            elif (cell.column - 1) == 20:
                L_list.append(cell.value)
            elif (cell.column - 1) == 21:
                M_list.append(cell.value)
            elif (cell.column - 1) == 22:
                N_list.append(cell.value)
            elif (cell.column - 1) == 23:
                O_list.append(cell.value)
            elif (cell.column - 1) == 24:
                P_list.append(cell.value)
            elif (cell.column - 1) == 25:
                Q_list.append(cell.value)
            elif (cell.column - 1) == 26:
                R_list.append(cell.value)
            elif (cell.column - 1) == 27:
                S_list.append(cell.value)
            elif (cell.column - 1) == 28:
                T_list.append(cell.value)
            elif (cell.column - 1) == 29:
                U_list.append(cell.value)
            elif (cell.column - 1) == 30:
                V_list.append(cell.value)
            elif (cell.column - 1) == 31:
                W_list.append(cell.value)
            elif (cell.column - 1) == 32:
                X_list.append(cell.value)
            elif (cell.column - 1) == 33:
                Y_list.append(cell.value)
            elif (cell.column - 1) == 34:
                Z_list.append(cell.value)
            elif (cell.column - 1) == 35:
                AA_list.append(cell.value)
            elif (cell.column - 1) == 36:
                AB_list.append(cell.value)
            elif (cell.column - 1) == 37:
                AC_list.append(cell.value)
            elif (cell.column - 1) == 38:
                AD_list.append(cell.value)
            elif (cell.column - 1) == 39:
                AE_list.append(cell.value)
            elif (cell.column - 1) == 40:
                AF_list.append(cell.value)
            elif (cell.column - 1) == 41:
                AG_list.append(cell.value)
            elif (cell.column - 1) == 42:
                AH_list.append(cell.value)
            elif (cell.column - 1) == 43:
                AI_list.append(cell.value)
            elif (cell.column - 1) == 44:
                AJ_list.append(cell.value)
            elif (cell.column - 1) == 45:
                AK_list.append(cell.value)
            elif (cell.column - 1) == 46:
                AL_list.append(cell.value)
            elif (cell.column - 1) == 47:
                AM_list.append(cell.value)
            elif (cell.column - 1) == 48:
                AN_list.append(cell.value)
            elif (cell.column - 1) == 49:
                AO_list.append(cell.value)
            elif (cell.column - 1) == 50:
                AP_list.append(cell.value)
            elif (cell.column - 1) == 51:
                AQ_list.append(cell.value)
            elif (cell.column - 1) == 52:
                AR_list.append(cell.value)
            elif (cell.column - 1) == 53:
                AS_list.append(cell.value)
            elif (cell.column - 1) == 54:
                AT_list.append(cell.value)
            elif (cell.column - 1) == 55:
                AU_list.append(cell.value)
            elif (cell.column - 1) == 56:
                AV_list.append(cell.value)
            elif (cell.column - 1) == 57:
                AW_list.append(cell.value)
            elif (cell.column - 1) == 58:
                AX_list.append(cell.value)
            elif (cell.column - 1) == 59:
                AY_list.append(cell.value)
            elif (cell.column - 1) == 60:
                AZ_list.append(cell.value)
            elif (cell.column - 1) == 61:
                BA_list.append(cell.value)
            elif (cell.column - 1) == 62:
                BB_list.append(cell.value)
            elif (cell.column - 1) == 63:
                BC_list.append(cell.value)
            elif (cell.column - 1) == 64:
                BD_list.append(cell.value)
            elif (cell.column - 1) == 65:
                BE_list.append(cell.value)
            elif (cell.column - 1) == 66:
                BF_list.append(cell.value)
            elif (cell.column - 1) == 67:
                BG_list.append(cell.value)
            elif (cell.column - 1) == 68:
                BH_list.append(cell.value)
            elif (cell.column - 1) == 69:
                BI_list.append(cell.value)
            elif (cell.column - 1) == 70:
                BJ_list.append(cell.value)
            elif (cell.column - 1) == 71:
                BK_list.append(cell.value)
            elif (cell.column - 1) == 72:
                BL_list.append(cell.value)
            elif (cell.column - 1) == 73:
                BM_list.append(cell.value)
            elif (cell.column - 1) == 74:
                BN_list.append(cell.value)
            elif (cell.column - 1) == 75:
                BO_list.append(cell.value)
            elif (cell.column - 1) == 76:
                BP_list.append(cell.value)
            elif (cell.column - 1) == 77:
                BQ_list.append(cell.value)
            elif (cell.column - 1) == 78:
                BR_list.append(cell.value)
            elif (cell.column - 1) == 79:
                BS_list.append(cell.value)
            elif (cell.column - 1) == 80:
                BT_list.append(cell.value)
            elif (cell.column - 1) == 81:
                BU_list.append(cell.value)
            elif (cell.column - 1) == 82:
                BV_list.append(cell.value)
            elif (cell.column - 1) == 83:
                BW_list.append(cell.value)
            elif (cell.column - 1) == 84:
                BX_list.append(cell.value)
            elif (cell.column - 1) == 85:
                BY_list.append(cell.value)
            elif (cell.column - 1) == 86:
                BZ_list.append(cell.value)
            elif (cell.column - 1) == 87:
                CA_list.append(cell.value)
            elif (cell.column - 1) == 88:
                CB_list.append(cell.value)
json_list = []

"""

for i in range(len(title_list)):
    data = OrderedDict()
    data["title_list"] = title_list[i]
    data["folder_list"] = folder_list[i]
    data["subject_list"] = subject_list[i]
    data["class_list"] = class_list[i]
    data["instructor_list"] = instructor_list[i]
    data["grade_list"] = grade_list[i]
    data["semester_list"] = semester_list[i]
    data["day_list"] = day_list[i]
    data["A_list"] = A_list[i]
    data["B_list"] = B_list[i]
    data["C_list"] = C_list[i]
    data["D_list"] = D_list[i]
    data["E_list"] = E_list[i]
    data["F_list"] = F_list[i]
    data["G_list"] = G_list[i]
    data["H_list"] = H_list[i]
    data["I_list"] = I_list[i]
    data["J_list"] = J_list[i]
    data["K_list"] = K_list[i]
    data["L_list"] = L_list[i]
    data["M_list"] = M_list[i]
    data["N_list"] = N_list[i]
    data["O_list"] = O_list[i]
    data["P_list"] = P_list[i]
    data["Q_list"] = Q_list[i]
    data["R_list"] = R_list[i]
    data["S_list"] = S_list[i]
    data["T_list"] = T_list[i]
    data["U_list"] = U_list[i]
    data["V_list"] = V_list[i]
    data["W_list"] = W_list[i]
    data["X_list"] = X_list[i]
    data["Y_list"] = Y_list[i]
    data["Z_list"] = Z_list[i]
    data["AA_list"] = AA_list[i]
    data["AB_list"] = AB_list[i]
    data["AC_list"] = AC_list[i]
    data["AD_list"] = AD_list[i]
    data["AE_list"] = AE_list[i]
    data["AF_list"] = AF_list[i]
    data["AG_list"] = AG_list[i]
    data["AH_list"] = AH_list[i]
    data["AI_list"] = AI_list[i]
    data["AJ_list"] = AJ_list[i]
    data["AK_list"] = AK_list[i]
    data["AL_list"] = AL_list[i]
    data["AM_list"] = AM_list[i]
    data["AN_list"] = AN_list[i]
    data["AO_list"] = AO_list[i]
    data["AP_list"] = AP_list[i]
    data["AQ_list"] = AQ_list[i]
    data["AR_list"] = AR_list[i]
    data["AS_list"] = AS_list[i]
    data["AT_list"] = AT_list[i]
    data["AU_list"] = AU_list[i]
    data["AV_list"] = AV_list[i]
    data["AW_list"] = AW_list[i]
    data["AX_list"] = AX_list[i]
    data["AY_list"] = AY_list[i]
    data["AZ_list"] = AZ_list[i]
    data["BA_list"] = BA_list[i]
    data["BB_list"] = BB_list[i]
    data["BC_list"] = BC_list[i]
    data["BD_list"] = BD_list[i]
    data["BE_list"] = BE_list[i]
    data["BF_list"] = BF_list[i]
    data["BG_list"] = BG_list[i]
    data["BH_list"] = BH_list[i]
    data["BI_list"] = BI_list[i]
    data["BJ_list"] = BJ_list[i]
    data["BK_list"] = BK_list[i]
    data["BL_list"] = BL_list[i]
    data["BM_list"] = BM_list[i]
    data["BN_list"] = BN_list[i]
    data["BO_list"] = BO_list[i]
    data["BP_list"] = BP_list[i]
    data["BQ_list"] = BQ_list[i]
    data["BR_list"] = BR_list[i]
    data["BS_list"] = BS_list[i]
    data["BT_list"] = BT_list[i]
    data["BU_list"] = BU_list[i]
    data["BV_list"] = BV_list[i]
    data["BW_list"] = BW_list[i]
    data["BX_list"] = BX_list[i]
    data["BY_list"] = BY_list[i]
    data["BZ_list"] = BZ_list[i]
    data["CA_list"] = CA_list[i]
    data["CB_list"] = CB_list[i]

    json_list.append(data)

output_name = './output/syllabus.json'
with open(output_name, 'w') as file:
    json.dump(json_list, file, indent=4, ensure_ascii=False)
"""
print("Success!!")


print(
    len(title_list),
    len(folder_list),
    len(subject_list),
    len(class_list),
    len(instructor_list),
    len(grade_list),
    len(semester_list),
    len(day_list),
    len(A_list),
    len(B_list),
    len(C_list),
    len(D_list),
    len(E_list),
    len(F_list),
    len(G_list),
    len(H_list),
    len(I_list),
    len(J_list),
    len(K_list),
    len(L_list),
    len(M_list),
    len(N_list),
    len(O_list),
    len(P_list),
    len(Q_list),
    len(R_list),
    len(S_list),
    len(T_list),
    len(U_list),
    len(V_list),
    len(W_list),
    len(X_list),
    len(Y_list),
    len(Z_list),
    len(AA_list),
    len(AB_list),
    len(AC_list),
    len(AD_list),
    len(AE_list),
    len(AF_list),
    len(AG_list),
    len(AH_list),
    len(AI_list),
    len(AJ_list),
    len(AK_list),
    len(AL_list),
    len(AM_list),
    len(AN_list),
    len(AO_list),
    len(AP_list),
    len(AQ_list),
    len(AR_list),
    len(AS_list),
    len(AT_list),
    len(AU_list),
    len(AV_list),
    len(AW_list),
    len(AX_list),
    len(AY_list),
    len(AZ_list),
    len(BA_list),
    len(BB_list),
    len(BC_list),
    len(BD_list),
    len(BE_list),
    len(BF_list),
    len(BG_list),
    len(BH_list),
    len(BI_list),
    len(BJ_list),
    len(BK_list),
    len(BL_list),
    len(BM_list),
    len(BN_list),
    len(BO_list),
    len(BP_list),
    len(BQ_list),
    len(BR_list),
    len(BS_list),
    len(BT_list),
    len(BU_list),
    len(BV_list),
    len(BW_list),
    len(BX_list),
    len(BY_list),
    len(BZ_list),
    len(CA_list),
    len(CB_list),
)


# print(len(title_list))
