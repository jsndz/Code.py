import sqlite3 
con = sqlite3.connect('sjec.db')  

def select():
    print()
def insert():
    id=(input("Enter the ID"))
    name=(input("Enter the name"))
    salary=(input("Enter the salary"))
    con.execute("insert into employee(id,name,salary)values("+id+","+name+","+salary+")") 
    
    # con.execute("insert table employee(id,name,salary)values('2','rdtfxftr','567567')") 
    
def update():
    print("Coming soon")
def delete():
    print("Coming soon")
def selectAll():
    res=con.execute("select * from employee") 
    emp= res.fetchall() 
    print(emp)
def main():
    
    print("_______MENU_______")
    print("1. SELECT")
    print("2.SELECT ALL")
    print("3.iNSERT")
    print("4.DELETE")
    print("5.UPDATE")
    print("6.EXIT")
    c=int(input("enter your choice"))
    if(c==1):
        select()
    elif(c==2):
        selectAll()
    elif(c==3):
        insert()
    elif(c==4):
        delete()
    elif(c==5):
        update()
    elif(c==6):
        exit()
    else:
        print("Invalid choice")

main()