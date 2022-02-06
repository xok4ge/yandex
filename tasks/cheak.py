def cheak_num(hight, wight):
    k1 = 0
    if len(hight) == 0 or len(wight) == 0:
        k1 = 0
    else:
        lst_hight = list(hight)
        lst_wight = list(wight)

        if lst_hight.count(".") <= 1 and lst_hight.count("-") <= 1 and lst_wight.count(".") <= 1 and lst_wight.count(
                "-") <= 1:
            for s in lst_hight:
                if s == "-" or s == ".":
                    lst_hight.remove(s)

            for s in lst_wight:
                if s == "-" or s == ".":
                    lst_wight.remove(s)

            str_hight = "".join(lst_hight)
            str_wight = ''.join(lst_wight)

            # print(str_hight, str_wight)

            if str_hight.isdigit() == True and str_wight.isdigit() == True:
                if -180 <= float(hight) <= 180 and -85 <= float(wight) <= 85:
                    k1 = 1
                else:
                    k1 = 0

        else:
            k1 = 0

    return k1


def cheak_map(r1, r2, r3):
    if r1 == False and r2 == False and r3 == False:
        k2 = 0
        return k2, "map"
    else:
        if r3:
            type = "sat,skl"
        elif r2:
            type = 'sat'
        else:
            type = "map"
        k2 = 1
        return k2, type

# print(cheak_num("-7.78", "-59.25"), cheak_map(False, False, False))
