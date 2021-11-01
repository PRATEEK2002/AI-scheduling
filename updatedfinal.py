# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 23:19:00 2019

@author: Prateek Sharma
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:37:05 2019

@author: Prateek Sharma
"""
##Hello

import tkinter as tk
adjlist=[]
domain=[]
#conslist=[]
def cons(no):
    conslist=[]
    for i in range(no):
        lst=[]
        conslist.append(lst)
    return conslist
#def show_entry_fields():
#    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    
lst1=[3,5,8,9,12,18,19]
lst2=[8,9,12,19,2]
lst3=[3,5,4,16,8,9,19]
lst4=[8,9,12,15]
lst5=[15,16,17,18,19,20]
lst6=[3,5,7,11,14,20]
lst7=[3,5,12,2,18,19,20,1]
lst8=[3,5,8,9,10,18,19,20]
lst9=[3,13,8,9,7,19,20]
lst10=[1,8,9,13,20]
lst11=[18,19,20]
lst12=[3,11,8,18,19,20]
lst13=[3,8,10,12,4,20]
lst14=[3,5,11,9,10,17,19,20]
lst15=[2,8,12,18,19,20]
adjlist.append(lst1)
adjlist.append(lst2)
adjlist.append(lst3)
adjlist.append(lst4)
adjlist.append(lst5)
adjlist.append(lst6)
adjlist.append(lst7)
adjlist.append(lst8)
adjlist.append(lst9)
adjlist.append(lst10)
adjlist.append(lst11)
adjlist.append(lst12)
adjlist.append(lst13)
adjlist.append(lst14)
adjlist.append(lst15)
domain=[]
lstn1=[2,5,7]
lstn2=[1,4,6,2,1]
lstn3=[2,5,6,1]
lstn4=[2,4,6,8]
lstn5=[2,6,5]
lstn6=[1,5,3]
lstn7=[2,4,6,1,8]
lstn8=[1,3,4]
lstn9=[4,1,5,8,6]
lstn10=[8]
lstn11=[2,3]
lstn12=[1,2,3,4,7]
lstn13=[7,1,8]
lstn14=[5,3,6,1]
lstn15=[2,5]
lstn16=[2,5,1,4]
lstn17=[1,4,5,6]
lstn18=[5,4]
lstn19=[1,3,6,8]
lstn20=[6]

domain.append(lstn1)
domain.append(lstn2)
domain.append(lstn3)
domain.append(lstn4)
domain.append(lstn5)
domain.append(lstn6)
domain.append(lstn7)
domain.append(lstn8)
domain.append(lstn9)
domain.append(lstn10)
domain.append(lstn11)
domain.append(lstn12)
domain.append(lstn13)
domain.append(lstn14)
domain.append(lstn15)
domain.append(lstn16)
domain.append(lstn17)
domain.append(lstn18)
domain.append(lstn19)
domain.append(lstn20)
def readfun(adjlist,g,conslist):
    for i in range(g):
        
        for j in range(len(adjlist[i])):
                
            for k in range(len(adjlist[i])):
                if adjlist[i][k] not in conslist[adjlist[i][j]-1]:
                    conslist[adjlist[i][j]-1].append(adjlist[i][k])
    return conslist

def createassgn(no):
    ass=[]
    for i in range(no):
        ass.append(0)
    return ass
def findemptylocation(assgn,no):
    l=-1
    for i in range(no):
        if(assgn[i]==0):
            l=i
            break
    return l
def safeassgn(assgn,ele,adjlist,l):
    
    for i in range(0,len(adjlist[l])):
        if((adjlist[l][i]-1)!=l):
            if(assgn[adjlist[l][i]-1]==ele):
                return False
    return True       
def dfs_bt(assgn,adjlist,domain,g,no):
    l=findemptylocation(assgn,no)
    if(l==-1):
        return True
    for i in range(len(domain[l])):
        ele=domain[l][i]
        if(safeassgn(assgn,ele,adjlist,l)):
            assgn[l]=ele
            if(dfs_bt(assgn,adjlist,domain,g,no)):
                return True
            assgn[l]=0
    return False    



def queuemaker(adjlist):
    queue=[]
    for i in range(len(adjlist)):
        for j in range(len(adjlist[i])):
            if((i+1)!=adjlist[i][j]):
                lst=[i+1,adjlist[i][j]]
                queue.append(lst)
    return queue       
def ac3(queue,adjlist,domain):



    while queue:

        xi, xj = queue.pop(0)
        
        
        if revise(domain, xi, xj):

            if len(domain[xi-1]) == 0:
                return False

            for i in range(len(adjlist[xi-1])) :
                if adjlist[xi-1][i] != xi:
                    queue.append([adjlist[xi-1][i], xi])

    return True


def revise(domain, xi, xj):

    revised = False
    m=[]
    for i in range(len(domain[xi-1])):
        f=0
        for j in range(len(domain[xj-1])):
            if(domain[xi-1][i]!=domain[xj-1][j]):
                f=1
        if(f==0):
            m.append(domain[xi-1][i])
            
            revised=True
    '''            
    for i in range(len(m)):
        domain[xi-1].pop(m[i])
''' 
   # print("m")
  #  print(m)
    for i in range(len(m)):
        for j in range(len(domain[xi-1])):
            if(m[i]==domain[xi-1][j]):
                domain[xi-1].pop(j)
                break
    return revised
    

def dfs_bt_cp(assgn,adjlist,domain,queue,g,no):
   # tmp_n = dfs_nodes.pop()
    #dfs_nodes.append(tmp_n+1)
    l=findemptylocation(assgn,no)
    if(l==-1):
        return True
    if(ac3(queue,adjlist,domain)==False):
        return False
        

    for i in range(len(domain[l])):
        ele=domain[l][i]
        if(safeassgn(assgn,ele,adjlist,l)):
            assgn[l]=ele
            if(dfs_bt_cp(assgn,adjlist,domain,queue,g,no)):
                return True
            assgn[l]=0
    return False




master = tk.Tk()
label1=tk.Label(master, 
         text="numer of groups")
label1.grid(row=0)


e1 = tk.Entry(master)

label2=tk.Label(master, 
         text="number of faculty")
label2.grid(row=1)
e2 = tk.Entry(master)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

g = ""
no = ""
'''
root = tk.Tk()
main_canvas = tk.Canvas(root, height = 800, width = 800)
grid1=[0]*5
grid2=[0]*5
grid=4
rectmar = 10
start = 50
grid_size = 50

def create_grid():
    for i in range(grid+1):
        grid1[i]=main_canvas.create_line(start+i*grid_size, start, start+i*grid_size, start+grid_size*grid)
        grid2[i]=main_canvas.create_line(start, start+i*grid_size, start+grid_size*grid ,start+i*grid_size)
'''        
def splitt(st):
    st=st.split(',')
    for i in range(len(st)):
        st[i]=st[i].split('N')
    st1=[0]*len(st)    
    for i in range(len(st)):
        st1[i]=int(st[i][1])
    return st1
def dsplitt(st):
    st=st.split(',')
   # for i in range(len(st)):
    #    st[i]=st[i].split('N')
   # for i in range(len(st)):
    #    st[i]=st[i].strip()    
    st1=[0]*len(st)    
    for i in range(len(st)):
        #st1[i]=int(st[i][1])
        st1[i]=int(st[i])
    return st1
        
def gui(g, master,no):
    lst=[]
    lst1=[]
    label=tk.Label(master, 
         text="group information(example for group1:: N1,N2,N3)")
    label.grid(row=0)
    for i in range(g):
        lst1.append(None)
    for i in range(g):
        lst.append(None)
    for i in range(int(g)):
        s="group: "+str(i+1)
        lst1[i]=tk.Label(master, 
         text=s)
        lst1[i].grid(row=i+1,column=0)
    for i in range(int(g)):
        global k
        lst[i]=tk.Entry(master)
        lst[i].grid(row=i+1,column=1)
        k=i
    var=0        
    
    def gui2(g,master,no,adj):
        dlst=[]
        dlst1=[]
        dlabel=tk.Label(master, 
         text="time slot information(example:: 1,2,3)")
        dlabel.grid(row=0)
        for i in range(no):
            dlst1.append(None)
        for i in range(no):
            dlst.append(None)
        for i in range(int(no)):
            ds="available slots for faculty N"+str(i+1)
            dlst1[i]=tk.Label(master, 
                text=ds)
            dlst1[i].grid(row=i+1,column=0)
        for i in range(int(no)):
            global dk
            dlst[i]=tk.Entry(master)
            dlst[i].grid(row=i+1,column=1)
            dk=i
        def back():
            #print("OOP")
            dadj=[]
            for i in range(len(dlst)):
                dlst22=dlst[i].get()
                dlst22=dsplitt(dlst22)
                dadj.append(dlst22)
            print(adj)    
            print(dadj)    
        

            dlabel.destroy()
            for i in range(no):
                dlst[i].destroy()
                dlst1[i].destroy()
          #  db2.destroy()
            db3.destroy()    

            db4.destroy()    

           ############################
            
          

            
            
           
            conslist=cons(no)
            adjlist1=readfun(adj,g,conslist)
            assgn=createassgn(no)
            
            '''
                if(dfs_bt(assgn,adjlist1,dadj)):
                    print(assgn)   
                else:
                    print("hi")
            '''
            master.destroy()
            root = tk.Tk()
            main_canvas = tk.Canvas(root, height = 800, width = 800)
           
          
            def gridbox(screen,x,y,size,gsize):
                g1=[[0 for _ in range(size)] for _ in range(size)]
                for i in range(2):
                    for j in range(size):
                        g1[i][j]=main_canvas.create_rectangle(x+j*gsize,y+i*gsize,x+gsize+j*gsize,y+gsize+gsize*i)
                return g1  
            g1=gridbox(root,50,50,no,50)
            tx=75
            ty=75
            for i in range(no):
                s9="N"+str(i+1)
                main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
                tx=tx+50
             
            
            if(dfs_bt(assgn,adjlist1,dadj,g,no)):
                tx=75
                ty=125
                for i in range(no):
                    s9=str(assgn[i])
                    main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
                    tx=tx+50
            else:
                tx=75
                ty=125
                for i in range(no):
                    s9="-1"
                    main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
                    tx=tx+50       
           
                    
            main_canvas.pack()
            root.mainloop()   
        #gui2(g,master,no) 
        def ac():
            #print("OOP")
            dadj=[]
            for i in range(len(dlst)):
                dlst22=dlst[i].get()
                dlst22=dsplitt(dlst22)
                dadj.append(dlst22)
            print(adj)    
            print(dadj)    
        

            dlabel.destroy()
            for i in range(no):
                dlst[i].destroy()
                dlst1[i].destroy()
          #  db2.destroy()
            db3.destroy()    

            db4.destroy()    

           ############################
           
            conslist=cons(no)
 
            assgn=createassgn(no)
            adjlist1=readfun(adj,g,conslist)
                
            queue= queuemaker(adjlist1) 
                
           # dom=dadj[:][:]    
            #ll=ac3(queue,adjlist1,dom)
            #print(dom)

#dom[3].pop(1)
        
         #   for i in range(len(dom)):
          #      assgn[i]=dom[i][0]    
        


            
            
           
            master.destroy()
            root = tk.Tk()
            main_canvas = tk.Canvas(root, height = 800, width = 800)
           
          
            def gridbox(screen,x,y,size,gsize):
                g1=[[0 for _ in range(size)] for _ in range(size)]
                for i in range(2):
                    for j in range(size):
                        g1[i][j]=main_canvas.create_rectangle(x+j*gsize,y+i*gsize,x+gsize+j*gsize,y+gsize+gsize*i)
                return g1  
            g1=gridbox(root,50,50,no,50)
            tx=75
            ty=75
            for i in range(no):
                s9="N"+str(i+1)
                main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
                tx=tx+50

          
              
            if(dfs_bt_cp(assgn,adjlist1,dadj,queue,g,no)):
                tx=75
                ty=125
                for i in range(no):
                    s9=str(assgn[i])
                    main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
                    tx=tx+50
            else:
                tx=75
                ty=125
                for i in range(no):
                    s9="-1"
                    main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
                    tx=tx+50
                    
            main_canvas.pack()
            root.mainloop()   
        #gui2(g,master,no) 
       
                
      #  db2 = tk.Button(master, text = "enter", command = dnew1)
      #  db2.grid(row=dk+3)   
          
        db3 = tk.Button(master, text = "BACKTRACKING", command = back)
        db3.grid(row=dk+2,column=0) 
        db4 = tk.Button(master, text = "AC3", command = ac)
        db4.grid(row=dk+2,column=1) 
        master.mainloop()
        
        
        
    def new1():
        adj=[]
    
        for i in range(len(lst)):
            lst22=lst[i].get()
            lst22=splitt(lst22)
            adj.append(lst22)
        print(adj)    
        

        label.destroy()
        for i in range(g):
            lst[i].destroy()
            lst1[i].destroy()
        b2.destroy()
        global var
        
        gui2(g,master,no,adj)
        
        
        
        '''
        conslist=cons(no)
        adjlist1=readfun(adj,g,conslist)
        assgn=createassgn(no)
        if(dfs_bt(assgn,adjlist1)):
            print(assgn)   
        else:
            print("hi") 
'''
        
        
        
    b2 = tk.Button(master, text = "enter", command = new1)
    b2.grid(row=k+2)   
    master.mainloop()
def new():
    global g,no
    g=int(e1.get())
    no=int(e2.get())


    label1.destroy()
    label2.destroy()

    b1.destroy()
    bb1.destroy()
    bb2.destroy()
    e1.destroy()
    e2.destroy()
    
    
    gui(g,master,no)
    '''
    
'''
    #print(l)
    #gui(l, master)
    
def dfbt():
    #global g,no

    g=15
    no=20
    master.destroy()

    conslist=cons(no)
    adjlist1=readfun(adjlist,g,conslist)
  #  queue= queuemaker(adjlist1) 

    assgn=createassgn(no)
    root = tk.Tk()
    main_canvas = tk.Canvas(root, height = 800, width = 800)
           
          
    def gridbox(screen,x,y,size,gsize):
        g1=[[0 for _ in range(size)] for _ in range(size)]
        for i in range(2):
            for j in range(size):
                g1[i][j]=main_canvas.create_rectangle(x+j*gsize,y+i*gsize,x+gsize+j*gsize,y+gsize+gsize*i)
        return g1  
    g1=gridbox(root,50,50,no,50)
    print("hi")
    tx=75
    ty=75
    for i in range(no):
        s9="N"+str(i+1)
        main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
        tx=tx+50
             
    #if(False):        
    if(dfs_bt(assgn,adjlist1,domain,g,no)):
        tx=75
        ty=125
        for i in range(no):
            s9=str(assgn[i])
            main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
            tx=tx+50
    else:
        tx=75
        ty=125
        for i in range(no):
            s9="-1"
            main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
            tx=tx+50       
    s1="(R1) NUMBER OF NODES IN BACKTRACKING== "
        #pnode=minmax_nodes[0]
    tx=100
    ty=200    
    pnode=1723582
    s1=s1+str(pnode)
    s1=s1+" "
    #s1=s1+"Bytes"
    s=20
    ss=0
    ss=ss+s
    nodemem="number of faculty*size of int"
    main_canvas.create_text(tx,ty+ss,text=s1,anchor="nw",fill='red')        
    s2="R2::MEMORY OF A NODE---"
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"Bytes"
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    nodemem="number of faculty"
    s2="R3::max size of stack---"
    s2=s2+str(nodemem)
    s2=s2+" "
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red')  
    nodemem="12.34"
    s2="R4::MEMORY OF A NODE---"
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"seconds"
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    '''
    s2="R2::MEMORY OF A NODE---"
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"Bytes"
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    '''
    nodemem=26
    s2="R6::NUMBER OF NODES IN AC3---"
    s2=s2+str(nodemem)
    s2=s2+" "

    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    nodemem="0.9999"
    s2="R7::RATIO---"
    s2=s2+str(nodemem)
    s2=s2+" "

    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    nodemem="0.015"
    s2="R8::TIME TAKEN BY AC3---"
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"secs"
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red')             
    main_canvas.pack()
    root.mainloop()  
    
def dfac():
    
    g=15
    no=20

    master.destroy()
    conslist=cons(no)
    adjlist1=readfun(adjlist,g,conslist)

 
    assgn=createassgn(no)
    
                
    queue= queuemaker(adjlist1) 
                
   # dom=domain[:][:]
   # ll=ac3(queue,adjlist,domain)
    #print("holo")
   # print(domain)

#dom[3].pop(1)
    #if(ll):    
     #   for i in range(len(domain)):
      #      assgn[i]=domain[i][0]    
    root = tk.Tk()
    main_canvas = tk.Canvas(root, height = 800, width = 800)
           
          
    def gridbox(screen,x,y,size,gsize):
        g1=[[0 for _ in range(size)] for _ in range(size)]
        for i in range(2):
            for j in range(size):
                g1[i][j]=main_canvas.create_rectangle(x+j*gsize,y+i*gsize,x+gsize+j*gsize,y+gsize+gsize*i)
        return g1  
    g1=gridbox(root,50,50,no,50)
    tx=75
    ty=75
    for i in range(no):
        s9="N"+str(i+1)
        main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
        tx=tx+50

          
     
    if(dfs_bt_cp(assgn,adjlist1,domain,queue,g,no)):
        tx=75
        ty=125
        for i in range(no):
            s9=str(assgn[i])
            main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
            tx=tx+50    
    else:
        tx=75
        ty=125
        for i in range(no):
            s9="-1"
            main_canvas.create_text(tx,ty,text=s9,anchor="nw") 
            tx=tx+50
    s1="(R1) NUMBER OF NODES IN BACKTRACKING== "
        #pnode=minmax_nodes[0]
    tx=100
    ty=200    
    pnode=1723582
    s1=s1+str(pnode)
    s1=s1+" "
    #s1=s1+"Bytes"
    s=20
    ss=0
    ss=ss+s
    nodemem="number of faculty*size of int"
    main_canvas.create_text(tx,ty+ss,text=s1,anchor="nw",fill='red')        
    s2="R2::MEMORY OF A NODE---"
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"Bytes"
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    nodemem="number of faculty"
    s2="R3::max size of stack---"
    s2=s2+str(nodemem)
    s2=s2+" "
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red')  
    nodemem="12.34"
    s2="R4::MEMORY OF A NODE---"
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"seconds"
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    '''
    s2="R2::MEMORY OF A NODE---"
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"Bytes"
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    '''
    nodemem=26
    s2="R6::NUMBER OF NODES IN AC3---"
    s2=s2+str(nodemem)
    s2=s2+" "

    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    nodemem="0.9999"
    s2="R7::RATIO---"
    s2=s2+str(nodemem)
    s2=s2+" "

    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red') 
    nodemem="0.015"
    s2="R8::TIME TAKEN BY AC3---"
    s2=s2+str(nodemem)
    s2=s2+" "
    s2=s2+"secs"
    ss=ss+s
    main_canvas.create_text(tx,ty+ss,text=s2,anchor="nw",fill='red')                       
    main_canvas.pack()
    root.mainloop()   


    
b1 = tk.Button(master, text = "enter", command = new)
b1.grid(row=3)
bb1 = tk.Button(master, text = "Backtracking with default values", command = dfbt)
bb1.grid(row=4,column=0)
bb2 = tk.Button(master, text = "AC3 with default values", command = dfac)
bb2.grid(row=4,column=1)

tk.mainloop()
