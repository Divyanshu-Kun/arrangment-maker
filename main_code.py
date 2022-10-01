import pickle
from random import randrange
from tkinter import *
from tkinter import messagebox
root=Tk()


def clicked1():#To add an entry of teacher

    def done():#To moe the data rom on schreen to files

        if name.get()=="":#checking if a name is  present
            messagebox.showwarning(detail="Name field can not be empty")
        else:#if name is present addind the timetable to the files
            content=[name.get(),
            [entry_row_2_1.get(),entry_row_2_2.get(),entry_row_2_3.get(),entry_row_2_4.get(),entry_row_2_5.get(),entry_row_2_6.get(),entry_row_2_7.get(),entry_row_2_8.get()],
            [entry_row_3_1.get(),entry_row_3_2.get(),entry_row_3_3.get(),entry_row_3_4.get(),entry_row_3_5.get(),entry_row_3_6.get(),entry_row_3_7.get(),entry_row_3_8.get()],
            [entry_row_4_1.get(),entry_row_4_2.get(),entry_row_4_3.get(),entry_row_4_4.get(),entry_row_4_5.get(),entry_row_4_6.get(),entry_row_4_7.get(),entry_row_4_8.get()],
            [entry_row_5_1.get(),entry_row_5_2.get(),entry_row_5_3.get(),entry_row_5_4.get(),entry_row_5_5.get(),entry_row_5_6.get(),entry_row_5_7.get(),entry_row_5_8.get()],
            [entry_row_6_1.get(),entry_row_6_2.get(),entry_row_6_3.get(),entry_row_6_4.get(),entry_row_6_5.get(),entry_row_6_6.get(),entry_row_6_7.get(),entry_row_6_8.get()],
            [entry_row_7_1.get(),entry_row_7_2.get(),entry_row_7_3.get(),entry_row_7_4.get(),entry_row_7_5.get(),entry_row_7_6.get(),entry_row_7_7.get(),entry_row_7_8.get()],
            ]
            file=open(r".\Teacher_Records.bin","rb")

            try:
                full_thing=pickle.load(file)
            except EOFError:
                full_thing=[]
            file.close()

            full_thing.append(content)
            
            file=open(r".\Teacher_Records.bin","wb")
            

            
            pickle.dump(full_thing,file)


            file.close()

            choice=messagebox.askyesno("Record Added","Recoed Added . Add New Records ?")
            if choice==1:
                teacher_detail_add.destroy()
                clicked1()
            elif choice==0:
                teacher_detail_add.destroy()
            #Data added to files


    #Making the layout of  adding teachers data

    teacher_detail_add=Toplevel()
    label1=Label(teacher_detail_add,text="Enter teacher name ",padx=300).grid(row=0,column=0)
    name=Entry(teacher_detail_add)
    name.grid(row=1,column=0)
    button1=Button(teacher_detail_add,text="Add details",command=done).grid(row=1,column=1)
    label2=Label(teacher_detail_add,text="Enter the class with section separarted by a dash (-)").grid(row=2,column=0)
    label3=Label(teacher_detail_add,text="If the teacher doesn\'t have a class just enter dash(-) ").grid(row=3,column=0)

    row1=LabelFrame(teacher_detail_add,padx=10)
    
    #First line

    label_row_1_0=Label(row1,text="\t     ").grid(row=0,column=0)
    label_row_1_1=Label(row1,text="    I    ").grid(row=0,column=1)
    label_row_1_2=Label(row1,text="    II   ").grid(row=0,column=2)
    label_row_1_3=Label(row1,text="   III   ").grid(row=0,column=3)
    label_row_1_4=Label(row1,text="    IV   ").grid(row=0,column=4)
    label_row_1_5=Label(row1,text="    V    ").grid(row=0,column=5)
    label_row_1_6=Label(row1,text="    VI   ").grid(row=0,column=6)
    label_row_1_7=Label(row1,text="   VII   ").grid(row=0,column=7)
    label_row_1_8=Label(row1,text="   VIII  ").grid(row=0,column=8)
    
    lst=['   Monday   ',"   Tuesday   ",'Wednesday','  Thrusday  ','    Friday     ','  Saturday   ']

    #Monday
    
    label_row_2_0=Label(row1,text=lst[0]).grid(row=1,column=0)
    entry_row_2_1=Entry(row1)
    entry_row_2_1.grid(row=1,column=1)
    entry_row_2_2=Entry(row1)
    entry_row_2_2.grid(row=1,column=2)
    entry_row_2_3=Entry(row1)
    entry_row_2_3.grid(row=1,column=3)
    entry_row_2_4=Entry(row1)
    entry_row_2_4.grid(row=1,column=4)
    entry_row_2_5=Entry(row1)
    entry_row_2_5.grid(row=1,column=5)
    entry_row_2_6=Entry(row1)
    entry_row_2_6.grid(row=1,column=6)
    entry_row_2_7=Entry(row1)
    entry_row_2_7.grid(row=1,column=7)
    entry_row_2_8=Entry(row1)
    entry_row_2_8.grid(row=1,column=8)

    #Tuesday

    label_row_3_0=Label(row1,text=lst[1]).grid(row=2,column=0)
    entry_row_3_1=Entry(row1)
    entry_row_3_1.grid(row=2,column=1)
    entry_row_3_2=Entry(row1)
    entry_row_3_2.grid(row=2,column=2)
    entry_row_3_3=Entry(row1)
    entry_row_3_3.grid(row=2,column=3)
    entry_row_3_4=Entry(row1)
    entry_row_3_4.grid(row=2,column=4)
    entry_row_3_5=Entry(row1)
    entry_row_3_5.grid(row=2,column=5)
    entry_row_3_6=Entry(row1)
    entry_row_3_6.grid(row=2,column=6)
    entry_row_3_7=Entry(row1)
    entry_row_3_7.grid(row=2,column=7)
    entry_row_3_8=Entry(row1)
    entry_row_3_8.grid(row=2,column=8)

    #Wesnesday

    label_row_4_0=Label(row1,text=lst[2]).grid(row=3,column=0)
    entry_row_4_1=Entry(row1)
    entry_row_4_1.grid(row=3,column=1)
    entry_row_4_2=Entry(row1)
    entry_row_4_2.grid(row=3,column=2)
    entry_row_4_3=Entry(row1)
    entry_row_4_3.grid(row=3,column=3)
    entry_row_4_4=Entry(row1)
    entry_row_4_4.grid(row=3,column=4)
    entry_row_4_5=Entry(row1)
    entry_row_4_5.grid(row=3,column=5)
    entry_row_4_6=Entry(row1)
    entry_row_4_6.grid(row=3,column=6)
    entry_row_4_7=Entry(row1)
    entry_row_4_7.grid(row=3,column=7)
    entry_row_4_8=Entry(row1)
    entry_row_4_8.grid(row=3,column=8)

    #Thrusday

    label_row_5_0=Label(row1,text=lst[3]).grid(row=4,column=0)
    entry_row_5_1=Entry(row1)
    entry_row_5_1.grid(row=4,column=1)
    entry_row_5_2=Entry(row1)
    entry_row_5_2.grid(row=4,column=2)
    entry_row_5_3=Entry(row1)
    entry_row_5_3.grid(row=4,column=3)
    entry_row_5_4=Entry(row1)
    entry_row_5_4.grid(row=4,column=4)
    entry_row_5_5=Entry(row1)
    entry_row_5_5.grid(row=4,column=5)
    entry_row_5_6=Entry(row1)
    entry_row_5_6.grid(row=4,column=6)
    entry_row_5_7=Entry(row1)
    entry_row_5_7.grid(row=4,column=7)
    entry_row_5_8=Entry(row1)
    entry_row_5_8.grid(row=4,column=8)

    #Friday

    label_row_6_0=Label(row1,text=lst[4]).grid(row=5,column=0)
    entry_row_6_1=Entry(row1)
    entry_row_6_1.grid(row=5,column=1)
    entry_row_6_2=Entry(row1)
    entry_row_6_2.grid(row=5,column=2)
    entry_row_6_3=Entry(row1)
    entry_row_6_3.grid(row=5,column=3)
    entry_row_6_4=Entry(row1)
    entry_row_6_4.grid(row=5,column=4)
    entry_row_6_5=Entry(row1)
    entry_row_6_5.grid(row=5,column=5)
    entry_row_6_6=Entry(row1)
    entry_row_6_6.grid(row=5,column=6)
    entry_row_6_7=Entry(row1)
    entry_row_6_7.grid(row=5,column=7)
    entry_row_6_8=Entry(row1)
    entry_row_6_8.grid(row=5,column=8)

    #Saturday

    label_row_7_0=Label(row1,text=lst[5]).grid(row=6,column=0)
    entry_row_7_1=Entry(row1)
    entry_row_7_1.grid(row=6,column=1)
    entry_row_7_2=Entry(row1)
    entry_row_7_2.grid(row=6,column=2)
    entry_row_7_3=Entry(row1)
    entry_row_7_3.grid(row=6,column=3)
    entry_row_7_4=Entry(row1)
    entry_row_7_4.grid(row=6,column=4)
    entry_row_7_5=Entry(row1)
    entry_row_7_5.grid(row=6,column=5)
    entry_row_7_6=Entry(row1)
    entry_row_7_6.grid(row=6,column=6)
    entry_row_7_7=Entry(row1)
    entry_row_7_7.grid(row=6,column=7)
    entry_row_7_8=Entry(row1)
    entry_row_7_8.grid(row=6,column=8)

    row1.grid(row=4,column=0)





def clicked2():#If the user decides to generate a timetable


    def generate():#Actual logic behind generation
        
        day=(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"].index(clicked.get())+1)



        absent_teachers=e1.get().split(",")
        absent_teacher_lst=[]
        for i in absent_teachers:
            file=open(r".\Teacher_Records.bin","rb")
            content=pickle.load(file)
            absent_teacher_lst.append(content.pop(int(i)-2+1))
            file.close()
        file=open(r".\Teacher_Records.bin","rb")
        content=pickle.load(file)

        file.close()
        
        for i in absent_teacher_lst:
            content.remove(i)




        spots_to_fill={}
        for i in absent_teacher_lst:
            spots_to_fill[i[0]]=i[day]
        
        present_teachers={}
        for  i in content:
            present_teachers[i[0]]=i[day]
        
        teacher_at_disposal=[[],[],[],[],[],[],[],[]]

        for i in present_teachers:
            for j in range(len(present_teachers[i])):
                if present_teachers[i][j]=='-':
                    teacher_at_disposal[j].append(i)
        

        #Printing and rest of the logic

        arrangement=Toplevel()
        row1=LabelFrame(arrangement,padx=10)
        label_row_1_0=Label(row1,text="Teacher's name").grid(row=0,column=0)
        label_decoration_vertical_1=Label(row1,text="||").grid(row=0,column=1)
        label_row_1_1=Label(row1,text="    I    ").grid(row=0,column=2)
        label_decoration_vertical_1=Label(row1,text="||").grid(row=0,column=3)
        label_row_1_2=Label(row1,text="    II   ").grid(row=0,column=4)
        label_decoration_vertical_1=Label(row1,text="||").grid(row=0,column=5)
        label_row_1_3=Label(row1,text="   III   ").grid(row=0,column=6)
        label_decoration_vertical_1=Label(row1,text="||").grid(row=0,column=7)
        label_row_1_4=Label(row1,text="    IV   ").grid(row=0,column=8)
        label_decoration_vertical_1=Label(row1,text="||").grid(row=0,column=9)
        label_row_1_5=Label(row1,text="    V    ").grid(row=0,column=10)
        label_decoration_vertical_1=Label(row1,text="||").grid(row=0,column=11)
        label_row_1_6=Label(row1,text="    VI   ").grid(row=0,column=12)
        label_decoration_vertical_1=Label(row1,text="||").grid(row=0,column=13)
        label_row_1_7=Label(row1,text="   VII   ").grid(row=0,column=14)
        label_decoration_vertical_1=Label(row1,text="||").grid(row=0,column=15)
        label_row_1_8=Label(row1,text="   VIII  ").grid(row=0,column=16)
        label_decoration_vertical_1=Label(row1,text="||").grid(row=0,column=17)
        label_decoration_horizontal_1=Label(row1,text="").grid(row=1,column=0)
        for k in range(1,18,2):
                    label_decoration_vertical_2=Label(row1,text="||").grid(row=1,column=k)
        position=2
        for i  in spots_to_fill:
            name_label=Label(row1,text=i).grid(row=position,column=0)
            label_decoration_vertical_1=Label(row1,text="||").grid(row=position,column=1)
            label_decoration_horizontal_1=Label(row1,text="").grid(row=position+1,column=0)
            for k in range(1,18,2):
                    label_decoration_vertical_2=Label(row1,text="||").grid(row=position+1,column=k)
            temp=1
            period_position=2
            for j in spots_to_fill[i]:
                if j=="-":
                    arrangement_label=Label(row1,text="-").grid(row=position,column=period_position)
                    label_decoration_vertical_1=Label(row1,text="||").grid(row=position,column=period_position+1)
                    label_decoration_horizontal_1=Label(row1,text="").grid(row=position+1,column=period_position)
                    for k in range(1,18,2):
                        label_decoration_vertical_2=Label(row1,text="||").grid(row=position+1,column=k)
                elif len(teacher_at_disposal[temp-1])==0:
                    arrangement_label=Label(row1,text="S Mishra"+"("+j+")").grid(row=position,column=period_position)
                    label_decoration_vertical_1=Label(row1,text="||").grid(row=position,column=period_position+1)
                    label_decoration_horizontal_1=Label(row1,text="").grid(row=position+1,column=period_position)
                    for k in range(1,18,2):
                        label_decoration_vertical_2=Label(row1,text="||").grid(row=position+1,column=k)
                else:
                    seleted_teacher=teacher_at_disposal[temp-1].pop(randrange(len(teacher_at_disposal[temp-1])))
                    arrangement_label=Label(row1,text=seleted_teacher+"("+j+")").grid(row=position,column=period_position)
                    label_decoration_vertical_1=Label(row1,text="||").grid(row=position,column=period_position+1)
                    label_decoration_horizontal_1=Label(row1,text="").grid(row=position+1,column=period_position)
                    for k in range(1,18,2):
                        label_decoration_vertical_2=Label(row1,text="||").grid(row=position+1,column=k)
                    
                
                temp+=1
                period_position+=2

               
            

            position+=2



        row1.pack()
        



        

        

        


    #Choice winndow od second option

    show_arrangements=Toplevel()
    label1=Label(show_arrangements,text='From The following list enter the serial number of absent teachers separated by a comma ').grid(row=0,column=0)
    frame1=LabelFrame(show_arrangements)
    label2=Label(frame1,text="Serial number").grid(row=0,column=0)
    label3=Label(frame1,text="Name").grid(row=0,column=1)
    options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    clicked = StringVar()
    clicked.set( "Monday" )
    drop = OptionMenu( show_arrangements , clicked , *options )
    drop.grid(row=1,column=0)

    file=open(r".\Teacher_Records.bin","rb")



    
    content=pickle.load(file)
    if  len(content)==0:
        choice2=messagebox.askquestion("No Records Found","Add new records ?")
        if choice2=="yes":
            show_arrangements.destroy()
            clicked1()
        else:
            show_arrangements.destroy()
            





    i=1
    for record in content:
            label4=Label(frame1,text=str(i)).grid(row=i,column=0)
            label5=Label(frame1,text=record[0]).grid(row=i,column=1)
            i+=1

    frame1.grid(row=2,column=0,sticky=E+W)


    e1=Entry(show_arrangements,width=50)
    e1.grid(row=3,column=0)

    buttonn1=Button(show_arrangements,text="Generate timetalbe :",command=generate).grid(row=3,column=1)





















    
def clicked3():#To delete a record


    def delete_record():
        
        #Asking for conformation and deleting data of seleted teacher 

        to_delete=int(e.get())
        file=open(r".\Teacher_Records.bin","rb")

        original=pickle.load(file)

        file.close()


        choice=messagebox.askyesno("canformation for deletion ","are you sure you want to delete "+original[to_delete-1][0]+"\'s record")
        if choice==1:
            original.pop(to_delete-1)

            file=open(r".\Teacher_Records.bin","wb")
            

            
            pickle.dump(original,file)


            file.close()
            teacher_detail_delete.destroy()
            clicked3()


        

    #Checking if there is any data in the file...and checking other stuff to show error for
    #Making the frameforrk for the third window

    teacher_detail_delete=Toplevel()
    label1=Label(teacher_detail_delete,text="These are the name of teacher whose records have been added : ").grid(row=0,column=0)
    frame1=LabelFrame(teacher_detail_delete)
    label2=Label(frame1,text="Serial number").grid(row=0,column=0)
    label3=Label(frame1,text="Name").grid(row=0,column=1)
    file=open(r".\Teacher_Records.bin","rb")



    
    content=pickle.load(file)
    if  len(content)==0:
        choice2=messagebox.askquestion("No Records Found","Add new records ?")
        if choice2=="yes":
            teacher_detail_delete.destroy()
            clicked1()
        else:
            teacher_detail_delete.destroy()
            





    i=1
    for record in content:
            label4=Label(frame1,text=str(i)).grid(row=i,column=0)
            label5=Label(frame1,text=record[0]).grid(row=i,column=1)
            i+=1

    frame1.grid(row=3,column=0,sticky=E+W)

    label6=Label(teacher_detail_delete,text="enter the serial number of the teacher whose data  you want to delete").grid(row=4,column=0)
    e=Entry(teacher_detail_delete)
    e.grid(row=5,column=0)

    button1=Button(teacher_detail_delete,text="DELETE !!!",command=delete_record).grid(row=5,column=1)
    file.close()

def clicked4():
    edit_teacher_detial=Toplevel()

    row1=LabelFrame(edit_teacher_detial,padx=10)
    
    options = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    clicked = StringVar()
    clicked.set( "Monday" )
    drop = OptionMenu( edit_teacher_detial , clicked , *options )

    name=Entry(edit_teacher_detial)
    name.grid(row=1,column=0)
    #button1=Button(edit_teacher_detial,text="Edit details",command=done).grid(row=1,column=1)
    

    
    
    #First line

    label_row_1_0=Label(row1,text="\t     ").grid(row=0,column=0)
    label_row_1_1=Label(row1,text="    I    ").grid(row=0,column=1)
    label_row_1_2=Label(row1,text="    II   ").grid(row=0,column=2)
    label_row_1_3=Label(row1,text="   III   ").grid(row=0,column=3)
    label_row_1_4=Label(row1,text="    IV   ").grid(row=0,column=4)
    label_row_1_5=Label(row1,text="    V    ").grid(row=0,column=5)
    label_row_1_6=Label(row1,text="    VI   ").grid(row=0,column=6)
    label_row_1_7=Label(row1,text="   VII   ").grid(row=0,column=7)
    label_row_1_8=Label(row1,text="   VIII  ").grid(row=0,column=8)
    
    lst=['   Monday   ',"   Tuesday   ",'Wednesday','  Thrusday  ','    Friday     ','  Saturday   ']

    #Monday
    
    label_row_2_0=Label(row1,text=lst[0]).grid(row=1,column=0)
    entry_row_2_1=Entry(row1)
    entry_row_2_1.grid(row=1,column=1)
    entry_row_2_2=Entry(row1)
    entry_row_2_2.grid(row=1,column=2)
    entry_row_2_3=Entry(row1)
    entry_row_2_3.grid(row=1,column=3)
    entry_row_2_4=Entry(row1)
    entry_row_2_4.grid(row=1,column=4)
    entry_row_2_5=Entry(row1)
    entry_row_2_5.grid(row=1,column=5)
    entry_row_2_6=Entry(row1)
    entry_row_2_6.grid(row=1,column=6)
    entry_row_2_7=Entry(row1)
    entry_row_2_7.grid(row=1,column=7)
    entry_row_2_8=Entry(row1)
    entry_row_2_8.grid(row=1,column=8)

    #Tuesday

    label_row_3_0=Label(row1,text=lst[1]).grid(row=2,column=0)
    entry_row_3_1=Entry(row1)
    entry_row_3_1.grid(row=2,column=1)
    entry_row_3_2=Entry(row1)
    entry_row_3_2.grid(row=2,column=2)
    entry_row_3_3=Entry(row1)
    entry_row_3_3.grid(row=2,column=3)
    entry_row_3_4=Entry(row1)
    entry_row_3_4.grid(row=2,column=4)
    entry_row_3_5=Entry(row1)
    entry_row_3_5.grid(row=2,column=5)
    entry_row_3_6=Entry(row1)
    entry_row_3_6.grid(row=2,column=6)
    entry_row_3_7=Entry(row1)
    entry_row_3_7.grid(row=2,column=7)
    entry_row_3_8=Entry(row1)
    entry_row_3_8.grid(row=2,column=8)

    #Wesnesday

    label_row_4_0=Label(row1,text=lst[2]).grid(row=3,column=0)
    entry_row_4_1=Entry(row1)
    entry_row_4_1.grid(row=3,column=1)
    entry_row_4_2=Entry(row1)
    entry_row_4_2.grid(row=3,column=2)
    entry_row_4_3=Entry(row1)
    entry_row_4_3.grid(row=3,column=3)
    entry_row_4_4=Entry(row1)
    entry_row_4_4.grid(row=3,column=4)
    entry_row_4_5=Entry(row1)
    entry_row_4_5.grid(row=3,column=5)
    entry_row_4_6=Entry(row1)
    entry_row_4_6.grid(row=3,column=6)
    entry_row_4_7=Entry(row1)
    entry_row_4_7.grid(row=3,column=7)
    entry_row_4_8=Entry(row1)
    entry_row_4_8.grid(row=3,column=8)

    #Thrusday

    label_row_5_0=Label(row1,text=lst[3]).grid(row=4,column=0)
    entry_row_5_1=Entry(row1)
    entry_row_5_1.grid(row=4,column=1)
    entry_row_5_2=Entry(row1)
    entry_row_5_2.grid(row=4,column=2)
    entry_row_5_3=Entry(row1)
    entry_row_5_3.grid(row=4,column=3)
    entry_row_5_4=Entry(row1)
    entry_row_5_4.grid(row=4,column=4)
    entry_row_5_5=Entry(row1)
    entry_row_5_5.grid(row=4,column=5)
    entry_row_5_6=Entry(row1)
    entry_row_5_6.grid(row=4,column=6)
    entry_row_5_7=Entry(row1)
    entry_row_5_7.grid(row=4,column=7)
    entry_row_5_8=Entry(row1)
    entry_row_5_8.grid(row=4,column=8)

    #Friday

    label_row_6_0=Label(row1,text=lst[4]).grid(row=5,column=0)
    entry_row_6_1=Entry(row1)
    entry_row_6_1.grid(row=5,column=1)
    entry_row_6_2=Entry(row1)
    entry_row_6_2.grid(row=5,column=2)
    entry_row_6_3=Entry(row1)
    entry_row_6_3.grid(row=5,column=3)
    entry_row_6_4=Entry(row1)
    entry_row_6_4.grid(row=5,column=4)
    entry_row_6_5=Entry(row1)
    entry_row_6_5.grid(row=5,column=5)
    entry_row_6_6=Entry(row1)
    entry_row_6_6.grid(row=5,column=6)
    entry_row_6_7=Entry(row1)
    entry_row_6_7.grid(row=5,column=7)
    entry_row_6_8=Entry(row1)
    entry_row_6_8.grid(row=5,column=8)

    #Saturday

    label_row_7_0=Label(row1,text=lst[5]).grid(row=6,column=0)
    entry_row_7_1=Entry(row1)
    entry_row_7_1.grid(row=6,column=1)
    entry_row_7_2=Entry(row1)
    entry_row_7_2.grid(row=6,column=2)
    entry_row_7_3=Entry(row1)
    entry_row_7_3.grid(row=6,column=3)
    entry_row_7_4=Entry(row1)
    entry_row_7_4.grid(row=6,column=4)
    entry_row_7_5=Entry(row1)
    entry_row_7_5.grid(row=6,column=5)
    entry_row_7_6=Entry(row1)
    entry_row_7_6.grid(row=6,column=6)
    entry_row_7_7=Entry(row1)
    entry_row_7_7.grid(row=6,column=7)
    entry_row_7_8=Entry(row1)
    entry_row_7_8.grid(row=6,column=8)

    row1.grid(row=4,column=0)







    
    

frame1=LabelFrame(root,padx=200,pady=45)
frame2=LabelFrame(root,padx=200,pady=45)
frame3=LabelFrame(root,padx=200,pady=45)
frame4=LabelFrame(root,padx=200,pady=45)

but1=Button(frame1,text='Add teacher details',command=clicked1).grid(row=0,column=0,padx=10)
frame1.grid(row=0,column=0)
but2=Button(frame2,text='Show Arrangements',command=clicked2).grid(row=0,column=0,padx=7)
frame2.grid(row=1,column=0)
but3=Button(frame3,text='Delete teacher details',command=clicked3).grid(row=0,column=0,padx=4.5)
frame3.grid(row=2,column=0)
but4=Button(frame4,text='Edit teacher details',command=clicked4).grid(row=0,column=0,padx=11)
frame4.grid(row=3,column=0)


mainloop()
