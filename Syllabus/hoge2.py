li = [
    "title_list",
    "folder_list",
    "subject_list",
    "class_list",
    "instructor_list",
    "grade_list",
    "semester_list",
    "day_list",
    "A_list",
    "B_list",
    "C_list",
    "D_list",
    "E_list",
    "F_list",
    "G_list",
    "H_list",
    "I_list",
    "J_list",
    "K_list",
    "L_list",
    "M_list",
    "N_list",
    "O_list",
    "P_list",
    "Q_list",
    "R_list",
    "S_list",
    "T_list",
    "U_list",
    "V_list",
    "W_list",
    "X_list",
    "Y_list",
    "Z_list",
    "AA_list",
    "AB_list",
    "AC_list",
    "AD_list",
    "AE_list",
    "AF_list",
    "AG_list",
    "AH_list",
    "AI_list",
    "AJ_list",
    "AK_list",
    "AL_list",
    "AM_list",
    "AN_list",
    "AO_list",
    "AP_list",
    "AQ_list",
    "AR_list",
    "AS_list",
    "AT_list",
    "AU_list",
    "AV_list",
    "AW_list",
    "AX_list",
    "AY_list",
    "AZ_list",
    "BA_list",
    "BB_list",
    "BC_list",
    "BD_list",
    "BE_list",
    "BF_list",
    "BG_list",
    "BH_list",
    "BI_list",
    "BJ_list",
    "BK_list",
    "BL_list",
    "BM_list",
    "BN_list",
    "BO_list",
    "BP_list",
    "BQ_list",
    "BR_list",
    "BS_list",
    "BT_list",
    "BU_list",
    "BV_list",
    "BW_list",
    "BX_list",
    "BY_list",
    "BZ_list",
    "CA_list",
    "CB_list"
]

txt = '    {}.append(cell.value)'
count = 1

for i in li:
    print("elif cell.column == " + str(count) + ":")
    count += 1
    print(txt.format(i))

"""
for i in li:
    print(txt.format(i))
"""
