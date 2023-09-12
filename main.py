import time

var={}

f=open("test.zc","r",encoding="utf-8")
o_code=f.read().replace(" ","").replace("\n","").split(",")
code=[]
for i in o_code:
    if "." in i:
        for a in i.replace(".","。.").split("."):
            code.append(a.replace("。","."))
    else:
        code.append(i)

now_line=-1
ch_if=False



for fo in range(len(code)):
    now_line+=1

    try:
        i=code[now_line]
    except:
        pass
    if ch_if:
        if ch_if_text:
            if i.endswith("."):
                i=i.replace(".","")
                ch_if=False

        else:
            while not i.endswith("."):
                now_line+=1
                i=code[now_line]
            now_line+=1
            ch_if=False
    try:
        i=code[now_line]
    except:
        pass
    
    if i.startswith("設定變數"):
        l=i.replace("設定變數","")
        ls=l.split("為")
        var[ls[0]]=ls[1]

    elif i.startswith("顯示"):
        p=i.replace("顯示","").replace(".","")
        try:
            print(var[p])
        except:
            print(p)

    elif i.startswith("如果"):
        c=i.replace("如果","")
        if not "不等於" in c:
            c_if=c.split("等於")
            try:
                if_1=var[c_if[0]]
            except:
                if_1=c_if[0]
            try:
                if_2=var[c_if[1]]
            except:
                if_2=c_if[1]
            if if_1==if_2:
                ch_if=True
                ch_if_text=True

            else:
                ch_if=True
                ch_if_text=False
        else:
            c_if=c.split("不等於")
            try:
                if_1=var[c_if[0]]
            except:
                if_1=c_if[0]
            try:
                if_2=var[c_if[1]]
            except:
                if_2=c_if[1]
            if if_1==if_2:

                ch_if=True
                ch_if_text=False
            else:
                ch_if=True
                ch_if_text=True
    
    elif i.startswith("輸入"):
        c=i.replace("輸入","")
        var[c]=input("輸入: ")

    elif i.startswith("計算"):
        c=i.replace("計算","").replace(".","").replace(",","")
        print(eval(var[c]))

    elif i.startswith("等待"):
        c=i.replace("等待","").replace(".","").replace(",","")
        time.sleep(int(c))

    elif i.startswith("換行"):
        print("\n")
        
    elif i.startswith("退出"):
        exit()