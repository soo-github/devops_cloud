import pymysql
from tkinter import *
from tkinter import messagebox


# 삭제
def deleteData():
    conn = None
    cur = None

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='rentalDB', charset='utf8')

    cur = conn.cursor()

    memberID = listMemberID.get(listMemberID.curselection())
    print(memberID)

    sql = "DELETE FROM memberTBL WHERE memberID = '" +memberID +"'"

    print(sql)

    try :
        cur.execute(sql)
    except:
        messagebox.showerror("삭제오류", "데이터 삭제 오류가 발생 했습니다.")
    else:
        messagebox.showinfo("성공", "회원 정보가 삭제되었습니다.")
        conn.commit()
        selectAllData()

    conn.close()





def insertData():
    conn = None
    cur = None

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='rentalDB', charset='utf8')

    cur = conn.cursor()

    memberID, name, addr, tel = "", "", "", ""

    memberID = edt1.get()
    name = edt2.get()
    addr = edt3.get()
    tel = edt4.get()


    # sql 쿼리 만들기
    sql = ""

    sql = "INSERT INTO memberTBL (memberID, name, addr, tel) VALUES " \
          "('" + memberID + "','" + name + "', '" + addr + "', '" + tel + "')"

    print(sql)

    try :
        cur.execute(sql)
    except:
        messagebox.showerror("입력오류", "데이터 입력 오류가 발생 했습니다.")
    else:
        messagebox.showinfo("성공", "회원 정보가 입력되었습니다.")
        conn.commit()
        selectData()

    # GUI에서 입력한 데이터 삭제
    edt1.delete(0, "end")
    edt2.delete(0, "end")
    edt3.delete(0, "end")
    edt4.delete(0, "end")

    conn.close()




# 전체 조회
def selectAllData():
    conn = None
    cur = None

    memberID = edt1.get()
    name = edt2.get()
    addr = edt3.get()
    tel = edt4.get()

    lMemberID, lName, lAddr, lTel = [], [], [], []

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='rentalDB', charset='utf8')

    cur = conn.cursor()

    lMemberID.append("회원 ID")
    lMemberID.append("--------")

    lName.append("회원명")
    lName.append("--------")

    lAddr.append("주소")
    lAddr.append("--------")

    lTel.append("폰번호")
    lTel.append("--------")

    # sql = "SELECT memberID, name, addr, tel from memberTBL"

    sql = "SELECT memberID, name, IFNULL(addr,'-') AS addr, tel FROM memberTBL"

    cur.execute(sql)

    while (True):
        row = cur.fetchone()

        if row == None:
            break

        lMemberID.append(row[0])
        lName.append(row[1])
        lAddr.append(row[2])
        lTel.append(row[3])

    listMemberID.delete(0, listMemberID.size() - 1)
    listName.delete(0, listName.size() - 1)
    listAddr.delete(0, listAddr.size() - 1)
    listTel.delete(0, listTel.size() - 1)

    for item1, item2, item3, item4 in zip(lMemberID, lName, lAddr, lTel):
        listMemberID.insert(END, item1)
        listName.insert(END, item2)
        listAddr.insert(END, item3)
        listTel.insert(END, item4)

    conn.close()


def selectData():
    conn = None
    cur = None

    memberID = edt1.get()
    name = edt2.get()

    lMemberID, lName, lAddr, lTel = [], [], [], []

    conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='rentalDB', charset='utf8')

    cur = conn.cursor()

    # 데이터 초기화
    lMemberID.append("회원 ID")
    lMemberID.append("--------")

    lName.append("회원명")
    lName.append("--------")

    lAddr.append("주소")
    lAddr.append("--------")

    lTel.append("폰번호")
    lTel.append("--------")

    sql = "SELECT memberID, name, addr, tel from memberTBL WHERE memberID='"+memberID+"' OR  name='"+name+"'"
    cur.execute(sql)


    while(True):
        row = cur.fetchone()

        if row == None:
            break

        lMemberID.append(row[0])
        lName.append(row[1])
        lAddr.append(row[2])
        lTel.append(row[3])


    listMemberID.delete(0, listMemberID.size() - 1)
    listName.delete(0, listName.size() - 1)
    listAddr.delete(0, listAddr.size() - 1)
    listTel.delete(0, listTel.size() - 1)


    for item1, item2, item3, item4 in zip(lMemberID, lName, lAddr, lTel):
        listMemberID.insert(END, item1)
        listName.insert(END, item2)
        listAddr.insert(END, item3)
        listTel.insert(END, item4)

    conn.close()

# 돌아가기
def backFrame():
    editFrame.pack()
    listFrame.pack_forget()


window = Tk()
window.geometry("900x300")
window.title("회원정보")

editFrame = Frame(window)
editFrame.pack()

listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

label1 = Label(editFrame, text ="회원 ID")
label1.pack(side=LEFT, padx=10, pady=10)

edt1 = Entry(editFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)

label2 = Label(editFrame, text ="회원명")
label2.pack(side=LEFT, padx=10, pady=10)

edt2 = Entry(editFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)

label3 = Label(editFrame, text ="주소")
label3.pack(side=LEFT, padx=10, pady=10)

edt3 = Entry(editFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)

label4 = Label(editFrame, text ="폰번호")
label4.pack(side=LEFT, padx=10, pady=10)

edt4 = Entry(editFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

# 버튼
btnInsert = Button(editFrame, text ="입력", command = insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

btnSelect = Button(editFrame, text ="조회", command = selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

btnSelectAll = Button(editFrame, text ="전체 조회", command = selectAllData)
btnSelectAll.pack(side=LEFT, padx=10, pady=10)

btnDelete = Button(editFrame, text ="삭제", command = deleteData)
btnDelete.pack(side=LEFT, padx=10, pady=10)

listMemberID = Listbox(listFrame)
listMemberID.pack(side=LEFT, fill=BOTH, expand=1)

listName = Listbox(listFrame)
listName.pack(side=LEFT, fill=BOTH, expand=1)

listAddr = Listbox(listFrame)
listAddr.pack(side=LEFT, fill=BOTH, expand=1)

listTel = Listbox(listFrame)
listTel.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()