from tkinter import *
root = Tk()
root.title("FUTOSHIKI PUZZLE")
root.geometry("800x500")
puzzle1 = []
puzzle2 = []
#function for structure
def futo_puzzle(puzzle,logic):
    for i,ele in enumerate(logic):
        if i%2 == 0:
            line = ""
            for j in range(len(puzzle[i // 2])-1):
                line += "{n}{l:1}".format(n=puzzle[i // 2][j],l = ele[j])
            line += "{}".format(puzzle[i // 2][-1])
            print(line)
        else:
            line = ""
            for l in range(len(ele)):
                line += "{:1}".format(ele[l])
            print(line)
    return True            

def check_answer(n,puzzle):
    for j in range(n):
        p = [row[j] for row in puzzle]

        if(len(p)!=len(set(p))):
            return False

    for k in range(n):
        m=puzzle[k]
        
        if(len(m)!=len(set(m))):
            return False

    if n == 4:
        if (puzzle[0][0]>puzzle[0][1]) and (puzzle[0][2]<puzzle[0][3]) and (puzzle[1][3]<puzzle[2][3]) and (puzzle[2][1]>puzzle[2][2]):
            return True
    elif n == 5:
        if(puzzle[0][1]<puzzle[1][1]) and (puzzle[2][2]>puzzle[2][3]) and (puzzle[3][2]<puzzle[4][2]):
            return True

def level1():  
    my_entries = []
    index=0
    for y in range(4):
        my_entries.append([])
    for y in range(8):
        if(y%2!=0):
            index+=1
        for x in range(8):
            my_entry = Entry(root,width=2)
            my_entry.grid(row=y,column=x,pady=2,padx=2)
            if(y%2!=0 and x%2!=0):
                my_entries[y-index].append(my_entry)
            #my_label=Label(root,text='')
            #my_label.grid(row=15,column=1,pady=20)
            if(y==1 and x==2):
                logic_label = Label(root,text="  >  ")
                logic_label.grid(row=y,column=x)
            elif(y==1 and x==6):
                logic_label = Label(root,text="  <  ")
                logic_label.grid(row=y,column=x)
            elif(y==4 and x==7):
                logic_label = Label(root,text="  ^ ")
                logic_label.grid(row=y,column=x) 
            elif(y==5 and x==4):
                logic_label = Label(root,text="  > ")
                logic_label.grid(row=y,column=x)
            elif(y%2==0 or x%2==0):
                logic_label = Label(root,text="     ")
                logic_label.grid(row=y,column=x,pady=2,padx=2)
                
    def input():
        for i in range(0,4):
            row = []
            for j in range(0,4):
                row.append(my_entries[i][j].get())
            puzzle1.append(row)              
        logic = [
    [">"," ","<"],
    [" "," "," "," "],

    [" "," "," "],
    ["  ","  ","  ","^"],

    [" ",">"," "],
    [" "," "," "," "],

    [" "," "," "],
    [" "," "," "," "]]
        
        futo_puzzle(puzzle1,logic)
        n = 4
        if check_answer(n,puzzle1):
            print("Correct")
            res_label=Label(root,text="Correct!")
            res_label.grid(row=15,column=13,pady=20)
        else:
            print("Incorrect")
            res_label=Label(root,text="InCorrect!")
            res_label.grid(row=15,column=13,pady=20)

        def remove_text():
            res_label.config(text='')

        puzzle1.clear()

        clear=Button(root,text="CLEAR",command=remove_text)
        clear.grid(row=14,column=21,pady=20,padx=10)

    my_button=Button(root,text="SUBMIT",command=input)
    my_button.grid(row=14,column=19,pady=20,padx=10)
        
lvl1b=Button(root,text="EASY 4X4",command=level1)
lvl1b.grid(row=14,column=13,pady=20,padx=10)
     
def level2():
    my_entries = []
    index=0
    for y in range(5):
        my_entries.append([])
    for y in range(10):
        if(y%2!=0):
            index+=1
        for x in range(10):
            my_entry = Entry(root,width=2)
            my_entry.grid(row=y,column=x,pady=2,padx=2)
            if(y%2!=0 and x%2!=0):
                my_entries[y-index].append(my_entry)
            my_label=Label(root,text='')
            my_label.grid(row=15,column=1,pady=20)
            if(y==2 and x==3):
                logic_label = Label(root,text="  ^  ")
                logic_label.grid(row=y,column=x)
            elif(y==5 and x==6):
                logic_label = Label(root,text="  >  ")
                logic_label.grid(row=y,column=x)
            elif(y==8 and x==5):
                logic_label = Label(root,text="  ^ ")
                logic_label.grid(row=y,column=x) 
            elif(y%2==0 or x%2==0):
                logic_label = Label(root,text="     ")
                logic_label.grid(row=y,column=x,pady=2,padx=2)
    def input():
         for i in range(0,5):
            row = []
            for j in range(0,5):
                row.append(my_entries[i][j].get())
            puzzle2.append(row)
         logic = [
    [" ", " ", " ", " "],
    ["  ", "^", "  ", " ", " "],
   
    [" ", " ", " ", " "],
    ["  ", "  ", " ", " ", " "],
   
    [" ", " ", ">", " "],
    ["  ", "  ", "  ", " ", " "],
   
    [" ", " ", " ", " "],
    ["  ", "  ", "^", " ", " "],

    [" ", " ", " ", " "],
    [" ", " ", " ", " ", " "],]
         futo_puzzle(puzzle2,logic)
         n = 5

         if check_answer(n,puzzle2):
            print("Correct")
            res_label=Label(root,text="Correct!")
            res_label.grid(row=15,column=13,pady=20)
         else:
            print("Incorrect")
            res_label=Label(root,text="InCorrect!")
            res_label.grid(row=15,column=13,pady=20)

         puzzle2.clear()

         def remove_text():
            res_label.config(text='')

         clear=Button(root,text="CLEAR",command=remove_text)
         clear.grid(row=14,column=21,pady=20,padx=10)

    my_button=Button(root,text="SUBMIT",command=input)
    my_button.grid(row=14,column=19,pady=20,padx=10)

lvl2b=Button(root,text="HARD 5X5",command=level2)
lvl2b.grid(row=14,column=15,pady=20,padx=10)

root.mainloop()
