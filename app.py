#IMPORTS
import getpass
import os
import mysql.connector
import math 
from prettytable import from_db_cursor

#Global variables
clear = lambda:os.system('cls')
conn = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345",
  database="bookmovie"
)
exeSql = conn.cursor()
 
#Functions
def admin_control(inv = None):
    clear()
    if inv:
        print('INVALID CHOICE \n')
    print('''---------Admin Login-----------
    1. Add New Movie
    2. Display all the movies
    3. Modify Movie details
    4. Remove a Movie
    ------------------
    9. Change login password
    10. Logout
    \n\nEnter your choice''', end=' ')
    ch = int(input('-> '))

    # ADDING A MOVIE
    if ch == 1:
        clear()
        print('-------------ADD MOVIE-------------')
        movieName = input("Enter Movie name: ")
        desc = input("Enter Description: ")
        cast = input("Enter the Cast Names: ")
        audi_id = int(input("Enter the Audi_ID: "))
        p_silver = int(input("Enter the Price for Silver Class: "))
        p_gold = int(input("Enter the Price for Gold Class: "))
        p_platinium = int(input("Enter the Price for Platinium Class: "))
        show_timing = input("Enter Show Timing (HH:MM - HH:MM): ")
        clear()
        print("\n---------- REVIEW DETAILS ----------\n")
        print("Name\t\t:\t",movieName)
        print("Description\t:\t",desc)
        print("Cast\t\t:\t",cast)
        print("Audi_id\t\t:\t",audi_id)
        print("Price silver\t:\t",p_silver)
        print("Price Gold\t:\t",p_gold)
        print("Price Platinium\t:\t",p_platinium)
        print("Show Timings\t:\t",show_timing)
        print("\nDo you wish to continue (Y/N):\t",end='')
        ch1 = input()
        if ch1 == 'y' or ch1 == 'Y':
            clear()

            print("Record Added Successfully")
            query = "INSERT INTO MOVIES (movie_name,movie_desc,movie_cast,Audi_id ,Price_Silver,Price_Gold,Price_Platinum,Show_timing) values (%s,%s,%s,%s,%s,%s,%s,%s)";
            val = (movieName,desc,cast,audi_id,p_silver,p_gold,p_platinium,show_timing)
            exeSql.execute(query,val)
            conn.commit()
            input("Press enter to continue")
            admin_control()
        else: 
            admin_control()
    # DISPLAYING A MOVIE
    elif ch == 2:
        clear()
        exeSql.execute("SELECT * FROM MOVIES")
        mytable = from_db_cursor(exeSql)
        print("\n\t\t\t\t\t-------------- MOVIE DETAILS --------------\n")
        print(mytable)
        input("Press enter to continue")
        admin_control()
    # MODIFYING A MOVIE
    elif ch ==3:
        clear()
        exeSql.execute("SELECT * FROM MOVIES")
        mytable = from_db_cursor(exeSql)
        print("\n\t\t\t\t\t-------------- MOVIE DETAILS --------------\n")
        print(mytable)
        inp = int(input('Enter the Movies ID :'))
        exeSql.execute("SELECT * FROM MOVIES WHERE M_ID=%s"%(inp))
        row = exeSql.fetchall()
        print("Movie ID:\t\t",row[0][0])
        print("Movie Name\t\t",row[0][1])
        choice = input("Do you want to make changes (Y/N): ")
        if choice == 'Y' or choice == 'y':
            movieName = input("Enter Movie Name: ")
            desc = input("Enter Description: ")
            cast = input("Enter the Cast names: ")
            audi_id = int(input("Enter the Audi_ID: "))
            p_silver = int(input("Enter the Price for Silver Class: "))
            p_gold = int(input("Enter the Price for Gold Class: "))
            p_platinium = int(input("Enter the Price for Platinium Class: "))
            show_timing = input("Enter Show Timing (HH:MM - HH:MM): ")
            clear()
            print("\n---------- REVIEW DETAILS ----------\n")
            print("Name\t\t:\t",movieName)
            print("Description\t:\t",desc)
            print("Cast\t\t:\t",cast)
            print("Audi_id\t\t:\t",audi_id)
            print("Price silver\t:\t",p_silver)
            print("Price Gold\t:\t",p_gold)
            print("Price Platinium\t:\t",p_platinium)
            print("Show Timings\t:\t",show_timing)
            print("\nDo you wish to continue (Y/N):\t",end='')
            ch1 = input()
            if ch1 == 'y' or ch1 == 'Y':
                clear()
                print("Record Modified Successfully")
                query = "UPDATE MOVIES SET movie_name=%s,movie_desc=%s,movie_cast=%s,Audi_id=%s ,Price_Silver=%s,Price_Gold=%s,Price_Platinum=%s,Show_timing=%s WHERE M_id = %s;"
                val = (movieName,desc,cast,audi_id,p_silver,p_gold,p_platinium,show_timing,inp)
                exeSql.execute(query,val)
                conn.commit()
                print("1 record updated, ID:", exeSql.lastrowid)
                input("Press enter to continue")
                admin_control()
    # REMOVING A MOVIE    
    elif ch == 4:
        clear()
        exeSql.execute("SELECT * FROM MOVIES")
        mytable = from_db_cursor(exeSql)
        print("\n\t\t\t\t\t-------------- MOVIE DETAILS --------------\n")
        print(mytable)
        rowid = int(input("Enter Movie ID to Remove: "))
        exeSql.execute("SELECT * from movies where m_id =%s"%(rowid))
        rows = exeSql.fetchall()
        print(rows)
        if rows != []:
            clear()
            print("Movie Id:\t\t",rows[0][0])
            print("Movie Name\t\t",rows[0][1])
            choice = input("Sure (Y/N): ")
            if choice == 'Y' or choice == 'y':
                exeSql.execute("DELETE FROM MOVIES WHERE m_id = %s;"%(rowid))
                print("Deleted Successfully")
                conn.commit()
                input("Press enter to continue")

                admin_control()
            else:
                admin_control()
        else:
            print("Invalid Choice:")
            input("Press enter to continue")
            admin_control()
    # CHANGING PASSWORD
    elif ch==9:
        clear()
        print('\t-----Change Password------')
        old=input('Enter Old Password : ')
        new=input('Enter New Password : ')
        re=input('Re-Type Password : ')
        exeSql.execute("SELECT PWD FROM AUTH WHERE PWD= '%s';"%(old,))        
        rowid= exeSql.fetchall()
        
        if rowid==[]:
            print('''Old Password dosen't match''')
        elif old==rowid[0][0]:
            if new==re:
                exeSql.execute("UPDATE AUTH SET PWD='%s' WHERE ID=1;"%(new,))
                conn.commit()
                print('Password have been updated successfully!')
                input("Press enter to continue")
                admin_control()
        # elif:
        #         print('Re-Type Password did not match.')
        
        else:
            ('Old Password not matched!')
    #LOGOUT
    elif ch == 10:
        auth(1)
    else:
        admin_control(1)

def user_control():
    clear()
    print('''\t\t-------Booking--------
    1. Book Ticket
    2. Display Bookings
    3. Cancel Ticket
    ------------------
    9.Change Login Password
    10.Logout
    \n\nEnter your choice''', end=' ')
    ch=int(input('->'))
    if ch == 1:
        phno = int(input("Enter your Phone Number: "))
        exeSql.execute("SELECT * FROM CUSTOMER WHERE CUST_PHONE=%s"%(phno))
        row = exeSql.fetchall()
        if row == []:
            clear()
            print("------New Customer------")
            print("Customer Phone no: ",phno)
            name = input("Enter Customer Name: ")
            exeSql.execute("INSERT INTO CUSTOMER (CUST_NAME,CUST_PHONE) VALUES ('%s',%s);"%(name,phno))
            conn.commit()
        clear()
        exeSql.execute("SELECT * FROM CUSTOMER WHERE CUST_PHONE=%s"%(phno))
        row1 = exeSql.fetchall()
        print("Customer Name\t\t: ",row1[0][1])
        print("Customer Phone No\t: ",row1[0][2])
        cust_id = row1[0][0] #To input the id into booking table
        input("Press enter to continue")
        exeSql.execute("SELECT M_ID,MOVIE_NAME,MOVIE_DESC,MOVIE_CAST,PRICE_SILVER,PRICE_GOLD,PRICE_PLATINUM,SHOW_TIMING,NO_OF_SEAT,AUDI_NAME FROM MOVIES M,AUDI A WHERE M.AUDI_ID = A.AUDI_ID;")
        mytable = from_db_cursor(exeSql)
        print("\n\t\t\t\t\t-------------- MOVIE DETAILS --------------\n")
        print(mytable)
        id = int(input("Enter the Movie ID to Book: "))
        exeSql.execute("SELECT MOVIE_NAME,PRICE_SILVER,PRICE_GOLD,PRICE_PLATINUM,SHOW_TIMING,NO_OF_SEAT,AUDI_NAME,MOVIES.M_ID FROM MOVIES JOIN AUDI ON MOVIES.AUDI_ID = AUDI.AUDI_ID WHERE MOVIES.M_ID = %s;"%(id))
        row = exeSql.fetchall()
        if row == []:
            print("Invalid choice")
            input("Press enter to continue ")
            user_control()
        clear()
        print("------------------SELECTED MOVIE---------------------")
        print("Movie Name\t\t:",row[0][0])
        print("Silver Price\t\t:",row[0][1],'/-')
        print("Gold Price\t\t:",row[0][2],'/-')
        print("Platinum Price\t\t:",row[0][3],'/-')
        print("Show Timing\t\t:",row[0][4])
        print("Seats Left\t\t:",row[0][5])
        print("Audi Name\t\t:",row[0][6])
        clas = int(input('''\nClass\n---------\n1. Silver\n2.Gold\n3.Platinum\n->'''))
        No_of_tickets = int(input("Number of Tickets: "))
        ch = input("Confirm (Y/N) : ")
        if ch != 'Y' and ch != 'y':
            user_control()
        clear()
        if clas == 1:
            clas_name = "Silver"
            typ = row[0][1]
        elif clas == 2:
            clas_name = "Gold"
            typ = row[0][2]
        else:
            clas_name = "Platinum"
            typ = row[0][3]
        net_amount = typ * No_of_tickets
        tax = net_amount*0.18
        movie_id = row[0][7]
        if row[0][5] - No_of_tickets < 0:
            print("Sorry we're Housefull")
            input("Press enter to continue")
            user_control()
        exeSql.execute("INSERT INTO BOOKING (CUST_ID,M_ID,TYPES_OF_SEATS,AMOUNT,TAX,NO_OF_SEAT) VALUES (%s,%s,'%s',%s,%s,%s);"%(cust_id,movie_id,clas_name,net_amount,tax,No_of_tickets))
        exeSql.execute("UPDATE AUDI SET NO_OF_SEAT = %s where Audi_name = %s;",(row[0][5] - No_of_tickets, row[0][6]))
        conn.commit()
        clear()
        print('''\n\t                               BILL                     ''')
        print('\t\t_________________________________________')
        print('''
\t\tCustomer Name\t\t:\t%s
\t\tMovie Name\t\t:\t%s
\t\tShow Timing\t\t:\t%s
\t\tNo of Seats\t\t:\t%s
\t\tClass\t\t\t:\t%s

\t\t+---------------------------------------+
\t\t|             Price Breakdown           |
\t\t+---------------------------------------+
\t\t| Total Amount\t\t:\t%s\t|
\t\t| Tax (+)\t\t: \t%s\t|
\t\t+---------------------------------------+
\t\t| Amount payble\t\t:\t%s\t|
\t\t+---------------------------------------+'''%(row1[0][1],row[0][0],row[0][4],No_of_tickets,clas_name,net_amount,round(tax,2),round(net_amount+tax,2)))
        input("\n\nPress enter to continue")
        user_control()
    elif ch == 2:
        clear()
        exeSql.execute("select b.book_id, c.cust_name, m.movie_name, b.amount, b.tax, b.NO_OF_SEAT, a.audi_id from booking b join movies m on b.m_id = m.m_id join customer c on c.cust_id = b.cust_id join audi a on a.audi_id = m.audi_id;")
        mytable = from_db_cursor(exeSql)
        print(mytable)
        input("Press enter to continue")
        user_control()
    elif ch == 3:
        ticketId = int(input("Enter the Ticket ID: "))
        exeSql.execute('select b.book_id, c.cust_name, m.movie_name, b.amount, b.tax, b.NO_OF_SEAT, a.audi_id from booking b join movies m on b.m_id = m.m_id join customer c on c.cust_id = b.cust_id join audi a on a.audi_id = m.audi_id where book_id = %s;'%(ticketId))
        row = exeSql.fetchall()
        if row == []:
            print("No Booking found under this ID")
            input("Press enter to continue")
            user_control()
        else:
            print("Customer Name\t\t: \t",row[0][1])
            print("Movie Name\t\t: \t",row[0][2])
            print("Refundable Amount\t: \t",row[0][3])
            seat = row[0][5]
            audi_id = row[0][6]
            print("\n\n")
            confirm = input("Confirm (Y/N): ")
            if confirm == 'y' or confirm == 'Y':
                exeSql.execute("Update audi set no_of_seat =%s+no_of_seat where audi_id = %s;"%(seat,audi_id))
                exeSql.execute("Delete from booking where book_id = %s"%(ticketId))
                conn.commit()
                clear()
                print("Booking Cancelled Successfully\nTotal Refundable Amount is:",row[0][3])
                input("Press enter to continue")
                user_control()
            else:
                user_control()
    elif ch == 9:
        clear()
        print('\t-----Change Password------')
        old=input('Enter Old Password : ')
        new=input('Enter New Password : ')
        re=input('Re-Type Password : ')
        exeSql.execute("SELECT PWD FROM AUTH WHERE PWD= '%s';"%(old,))        
        rowid= exeSql.fetchall()
        
        if rowid==[]:
            print('''Old Password dosen't match''')
        elif old==rowid[0][0]:
            if new==re:
                exeSql.execute("UPDATE AUTH SET PWD='%s' WHERE ID=2;"%(new,))
                conn.commit()
                print('Password have been updated successfully!')
                input("Press enter to continue")
                user_control()
            else:
                print('Re-Type Password did not match.')
        
        else:
            ('Old Password not matched!')

    elif ch == 10:
        auth(1)
    else:
        user_control()

def auth(alert = None):
    clear()
    if alert:
        print("\nLogged out successfully")
    print("\n ------------Welcome------------")
    uname = input("Enter username: ")
    pwd = getpass.getpass("Enter password: ")
    
    qry = "SELECT * FROM auth where Uname = %s and pwd = %s;"
    val = (uname,pwd)
    exeSql.execute(qry,val)
    result = exeSql.fetchall()
    if result == []:
        print("Invalid Username / Password")
        exit()
    elif (uname == result[0][1] and pwd == result[0][2]):
        if result[0][3] == 1:
            user_control()
        else:
            admin_control()
    else:
        print("Invalid Username \ Password")
        exit()

if __name__ == '__main__':
    clear()
    auth()
