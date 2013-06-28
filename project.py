#!/usr/bin/python

from Tkinter import *
from easygui import *
from tkMessageBox import askyesno, showerror
import time
import math

def new():
    y=boolbox(msg='Do you want to save?', title='Save', choices=('Yes', 'No'))
    if y==1:
        savefile()
    else:
        update()
    
def openfile():
    path=fileopenbox(msg='Open ')
    print path
    fopen=open(path,'r+')
    var=fopen.read()
    obj_list=eval(var)
    #print obj_list   
  
    for i in range(len(obj_list)):
        xy=obj_list[i][0]
        if obj_list[i][2]=='connector':
            canvas.create_line(xy,tag='connector',activewidth=2)
        elif obj_list[i][2]=='7_seg':
            canvas.create_polygon(xy, outline='black', tag='7_seg',activewidth=2, fill='light blue',activefill='light yellow')
        else:
            canvas.create_polygon(xy,outline='black',tag='not',fill='white',activewidth=2, activefill='light yellow')
    return
        
def savefile():
    temp_id=canvas.find(ALL)
    for i in range(len(temp_id)):
        temp_name=canvas.gettags(temp_id[i])
        temp_cords=canvas.coords(temp_id[i])
        obj_list.append([ temp_cords,temp_id[i],temp_name[0] ])
        
    var= obj_list
    var=str(var)
    path=filesavebox(msg='save file : ')
    fsave=open(path,'w')
    fsave.write(var)
    fsave.close()
    
    return

def and_eg():
    canvas.bind('<Double-1>', And)
    return 0

def or_eg():
    canvas.bind('<Double-1>', Or)
    return 0

def not_eg():
    canvas.bind('<Double-1>', Not)
    return 0

def Not(event):
    x=event.x;y=event.y
    xy=[x+10,y, x-10,y, x-15,y-5, x-20,y, x-35,y-15, x-35,y-5, x-35,y, x-55,y,
        x-35,y, x-35, y+15, x-20,y, x-15,y+5, x-10,y]
    object_not=canvas.create_polygon(xy,outline='black',tag='not',fill='white',
                                     activewidth=2, activefill='light yellow')
    not_gates_id.append(object_not)
    no_not=len(not_gates_id)
    #print not_gates_id
    return 

def Or(event):
    x=event.x;y=event.y
    xy=[x+25,y, x,y, x-15,y-20, x-35,y-20, x-28,y-10, x-50,y-10,
        x-28,y-10, x-20,y, x-28,y+10, x-50,y+10, x-28,y+10,x-35,y+20, x-15,y+20, x,y]
    object_or=canvas.create_polygon(xy, outline='black', tag='or', fill='white',
                                    activewidth=2, activefill='light yellow')
    or_gates_id.append(object_or)
    no_or=len(or_gates_id)
    #print or_gates_id
    return 
    
def And(event):
    x=event.x;y=event.y
    xy=[x-15,y, x-50,y, x-57,y-13, x-70,y-23, x-80,y-23, x-80,y-13, x-110,y-13, x-80,y-13,
        x-80,y+13, x-110,y+13, x-80,y+13, x-80,y+23, x-70,y+23, x-57,y+13, x-50,y]
    object_and=canvas.create_polygon(xy, outline='black', tag='and', fill='white',
                                     activewidth=2, activefill='light yellow')
    and_gates_id.append(object_and)
    no_and=len(and_gates_id)
    #print and_gates_id
    return 

def connector():
    canvas.bind("<ButtonPress-2>", point)
    canvas.bind("<ButtonRelease-2>", graph)
    return 0

def distance(x,y,x1,y1):
        #print x,y,x1,y1
        dist=(x-x1)**2+(y-y1)**2
        dist=math.sqrt(dist)
        return dist

def get_point(x,y):
    close=canvas.find_closest(x,y)
    tag_name=canvas.gettags(close)
    #----------CONNECTOR---------#
    if len(tag_name)!=0 and tag_name[0]=='connector':
        cord=canvas.coords(close)
        dist1=distance(x,y, cord[0],cord[1])
        dist2=distance(x,y, cord[4],cord[5])
        if dist1<dist2 and dist1<=15:
            return cord[0],cord[1]
        if dist1>dist2 and dist2<=15:
            return cord[4],cord[5]
        else:
            return x,y
    #--------AND--------#    
    elif len(tag_name)!=0 and tag_name[0]=='and':
        cord=canvas.coords(close)
        dist1=distance(x,y, cord[0],cord[1])
        dist2=distance(x,y, cord[12],cord[13])
        dist3=distance(x,y, cord[18],cord[19])
        if dist1<dist2:
                if dist1<dist3 and dist1<=15:
                    return cord[0],cord[1]
                elif dist1>dist3 and dist3<=15:
                    return cord[18],cord[19]
        elif dist1>dist2:
                if dist2<dist3 and dist2<=15:
                    return cord[12],cord[13]
                elif dist2>dist3 and dist3<=15:
                    return cord[18],cord[19]
        else:
            return x,y
    #-------------OR-------------------#
    elif len(tag_name)!=0 and tag_name[0]=='or':
        cord=canvas.coords(close)
        dist1=distance(x,y, cord[0],cord[1])
        dist2=distance(x,y, cord[10],cord[11])
        dist3=distance(x,y, cord[18],cord[19])
        if dist1<dist2:
            if dist1<dist3 and dist1<=10:
                return cord[0],cord[1]
            elif dist1>dist3 and dist3<=10:
                return cord[18],cord[19]
        elif dist1>dist2:
            if dist2<dist3 and dist2<=10:
                return cord[10],cord[11]
            elif dist2>dist3 and dist3<=10:
                return cord[18],cord[19]
        else:
            return x,y
    #-------------NOT--------------#
    elif len(tag_name)!=0 and tag_name[0]=='not':
        cord=canvas.coords(close)
        dist1=distance(x,y, cord[0],cord[1])
        dist2=distance(x,y, cord[14],cord[15])
        if dist1<dist2 and dist1<=10:
            return cord[0],cord[1]
        elif dist1>dist2 and dist2<=10:
            return cord[14],cord[15]
        else:
            return x,y
    #-----------SEVEN-SEGMENT--------#
    elif len(tag_name)!=0 and tag_name[0]=='7_seg':
        cord=canvas.coords(close)
        dist=distance(x,y,cord[6],cord[7])
        if dist<=10:
            return cord[6],cord[7]
        else:
            return x,y
    #-------------OTHER--------------#
    else:
        return x,y 


#-------------------ALL OBJECTS-------------------------------------#
def all_objects():
        All=canvas.find(ALL)
        for i in range(len(All_obj)):   All_obj.pop()
        for i in range(len(All)):
                x=canvas.gettags(All[i])
                if x[0]!='connector':
                        All_obj.append(All[i])
        #print All_obj
        return

#-----------------------------FINAL CONNECTION OF CONNECTORS------------------#    
def final_connection():
        global con_count
        global con_cords
        global fin_con
        global All_obj
        connection()
        coordinates()
        all_objects()
        if len(con_count)==0:
                print 'Not a single connection!!'
        else:
                for i in range(len(fin_con)):   fin_con.pop()
                for i in range(len(con_count)):
                    fin_con.append([con_count[i]])
                    x_pos=-4;y_pos=-3
                    for k in range(2):
                        x_pos+=4;y_pos+=4
                        for j in range(len(All_obj)):
                            temp=canvas.gettags(All_obj[j])
                            obj_cords=canvas.coords(All_obj[j])
                            if temp[0]=='7_seg' and con_cords[i][x_pos]==obj_cords[6] and con_cords[i][y_pos]==obj_cords[7]:
                                fin_con[i].append((temp[0],All_obj[j]))
                            elif temp[0]=='not':
                                if con_cords[i][x_pos]==obj_cords[14] and con_cords[i][y_pos]==obj_cords[15]:
                                    fin_con[i].append(('not_in',All_obj[j]))
                                elif con_cords[i][x_pos]==obj_cords[0] and con_cords[i][y_pos]==obj_cords[1]:
                                    fin_con[i].append(('not_out',All_obj[j]))
                            elif temp[0]=='or':
                                if con_cords[i][x_pos]==obj_cords[0] and con_cords[i][y_pos]==obj_cords[1]:
                                    fin_con[i].append(('or_out',All_obj[j]))
                                elif con_cords[i][x_pos]==obj_cords[10] and con_cords[i][y_pos]==obj_cords[11]:
                                    fin_con[i].append(('or_in_1',All_obj[j]))
                                elif con_cords[i][x_pos]==obj_cords[18] and con_cords[i][y_pos]==obj_cords[19]:
                                    fin_con[i].append(('or_in_2',All_obj[j]))
                            elif temp[0]=='and':
                                if con_cords[i][x_pos]==obj_cords[0] and con_cords[i][y_pos]==obj_cords[1]:
                                    fin_con[i].append(('and_out',All_obj[j]))
                                elif con_cords[i][x_pos]==obj_cords[12] and obj_cords[13]==con_cords[i][y_pos]:
                                    fin_con[i].append(('and_in_1',All_obj[j]))
                                elif con_cords[i][x_pos]==obj_cords[18] and con_cords[i][y_pos]==obj_cords[19]:
                                    fin_con[i].append(('and_in_2',All_obj[j]))
                            else:
                                """This is the case of the connector,will come to it later"""
                                #print 'one end is free!!'
        for i in range(len(fin_con)):   print fin_con[i]
        return

#-------------------COORDINATES OF CONNECTORS-----------------------------#
def coordinates():
        global All
        connection()
        for i in range(len(con_cords)): con_cords.pop()
        if len(con_count)!=0:
                for i in range(len(con_count)):
                        #print 'con_count[0][i]',con_count[0][i]
                        con_cords.append(canvas.coords(con_count[i]))
                        #print 'con_cords',con_cords
        else:
               print 'Not a single connector?'
        #print con_cords
        return

#---------------------------------MAIN ACTIVATION------------------------------#
def check():
        global fin_con
        global Inputs
        global Outputs
        global sev_seg_id
        global only_gates
        activate()
        final_connection()
        #disp_cord=[]
        temp=[]
        #print only_gates
        #print sev_seg_id
        len_input1=len(Inputs)
        if len(sev_seg_id)!=0 and len(only_gates)!=0 and len(fin_con)!=0:
            #for i in range(len_input1):
            i=0
            while i<=(len(Inputs)-1):
                for j in range(len(fin_con)):
                    if len(Inputs[i])!=3:
                        if Inputs[i][0]==fin_con[j][1][1]:
                            var_name=canvas.gettags(fin_con[j][2][1])
                            var_name=var_name[0]
                            if var_name=='7_seg':
                                if Inputs[i][1]=='not':
                                    Inputs.append([fin_con[j][2][1],var_name,var_name,var_name,Inputs[i][3]])
                                else:
                                    Inputs.append([fin_con[j][2][1],var_name,var_name,var_name,Inputs[i][4]])
                            if var_name=='not':
                                #print 'Entered!! in not'
                                if Inputs[i][1]=='not':
                                    ans=not(Inputs[i][3])
                                    ans=int(ans)
                                    Inputs.append([fin_con[j][2][1],var_name,Inputs[i][3],ans])
                                else:
                                    ans=not(Inputs[i][4])
                                    ans=int(ans)
                                    Inputs.append([fin_con[j][2][1],var_name,Inputs[i][4],ans])
                            elif var_name=='and':
                                if Inputs[i][1]=='not':
                                    ans=not(Inputs[i][3])
                                    ans=int(ans)
                                    Inputs.append([fin_con[j][2][1],var_name,ans])
                                else:
                                    Inputs.append([fin_con[j][2][1],var_name,Inputs[i][4]])
                            elif var_name=='or':
                                if Inputs[i][1]=='not':
                                    ans=not(Inputs[i][3])
                                    ans=int(ans)
                                    Inputs.append([fin_con[j][2][1],var_name,ans])
                                else:
                                    Inputs.append([fin_con[j][2][1],var_name,Inputs[i][4]])    
                    elif len(Inputs[i])==3 and j==0:
                        temp.append(Inputs[i])
                        if len(temp)>1:
                            #print 'Entered 1'
                            x=Inputs[i][2]
                            Inputs.pop()
                            i-=1
                            Inputs[i].append(x)
                            if Inputs[i][1]=='and':
                                #print 'Entered2'
                                ans=Inputs[i][2] and Inputs[i][3]
                            if Inputs[i][1]=='or':
                                ans=Inputs[i][2] or Inputs[i][3]
                            Inputs[i].append(ans)
                print Inputs
                i+=1
            #print Inputs
            #print temp
            
            '''
            a=Inputs[3][2]
            print a
            Inputs.pop()
            Inputs[2].append(a)
            if Inputs[2][1]=='and':
                answ=Inputs[2][2] and Inputs[2][3]
            elif Inputs[2][1]=='or':
                answ=Inputs[2][2] or Inputs[2][3]
            
            Inputs[2].append(answ)
            print Inputs
            Inputs.append(['7_seg',Inputs[2][4]])
            '''
            for i in range(len(Inputs)):
                if Inputs[i][1]=='7_seg':
                    disp_cord=canvas.coords(Inputs[i][0])
                    #print disp_cord
                    if Inputs[i][4]==1:
                        one(disp_cord[0],disp_cord[1])
                    elif Inputs[i][4]==0:
                        zero(disp_cord[0],disp_cord[1])
        else:
            print 'No seven segment is present!!'
                
        return


#--------------------------CONNECTION----------------------------------#
def connection():
        global con_count
        All=canvas.find(ALL)
        #print All
        i=0;
        while(i<=len(All)-1):
                tag=canvas.gettags(All[i])
                a=tag[0]
                if tag[0]=='connector':
                        con_count=[canvas.find_withtag(a)]
                i+=1;
        con_count=con_count[0]
        #print con_count
        return All


def point(event):
    x=event.x;y=event.y
    d_points.append(x)
    d_points.append(y)
    canvas.bind('<Motion>',drag)
    if len(points)==0:
        z=get_point(event.x,event.y)
        if z:
            points.append(z[0])
            points.append(z[1])
        else:
            points.append(event.x)
            points.append(event.y)    
    else:
        points.append(event.x)
        points.append(event.y)
    return points

def drag(event):
    canvas.delete('line')
    canvas.create_line(d_points[0],d_points[1],event.x,event.y, tag='line')
    canvas.unbind('<Motion>')
    canvas.bind('<Motion>',drag)

def graph(event):
    canvas.delete('line')
    canvas.unbind('<Motion>')
    z=get_point(event.x,event.y)
    if z:
        points.append(z[0])
        points.append(z[1])
    else:
        points.append(event.x)
        points.append(event.y)
    l=len(points)
    if l==0:
        showerror('Co-ordinates','Atleast 2 co-ordinates required.\nNone given!')
        return
    if l==2:
        showerror('Co-ordinates','Atleast 2 co-ordinates required.\nOnly one given!')
        points.pop()
        points.pop()
        return
    pos=2
    i=1;temp=0;L=l/2
    while(i<=(L-1)):
        x=points[temp]
        y=points[temp+3]
        points.insert(pos,x)
        points.insert(pos+1,y)
        pos=pos+4
        temp=temp+4
        i+=1
    canvas.delete('line')
    object_line=canvas.create_line(points, tag="connector", activewidth=2)
    connect_gates_id.append(object_line)
    #print 'points=',points
    l=len(points)
    for i in range(l):  points.pop()
    l=len(d_points)
    for i in range(l):  d_points.pop()
    return 

def sev_seg():
    canvas.bind('<Double-1>', display)
    return

def display(event):
    Sx=event.x;Sy=event.y
    #canvas.create_rectangle(Sx,Sy,Sx+36,Sy+48,width=2, fill='Light Yellow')
    object_sev_seg=canvas.create_polygon(Sx,Sy, Sx+36,Sy, Sx+36,Sy+48, Sx-15,Sy+48, Sx,Sy+48, Sx,Sy,
                          fill='light blue', outline='black',
                                         activewidth=2, activefill='light yellow', tag='7_seg')
    #canvas.create_line(Sx,Sy+48,Sx-15,Sy+48, width=2)
    sev_seg_id.append(object_sev_seg)
    #zero(Sx,Sy)
    return 0

def zero(Sx,Sy):
    eight(Sx,Sy)
    canvas.delete('fourth')
    canvas.update()
    return 0

def one(Sx,Sy):
    eight(Sx,Sy)
    canvas.update()
    canvas.delete('first')
    canvas.delete('second')
    canvas.delete('fourth')
    canvas.delete('fifth')
    canvas.delete('seventh')
    return 0


def eight(Sx,Sy):
    #Sx=event.x;Sy=event.y
    #canvas.create_rectangle(Sx,Sy,Sx+36,Sy+48,width=2, fill='Light Yellow')
    canvas.create_line(Sx+8,Sy+7,Sx+28,Sy+7, width=2, tag='first', fill='red')
    canvas.create_line(Sx+8,Sy+10,Sx+8,Sy+22, width=2, tag='second',fill='red')
    canvas.create_line(Sx+28,Sy+10,Sx+28,Sy+22, width=2, tag='third',fill='red')
    canvas.create_line(Sx+10,Sy+24,Sx+26,Sy+24, width=2, tag='fourth',fill='red')
    canvas.create_line(Sx+8,Sy+27,Sx+8,Sy+39, width=2, tag='fifth',fill='red')
    canvas.create_line(Sx+28,Sy+27,Sx+28,Sy+39, width=2, tag='sixth',fill='red')
    canvas.create_line(Sx+9,Sy+42,Sx+27,Sy+42, width=2, tag='seventh',fill='red')
    #canvas.create_line(Sx,Sy+48,Sx-15,Sy+48, width=2)
    return 0

def data():
    #print 'points',points
    print 'and_gates=',and_gates_id
    print 'or_gates=',or_gates_id
    print 'not_gates=',not_gates_id
    print 'connector=',connect_gates_id
    print 'seven_segment',sev_seg_id
    return

def move():
    canvas.bind('<ButtonPress-1>', replace)
    return 0

def replace(event):
    canvas.coords('current',event.x, event.y)
    return 0

def update():
    canvas.delete('all')
    for i in range(len(points)):  points.pop()
    for i in range(len(d_points)):  d_points.pop()
    for i in range(len(and_gates_id)):  and_gates_id.pop()
    for i in range(len(or_gates_id)):  or_gates_id.pop()
    for i in range(len(not_gates_id)):  not_gates_id.pop()
    for i in range(len(connect_gates_id)):  connect_gates_id.pop()
    for i in range(len(sev_seg_id)):    sev_seg_id.pop()
    for i in range(len(Inputs)):    Inputs.pop()
    for i in range(len(Outputs)):    Outputs.pop()
    for i in range(len(fin_con)):   fin_con.pop()
    return 0

def delete():
    canvas.bind('<Double-1>', remove)
    return 0

def remove(event):
    rem_tag=canvas.gettags('current')
    if len(rem_tag)==0:
        showerror('Delete','No item selected')
    else:
        rem_id=canvas.find_withtag('current')
        rem_id=rem_id[0]
        if rem_tag[0]=='and':
            and_gates_id.remove(rem_id)
        elif rem_tag[0]=='or':
            or_gates_id.remove(rem_id)
        elif rem_tag[0]=='not':
            not_gates_id.remove(rem_id)
        elif rem_tag[0]=='connector':
            connect_gates_id.remove(rem_id)
        elif rem_tag[0]=='7_seg':
            sev_seg_id.remove(rem_id)
    canvas.delete('current')
    for i in range(len(d_points)):  d_points.pop()
    return 0

def right_click(event):
    menu.post(event.x_root,event.y_root)
    return 

def Input():
    """
    Inputs_format=[(gate_id, gate_name, input1, input2,output)]
    """
    Tag=canvas.gettags('current')
    if len(Tag)==0:
        showerror('Inputs','No Input can be given because no item is selected!!')
    elif Tag[0]=='connector':
        showerror('Inputs','Inputs can\'t be given to the connector')
    elif Tag[0]=='7_seg':
        showerror('Inputs','Inputs can\'t be given to the Seven Segment')
    else:
        Tag_Id=canvas.find_withtag(Tag[1])
        if Tag[0]=='not':
            A=boolbox('B-Input choose.','Input',choices=('1','0'))
            ans=not A
            Inputs.append([Tag_Id[0],Tag[0],A,int(ans)])
        else:
            A=boolbox('A-Input choose.','Input',choices=('1','0'))
            B=boolbox('B-Input choose.','Input',choices=('1','0'))
            if Tag[0]=='and':
                ans=A and B
            elif Tag[0]=='or':
                ans=A or B
            Inputs.append([Tag_Id[0],Tag[0],A,B,ans])
    #for i in range(len(Inputs)):    print Inputs[i]
    return Inputs


def activate():
    """
    Output_format=[(gate_id, gate_name, output)]
    """
    global Outputs
    global only_gates
    All_obj=[]
    only_gates=[]
    All_obj=canvas.find(ALL)
    for i in range(len(Outputs)):   Outputs.pop()
    for i in range(len(only_gates)):     only_gates.pop()
    for i in range(len(Inputs)):
        if Inputs[i][1]=='not':
            Outputs.append((Inputs[i][0],Inputs[i][1],Inputs[i][3]))
        else:
            Outputs.append((Inputs[i][0],Inputs[i][1],Inputs[i][4]))
    #for i in range(len(Inputs)):    print Inputs[i]
    #for i in range(len(Outputs)):    print Outputs[i]
    for i in range(len(All_obj)):
        temp=canvas.gettags(All_obj[i])
        if temp[0]=='7_seg' or temp[0]=='connector':
            continue
        else:
            only_gates.append([All_obj[i], temp[0]])
    #print 'gates',only_gates
    #print 'Inputs',Inputs
    #print 'outputs',Outputs
    return 0

def callback():
    return 0

def docs():
    root = Tk()
    root.iconbitmap(bitmap='@./_assets/Help.xbm')
    root.title('Electrical Docs')
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(root, yscrollcommand=scrollbar.set)
    s=open('./_assets/docs.txt')
    f=s.read()
    s.close()
    f=f.split('\n');i=0
    while i<=len(f)-1:
        listbox.insert(END, f[i])
        i+=1
    listbox.pack(side=LEFT, fill=BOTH, expand=YES)
    scrollbar.config(command=listbox.yview)
    mainloop()
    return 0


def about():
    win=Tk()
    Label(win, text='This is all about VDT').pack()
    win.mainloop()

def identify(event):
    Id=canvas.gettags('current')
    if len(Id)!=0:
        print Id
        Id=Id[0]
        print canvas.find_withtag(Id)
    return 0

def status(event):
    global ss
    sta_item=canvas.gettags('current')
    if len(sta_item)==0:
        ss='No item selected!!\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tx='
        ss=ss+str(event.x)+'\t\ty='+str(event.y)
    elif sta_item[0]=='and':
        ss='and\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tx='
        ss=ss+str(event.x)+'\t\ty='+str(event.y)
    elif sta_item[0]=='or':
        ss='or\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tx='
        ss=ss+str(event.x)+'\t\ty='+str(event.y)
    elif sta_item[0]=='not':
        ss='not\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tx='
        ss=ss+str(event.x)+'\t\ty='+str(event.y)
    elif sta_item[0]=='connector':
        ss='connector\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tx='
        ss=ss+str(event.x)+'\t\ty='+str(event.y)
    elif sta_item[0]=='7_seg':
        ss='seven segment\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tx='
        ss=ss+str(event.x)+'\t\ty='+str(event.y)
    sts.config(text=ss)
    return 

#----------------------MAIN--------------------#
root=Tk()
root.geometry('400x275+450+250')
root.overrideredirect(1)
canvas=Canvas(bg='light yellow', width=400, height=275)
canvas.pack(expand=YES)

a=0
xy=[10,240,20,260,]
t=['Loading ....','importing gates ..','importing Ic\'s ..','system files..','virtual circuits..','sources..',
   'basic..','transistors..','indicators..','controls..','instruments..','miscellaneous..','initializing vdt..']
photo=PhotoImage(file='./_assets/Ic.gif')
#photo=PhotoImage(file='/media/Sagar/Wallpapers/Icons/ICIC.gif')
canvas.create_image(45,50, image=photo)
canvas.create_rectangle(xy, fill='blue', outline='blue', tag='rect')
canvas.create_text(195,25, text='VIRTUAL DIGITAL TRAINER', font=('Times', 13, 'bold'), fill='purple')
canvas.create_text(220, 65, text='Copyright @ 2011 VIT Projects 2011-2012', font=('verdana', 10))
canvas.create_text(70,90, text='Created by...', font=('verdana', 10), fill='red')
canvas.create_text(190, 110, text='Nisarg Patel, Sanket Sudake, Nikhil Pachpande')
canvas.create_text(190, 125, text='Sourabh Modani, Sagar Rakshe')
canvas.create_text(90,150, text='Under guidance of...', font=('verdana', 10), fill='red')
canvas.create_text(180, 170, text='Prof. Jayesh Bhangdiya', )
canvas.create_text(50,195, text='Google Inc.')

for i in range(38):
    if (i%3==0):
        a+=1
    canvas.delete('text')
    canvas.create_text(60,225, text=t[a-1], tag='text', font=('Times'))
    canvas.update()
    time.sleep(0.25)
    canvas.delete('rect')
    canvas.create_rectangle(xy, fill='blue', outline='blue', tag='rect')
    xy[2]+=10
#time.sleep(1)
root.destroy()
root.mainloop()

root=Tk()
d_points=[]
points = []
Sx=0
Sy=0

and_gates_id=[]
or_gates_id=[]
not_gates_id=[]
connect_gates_id=[]
sev_seg_id=[]

Inputs=[]
Outputs=[]
only_gates=[]

All=[]
All_obj=[]
con_count=[]
con_cords=[]
fin_con=[]

#global obj_list
obj_list=[]

ss='Status\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tx\t\ty'

root.title('DIGICAL')
root.iconbitmap(bitmap = "@./_assets/Transform.xbm")
root.geometry('1348x700+5+5')
#root.resizable(0,0)

menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=new)
filemenu.add_command(label="Open...", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_command(label="Exit", command=root.destroy)

editmenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="View",command=callback)

toolsmenu = Menu(menu)
menu.add_cascade(label="Tools", menu=toolsmenu)
toolsmenu.add_command(label='Gates', command=callback)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Electrical Docs", command=docs)
helpmenu.add_separator()
helpmenu.add_command(label="About...", command=about)

AND=Button(root, text='AND', command=and_eg)
OR=Button(root, text='OR', command=or_eg)
NOT=Button(root, text='NOT', command=not_eg)
SEG=Button(root, text='7-Seg Disp', command=sev_seg)
DAT=Button(root, text='DATA', command=data)
ACT=Button(root, text='ACTIVATE', command=activate)
DEL=Button(root, text='DELETE', command=delete)
UPDT=Button(root, text='CLEAR ALL', command=update)
EXIT=Button(root, text='EXIT', command=root.destroy)

canvas = Canvas(width=1342, height=630, bg='WHITE')
sts=Label(root, text=ss, relief='sunken', anchor=W)

sts.pack(side=BOTTOM, fill=X)
canvas.pack(side=BOTTOM)
AND.pack(side=LEFT, expand=YES)
OR.pack(side=LEFT, expand=YES)
NOT.pack(side=LEFT, expand=YES)
SEG.pack(side=LEFT, expand=YES)
DAT.pack(side=LEFT, expand=YES)
ACT.pack(side=LEFT, expand=YES)
DEL.pack(side=LEFT, expand=YES)
UPDT.pack(side=LEFT, expand=YES)
EXIT.pack(side=RIGHT, expand=YES)
#Button(root, text='connections', command=connection).pack(side=LEFT)
#Button(root, text='coordinates', command=coordinates).pack(side=LEFT)
Button(root, text='FINAL CONNECTIONS', command=final_connection).pack(side=LEFT, expand=YES)
Button(root, text='SIMULATE', command=check).pack(side=LEFT, expand=YES)

menu=Menu(root, tearoff=0)
choice='Input'
menu.add_radiobutton(label=choice, command=Input)

canvas.bind('<ButtonPress-3>',right_click)
canvas.bind('<B1-Motion>',status)
canvas.bind('<ButtonPress-2>',point)
canvas.bind('<ButtonRelease-2>',graph)
root.mainloop()
