result = ["","","","",""]

df = "*****"
db = "*   *"
dr = "    *"
de = "     "
db = "*   *"
dm = "  *  "
dl = "*    "
dll= " **  "

big_font_0 = "%s\n%s\n%s\n%s\n%s" % (df,db,db,db,df)
big_font_1 = "%s\n%s\n%s\n%s\n%s" % (dm,dm,dm,dm,dm)
big_font_2 = "%s\n%s\n%s\n%s\n%s" % (df,dr,df,dl,df)
big_font_3 = "%s\n%s\n%s\n%s\n%s" % (df,dr,df,dr,df)
big_font_4 = "%s\n%s\n%s\n%s\n%s" % (dm,dll,df,dm,dm)
big_font_5 = "%s\n%s\n%s\n%s\n%s" % (df,dl,df,dr,df)
big_font_6 = "%s\n%s\n%s\n%s\n%s" % (df,dl,df,db,df)
big_font_7 = "%s\n%s\n%s\n%s\n%s" % (df,db,db,dr,dr)
big_font_8 = "%s\n%s\n%s\n%s\n%s" % (df,db,df,db,df)
big_font_9 = "%s\n%s\n%s\n%s\n%s" % (df,db,df,dr,dr)
big_font_10 = "%s\n%s\n%s\n%s\n%s" % (de,de,df,de,de)
big_font_11 = "%s\n%s\n%s\n%s\n%s" % (dm,de,de,de,dm)

big_font = [
            big_font_0,
            big_font_1,
            big_font_2,
            big_font_3,
            big_font_4,
            big_font_5,
            big_font_6,
            big_font_7,
            big_font_8,
            big_font_9,
            big_font_10,
            big_font_11,
            ]


date = "2020-07-23"


for i in date:
    if i == "-":
        print(big_font_10)
    elif i == ":":
        print(big_font_11)
    else :
        i = int(i)
        print(big_font[i])






'''
a1 = "  *  \n  *  \n  *  \n  *  \n  *  "
a2 = "*****\n    *\n*****\n*    \n*****"
a3 = "*****\n    *\n*****\n    *\n*****"
a4 = "  *  \n **  \n*****\n  *  \n  *  "
a5 = "*****\n*    \n*****\n    *\n*****"
a6 = "*****\n*    \n*****\n*   *\n*****"
a7 = "*****\n*   *\n*   *\n    *\n    *"
a8 = "*****\n*   *\n*****\n*   *\n*****"
a9 = "*****\n*   *\n*****\n    *\n    *"
'''











