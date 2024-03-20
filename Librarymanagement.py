import calendar
from datetime import date,timedelta
class Library():
    
    def __init__(self):
        self.books=['to kill a mockingbird','the great gatsby','pride and prejudice','the catcher in the rye','animal farm','lord of the flies','brave new world','the hobbit','fahrenheit 451','the lord of the rings','the chronicles of narnia']


    def add_book(self,title):
        self.books.append(title)

    def display_book(self):
                if len(self.books)>0:
                    print('Available books:')
                    for i in self.books:
                        print('-',i) 
                             
                else:
                    print('Book is not available')
    def borrow(self):
        
        print('Book rentals price for one day is 10')
        choose_book=input('Enter which book you want to borrow:')
        hdays=int(input('How many days do you need:'))
        pay=hdays*10
        print('You need to pay:',pay,'rs')
        confirm=input('Enter yes to pay and confirm:')
        if confirm=='yes':
            self.books.remove(choose_book)
            today=date.today()
            print('purchase date:',today)
            returnd=today+timedelta(days=hdays)
            print('Return date:',returnd)
            print('Thankyou for purchasing')

            
        else:
             print('Not confirmed,Thankyou for visiting')
    
    def return_book(self):
        
        return_name=input('Enter return Book name:')
        self.books.append(return_name)
        print('thankyou for returning in/before correct date')

            
def main():
    library=Library()   
    print('LIBRARY MANAGEMENT SYSTEM')
    while True:
        print('1. Add book')
        print('2. Display book')
        print('3. Borrow book')
        print('4. Return book')
        print('5. Exit')

        choice=int(input('Enter your choice:'))
        
        if choice==1:       
            title=input('Enter your book title:')
            library.add_book(title)                   
        elif choice==2:
            library.display_book()
        elif choice==3:
             library.borrow()
        elif choice==4:
            library.return_book()
        elif choice==5:
            break
        else:
            print('wrong choice')

main()

