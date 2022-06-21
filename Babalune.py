import tkinter as tk
import sqlite3

class Abalone:
    def __init__(self,p=1):
        self.c=tk.Canvas(fenetre,width=1700,height=956,bg='white')
        self.fond1=tk.PhotoImage(file='plateau.png')
        self.fond=self.c.create_image(850,510,image=self.fond1,state=tk.NORMAL,tags='fond')
        self.cercler=dict()
        self.cercleb=dict()
        self.fleche=dict()
        self.labels=dict()
        r=30
        
        
        for i in range(15):
            if i>0 and i<6:
                x,yr,yb=685+80*(i-1),230,780
                self.cercler[i]=self.c.create_oval(x-r,yr-r,x+r,yr+r,fill='red',tags='cr')  #créer un cercle de centre x,y et de rayon r
                self.cercleb[i]=self.c.create_oval(x-r,yb-r,x+r,yb+r,fill='blue',tags='cb')
                self.c.tag_bind(self.cercler[i],'<Button-1>',self.coord)
                self.c.tag_bind(self.cercleb[i],'<Button-1>',self.coord)

            elif i>5 and i<12:
                x,yr,yb=645+80*(i-6),295,715
                self.cercler[i]=self.c.create_oval(x-r,yr-r,x+r,yr+r,fill='red',tags='cr')
                self.cercleb[i]=self.c.create_oval(x-r,yb-r,x+r,yb+r,fill='blue',tags='cb')
                self.c.tag_bind(self.cercler[i],'<Button-1>',self.coord)
                self.c.tag_bind(self.cercleb[i],'<Button-1>',self.coord)
            elif i>11:
                x,yr,yb=765+80*(i-12),365,645
                self.cercler[i]=self.c.create_oval(x-r,yr-r,x+r,yr+r,fill='red',tags='cr')
                self.cercleb[i]=self.c.create_oval(x-r,yb-r,x+r,yb+r,fill='blue',tags='cb')
                self.c.tag_bind(self.cercler[i],'<Button-1>',self.coord)
                self.c.tag_bind(self.cercleb[i],'<Button-1>',self.coord)

        textrouge=self.c.create_text(200,20,text="Boules rouges en dehors du jeu:",font=('Times','20','bold'))
        textbleu=self.c.create_text(1500,20,text="Boules bleues en dehors du jeu:",font=('Times','20','bold'))
        boulerdeco=self.c.create_oval(80-r,80-r,80+r,80+r,fill='red')
        boulebdeco=self.c.create_oval(1380-r,80-r,1380+r,80+r,fill='blue')
        scoreb="0"
        scorer="0"
        self.textscorer=self.c.create_text(150,80,text=scorer,font=('Times','26','bold'))
        self.textscoreb=self.c.create_text(1450,80,text=scorer,font=('Times','26','bold'))
        self.tour=0



        self.buthist=self.c.create_rectangle(1500,800,1600,850,fill='salmon',tags="histo")
        self.histtext=self.c.create_text(1550,825,text="Historique",font=("Times","16"),tags="histo")
        self.c.tag_bind("histo",'<Button-1>',self.affichehisto)

        
        self.c.pack()
        self.x,self.y=10,10
    #------------------------------------------------------------------------------------------------------------------


    def affichehisto(self,event):
        F1=tk.Toplevel()
        self.conn=sqlite3.connect('Babalune.db')
        self.cursor=self.conn.cursor()
        listeparties=self.cursor.execute("Select * from Parties""").fetchall()
        listejoueurs=self.cursor.execute("Select Nom from Joueurs").fetchall()

        for i in range(len(listeparties)):
            self.labels[i]=tk.Label(F1,text="{} contre {}, gagnant: {} en {} coups".format(listejoueurs[listeparties[i][0]-1][0],listejoueurs[listeparties[i][1]-1][0],listejoueurs[listeparties[i][2]-1][0],listeparties[i][3]))
            self.labels[i].grid(row=i,column=0)
            
        
        print(listeparties)
        self.conn.close()
        
    #------------------------------------------------------------------------------------------------------------------     coord
    def coord(self,event):                    #clic gauche                                               
        self.x,self.y=event.x,event.y
        cercle=self.c.find_closest(self.x,self.y)
        j=cercle[0]
        
        
        
        if j in self.c.find_withtag('cr'):
            r=30
            a,b,c,d=self.c.coords(cercle)
            
            self.c.delete('fleches')
            self.c.dtag('selectcr','selectcr')
            self.c.dtag('selectcb','selectcb')
            self.c.dtag('pret2','pret2')
            self.c.dtag('pret3','pret3')  
            self.c.dtag('premiereb','premiereb')
            self.c.dtag('premierer','premierer')
            self.c.dtag('clicmoletteb','clicmoletteb')
            self.c.dtag('deuxiemer','deuxiemer')
            self.c.dtag('deuxiemeb','deuxiemeb')
            self.c.dtag('rectb','rectb')
            self.c.dtag('clicmoletter','clicmoletter')
            self.c.dtag('rectr','rectr')
            self.c.dtag('troisiemeb','troisiemeb')
            self.c.dtag('troisiemer','troisiemer')
            self.c.dtag('depl','depl')
            self.c.dtag('test','test')
            self.c.dtag('suppr2','suppr2')
            self.c.dtag('suppr3','suppr3')
            
            
            self.c.addtag_withtag('premierer',cercle)
            for i in range(6):
                if i==0:        
                    self.fleche[i]=self.c.create_line(a+r,b+r,a+r+20,b+r,arrow=tk.LAST,tags='d')         #droite 
                    self.c.addtag_withtag('fleches','d')
                    self.c.tag_bind(self.c.find_withtag('d'),'<Button-1>',self.droite)
                elif i==1:
                    self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b+17+r,arrow=tk.LAST,tags='hd')      #bas droite   
                    self.c.addtag_withtag('fleches','hd')
                    self.c.tag_bind(self.c.find_withtag('hd'),'<Button-1>',self.basdroite)
                elif i==2:  
                    self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b+17+r,arrow=tk.LAST,tags='hg')      #bas gauche   
                    self.c.addtag_withtag('fleches','hg')
                    self.c.tag_bind(self.c.find_withtag('hg'),'<Button-1>',self.basgauche)
                elif i==3:   
                    self.fleche[i]=self.c.create_line(a+r,b+r,a-20+r,b+r,arrow=tk.LAST,tags='g')         #gauche 
                    self.c.addtag_withtag('fleches','g')
                    self.c.tag_bind(self.c.find_withtag('g'),'<Button-1>',self.gauche)
                elif i==4:
                    self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b-17+r,arrow=tk.LAST,tags='bg')      #haut gauche
                    self.c.addtag_withtag('fleches','bg')
                    self.c.tag_bind(self.c.find_withtag('bg'),'<Button-1>',self.hautgauche)
                elif i==5:
                    self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b-17+r,arrow=tk.LAST,tags='bd')     #haut droite
                    self.c.addtag_withtag('fleches','bd')
                    self.c.tag_bind(self.c.find_withtag('bd'),'<Button-1>',self.hautdroite)
                    
            point=self.c.create_rectangle(a+r,b+r,a+r+1,b+r+1,fill='',outline='',tags='point')
            for i in range(6):
                if i==0:
                    m,n,o,p=self.c.coords('point')
                    
                
                    self.c.move('point',80,0)                   #droite
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcr',m,n,o,p)
                elif i==1:
                    self.c.move('point',-40,-69)                #haut droite
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcr',m,n,o,p)
                elif i==2:
                    self.c.move('point',-80,0)                #haut gauche
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcr',m,n,o,p)
                elif i==3:
                    self.c.move('point',-40,69)                #gauche
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcr',m,n,o,p)
                elif i==4:
                    self.c.move('point',40,69)                #bas gauche
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcr',m,n,o,p)
                elif i==5:
                    self.c.move('point',80,0)                #bas droite
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcr',m,n,o,p)
            self.c.delete(point)
            self.c.delete('point')
            self.c.dtag('cb','selectcr')
            self.c.dtag('fond','selectcr')
            self.c.tag_bind('selectcr','<Button-3>',self.selectcr)
            
        elif j in self.c.find_withtag('cb'):
            r=30
            a,b,c,d=self.c.coords(cercle)
            
            self.c.delete('fleches')
            self.c.dtag('selectcr','selectcr')
            self.c.dtag('selectcb','selectcb')
            self.c.dtag('pret2','pret2')
            self.c.dtag('pret3','pret3')  
            self.c.dtag('premiereb','premiereb')
            self.c.dtag('premierer','premierer')
            self.c.dtag('clicmoletteb','clicmoletteb')
            self.c.dtag('deuxiemer','deuxiemer')
            self.c.dtag('deuxiemeb','deuxiemeb')
            self.c.dtag('rectb','rectb')
            self.c.dtag('clicmoletter','clicmoletter')
            self.c.dtag('rectr','rectr')
            self.c.dtag('troisiemeb','troisiemeb')
            self.c.dtag('troisiemer','troisiemer')
            self.c.dtag('depl','depl')
            self.c.dtag('test','test')
            self.c.dtag('suppr2','suppr2')
            self.c.dtag('suppr3','suppr3')
            
            
            self.c.addtag_withtag('premiereb',cercle)
            for i in range(6):
                if i==0:        
                    self.fleche[i]=self.c.create_line(a+r,b+r,a+r+20,b+r,arrow=tk.LAST,tags='d')         #droite 
                    self.c.addtag_withtag('fleches','d')
                    self.c.tag_bind(self.c.find_withtag('d'),'<Button-1>',self.droite)
                elif i==1:
                    self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b+17+r,arrow=tk.LAST,tags='hd')      #bas droite   
                    self.c.addtag_withtag('fleches','hd')
                    self.c.tag_bind(self.c.find_withtag('hd'),'<Button-1>',self.basdroite)
                elif i==2:  
                    self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b+17+r,arrow=tk.LAST,tags='hg')      #bas gauche   
                    self.c.addtag_withtag('fleches','hg')
                    self.c.tag_bind(self.c.find_withtag('hg'),'<Button-1>',self.basgauche)
                elif i==3:   
                    self.fleche[i]=self.c.create_line(a+r,b+r,a-20+r,b+r,arrow=tk.LAST,tags='g')         #gauche 
                    self.c.addtag_withtag('fleches','g')
                    self.c.tag_bind(self.c.find_withtag('g'),'<Button-1>',self.gauche)
                elif i==4:
                    self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b-17+r,arrow=tk.LAST,tags='bg')      #haut gauche
                    self.c.addtag_withtag('fleches','bg')
                    self.c.tag_bind(self.c.find_withtag('bg'),'<Button-1>',self.hautgauche)
                elif i==5:
                    self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b-17+r,arrow=tk.LAST,tags='bd')     #haut droite
                    self.c.addtag_withtag('fleches','bd')
                    self.c.tag_bind(self.c.find_withtag('bd'),'<Button-1>',self.hautdroite)
                    
            point=self.c.create_rectangle(a+r,b+r,a+r+1,b+r+1,fill='',outline='',tags='point')
            for i in range(6):
                if i==0:
                    m,n,o,p=self.c.coords('point')
                    
                
                    self.c.move('point',80,0)                   #droite
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcb',m,n,o,p)
                elif i==1:
                    self.c.move('point',-40,-69)                #haut droite
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcb',m,n,o,p)
                elif i==2:
                    self.c.move('point',-80,0)                #haut gauche
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcb',m,n,o,p)
                elif i==3:
                    self.c.move('point',-40,69)                #gauche
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcb',m,n,o,p)
                elif i==4:
                    self.c.move('point',40,69)                #bas gauche
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcb',m,n,o,p)
                elif i==5:
                    self.c.move('point',80,0)                #bas droite
                    m,n,o,p=self.c.coords('point')
                    self.c.addtag_overlapping('selectcb',m,n,o,p)
            self.c.delete(point)
            self.c.delete('point')
            self.c.dtag('cr','selectcb')
            self.c.tag_bind('selectcb','<Button-3>',self.selectcb)
            self.c.dtag('fond','selectcb')
       
        

    #------------------------------------------------------------------------------------------------------------------     selectcr                               
                

    def selectcr(self,event):   #clic droit
        
        self.x,self.y=event.x,event.y 
        cercle=self.c.find_closest(self.x,self.y)
        r=30
        a,b,c,d=self.c.coords(cercle)
        if self.c.find_withtag('selectcb') or self.c.find_withtag('selectcr'):
            self.c.dtag('selectcb','selectcb')
            self.c.dtag('selectcr','selectcr')
        self.c.addtag_enclosed('pret2',a-1,b-1,c+1,d+1)
        if self.c.find_withtag('deuxiemer'):
            self.c.dtag('deuxiemer','deuxiemer')
        
        self.c.addtag_withtag('deuxiemer','pret2')
        
        for i in range(6):
            if i==0:        
                self.fleche[i]=self.c.create_line(a+r,b+r,a+r+20,b+r,arrow=tk.LAST,tags='d')         #droite 
                self.c.addtag_withtag('fleches','d')
                self.c.tag_bind(self.c.find_withtag('d'),'<Button-1>',self.droite)
            elif i==1:
                self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b+17+r,arrow=tk.LAST,tags='hd')      #bas droite   
                self.c.addtag_withtag('fleches','hd')
                self.c.tag_bind(self.c.find_withtag('hd'),'<Button-1>',self.basdroite)
            elif i==2:  
                self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b+17+r,arrow=tk.LAST,tags='hg')      #bas gauche   
                self.c.addtag_withtag('fleches','hg')
                self.c.tag_bind(self.c.find_withtag('hg'),'<Button-1>',self.basgauche)
            elif i==3:   
                self.fleche[i]=self.c.create_line(a+r,b+r,a-20+r,b+r,arrow=tk.LAST,tags='g')         #gauche 
                self.c.addtag_withtag('fleches','g')
                self.c.tag_bind(self.c.find_withtag('g'),'<Button-1>',self.gauche)
            elif i==4:
                self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b-17+r,arrow=tk.LAST,tags='bg')      #haut gauche
                self.c.addtag_withtag('fleches','bg')
                self.c.tag_bind(self.c.find_withtag('bg'),'<Button-1>',self.hautgauche)
            elif i==5:
                self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b-17+r,arrow=tk.LAST,tags='bd')     #haut droite
                self.c.addtag_withtag('fleches','bd')
                self.c.tag_bind(self.c.find_withtag('bd'),'<Button-1>',self.hautdroite)
        




        point=self.c.create_rectangle(a+r-10,b+r-10,a+r+10,b+r+10,fill='',outline='',tags='point')
        for i in range(6):
            g,h,j,k=self.c.coords('premierer')
            rect=self.c.create_rectangle(g+r,h+r,g+r+1,h+r+1,fill='',outline='',tag='rectr')
                        
                
            if i==0:
                m,n,o,p=self.c.coords('point') #centre cercle sur lequel on a cliqué 
                self.c.move('point',80,0)                   #droite
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectr'):
                    self.c.addtag_overlapping('clicmoletter',m+80,n,o+80,p)
                    self.c.addtag_overlapping('clicmoletter',m-160,n,o-160,p)
                    self.c.tag_bind('clicmoletter','<Button-2>',self.select3cr)
                    
                           
            elif i==1:
                self.c.move('point',-40,-69)                #haut droite
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectr'):
                    self.c.addtag_overlapping('clicmoletter',m+40,n-69,o+40,p-69)
                    self.c.addtag_overlapping('clicmoletter',m-80,n+138,o-80,p+138)
                    self.c.tag_bind('clicmoletter','<Button-2>',self.select3cr)
                    
            elif i==2:
                self.c.move('point',-80,0)                #haut gauche
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectr'):
                    self.c.addtag_overlapping('clicmoletter',m-40,n-69,o-40,p-69)
                    self.c.addtag_overlapping('clicmoletter',m+80,n+138,o+80,p+138)
                    self.c.tag_bind('clicmoletter','<Button-2>',self.select3cr)
                
                    
            elif i==3:
                self.c.move('point',-40,69)                #gauche
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectr'):
                    self.c.addtag_overlapping('clicmoletter',m-80,n,o-80,p)
                    self.c.addtag_overlapping('clicmoletter',m+160,n,o+160,p)
                    self.c.tag_bind('clicmoletter','<Button-2>',self.select3cr)
                                
                    
            elif i==4:
                self.c.move('point',40,69)                #bas gauche
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectr'):
                    self.c.addtag_overlapping('clicmoletter',m-40,n+69,o-40,p+69)
                    self.c.addtag_overlapping('clicmoletter',m+80,n-138,o+80,p-138)
                    self.c.tag_bind('clicmoletter','<Button-2>',self.select3cr)
                
            elif i==5:
                self.c.move('point',80,0)                #bas droite
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectr'):
                    self.c.addtag_overlapping('clicmoletter',m+40,n+69,o+40,p+69)
                    self.c.addtag_overlapping('clicmoletter',m-80,n-138,o-80,p-138)
                    self.c.tag_bind('clicmoletter','<Button-2>',self.select3cr)


        
        
        
        self.c.delete(point)   
        self.c.delete('point')
        self.c.delete('rectr')
        self.c.dtag('rectr','rectr')
        self.c.dtag('selectcr','selectcr')
        self.c.dtag('selectcb','selectcb')
        self.c.dtag('cr','clicmoletteb')
        self.c.dtag('cb','clicmoletter')
        self.c.dtag('fond','clicmoletteb')
        self.c.dtag('fond','clicmoletter')
        print(self.c.gettags(4))
        
        

     #------------------------------------------------------------------------------------------------------------------    selectcb


    def selectcb(self,event):       #clic droit
        
        self.x,self.y=event.x,event.y 
        cercle=self.c.find_closest(self.x,self.y)
        r=30
        a,b,c,d=self.c.coords(cercle)
        if self.c.find_withtag('selectcb') or self.c.find_withtag('selectcr'):
            self.c.dtag('selectcb','selectcb')
            self.c.dtag('selectcr','selectcr')
        self.c.addtag_enclosed('pret2',a-1,b-1,c+1,d+1)
        if self.c.find_withtag('deuxiemeb'):
            self.c.dtag('deuxiemeb','deuxiemeb')
        
        self.c.addtag_withtag('deuxiemeb','pret2')
        
        for i in range(6):
            if i==0:        
                self.fleche[i]=self.c.create_line(a+r,b+r,a+r+20,b+r,arrow=tk.LAST,tags='d')         #droite 
                self.c.addtag_withtag('fleches','d')
                self.c.tag_bind(self.c.find_withtag('d'),'<Button-1>',self.droite)
            elif i==1:
                self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b+17+r,arrow=tk.LAST,tags='hd')      #bas droite   
                self.c.addtag_withtag('fleches','hd')
                self.c.tag_bind(self.c.find_withtag('hd'),'<Button-1>',self.basdroite)
            elif i==2:  
                self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b+17+r,arrow=tk.LAST,tags='hg')      #bas gauche   
                self.c.addtag_withtag('fleches','hg')
                self.c.tag_bind(self.c.find_withtag('hg'),'<Button-1>',self.basgauche)
            elif i==3:   
                self.fleche[i]=self.c.create_line(a+r,b+r,a-20+r,b+r,arrow=tk.LAST,tags='g')         #gauche 
                self.c.addtag_withtag('fleches','g')
                self.c.tag_bind(self.c.find_withtag('g'),'<Button-1>',self.gauche)
            elif i==4:
                self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b-17+r,arrow=tk.LAST,tags='bg')      #haut gauche
                self.c.addtag_withtag('fleches','bg')
                self.c.tag_bind(self.c.find_withtag('bg'),'<Button-1>',self.hautgauche)
            elif i==5:
                self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b-17+r,arrow=tk.LAST,tags='bd')     #haut droite
                self.c.addtag_withtag('fleches','bd')
                self.c.tag_bind(self.c.find_withtag('bd'),'<Button-1>',self.hautdroite)

        point=self.c.create_rectangle(a+r-10,b+r-10,a+r+10,b+r+10,fill='',outline='',tags='point')

        for i in range(6):
            g,h,j,k=self.c.coords('premiereb')
            rect=self.c.create_rectangle(g+r,h+r,g+r+1,h+r+1,fill='',outline='',tag='rectb')
                        
                
            if i==0:
                m,n,o,p=self.c.coords('point') #centre cercle sur lequel on a cliqué 
                self.c.move('point',80,0)                   #droite
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectb'):
                    self.c.addtag_overlapping('clicmoletteb',m+80,n,o+80,p)
                    self.c.addtag_overlapping('clicmoletteb',m-160,n,o-160,p)
                    self.c.tag_bind('clicmoletteb','<Button-2>',self.select3cb)
                    
                           
            elif i==1:
                self.c.move('point',-40,-69)                #haut droite
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectb'):
                    self.c.addtag_overlapping('clicmoletteb',m+40,n-69,o+40,p-69)
                    self.c.addtag_overlapping('clicmoletteb',m-80,n+138,o-80,p+138)
                    self.c.tag_bind('clicmoletteb','<Button-2>',self.select3cb)
                    
            elif i==2:
                self.c.move('point',-80,0)                #haut gauche
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectb'):
                    self.c.addtag_overlapping('clicmoletteb',m-40,n-69,o-40,p-69)
                    self.c.addtag_overlapping('clicmoletteb',m+80,n+138,o+80,p+138)
                    self.c.tag_bind('clicmoletteb','<Button-2>',self.select3cb)
                
                    
            elif i==3:
                self.c.move('point',-40,69)                #gauche
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectb'):
                    self.c.addtag_overlapping('clicmoletteb',m-80,n,o-80,p)
                    self.c.addtag_overlapping('clicmoletteb',m+160,n,o+160,p)
                    self.c.tag_bind('clicmoletteb','<Button-2>',self.select3cb)
                                
                    
            elif i==4:
                self.c.move('point',40,69)                #bas gauche
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectb'):
                    self.c.addtag_overlapping('clicmoletteb',m-40,n+69,o-40,p+69)
                    self.c.addtag_overlapping('clicmoletteb',m+80,n-138,o+80,p-138)
                    self.c.tag_bind('clicmoletteb','<Button-2>',self.select3cb)
                
            elif i==5:
                self.c.move('point',80,0)                #bas droite
                m,n,o,p=self.c.coords('point')
                if self.c.find_enclosed(m+1,n+1,o,p)==self.c.find_withtag('rectb'):
                    self.c.addtag_overlapping('clicmoletteb',m+40,n+69,o+40,p+69)
                    self.c.addtag_overlapping('clicmoletteb',m-80,n-138,o-80,p-138)
                    self.c.tag_bind('clicmoletteb','<Button-2>',self.select3cb)
        

        self.c.delete(point) 
        self.c.delete('point')
        self.c.delete('rectb')
        self.c.dtag('rectb','rectb')
        self.c.dtag('cr','clicmoletteb')
        self.c.dtag('cb','clicmoletter')
        self.c.dtag('selectcr','selectcr')
        self.c.dtag('selectcb','selectcb')
        self.c.dtag('fond','clicmoletteb')
        self.c.dtag('fond','clicmoletter')
        


        

    #------------------------------------------------------------------------------------------------------------------         select3cr

    def select3cr(self,event):          #clic molette
        self.x,self.y=event.x,event.y 
        cercle=self.c.find_closest(self.x,self.y)
        r=30
        a,b,c,d=self.c.coords(cercle)
        self.c.addtag_enclosed('pret3',a-1,b-1,c+1,d+1)
        if self.c.find_withtag('troisemer'):
            self.c.dtag('troisiemer','troisiemer')
        self.c.addtag_withtag('troisiemer','pret3')
        
        for i in range(6):
            if i==0:        
                self.fleche[i]=self.c.create_line(a+r,b+r,a+r+20,b+r,arrow=tk.LAST,tags='d')         #droite 
                self.c.addtag_withtag('fleches','d')
                self.c.tag_bind(self.c.find_withtag('d'),'<Button-1>',self.droite)
            elif i==1:
                self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b+17+r,arrow=tk.LAST,tags='hd')      #bas droite   
                self.c.addtag_withtag('fleches','hd')
                self.c.tag_bind(self.c.find_withtag('hd'),'<Button-1>',self.basdroite)
            elif i==2:  
                self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b+17+r,arrow=tk.LAST,tags='hg')      #bas gauche   
                self.c.addtag_withtag('fleches','hg')
                self.c.tag_bind(self.c.find_withtag('hg'),'<Button-1>',self.basgauche)
            elif i==3:   
                self.fleche[i]=self.c.create_line(a+r,b+r,a-20+r,b+r,arrow=tk.LAST,tags='g')         #gauche 
                self.c.addtag_withtag('fleches','g')
                self.c.tag_bind(self.c.find_withtag('g'),'<Button-1>',self.gauche)
            elif i==4:
                self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b-17+r,arrow=tk.LAST,tags='bg')      #haut gauche
                self.c.addtag_withtag('fleches','bg')
                self.c.tag_bind(self.c.find_withtag('bg'),'<Button-1>',self.hautgauche)
            elif i==5:
                self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b-17+r,arrow=tk.LAST,tags='bd')     #haut droite
                self.c.addtag_withtag('fleches','bd')
                self.c.tag_bind(self.c.find_withtag('bd'),'<Button-1>',self.hautdroite)
        self.c.dtag('clicmoletter','clicmoletter')



    #------------------------------------------------------------------------------------------------------------------    select3cb


    def select3cb(self,event):              #clic molette
        self.x,self.y=event.x,event.y 
        cercle=self.c.find_closest(self.x,self.y)
        r=30
        a,b,c,d=self.c.coords(cercle)
        self.c.addtag_enclosed('pret3',a-1,b-1,c+1,d+1)
        if self.c.find_withtag('troisemeb'):
            self.c.dtag('troisiemeb','troisiemeb')
        self.c.addtag_withtag('troisiemeb','pret3')
        
        for i in range(6):
            if i==0:        
                self.fleche[i]=self.c.create_line(a+r,b+r,a+r+20,b+r,arrow=tk.LAST,tags='d')         #droite 
                self.c.addtag_withtag('fleches','d')
                self.c.tag_bind(self.c.find_withtag('d'),'<Button-1>',self.droite)
            elif i==1:
                self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b+17+r,arrow=tk.LAST,tags='hd')      #bas droite   
                self.c.addtag_withtag('fleches','hd')
                self.c.tag_bind(self.c.find_withtag('hd'),'<Button-1>',self.basdroite)
            elif i==2:  
                self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b+17+r,arrow=tk.LAST,tags='hg')      #bas gauche   
                self.c.addtag_withtag('fleches','hg')
                self.c.tag_bind(self.c.find_withtag('hg'),'<Button-1>',self.basgauche)
            elif i==3:   
                self.fleche[i]=self.c.create_line(a+r,b+r,a-20+r,b+r,arrow=tk.LAST,tags='g')         #gauche 
                self.c.addtag_withtag('fleches','g')
                self.c.tag_bind(self.c.find_withtag('g'),'<Button-1>',self.gauche)
            elif i==4:
                self.fleche[i]=self.c.create_line(a+r,b+r,a-10+r,b-17+r,arrow=tk.LAST,tags='bg')      #haut gauche
                self.c.addtag_withtag('fleches','bg')
                self.c.tag_bind(self.c.find_withtag('bg'),'<Button-1>',self.hautgauche)
            elif i==5:
                self.fleche[i]=self.c.create_line(a+r,b+r,a+10+r,b-17+r,arrow=tk.LAST,tags='bd')     #haut droite
                self.c.addtag_withtag('fleches','bd')
                self.c.tag_bind(self.c.find_withtag('bd'),'<Button-1>',self.hautdroite)
        self.c.dtag('clicmoletteb','clicmoletteb')
    
    #---------------------------------------------------------------------------------------------------------------------------
    def score(self):
            self.c.delete(self.textscorer)
            self.c.delete(self.textscoreb)
            r=30
            a=len(self.c.find_withtag('cr'))
            b=len(self.c.find_withtag('cb'))
            a,b=14-a,14-b
            scorer,scoreb="{}".format(a),"{}".format(b)
            self.textscorer=self.c.create_text(150,80,text=scorer,font=('Times','26','bold'))
            self.textscoreb=self.c.create_text(1450,80,text=scoreb,font=('Times','26','bold'))
            if a>=6:
                self.c.create_text(850,20,text="Les boules bleues ont gagné",font=('Times','26','bold'))
                self.gagnant=2
            if b>=6:
                self.c.create_text(850,20,text="Les boules rouges ont gagné",font=('Times','26','bold'))
                self.gagnant=1
            if a>=6 or b>=6:
                self.conn=sqlite3.connect('Babalune.db')
                self.cursor=self.conn.cursor()
                self.j1=tk.Label(fenetre,text="Joueur Rouge: ")
                self.j1nom=tk.Entry(fenetre,textvariable=tk.StringVar())
                self.valider1=tk.Button(fenetre,text="Valider",command=self.button1)
                self.j1.pack()
                self.j1nom.pack()
                self.valider1.pack()

            
    def button1(self):
        x=self.j1nom.get()
        self.cursor.execute("""SELECT Nom FROM Joueurs""")
        user=self.cursor.fetchall()
        a=1
        for i in range(len(user)):
            if x==user[i][0]:
                print("déja dans la base de donnée")
            else:
                a+=1
        if a!=len(user):
            self.cursor.execute("""INSERT INTO Joueurs(Nom) VALUES('{}')""".format(x))
        self.cursor.execute("""SELECT idJ FROM Joueurs WHERE Nom='{}'""".format(x))
        self.nom1=self.cursor.fetchone()
        self.conn.commit()
        self.j1.pack_forget()
        self.j1nom.pack_forget()
        self.valider1.pack_forget()
        self.j2=tk.Label(fenetre,text="Joueur Bleu: ")
        self.j2nom=tk.Entry(fenetre,textvariable=tk.StringVar())
        self.valider2=tk.Button(fenetre,text="Valider",command=self.button2)
        self.j2.pack()
        self.j2nom.pack()
        self.valider2.pack()
            
        
        

        
        
    def button2(self):
        y=self.j2nom.get()
        self.j2.pack_forget()
        self.j2nom.pack_forget()
        self.valider2.pack_forget()
        self.cursor.execute("""SELECT Nom FROM Joueurs""")
        user=self.cursor.fetchall()
        a=1
        for i in range(len(user)):
            if y==user[i][0]:
                print("déja dans la base de donnée")
            else:
                a+=1
        if a!=len(user):
            self.cursor.execute("""INSERT INTO Joueurs(Nom) VALUES('{}')""".format(y))
        self.cursor.execute("""SELECT idJ FROM Joueurs WHERE Nom='{}'""".format(y))
        self.nom2=self.cursor.fetchone()
        if self.gagnant==1:
            self.gagnant=self.nom1
        elif self.gagnant==2:
            self.gagnant=self.nom2
        self.cursor.execute("""INSERT INTO Parties(NumJ1,NumJ2,Gagnant,Tours) VALUES ('{}','{}','{}','{}')""".format(self.nom1[0],self.nom2[0],self.gagnant[0],self.tour))  #A COMPLETER
        self.conn.commit()
        self.conn.close()

    #------------------------------------------------------------------------------------------------------------------     basdroite

    def basdroite(self,event):
        
        def deplbd():
            self.c.move('depl',40,69)
            self.c.move('pret2',40,69)
            self.c.move('pret3',40,69)
            self.c.move('pret4',40,69)
            self.c.move('pret5',40,69)
            self.c.dtag('selectcr','selectcr')
            self.c.dtag('selectcb','selectcb')
            x,y,z,w=self.c.coords('depl')
            if y+r>785:                     #bas
                self.c.delete('depl')
            elif x+r>1010 and y+r>775:      #9eme rangée droite         
                self.c.delete('depl')
            elif x+r>1050 and y+r>710:      #8eme rangée droite
                self.c.delete('depl')
            elif x+r>1090 and y+r>640:      #7eme rangée droite 
                self.c.delete('depl')
            elif x+r>1130 and y+r>540:      #6eme rangée droite
                self.c.delete('depl')
                
            if self.c.find_withtag('pret2'):
                a,b,c,d=self.c.coords('pret2')            
                if b+r>785:                     #bas
                    self.c.delete('pret2')
                elif a+r>1010 and b+r>775:      #9eme rangée droite         
                    self.c.delete('pret2')
                elif a+r>1050 and b+r>710:      #8eme rangée droite
                    self.c.delete('pret2')
                elif a+r>1090 and b+r>640:      #7eme rangée droite 
                    self.c.delete('pret2')
                elif a+r>1130 and b+r>540:      #6eme rangée droite
                    self.c.delete('pret2')
                            
            if self.c.find_withtag('pret3'):
                a,b,c,d=self.c.coords('pret3')
                if b+r>785:                     #bas
                    self.c.delete('pret3')
                elif a+r>1010 and b+r>775:      #9eme rangée droite         
                    self.c.delete('pret3')
                elif a+r>1050 and b+r>710:      #8eme rangée droite
                    self.c.delete('pret3')
                elif a+r>1090 and b+r>640:      #7eme rangée droite
                    self.c.delete('pret3')
                elif a+r>1130 and b+r>540:      #6eme rangée droite
                    self.c.delete('pret3')
            if self.c.find_withtag('pret4'):
                print("allo")
                print(self.c.coords('pret4'))
                a,b,c,d=self.c.coords('pret4')
                if b+r>785:                     #bas
                    self.c.delete('pret4')
                elif a+r>1010 and b+r>775:      #9eme rangée droite         
                    self.c.delete('pret4')
                elif a+r>1050 and b+r>710:      #8eme rangée droite
                    self.c.delete('pret4')
                elif a+r>1090 and b+r>640:      #7eme rangée droite
                    print("ouuuiiii")
                    self.c.delete('pret4')
                elif a+r>1130 and b+r>540:      #6eme rangée droite
                    self.c.delete('pret4')
                else:
                    print("noooon")
            if self.c.find_withtag('pret5'):
                a,b,c,d=self.c.coords('pret5')
                if b+r>785:                     #bas
                    self.c.delete('pret5')
                elif a+r>1010 and b+r>775:      #9eme rangée droite         
                    self.c.delete('pret5')
                elif a+r>1050 and b+r>710:      #8eme rangée droite
                    self.c.delete('pret5')
                elif a+r>1090 and b+r>640:      #7eme rangée droite 
                    self.c.delete('pret5')
                elif a+r>1130 and b+r>540:      #6eme rangée droite
                    self.c.delete('pret5')
            self.tour+=1
            self.score()
                    

        def testpousse(x):
            if len(self.c.find_withtag('test'))!=0:
                while self.c.find_withtag('test')[0] in self.c.find_withtag('depl') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret2') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+40,y+r+69,x+r+41,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
            if self.c.find_withtag('depl')[0] in self.c.find_withtag('cr'): #si on joue les boules rouges
                if not self.c.find_withtag('pret2') and x==1:  #si on ne joue qu'une boule
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+40,y+r+69,x+r+41,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplbd()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #si la boule d'apres est une boule bleue
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1 
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r+40,t+r+69,s+r+41,t+r+70) #   test sur la deuxieme boule adverse   probleme ici                                                 #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r+40,t+r+69,s+r+41,t+r+70) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplbd()                                                                                                   #changer
                            
                else:
                    print("on ne peut pas pousser nos propres boules ")
                    self.c.dtag('test','test')
                
            elif self.c.find_withtag('depl')[0] in self.c.find_withtag('cb'):  #si on joue les boules bleues
                if not self.c.find_withtag('pret2') and x==1:
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+40,y+r+69,x+r+41,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplbd()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #si la boule d'apres est une boule rouge
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r+40,t+r+69,s+r+41,t+r+70) #test sur la deuxieme boule adverse                                                             #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r+40,t+r+69,s+r+41,t+r+70) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret3','pret3')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplbd()                                                                                                   #changer

                else:
                    print("deplacement impossible1 boule b-b")
                    self.c.dtag('test','test')
                    
                        
        
            
            
            
        self.x,self.y=event.x,event.y
        self.c.delete('fleches')
        cercle=self.c.find_closest(self.x,self.y)
        self.c.addtag_closest('depl',self.x,self.y)
        x,y,z,w=self.c.coords('depl')
        r=30
        q=0
        if self.c.find_withtag('pret2'): # si il y a une deuxieme boule
            print("il y a une deuxieme boule")
            self.c.addtag_overlapping('alignés',x+r+40,y+r+69,x+r+41,y+r+70)                                                                                                   #changer
            self.c.addtag_overlapping('alignés',x+r-41,y+r-70,x+r-40,y+r-69)                                                                                                   #changer
            if self.c.find_withtag('pret2')[0] in self.c.find_withtag('alignés'): #si les boules sont alignés
                print("les boules sont alignées")
                self.c.dtag('alignés','alignés')
                self.c.addtag_overlapping('test',x+r+40,y+r+69,x+r+41,y+r+70) # test sur 2eme boule                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la premiere boule
                    print("rien apres la premiere boule")
                    deplbd()                                                                                                   #changer
                elif self.c.find_withtag('test')==self.c.find_withtag('pret2') or self.c.find_withtag('test')==self.c.find_withtag('pret3'): #si il y a une deuxieme boule
                    print("il y a une deuxieme boule de rencontréé")
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+40,y+r+69,x+r+41,y+r+70) #test sur 3eme boule                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la deuxieme boule
                        print("rien apres la deuxieme boule")
                        deplbd()                                                                                                   #changer
                    elif self.c.find_withtag('test')==self.c.find_withtag('pret3'):# si il y a la troisieme boule
                        self.c.dtag('test','test')
                        x,y,z,w=self.c.coords('pret3')
                        self.c.addtag_overlapping('test',x+r+40,y+r+69,x+r+41,y+r+70)                                                                                                   #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la 3eme boule
                            deplbd()                                                                                                   #changer
                        else: #si il y'a autre chose apres la troisieme boule
                            testpousse(3)


                            
                    else: #si il y'au autre chose apres la deuxieme boule
                        testpousse(2)
                else: #si il y a autre chose apres la premiere boule
                    testpousse(1)
            else: #si les boules ne sont pas alignées
                self.c.dtag('test','test')
                n=0
                x,y,z,w=self.c.coords('depl')
                self.c.addtag_overlapping('test',x+r+40,y+r+69,x+r+41,y+r+70)                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0:
                    n+=1
                else:
                    n+=0
                self.c.dtag('test','test')
                if self.c.find_withtag('pret2'):
                    x,y,z,w=self.c.coords('pret2')
                    self.c.addtag_overlapping('test',x+r+40,y+r+69,x+r+41,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('pret3')
                    self.c.addtag_overlapping('test',x+r+40,y+r+69,x+r+41,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    k=3
                elif self.c.find_withtag('pret2'):
                    k=2
                elif self.c.find_withtag('depl'):
                    k=1
                if k==n:
                    deplbd()                                                                                                   #changer
                        
                    
        else: #si il n'y a pas de deuxieme boule
            testpousse(1)
            
        self.c.dtag('selectcr','selectcr')
        self.c.dtag('selectcb','selectcb')
        self.c.dtag('suppr2','suppr2')
        self.c.dtag('suppr3','suppr3')
        self.c.dtag('depl','depl')
        self.c.dtag('test','test')
        self.c.dtag('pret2','pret2')
        self.c.dtag('pret3','pret3')
        self.c.dtag('pret4','pret4')
        self.c.dtag('pret5','pret5')
        self.c.dtag('deuxiemer','deuxiemer')
        self.c.dtag('deuxiemeb','deuxiemeb')
        self.c.dtag('troisiemeb','troisiemeb')
        self.c.dtag('troisiemer','troisiemer')
        self.c.dtag('premierer','premierer')
        self.c.dtag('premiereb','premiereb')
        self.c.dtag('alignés','alignés')
       
    
        
        
        
        
        
        
    #------------------------------------------------------------------------------------------------------------------     droite
    def droite(self,event):
        def depld():
            self.c.move('depl',80,0)
            self.c.move('pret2',80,0)
            self.c.move('pret3',80,0)
            self.c.move('pret4',80,0)
            self.c.move('pret5',80,0)
            
            self.c.dtag('selectcr','selectcr')
            self.c.dtag('selectcb','selectcb')
            x,y,z,w=self.c.coords('depl')
            if x+r>1010 and y+r<290:        #1ere rangée droite 
                self.c.delete('depl')
            elif x+r>1050 and y+r<360:      #2eme rangée droite
                self.c.delete('depl')
            elif x+r>1090 and y+r<430:      #3eme et 4eme rangée droite
                self.c.delete('depl')
            elif x+r>1200 and y+r<540:      #5eme rangée droite
                self.c.delete('depl')
            elif x+r>1010 and y+r>775:      #9eme rangée droite
                self.c.delete('depl')
            elif x+r>1050 and y+r>710:      #8eme rangée droite
                self.c.delete('depl')
            elif x+r>1090 and y+r>640:      #7eme rangée droite 
                self.c.delete('depl')
            elif x+r>1130 and y+r>540:      #6eme rangée droite
                self.c.delete('depl')

            if self.c.find_withtag('pret2'):
                a,b,c,d=self.c.coords('pret2')
                if a+r>1010 and b+r<290:        #1ere rangée droite 
                    self.c.delete('pret2')
                elif a+r>1050 and b+r<360:      #2eme rangée droite
                    self.c.delete('pret2')
                elif a+r>1090 and b+r<430:      #3eme et 4eme rangée droite
                    self.c.delete('pret2')
                elif a+r>1200 and b+r<540:      #5eme rangée droite
                    self.c.delete('pret2')
                elif a+r>1010 and b+r>775:      #9eme rangée droite
                    self.c.delete('pret2')
                elif a+r>1050 and b+r>710:      #8eme rangée droite
                    self.c.delete('pret2')
                elif a+r>1090 and b+r>640:      #7eme rangée droite 
                    self.c.delete('pret2')
                elif a+r>1130 and b+r>540:      #6eme rangée droite
                    self.c.delete('pret2')
            

                
            
            if self.c.find_withtag('pret3'):
                a,b,c,d=self.c.coords('pret3')
                if a+r>1010 and b+r<290:        #1ere rangée droite 
                    self.c.delete('pret3')
                elif a+r>1050 and b+r<360:      #2eme rangée droite
                    self.c.delete('pret3')
                elif a+r>1090 and b+r<430:      #3eme et 4eme rangée droite
                    self.c.delete('pret3')
                elif a+r>1200 and b+r<540:      #5eme rangée droite
                    self.c.delete('pret3')
                elif a+r>1010 and b+r>775:      #9eme rangée droite
                    self.c.delete('pret3')
                elif a+r>1050 and b+r>710:      #8eme rangée droite
                    self.c.delete('pret3')
                elif a+r>1090 and b+r>640:      #7eme rangée droite 
                    self.c.delete('pret3')
                elif a+r>1130 and b+r>540:      #6eme rangée droite
                    self.c.delete('pret3')

            if self.c.find_withtag('pret4'):
                a,b,c,d=self.c.coords('pret4')
                if a+r>1010 and b+r<290:        #1ere rangée droite 
                    self.c.delete('pret4')
                elif a+r>1050 and b+r<360:      #2eme rangée droite
                    self.c.delete('pret4')
                elif a+r>1090 and b+r<430:      #3eme et 4eme rangée droite
                    self.c.delete('pret4')
                elif a+r>1200 and b+r<540:      #5eme rangée droite
                    self.c.delete('pret4')
                elif a+r>1010 and b+r>775:      #9eme rangée droite
                    self.c.delete('pret4')
                elif a+r>1050 and b+r>710:      #8eme rangée droite
                    self.c.delete('pret4')
                elif a+r>1090 and b+r>640:      #7eme rangée droite 
                    self.c.delete('pret4')
                elif a+r>1130 and b+r>540:      #6eme rangée droite
                    self.c.delete('pret4')

            if self.c.find_withtag('pret5'):
                a,b,c,d=self.c.coords('pret5')
                if a+r>1010 and b+r<290:        #1ere rangée droite 
                    self.c.delete('pret5')
                elif a+r>1050 and b+r<360:      #2eme rangée droite
                    self.c.delete('pret5')
                elif a+r>1090 and b+r<430:      #3eme et 4eme rangée droite
                    self.c.delete('pret5')
                elif a+r>1200 and b+r<540:      #5eme rangée droite
                    self.c.delete('pret5')
                elif a+r>1010 and b+r>775:      #9eme rangée droite
                    self.c.delete('pret5')
                elif a+r>1050 and b+r>710:      #8eme rangée droite
                    self.c.delete('pret5')
                elif a+r>1090 and b+r>640:      #7eme rangée droite 
                    self.c.delete('pret5')
                elif a+r>1130 and b+r>540:      #6eme rangée droite
                    self.c.delete('pret5')
            self.tour+=1
            self.score()
            
        def testpousse(x):
            if len(self.c.find_withtag('test'))!=0:
                while self.c.find_withtag('test')[0] in self.c.find_withtag('depl') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret2') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+80,y+r,x+r+81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
            if self.c.find_withtag('depl')[0] in self.c.find_withtag('cr'): #si on joue les boules rouges
                if not self.c.find_withtag('pret2') and x==1:  #si on ne joue qu'une boule
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+80,y+r,x+r+81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        depld()
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #si la boule d'apres est une boule bleue
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1 
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r+80,t+r,s+r+81,t+r+1) #   test sur la deuxieme boule adverse   probleme ici                                                 #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r+80,t+r,s+r+81,t+r+1) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        depld()
                            
                else:
                    print("on ne peut pas pousser nos propres boules ")
                    self.c.dtag('test','test')
                
            elif self.c.find_withtag('depl')[0] in self.c.find_withtag('cb'):  #si on joue les boules bleues
                if not self.c.find_withtag('pret2') and x==1:
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+80,y+r,x+r+81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        depld()
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #si la boule d'apres est une boule rouge
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r+80,t+r,s+r+81,t+r+1) #test sur la deuxieme boule adverse                                                             #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r+80,t+r,s+r+81,t+r+1) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret3','pret3')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        depld()

                else:
                    print("deplacement impossible1 boule b-b")
                    self.c.dtag('test','test')
                    
                        
    
            
        self.x,self.y=event.x,event.y
        self.c.delete('fleches')
        cercle=self.c.find_closest(self.x,self.y)
        self.c.addtag_closest('depl',self.x,self.y)
        x,y,z,w=self.c.coords('depl')
        r=30
        q=0
        if self.c.find_withtag('pret2'): # si il y a une deuxieme boule
            print("il y a une deuxieme boule")
            self.c.addtag_overlapping('alignés',x+r+80,y+r,x+r+81,y+r+1)                                                                                                   #changer
            self.c.addtag_overlapping('alignés',x+r-81,y+r-1,x+r-80,y+r)                                                                                                   #changer
            if self.c.find_withtag('pret2')[0] in self.c.find_withtag('alignés'): #si les boules sont alignés
                print("les boules sont alignées")
                self.c.dtag('alignés','alignés')
                self.c.addtag_overlapping('test',x+r+80,y+r,x+r+81,y+r+1) # test sur 2eme boule                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la premiere boule
                    print("rien apres la premiere boule")
                    depld()
                elif self.c.find_withtag('test')==self.c.find_withtag('pret2') or self.c.find_withtag('test')==self.c.find_withtag('pret3'): #si il y a une deuxieme boule
                    print("il y a une deuxieme boule de rencontréé")
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+80,y+r,x+r+81,y+r+1) #test sur 3eme boule                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la deuxieme boule
                        print("rien apres la deuxieme boule")
                        depld()
                    elif self.c.find_withtag('test')==self.c.find_withtag('pret3'):# si il y a la troisieme boule
                        self.c.dtag('test','test')
                        x,y,z,w=self.c.coords('pret3')
                        self.c.addtag_overlapping('test',x+r+80,y+r,x+r+81,y+r+1)                                                                                                   #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la 3eme boule
                            depld()
                        else: #si il y'a autre chose apres la troisieme boule
                            testpousse(3)


                            
                    else: #si il y'au autre chose apres la deuxieme boule
                        testpousse(2)
                else: #si il y a autre chose apres la premiere boule
                    testpousse(1)
            else: #si les boules ne sont pas alignées
                self.c.dtag('test','test')
                n=0
                x,y,z,w=self.c.coords('depl')
                self.c.addtag_overlapping('test',x+r+80,y+r,x+r+81,y+r+1)                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0:
                    n+=1
                else:
                    n+=0
                self.c.dtag('test','test')
                if self.c.find_withtag('pret2'):
                    x,y,z,w=self.c.coords('pret2')
                    self.c.addtag_overlapping('test',x+r+80,y+r,x+r+81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('pret3')
                    self.c.addtag_overlapping('test',x+r+80,y+r,x+r+81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    k=3
                elif self.c.find_withtag('pret2'):
                    k=2
                elif self.c.find_withtag('depl'):
                    k=1
                if k==n:
                    depld()
                        
                    
        else: #si il n'y a pas de deuxieme boule
            testpousse(1)
            
        self.c.dtag('selectcr','selectcr')
        self.c.dtag('selectcb','selectcb')
        self.c.dtag('suppr2','suppr2')
        self.c.dtag('suppr3','suppr3')
        self.c.dtag('depl','depl')
        self.c.dtag('test','test')
        self.c.dtag('pret2','pret2')
        self.c.dtag('pret3','pret3')
        self.c.dtag('pret4','pret4')
        self.c.dtag('pret5','pret5')
        self.c.dtag('deuxiemer','deuxiemer')
        self.c.dtag('deuxiemeb','deuxiemeb')
        self.c.dtag('troisiemeb','troisiemeb')
        self.c.dtag('troisiemer','troisiemer')
        self.c.dtag('premierer','premierer')
        self.c.dtag('premiereb','premiereb')
        self.c.dtag('alignés','alignés')
        
    #------------------------------------------------------------------------------------------------------------------     basgauche
    def basgauche(self,event):
        def deplbg():
            self.c.move('depl',-40,69)
            self.c.move('pret2',-40,69)
            self.c.move('pret3',-40,69)
            self.c.move('pret4',-40,69)
            self.c.move('pret5',-40,69)
            self.c.dtag('selectcr','selectcr')
            self.c.dtag('selectcb','selectcb')
            x,y,z,w=self.c.coords('depl')

            
            if y+r>785:                     #bas
                self.c.delete('depl')
            elif x+r<560 and y+r>540:       #6eme rangée gauche
                self.c.delete('depl')
            elif x+r<600 and y+r>640:       #7eme rangée gauche
                self.c.delete('depl')
            elif x+r<640 and y+r>710:       #8eme rangée gauche
                self.c.delete('depl')
            elif x+r<680 and y+r>775:       #9eme rangée gauche
                self.c.delete('depl')

            if self.c.find_withtag('pret2'):
                a,b,c,d=self.c.coords('pret2')
                if b+r>785:                     #bas
                    self.c.delete('pret2')
                elif a+r<560 and b+r>540:       #6eme rangée gauche
                    self.c.delete('pret2')
                elif a+r<600 and b+r>640:       #7eme rangée gauche
                    self.c.delete('pret2')
                elif a+r<640 and b+r>710:       #8eme rangée gauche
                    self.c.delete('pret2')
                elif a+r<680 and b+r>775:       #9eme rangée gauche
                    self.c.delete('pret2')

            if self.c.find_withtag('pret3'):
                a,b,c,d=self.c.coords('pret3')
                if b+r>785:                     #bas
                    self.c.delete('pret3')
                elif a+r<560 and b+r>540:       #6eme rangée gauche
                    self.c.delete('pret3')
                elif a+r<600 and b+r>640:       #7eme rangée gauche
                    self.c.delete('pret3')
                elif a+r<640 and b+r>710:       #8eme rangée gauche
                    self.c.delete('pret3')
                elif a+r<680 and b+r>775:       #9eme rangée gauche
                    self.c.delete('pret3')
                    
            if self.c.find_withtag('pret4'):
                a,b,c,d=self.c.coords('pret4')
                if b+r>785:                     #bas
                    self.c.delete('pret4')
                elif a+r<560 and b+r>540:       #6eme rangée gauche
                    self.c.delete('pret4')
                elif a+r<600 and b+r>640:       #7eme rangée gauche
                    self.c.delete('pret4')
                elif a+r<640 and b+r>710:       #8eme rangée gauche
                    self.c.delete('pret4')
                elif a+r<680 and b+r>775:       #9eme rangée gauche
                    self.c.delete('pret4')
                    
            if self.c.find_withtag('pret5'):
                a,b,c,d=self.c.coords('pret5')
                if b+r>785:                     #bas
                    self.c.delete('pret5')
                elif a+r<560 and b+r>540:       #6eme rangée gauche
                    self.c.delete('pret5')
                elif a+r<600 and b+r>640:       #7eme rangée gauche
                    self.c.delete('pret5')
                elif a+r<640 and b+r>710:       #8eme rangée gauche
                    self.c.delete('pret5')
                elif a+r<680 and b+r>775:       #9eme rangée gauche
                    self.c.delete('pret5')
            self.tour+=1
            self.score()
            
        def testpousse(x):
            if len(self.c.find_withtag('test'))!=0:
                while self.c.find_withtag('test')[0] in self.c.find_withtag('depl') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret2') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-41,y+r+69,x+r-40,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
            if self.c.find_withtag('depl')[0] in self.c.find_withtag('cr'): #si on joue les boules rouges
                if not self.c.find_withtag('pret2') and x==1:  #si on ne joue qu'une boule
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-41,y+r+69,x+r-40,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplbg()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #si la boule d'apres est une boule bleue
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1 
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r-41,t+r+69,s+r-40,t+r+70) #   test sur la deuxieme boule adverse   probleme ici                                                 #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r-41,t+r+69,s+r-40,t+r+70) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplbg()                                                                                                   #changer
                            
                else:
                    print("on ne peut pas pousser nos propres boules ")
                    self.c.dtag('test','test')
                
            elif self.c.find_withtag('depl')[0] in self.c.find_withtag('cb'):  #si on joue les boules bleues
                if not self.c.find_withtag('pret2') and x==1:
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-41,y+r+69,x+r-40,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplbg()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #si la boule d'apres est une boule rouge
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r-41,t+r+69,s+r-40,t+r+70) #test sur la deuxieme boule adverse                                                             #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r-41,t+r+69,s+r-40,t+r+70) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret3','pret3')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplbg()                                                                                                   #changer

                else:
                    print("deplacement impossible1 boule b-b")
                    self.c.dtag('test','test')
                    
                        
    
            
        self.x,self.y=event.x,event.y
        self.c.delete('fleches')
        cercle=self.c.find_closest(self.x,self.y)
        self.c.addtag_closest('depl',self.x,self.y)
        x,y,z,w=self.c.coords('depl')
        r=30
        q=0
        if self.c.find_withtag('pret2'): # si il y a une deuxieme boule
            print("il y a une deuxieme boule")
            self.c.addtag_overlapping('alignés',x+r-41,y+r+69,x+r-40,y+r+70)                                                                                                   #changer
            self.c.addtag_overlapping('alignés',x+r+40,y+r-70,x+r+41,y+r-69)                                                                                                   #changer
            if self.c.find_withtag('pret2')[0] in self.c.find_withtag('alignés'): #si les boules sont alignés
                print("les boules sont alignées")
                self.c.dtag('alignés','alignés')
                self.c.addtag_overlapping('test',x+r-41,y+r+69,x+r-40,y+r+70) # test sur 2eme boule                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la premiere boule
                    print("rien apres la premiere boule")
                    deplbg()                                                                                                   #changer
                elif self.c.find_withtag('test')==self.c.find_withtag('pret2') or self.c.find_withtag('test')==self.c.find_withtag('pret3'): #si il y a une deuxieme boule
                    print("il y a une deuxieme boule de rencontréé")
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-41,y+r+69,x+r-40,y+r+70) #test sur 3eme boule                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la deuxieme boule
                        print("rien apres la deuxieme boule")
                        deplbg()                                                                                                   #changer
                    elif self.c.find_withtag('test')==self.c.find_withtag('pret3'):# si il y a la troisieme boule
                        self.c.dtag('test','test')
                        x,y,z,w=self.c.coords('pret3')
                        self.c.addtag_overlapping('test',x+r-41,y+r+69,x+r-40,y+r+70)                                                                                                   #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la 3eme boule
                            deplbg()                                                                                                   #changer
                        else: #si il y'a autre chose apres la troisieme boule
                            testpousse(3)


                            
                    else: #si il y'au autre chose apres la deuxieme boule
                        testpousse(2)
                else: #si il y a autre chose apres la premiere boule
                    testpousse(1)
            else: #si les boules ne sont pas alignées
                self.c.dtag('test','test')
                n=0
                x,y,z,w=self.c.coords('depl')
                self.c.addtag_overlapping('test',x+r-41,y+r+69,x+r-40,y+r+70)                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0:
                    n+=1
                else:
                    n+=0
                self.c.dtag('test','test')
                if self.c.find_withtag('pret2'):
                    x,y,z,w=self.c.coords('pret2')
                    self.c.addtag_overlapping('test',x+r-41,y+r+69,x+r-40,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('pret3')
                    self.c.addtag_overlapping('test',x+r-41,y+r+69,x+r-40,y+r+70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    k=3
                elif self.c.find_withtag('pret2'):
                    k=2
                elif self.c.find_withtag('depl'):
                    k=1
                if k==n:
                    deplbg()                                                                                                   #changer
                        
                    
        else: #si il n'y a pas de deuxieme boule
            testpousse(1)
            
        self.c.dtag('selectcr','selectcr')
        self.c.dtag('selectcb','selectcb')
        self.c.dtag('suppr2','suppr2')
        self.c.dtag('suppr3','suppr3')
        self.c.dtag('depl','depl')
        self.c.dtag('test','test')
        self.c.dtag('pret2','pret2')
        self.c.dtag('pret3','pret3')
        self.c.dtag('pret4','pret4')
        self.c.dtag('pret5','pret5')
        self.c.dtag('deuxiemer','deuxiemer')
        self.c.dtag('deuxiemeb','deuxiemeb')
        self.c.dtag('troisiemeb','troisiemeb')
        self.c.dtag('troisiemer','troisiemer')
        self.c.dtag('premierer','premierer')
        self.c.dtag('premiereb','premiereb')
        self.c.dtag('alignés','alignés')
        
        
    #-------------------------------------------------------------------------------------------------------------------    gauche 
    def gauche(self,event):
        
        def deplg():
            self.c.move('depl',-80,0)
            self.c.move('pret2',-80,0)
            self.c.move('pret3',-80,0)
            self.c.move('pret4',-80,0)
            self.c.move('pret5',-80,0)
            self.c.dtag('selectcr','selectcr')
            self.c.dtag('selectcb','selectcb')
            x,y,z,w=self.c.coords('depl')
            if x+r<680 and y+r<290:         #1ere rangée gauche
                self.c.delete('depl')
            elif x+r<640 and y+r<360:       #2eme rangée gauche
                self.c.delete('depl')
            elif x+r<600 and y+r<430:       #3eme et 4eme rangée gauche
                self.c.delete('depl')
            elif x+r<490 and y+r<540:       #5eme rangée gauche
                self.c.delete('depl')
            elif x+r<560 and y+r>540:       #6eme rangée gauche
                self.c.delete('depl')
            elif x+r<600 and y+r>640:       #7eme rangée gauche
                self.c.delete('depl')
            elif x+r<640 and y+r>710:       #8eme rangée gauche
                self.c.delete('depl')
            elif x+r<680 and y+r>775:       #9eme rangée gauche
                self.c.delete('depl')

            if self.c.find_withtag('pret2'):
                a,b,c,d=self.c.coords('pret2')
                if a+r<680 and b+r<290:         #1ere rangée gauche
                    self.c.delete('pret2')
                elif a+r<640 and b+r<360:       #2eme rangée gauche
                    self.c.delete('pret2')
                elif a+r<600 and b+r<430:       #3eme et 4eme rangée gauche
                    self.c.delete('pret2')
                elif a+r<490 and b+r<540:       #5eme rangée gauche
                    self.c.delete('pret2')
                elif a+r<560 and b+r>540:       #6eme rangée gauche
                    self.c.delete('pret2')
                elif a+r<600 and b+r>640:       #7eme rangée gauche
                    self.c.delete('pret2')
                elif a+r<640 and b+r>710:       #8eme rangée gauche
                    self.c.delete('pret2')
                elif a+r<680 and b+r>775:       #9eme rangée gauche
                    self.c.delete('pret2')

            if self.c.find_withtag('pret3'):
                a,b,c,d=self.c.coords('pret3')
                if a+r<680 and b+r<290:         #1ere rangée gauche
                    self.c.delete('pret3')
                elif a+r<640 and b+r<360:       #2eme rangée gauche
                    self.c.delete('pret3')
                elif a+r<600 and b+r<430:       #3eme et 4eme rangée gauche
                    self.c.delete('pret3')
                elif a+r<490 and b+r<540:       #5eme rangée gauche
                    self.c.delete('pret3')
                elif a+r<560 and b+r>540:       #6eme rangée gauche
                    self.c.delete('pret3')
                elif a+r<600 and b+r>640:       #7eme rangée gauche
                    self.c.delete('pret3')
                elif a+r<640 and b+r>710:       #8eme rangée gauche
                    self.c.delete('pret3')
                elif a+r<680 and b+r>775:       #9eme rangée gauche
                    self.c.delete('pret3')
                    
            if self.c.find_withtag('pret4'):
                a,b,c,d=self.c.coords('pret4')
                if a+r<680 and b+r<290:         #1ere rangée gauche
                    self.c.delete('pret4')
                elif a+r<640 and b+r<360:       #2eme rangée gauche
                    self.c.delete('pret4')
                elif a+r<600 and b+r<430:       #3eme et 4eme rangée gauche
                    self.c.delete('pret4')
                elif a+r<490 and b+r<540:       #5eme rangée gauche
                    self.c.delete('pret4')
                elif a+r<560 and b+r>540:       #6eme rangée gauche
                    self.c.delete('pret4')
                elif a+r<600 and b+r>640:       #7eme rangée gauche
                    self.c.delete('pret4')
                elif a+r<640 and b+r>710:       #8eme rangée gauche
                    self.c.delete('pret4')
                elif a+r<680 and b+r>775:       #9eme rangée gauche
                    self.c.delete('pret4')

            if self.c.find_withtag('pret5'):
                a,b,c,d=self.c.coords('pret5')
                if a+r<680 and b+r<290:         #1ere rangée gauche
                    self.c.delete('pret5')
                elif a+r<640 and b+r<360:       #2eme rangée gauche
                    self.c.delete('pret5')
                elif a+r<600 and b+r<430:       #3eme et 4eme rangée gauche
                    self.c.delete('pret5')
                elif a+r<490 and b+r<540:       #5eme rangée gauche
                    self.c.delete('pret5')
                elif a+r<560 and b+r>540:       #6eme rangée gauche
                    self.c.delete('pret5')
                elif a+r<600 and b+r>640:       #7eme rangée gauche
                    self.c.delete('pret5')
                elif a+r<640 and b+r>710:       #8eme rangée gauche
                    self.c.delete('pret5')
                elif a+r<680 and b+r>775:       #9eme rangée gauche
                    self.c.delete('pret5')
            self.tour+=1
            self.score()
        def testpousse(x):
            if len(self.c.find_withtag('test'))!=0:
                while self.c.find_withtag('test')[0] in self.c.find_withtag('depl') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret2') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-80,y+r,x+r-81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
            if self.c.find_withtag('depl')[0] in self.c.find_withtag('cr'): #si on joue les boules rouges
                if not self.c.find_withtag('pret2') and x==1:  #si on ne joue qu'une boule
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-80,y+r,x+r-81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplg()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #si la boule d'apres est une boule bleue
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1 
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r-80,t+r,s+r-81,t+r+1) #   test sur la deuxieme boule adverse   probleme ici                                                 #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r-80,t+r,s+r-81,t+r+1) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplg()                                                                                                   #changer
                            
                else:
                    print("on ne peut pas pousser nos propres boules ")
                    self.c.dtag('test','test')
                
            elif self.c.find_withtag('depl')[0] in self.c.find_withtag('cb'):  #si on joue les boules bleues
                if not self.c.find_withtag('pret2') and x==1:
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-80,y+r,x+r-81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplg()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #si la boule d'apres est une boule rouge
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r-80,t+r,s+r-81,t+r+1) #test sur la deuxieme boule adverse                                                             #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r-80,t+r,s+r-81,t+r+1) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret3','pret3')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplg()                                                                                                   #changer

                else:
                    print("deplacement impossible1 boule b-b")
                    self.c.dtag('test','test')
                    
                        
    
            
        self.x,self.y=event.x,event.y
        self.c.delete('fleches')
        cercle=self.c.find_closest(self.x,self.y)
        self.c.addtag_closest('depl',self.x,self.y)
        x,y,z,w=self.c.coords('depl')
        r=30
        q=0
        if self.c.find_withtag('pret2'): # si il y a une deuxieme boule
            print("il y a une deuxieme boule")
            self.c.addtag_overlapping('alignés',x+r-80,y+r,x+r-81,y+r+1)                                                                                                   #changer
            self.c.addtag_overlapping('alignés',x+r+80,y+r,x+r+81,y+r+1)                                                                                                   #changer
            if self.c.find_withtag('pret2')[0] in self.c.find_withtag('alignés'): #si les boules sont alignés
                print("les boules sont alignées")
                self.c.dtag('alignés','alignés')
                self.c.addtag_overlapping('test',x+r-80,y+r,x+r-81,y+r+1) # test sur 2eme boule                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la premiere boule
                    print("rien apres la premiere boule")
                    deplg()                                                                                                   #changer
                elif self.c.find_withtag('test')==self.c.find_withtag('pret2') or self.c.find_withtag('test')==self.c.find_withtag('pret3'): #si il y a une deuxieme boule
                    print("il y a une deuxieme boule de rencontréé")
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-80,y+r,x+r-81,y+r+1) #test sur 3eme boule                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la deuxieme boule
                        print("rien apres la deuxieme boule")
                        deplg()                                                                                                   #changer
                    elif self.c.find_withtag('test')==self.c.find_withtag('pret3'):# si il y a la troisieme boule
                        self.c.dtag('test','test')
                        x,y,z,w=self.c.coords('pret3')
                        self.c.addtag_overlapping('test',x+r-80,y+r,x+r-81,y+r+1)                                                                                                   #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la 3eme boule
                            deplg()                                                                                                   #changer
                        else: #si il y'a autre chose apres la troisieme boule
                            testpousse(3)


                            
                    else: #si il y'au autre chose apres la deuxieme boule
                        testpousse(2)
                else: #si il y a autre chose apres la premiere boule
                    testpousse(1)
            else: #si les boules ne sont pas alignées
                self.c.dtag('test','test')
                n=0
                x,y,z,w=self.c.coords('depl')
                self.c.addtag_overlapping('test',x+r-80,y+r,x+r-81,y+r+1)                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0:
                    n+=1
                else:
                    n+=0
                self.c.dtag('test','test')
                if self.c.find_withtag('pret2'):
                    x,y,z,w=self.c.coords('pret2')
                    self.c.addtag_overlapping('test',x+r-80,y+r,x+r-81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('pret3')
                    self.c.addtag_overlapping('test',x+r-80,y+r,x+r-81,y+r+1)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    k=3
                elif self.c.find_withtag('pret2'):
                    k=2
                elif self.c.find_withtag('depl'):
                    k=1
                if k==n:
                    deplg()                                                                                                   #changer
                        
                    
        else: #si il n'y a pas de deuxieme boule
            testpousse(1)
            
        self.c.dtag('selectcr','selectcr')
        self.c.dtag('selectcb','selectcb')
        self.c.dtag('suppr2','suppr2')
        self.c.dtag('suppr3','suppr3')
        self.c.dtag('depl','depl')
        self.c.dtag('test','test')
        self.c.dtag('pret2','pret2')
        self.c.dtag('pret3','pret3')
        self.c.dtag('pret4','pret4')
        self.c.dtag('pret5','pret5')
        self.c.dtag('deuxiemer','deuxiemer')
        self.c.dtag('deuxiemeb','deuxiemeb')
        self.c.dtag('troisiemeb','troisiemeb')
        self.c.dtag('troisiemer','troisiemer')
        self.c.dtag('premierer','premierer')
        self.c.dtag('premiereb','premiereb')
        self.c.dtag('alignés','alignés')
            
        
    #------------------------------------------------------------------------------------------------------------------    hautgauche
    def hautgauche(self,event):
        def deplhg():
            self.c.move('depl',-40,-69)
            self.c.move('pret2',-40,-69)
            self.c.move('pret3',-40,-69)
            self.c.move('pret4',-40,-69)
            self.c.move('pret5',-40,-69)
            
            self.c.dtag('selectcr','selectcr')
            self.c.dtag('selectcb','selectcb')
            x,y,z,w=self.c.coords('depl')
            if y+r<225:                       #haut
                self.c.delete('depl')
            elif x+r<680 and y+r<290:         #1ere rangée gauche
                self.c.delete('depl')
            elif x+r<640 and y+r<360:       #2eme rangée gauche
                self.c.delete('depl')
            elif x+r<600 and y+r<430:       #3eme et 4eme rangée gauche
                self.c.delete('depl')
            elif x+r<490 and y+r<540:
                self.c.delete('depl')

            if self.c.find_withtag('pret2'):
                a,b,c,d=self.c.coords('pret2')
                if self.c.find_withtag('pret2'):
                    if b+r<225:                       #haut
                        self.c.delete('pret2')
                    elif a+r<680 and b+r<290:         #1ere rangée gauche
                        self.c.delete('pret2')
                    elif a+r<640 and b+r<360:       #2eme rangée gauche
                        self.c.delete('pret2')
                    elif a+r<600 and b+r<430:       #3eme et 4eme rangée gauche
                        self.c.delete('pret2')
                    elif a+r<490 and b+r<540:
                        self.c.delete('pret2')
                        
            if self.c.find_withtag('pret3'):
                a,b,c,d=self.c.coords('pret3')
                if self.c.find_withtag('pret3'):
                    if b+r<225:                       #haut
                        self.c.delete('pret3')
                    elif a+r<680 and b+r<290:         #1ere rangée gauche
                        self.c.delete('pret3')
                    elif a+r<640 and b+r<360:       #2eme rangée gauche
                        self.c.delete('pret3')
                    elif a+r<600 and b+r<430:       #3eme et 4eme rangée gauche
                        self.c.delete('pret3')
                    elif a+r<490 and b+r<540:
                        self.c.delete('pret3')
            if self.c.find_withtag('pret4'):
                a,b,c,d=self.c.coords('pret4')
                if self.c.find_withtag('pret4'):
                    if b+r<225:                       #haut
                        self.c.delete('pret4')
                    elif a+r<680 and b+r<290:         #1ere rangée gauche
                        self.c.delete('pret4')
                    elif a+r<640 and b+r<360:       #2eme rangée gauche
                        self.c.delete('pret4')
                    elif a+r<600 and b+r<430:       #3eme et 4eme rangée gauche
                        self.c.delete('pret4')
                    elif a+r<490 and b+r<540:
                        self.c.delete('pret4')
            if self.c.find_withtag('pret5'):
                a,b,c,d=self.c.coords('pret5')
                if self.c.find_withtag('pret5'):
                    if b+r<225:                       #haut
                        self.c.delete('pret5')
                    elif a+r<680 and b+r<290:         #1ere rangée gauche
                        self.c.delete('pret5')
                    elif a+r<640 and b+r<360:       #2eme rangée gauche
                        self.c.delete('pret5')
                    elif a+r<600 and b+r<430:       #3eme et 4eme rangée gauche
                        self.c.delete('pret5')
                    elif a+r<490 and b+r<540:
                        self.c.delete('pret5')
            self.tour+=1
            self.score()
            
            
        def testpousse(x):
            if len(self.c.find_withtag('test'))!=0:
                while self.c.find_withtag('test')[0] in self.c.find_withtag('depl') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret2') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-40,y+r-69,x+r-41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
            if self.c.find_withtag('depl')[0] in self.c.find_withtag('cr'): #si on joue les boules rouges
                if not self.c.find_withtag('pret2') and x==1:  #si on ne joue qu'une boule
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-40,y+r-69,x+r-41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplhg()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #si la boule d'apres est une boule bleue
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1 
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r-40,t+r-69,s+r-41,t+r-70) #   test sur la deuxieme boule adverse   probleme ici                                                 #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r-40,t+r-69,s+r-41,t+r-70) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplhg()                                                                                                   #changer
                            
                else:
                    print("on ne peut pas pousser nos propres boules ")
                    self.c.dtag('test','test')
                
            elif self.c.find_withtag('depl')[0] in self.c.find_withtag('cb'):  #si on joue les boules bleues
                if not self.c.find_withtag('pret2') and x==1:
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-40,y+r-69,x+r-41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplhg()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #si la boule d'apres est une boule rouge
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r-40,t+r-69,s+r-41,t+r-70) #test sur la deuxieme boule adverse                                                             #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r-40,t+r-69,s+r-41,t+r-70) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret3','pret3')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplhg()                                                                                                   #changer

                else:
                    print("deplacement impossible1 boule b-b")
                    self.c.dtag('test','test')
                    
                        
    
            
        self.x,self.y=event.x,event.y
        self.c.delete('fleches')
        cercle=self.c.find_closest(self.x,self.y)
        self.c.addtag_closest('depl',self.x,self.y)
        x,y,z,w=self.c.coords('depl')
        r=30
        q=0
        if self.c.find_withtag('pret2'): # si il y a une deuxieme boule
            print("il y a une deuxieme boule")
            self.c.addtag_overlapping('alignés',x+r-40,y+r-69,x+r-41,y+r-70)                                                                                                   #changer
            self.c.addtag_overlapping('alignés',x+r+41,y+r+70,x+r+40,y+r+69)                                                                                                   #changer
            if self.c.find_withtag('pret2')[0] in self.c.find_withtag('alignés'): #si les boules sont alignés
                print("les boules sont alignées")
                self.c.dtag('alignés','alignés')
                self.c.addtag_overlapping('test',x+r-40,y+r-69,x+r-41,y+r-70) # test sur 2eme boule                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la premiere boule
                    print("rien apres la premiere boule")
                    deplhg()                                                                                                   #changer
                elif self.c.find_withtag('test')==self.c.find_withtag('pret2') or self.c.find_withtag('test')==self.c.find_withtag('pret3'): #si il y a une deuxieme boule
                    print("il y a une deuxieme boule de rencontréé")
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r-40,y+r-69,x+r-41,y+r-70) #test sur 3eme boule                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la deuxieme boule
                        print("rien apres la deuxieme boule")
                        deplhg()                                                                                                   #changer
                    elif self.c.find_withtag('test')==self.c.find_withtag('pret3'):# si il y a la troisieme boule
                        self.c.dtag('test','test')
                        x,y,z,w=self.c.coords('pret3')
                        self.c.addtag_overlapping('test',x+r-40,y+r-69,x+r-41,y+r-70)                                                                                                   #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la 3eme boule
                            deplhg()                                                                                                   #changer
                        else: #si il y'a autre chose apres la troisieme boule
                            testpousse(3)


                            
                    else: #si il y'au autre chose apres la deuxieme boule
                        testpousse(2)
                else: #si il y a autre chose apres la premiere boule
                    testpousse(1)
            else: #si les boules ne sont pas alignées
                self.c.dtag('test','test')
                n=0
                x,y,z,w=self.c.coords('depl')
                self.c.addtag_overlapping('test',x+r-40,y+r-69,x+r-41,y+r-70)                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0:
                    n+=1
                else:
                    n+=0
                self.c.dtag('test','test')
                if self.c.find_withtag('pret2'):
                    x,y,z,w=self.c.coords('pret2')
                    self.c.addtag_overlapping('test',x+r-40,y+r-69,x+r-41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('pret3')
                    self.c.addtag_overlapping('test',x+r-40,y+r-69,x+r-41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    k=3
                elif self.c.find_withtag('pret2'):
                    k=2
                elif self.c.find_withtag('depl'):
                    k=1
                if k==n:
                    deplhg()                                                                                                   #changer
                        
                    
        else: #si il n'y a pas de deuxieme boule
            testpousse(1)
            
        self.c.dtag('selectcr','selectcr')
        self.c.dtag('selectcb','selectcb')
        self.c.dtag('suppr2','suppr2')
        self.c.dtag('suppr3','suppr3')
        self.c.dtag('depl','depl')
        self.c.dtag('test','test')
        self.c.dtag('pret2','pret2')
        self.c.dtag('pret3','pret3')
        self.c.dtag('pret4','pret4')
        self.c.dtag('pret5','pret5')
        self.c.dtag('deuxiemer','deuxiemer')
        self.c.dtag('deuxiemeb','deuxiemeb')
        self.c.dtag('troisiemeb','troisiemeb')
        self.c.dtag('troisiemer','troisiemer')
        self.c.dtag('premierer','premierer')
        self.c.dtag('premiereb','premiereb')
        self.c.dtag('alignés','alignés')
        
        
    #------------------------------------------------------------------------------------------------------------------    hautdroite
    def hautdroite(self,event):
        def deplhd():
            self.c.move('depl',40,-69)
            self.c.move('pret2',40,-69)
            self.c.move('pret3',40,-69)
            self.c.move('pret4',40,-69)
            self.c.move('pret5',40,-69)
            self.c.dtag('selectcr','selectcr')
            self.c.dtag('selectcb','selectcb')
            x,y,z,w=self.c.coords('depl')
            
            if y+r<225:                     #haut
                self.c.delete('depl')
            elif x+r>1010 and y+r<290:      #1ere rangée droite 
                self.c.delete('depl')
            elif x+r>1050 and y+r<360:      #2eme rangée droite
                self.c.delete('depl')
            elif x+r>1090 and y+r<430:      #3eme et 4eme rangée droite
                self.c.delete('depl')
            elif x+r>1200 and y+r<540:
                self.c.delete('depl')
                

            if self.c.find_withtag('pret2'):
                a,b,c,d=self.c.coords('pret2')
                if b+r<225:                     #haut
                    self.c.delete('pret2')
                elif a+r>1010 and b+r<290:      #1ere rangée droite 
                    self.c.delete('pret2')
                elif a+r>1050 and b+r<360:      #2eme rangée droite
                    self.c.delete('pret2')
                elif a+r>1090 and b+r<430:      #3eme et 4eme rangée droite
                    self.c.delete('pret2')
                elif a+r>1200 and b+r<540:
                    self.c.delete('pret2')
            if self.c.find_withtag('pret3'):
                a,b,c,d=self.c.coords('pret3')
                if b+r<225:                     #haut
                    self.c.delete('pret3')
                elif a+r>1010 and b+r<290:      #1ere rangée droite 
                    self.c.delete('pret3')
                elif a+r>1050 and b+r<360:      #2eme rangée droite
                    self.c.delete('pret3')
                elif a+r>1090 and b+r<430:      #3eme et 4eme rangée droite
                    self.c.delete('pret3')
                elif a+r>1200 and b+r<540:
                    self.c.delete('pret3')
            if self.c.find_withtag('pret4'):
                a,b,c,d=self.c.coords('pret4')
                if b+r<225:                     #haut
                    self.c.delete('pret4')
                elif a+r>1010 and b+r<290:      #1ere rangée droite 
                    self.c.delete('pret4')
                elif a+r>1050 and b+r<360:      #2eme rangée droite
                    self.c.delete('pret4')
                elif a+r>1090 and b+r<430:      #3eme et 4eme rangée droite
                    self.c.delete('pret4')
                elif a+r>1200 and b+r<540:
                    self.c.delete('pret4')

            if self.c.find_withtag('pret5'):
                a,b,c,d=self.c.coords('pret5')
                if b+r<225:                     #haut
                    self.c.delete('pret5')
                elif a+r>1010 and b+r<290:      #1ere rangée droite 
                    self.c.delete('pret5')
                elif a+r>1050 and b+r<360:      #2eme rangée droite
                    self.c.delete('pret5')
                elif a+r>1090 and b+r<430:      #3eme et 4eme rangée droite
                    self.c.delete('pret5')
                elif a+r>1200 and b+r<540:
                    self.c.delete('pret5')
            self.tour+=1
            self.score()
                
            
            
        def testpousse(x):
            if len(self.c.find_withtag('test'))!=0:
                while self.c.find_withtag('test')[0] in self.c.find_withtag('depl') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret2') or self.c.find_withtag('test')[0] in self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+40,y+r-69,x+r+41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
            if self.c.find_withtag('depl')[0] in self.c.find_withtag('cr'): #si on joue les boules rouges
                if not self.c.find_withtag('pret2') and x==1:  #si on ne joue qu'une boule
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+40,y+r-69,x+r+41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplhd()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #si la boule d'apres est une boule bleue
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1 
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r+40,t+r-69,s+r+41,t+r-70) #   test sur la deuxieme boule adverse   probleme ici                                                 #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r+40,t+r-69,s+r+41,t+r-70) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplhd()                                                                                                   #changer
                            
                else:
                    print("on ne peut pas pousser nos propres boules ")
                    self.c.dtag('test','test')
                
            elif self.c.find_withtag('depl')[0] in self.c.find_withtag('cb'):  #si on joue les boules bleues
                if not self.c.find_withtag('pret2') and x==1:
                    x,y,z,w=self.c.coords('depl')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+40,y+r-69,x+r+41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        deplhd()                                                                                                   #changer
                    else:
                        print("une boule seule ne peut pas pousser une autre boule")
                elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #si la boule d'apres est une boule rouge
                    if self.c.find_withtag('pret3'): #si on joue trois boules
                        h=3
                    elif self.c.find_withtag('pret2'): #si on joue 2 boules
                        h=2
                    else:
                        h=1
                    s,t,u,v=self.c.coords('test')
                    j=1
                    self.c.addtag_withtag('pret4','test') #on prepare la 1ere boule a se faire deplacer
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',s+r+40,t+r-69,s+r+41,t+r-70) #test sur la deuxieme boule adverse                                                             #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la premiere boule bleue
                        j=1
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cb'): #changer  si on retombe sur une boule de notre couleur
                        print("on ne peut pas se déplacer contre une boule de notre couleur")
                        j=99
                    elif self.c.find_withtag('test')[0] in self.c.find_withtag('cr'): #changer  si on continue dans les boules adverses
                        s,t,u,v=self.c.coords('test')
                        self.c.addtag_withtag('pret5','test') #on prepare la 2eme boule a se faire deplacer
                        self.c.dtag('test','test')
                        self.c.addtag_overlapping('test',s+r+40,t+r-69,s+r+41,t+r-70) # test sur la troisieme boule                                                                         #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0:#si il n'y a rien apres la deuxieme boule bleue
                            j=2
                        else:  #si il y a une quelconque 3eme boule
                            print("on ne peut pas pousser 3 boules")
                            j=99
                            self.c.dtag('test','test')
                            self.c.dtag('pret3','pret3')
                            self.c.dtag('pret4','pret4')
                            self.c.dtag('pret5','pret5')
                    if h>j:
                        deplhd()                                                                                                   #changer

                else:
                    print("deplacement impossible1 boule b-b")
                    self.c.dtag('test','test')
                    
                        
    
            
        self.x,self.y=event.x,event.y
        self.c.delete('fleches')
        cercle=self.c.find_closest(self.x,self.y)
        self.c.addtag_closest('depl',self.x,self.y)
        x,y,z,w=self.c.coords('depl')
        r=30
        q=0
        if self.c.find_withtag('pret2'): # si il y a une deuxieme boule
            print("il y a une deuxieme boule")
            self.c.addtag_overlapping('alignés',x+r+40,y+r-69,x+r+41,y+r-70)                                                                                                   #changer
            self.c.addtag_overlapping('alignés',x+r-41,y+r+70,x+r-40,y+r+69)                                                                                                   #changer
            if self.c.find_withtag('pret2')[0] in self.c.find_withtag('alignés'): #si les boules sont alignés
                print("les boules sont alignées")
                self.c.dtag('alignés','alignés')
                self.c.addtag_overlapping('test',x+r+40,y+r-69,x+r+41,y+r-70) # test sur 2eme boule                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la premiere boule
                    print("rien apres la premiere boule")
                    deplhd()                                                                                                   #changer
                elif self.c.find_withtag('test')==self.c.find_withtag('pret2') or self.c.find_withtag('test')==self.c.find_withtag('pret3'): #si il y a une deuxieme boule
                    print("il y a une deuxieme boule de rencontréé")
                    x,y,z,w=self.c.coords('test')
                    self.c.dtag('test','test')
                    self.c.addtag_overlapping('test',x+r+40,y+r-69,x+r+41,y+r-70) #test sur 3eme boule                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0: # si il n'y a rien apres la deuxieme boule
                        print("rien apres la deuxieme boule")
                        deplhd()                                                                                                   #changer
                    elif self.c.find_withtag('test')==self.c.find_withtag('pret3'):# si il y a la troisieme boule
                        self.c.dtag('test','test')
                        x,y,z,w=self.c.coords('pret3')
                        self.c.addtag_overlapping('test',x+r+40,y+r-69,x+r+41,y+r-70)                                                                                                   #changer
                        self.c.dtag('fond','test')
                        if len(self.c.find_withtag('test'))==0: #si il n'y a rien apres la 3eme boule
                            deplhd()                                                                                                   #changer
                        else: #si il y'a autre chose apres la troisieme boule
                            testpousse(3)


                            
                    else: #si il y'au autre chose apres la deuxieme boule
                        testpousse(2)
                else: #si il y a autre chose apres la premiere boule
                    testpousse(1)
            else: #si les boules ne sont pas alignées
                self.c.dtag('test','test')
                n=0
                x,y,z,w=self.c.coords('depl')
                self.c.addtag_overlapping('test',x+r+40,y+r-69,x+r+41,y+r-70)                                                                                                   #changer
                self.c.dtag('fond','test')
                if len(self.c.find_withtag('test'))==0:
                    n+=1
                else:
                    n+=0
                self.c.dtag('test','test')
                if self.c.find_withtag('pret2'):
                    x,y,z,w=self.c.coords('pret2')
                    self.c.addtag_overlapping('test',x+r+40,y+r-69,x+r+41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    x,y,z,w=self.c.coords('pret3')
                    self.c.addtag_overlapping('test',x+r+40,y+r-69,x+r+41,y+r-70)                                                                                                   #changer
                    self.c.dtag('fond','test')
                    if len(self.c.find_withtag('test'))==0:
                        n+=1
                    else:
                        n+=0
                    self.c.dtag('test','test')
                if self.c.find_withtag('pret3'):
                    k=3
                elif self.c.find_withtag('pret2'):
                    k=2
                elif self.c.find_withtag('depl'):
                    k=1
                if k==n:
                    deplhd()                                                                                                   #changer
                        
                    
        else: #si il n'y a pas de deuxieme boule
            testpousse(1)
            
        self.c.dtag('selectcr','selectcr')
        self.c.dtag('selectcb','selectcb')
        self.c.dtag('suppr2','suppr2')
        self.c.dtag('suppr3','suppr3')
        self.c.dtag('depl','depl')
        self.c.dtag('test','test')
        self.c.dtag('pret2','pret2')
        self.c.dtag('pret3','pret3')
        self.c.dtag('pret4','pret4')
        self.c.dtag('pret5','pret5')
        self.c.dtag('deuxiemer','deuxiemer')
        self.c.dtag('deuxiemeb','deuxiemeb')
        self.c.dtag('troisiemeb','troisiemeb')
        self.c.dtag('troisiemer','troisiemer')
        self.c.dtag('premierer','premierer')
        self.c.dtag('premiereb','premiereb')
        self.c.dtag('alignés','alignés')
    #------------------------------------------------------------------------------------------------------------------     Commentaires

    #tags:
        #premiere: premire boule, clic gauche   1 seule a la fois
        #deuxieme: deuxieme boule, clic droit   1 seule a la fois
        #cr,cb:  boule rouge, boule bleue
        #fleches: fleches
        #d,g,hd...: droite , gauche, haut droite etc
        #point: point qui permet de faire le tour des boules et d'utiliser l'overlapping
        #pret: tag qui permet a la deuxieme boule de bouger
        #depl: tag qui permet a la premiere boule de bouger
        #rect:  rectangle qui permet de verifier si le point est sur la premier boule 'premiere'
        #suppr2/3: permet de supprimer la 2eme ou 3eme boule lors d'un deplacement en dehors du plateau
        #clicmolette: boules sur lesquels il sera possible de les selectionner en tant que 3eme boule
        #test: rectangle qui permet de test les boules d'apres etc pour les deplacements


    #distances:
        #entre deux boules
        #horizontales: 80
        #horizontale diagonale :  40
        #vertical diagonale : 69

    #probleme potentiels:
        #probleme de selection de temps en temps

        
fenetre=tk.Tk()
App=Abalone(1)
fenetre.mainloop()
