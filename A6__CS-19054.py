import sys
import datetime
  


class SHOPPING_CART:
    ''' Welcome the customer to the online shopping wear'''
    
            ###################### Opening lines  ####################
    print('   *****************************************************************')        
    print('   *            Hello customer!!!                                  *')
    print('   *      WELCOME TO  WILLY WONKAS SHOPPING WEAR  0*^__^*0         *')
    print('   *  Fashion as Unique as You Are                                 *')
    print('   *  And get 70% discount on our new Arrivals                     *')
    print('   *****************************************************************')


        
class CUSTOMERLOGIN(SHOPPING_CART):
    '''When customer sign in successfully then this class Display Menu of Service '''
     ### Services available in Wear appear to customer ###
    def customer_login(self):
        print('\n\n***********************************\n1-Display Menu\n2-Give Order\n3-Remove Items from Cart\n4-Items in Stock\n5-Customer Carts Items\n6-Shopping History\n7-Logout\n************************************')
     
class SHOPPING_LIST:
    ''' Contain list of Shopping Items'''
    ### All the items placed in a list ###
    list=[{"No":1,"Item":"Peach Flower Pret Dress","Stock":5,"Cost":3500},{'No':2,'Item':'Lilac Ray Florence Dress','Stock':10,'Cost':6500},{'No':3,'Item':'Pistachio Green Pearlfrock','Stock':3,'Cost':7000},{'No':4,'Item':'Golden template Maxxi','Stock':4,'Cost':9000},{'No':5,'Item':'Nike Blue Joggers','Stock':5,'Cost':8000},{'No':6,'Item':'Red velvet Frock','Stock':7,'Cost':7500},
          {'No':7,'Item':'Black Silver Sneakers','Stock':2,'Cost':6500},{'No':8,'Item':'Red Glassy pumpies','Stock':5,'Cost':7500},{'No':9,'Item':'Gladiator sandals','Stock':6,'Cost':5500},{'No':10,'Item':'Willington Boots','Stock':2,'Cost':10000}]
    def items(self):
        pass
    
class MENU:
    '''Display Shopping list to customer'''
    ### Shows list of available Items with proper format ###
    def Display_Menu(self):
        print('\n\n\n*************************\n### Items Available in our WILLY WONKAS SHOPPING WEAR ###')
        print('\n*********************************************')
        print('No\tItem\t\t\t\t\t\tStock\tCost')
        association=SHOPPING_LIST()
        for d in association.list:
            print(f'{d["No"]}\t{d["Item"]:30}\t{d["Stock"]:17}\t{d["Cost"]}')
        
class ITEMS_IN_CARTS(SHOPPING_LIST):
    '''Tell customer total Number of Items in our Shopping List'''
    ### To calculate total items it assigned to a variable Amount ###
    Amount=0
    def items(self):
        print('### Total Items in Shopping Mart ###')
        print('\n****************************\n')
        print('\nNo\tItem\t\t\t\tStock\n')
        for d in self.list:
            print(f'{d["No"]}    {d["Item"]:30}     {d["Stock"]:}')
            ITEMS_IN_CARTS.Amount+=(d["Stock"])
        return ITEMS_IN_CARTS.Amount
        print('\nTotal Items in Stock are:',ITEMS_IN_CARTS.Amount)

class CUSTOMER_ID(MENU):
    '''Ask customer to Enter no of Item you want to buy'''
    ### Function ask customer to input the number of respective item you want to buy ###
    def Customer_id(self):
        self.Display_Menu()
        try:
            self.cus_id=int(input('\n***************************\nEnter the number of item you want to buy: '))
        except:
            print('Invalid input,Number must be integer:')
            self.customer_id()

class SAVE_ITEM:
    '''Save all shopping data in a file '''
    def saveitemstofile(self,itemlist):
        if itemlist==[]:
            pass
        else:
            a=datetime.datetime.now()
            itemlist.append(['ORDER DATE:'+a.strftime("%m/%d/%y")+'  ORDERING TIME='+a.strftime("%H:%M:%S")])
        ### Item file opens in which shopping history is stored ###
            f=open('ItemFile.txt','a')
            for item in itemlist:
                f.write(str(item)+'\n')
            f.close()

class GIVE_ORDER(CUSTOMER_ID,SAVE_ITEM):
    '''Customer can give order by entering no of Item given in Shopping List'''
    Cart=[]
    def order(self):
        self.Display_Menu()
        try:
            self.per_id=int(input('\n****************************\nEnter the number of item you want to order: '))
        except:
            print('Invalid input,enter numbers in integers:')
            self.order()
        if self.per_id in [1,2,3,4,5,6,7,8,9,10]:
            for d in self.list:
                if d['No']==self.per_id:
                    print('************************************\nNo\tItem\t\t\t\t\tStock\t\tCost\n')
                    print(f'{d["No"]}\t{d["Item"]}\t\t\t{d["Stock"]}\t\t{d["Cost"]}')
                    self.ord='{d["No"]}\t{d["Item"]}\t{d["Stock"]}\t\t{d["Cost"]}'
                    self.want=[d['No'],d['Item'],d['Cost']]
                    GIVE_ORDER.Cart.append(self.want)
                    self.saveitemstofile(GIVE_ORDER.Cart)
                    self.choice=input('\n\n**************************\nAre you sure you want to buy the above item from given Shopping List: ')
                    if self.choice=='Y' or self.choice=='y':
                        print('\n*****************************************\n\nTHANK YOU FOR YOUR SHOPPING\nYou have bought our Item Number  {}'.format(d["No"]),'from the new arrivals\n***************************************************\n')
        
                        d["Stock"]-=1
                        self.more=input('Do you want to buy our other products\nFor more order Enter your action in Y or N: ')
                        if self.more=='Y' or self.more=='y':
                            self.order()

                        elif self.more=='N' or self.more=='n':
                            self.customer_login()
                            self.customer_choice()

                        else:
                            print('Kindly enter correct option!!!!')
                            self.more=input('Do you want to buy our other products\nFor more order Enter your action in Y or N ')
                            if self.more=='Y' or self.more=='y':
                                self.order()
                                
                            elif self.more=='n' or self.more=='N':
                                self.customer_login()
                                self.customer_choice()

                    elif self.choice=='N' or self.choice=='n':
                        print('The item you ordered was removed')
                        self.more=input('Do you want to buy our other products\nFor more order Enter your action in Y or N ')
                        if self.more=='Y' or self.more=='y':
                            self.order()
                                
                        elif self.more=='n' or self.more=='N':
                            self.customer_login()
                            self.customer_choice()

                        else:
                            print('Kindly enter correct option!!!!')
                            self.more=input('Do you want to buy our other products\nFor more order Enter your action in Y or N ')
                            if self.more=='Y' or self.more=='y':
                                self.order()
                                
                            elif self.more=='n' or self.more=='N':
                                self.customer_login()
                                self.customer_choice()

                    else:
                        print('\nKindly enter correct option!!!!\nThe input is invalid!!\n')
                        self.more=input('Do you want to buy our other products\nFor more order Enter your action in Y or N ')
                        if self.more=='Y' or self.more=='y':
                            print('*********************\nTHANK YOU FOR YOUR SHOPPING\n You have bought our item from the new arrivals {}'.format(d["No"]),'***************************************************')
                            d["Stock"]-=1
                            self.more=input('Do you want to buy our other products\nFor more order Enter your action in Y or N: ')
                            if self.more=='Y' or self.more=='y':
                                self.order()

                            elif self.more=='N' or self.more=='n':
                                self.customer_login()
                                self.customer_choice()

                            else:
                                print('Kindly enter correct option!!!!')
                                self.more=input('Do you want to buy our other products\nFor more order Enter your action in Y or N ')
                                if self.more=='Y' or self.more=='y':
                                    self.order()
                                
                                elif self.more=='n' or self.more=='N':
                                    self.customer_login()
                                    self.customer_choice()
            

        else:
            print('\n******************************************************\nThere is no Item at your input Number.\nKindly enter valid Number of Item')
            self.order()

class REMOVE_ITEM_FROMCART(GIVE_ORDER):
    '''Ask customer if he(s) wanted to remove item from his/her Cart'''
    ### Ask customer to input the no you want to remove from your Cart before loging out ###
    def remove_item(self):
        try:
            self.ord_no=input('\n\nEnter the number of Item you want to remove:')
        except:
            print('Invalid input,enter numbers in integers')
            self.remove_item()
        for d in self.list:
            if d["No"]==self.ord_no:
                d["Stock"]+=1
        for d in self.Cart:  ## if the input no is present in your cart must e removed ##
            if int(self.ord_no) in d:
                self.Cart.remove(d)
                print('\n***********************************\n')
                print('Item No.',self.ord_no,'removed from your cart')
                break
            ### if Item not found  ###
        else:
            print('***********************************************')
            print('Item No.',self.ord_no,'not found in your cart')
            

class CUSTOMER_CART(GIVE_ORDER):
    '''Customer can see the Items present in his/her Cart '''
    def customer_cart(self):
        if self.Cart==[]:    ## when your cart is empty
            print('*****************************************************\n')
            print('Dear Customer you hadn\'t buy anything from our new arrivals\nAvail our Discount offer!!\n')
        else:
            print('*****************************************************\n')
            print('Dear Customer you have these Items in your Cart')
            for i in range(0,len(self.Cart)):
                print(self.Cart[i],'\n')
                
                      
class CUSTOMER_CHOICE(ITEMS_IN_CARTS,CUSTOMER_CART,REMOVE_ITEM_FROMCART,CUSTOMERLOGIN):
    '''Customer input their choice that what they want to enjoy our Wonkas Service'''
    def customer_choice(self):
        try:
            self.input=input('\nSelect a number for the action that you would like to do:')
        except:
            print('Invalid input,enter numbers in integers:')
            self.customer_choice()
        ### self.input equal to our service no available ###
        if self.input=='1':
            self.Display_Menu()
            print('***************************************************')
            self.customer_login()
            print('***************************************************')
            self.customer_choice()
        elif self.input=='2':
            self.order()
            print('***************************************************')
            self.customer_login()
            print('***************************************************')
            self.customer_choice()
        elif self.input=='3':
            self.remove_item()
            print('\n**************************************************\n')
            self.customer_login()
            print('\n**************************************************\n')
            self.customer_choice()
        elif self.input=='4':
           self.items()
           print('\n**************************************************\n')
           self.customer_login()
           print('\n**************************************************\n')
           self.customer_choice()
        elif self.input=='5':
           self.customer_cart()
           print('\n**************************************************\n')
           self.customer_login()
           print('\n**************************************************\n')
           self.customer_choice()
        elif self.input=='6':
           f=open('ItemFile.txt','a+') ### Create file to store Shopping History ###
           print('\n**************************************************\n')
           f.seek(0)
           for line in f:
               line=eval(line.strip())
               print(line)
               
           print('\n***************************************************\n')
           f.close()
           self.customer_login()
           print('\n*************************************************\n')
           self.customer_choice()
        elif self.input=='7':
            ## Ask customer to logout or not ##
           self.a=input('Dear Customer are you sure you want to log out!!!\nEnter your Choice.\nPress Y or y for yes and N or n for No:')
           if self.a=='Y' or self.a=='y':
               print('Dear Customer you are logging out\nHope you like our service\nSee you Again!!!\nBYEEEEEEEEEE\n*************************************************')
               sys.exit()  ## using of module sys ##
            
           elif self.a=='N' or self.a=='n':
               print('\n********************************\nThank you customer you are not logging Out\nEnjoy our service\n************************************')
               self.customer_login()
               print('\n*************************************************\n')
               self.customer_choice()
           else:
               print('\nInvalid input,enter your choice')
               self.a=input('\nDear Customer are you sure you want to log out!!!\nEnter your Choice.\nPress Y or y for yes and N or n for No:')
               if self.a=='Y' or self.a=='y':
                   print('Dear Customer you are logging out\nHope you like our service\nSee you Again!!!\nBYEEEEEEEEEE\n*************************************************')
                   sys.exit()  ## using of module sys ##
               elif self.a=='N' or self.a=='n':
                   print('\n********************************\nThank you customer you are not logging Out\nEnjoy our service\n************************************')
                   self.customer_login()
                   print('\n*************************************************\n')
                   self.customer_choice()
                   
               
        else:
            print('\nKindly enter correct option!!!!\nThe input is invalid!!\n')
            self.customer_login()
            print('\n*************************************************\n')
            self.customer_choice()
               
class LOGIN(CUSTOMER_CHOICE):
    '''Manages customer Accounts,check passwords or asked them to sign up if they are new customer of WILLY WONKAS SHOPPING WEAR '''
      ## In data list customer data is stored in the form of List ##
    datalist=[]
    def login(self):
        print('####  ACCOUNT MANAGER #####')
        self.x=input('\nDear Customer\nDo you have an account in our Wonkas Mart\nPress Y or y for yes and N or n for No:')
        print('******************************************************')

     ### self.x ask user if customer have account or not
       
        if self.x=='Y' or self.x=='y':
            ### Taking password ###
            self.pwd=input('\nEnter the password:')
            f=open('customerlogindata.txt','a+')
            f.seek(0)
            for data in f:
                dt=eval(data.strip())

                ### if input password is other than regular customer password ###
                if self.pwd==dt[2]:
                    print('\n****************************\nThe password you enter is correct\nCongratulations!!!\n***************************')
                    print('#### CUSTOMER ACCOUNT DETAILS #####')
                    print('\nCustomer_Name:',dt[1],'\nPassword:',dt[2],'\nFirst_name:',dt[3],'\nAdress:',dt[0])
            
                    self.customer_login()
                    self.customer_choice()
            f.close()

            ### if input password is equals to regular customer password ### 
            if self.pwd=='Mart@Wonkas':
                print('Congratulations!!\nYou are our logged in regular customer\nNice to see you!!!!\n**************************')
                self.w=input('Dear customer are you interested in the account history of Customer\nEnter Y for yes and N for No:')
                if self.w=='y' or self.w=='Y':
                    f=open('customerlogindata.txt','a+')
                    print('\n************************\n')
                    for line in f:
                        line=eval(line.strip())
                        print(line)
                    print('\n************************\n')
                    f.close()
                    print('   *      WELCOME TO  WILLY WONKAS SHOPPING WEAR  0*^__^*0         *')
                    print('   *  Fashion as Unique as You Are                                 *')

                    self.customer_login()
                    self.customer_choice()
                    
                else:
                    print('   *      WELCOME TO  WILLY WONKAS SHOPPING WEAR  0*^__^*0         *')
                    print('   *  Fashion as Unique as You Are                                 *')

                    self.customer_login()
                    self.customer_choice()

            ## when customer say he has an account but not present in our logindata ###    
            elif self.pwd!='Mart@Wonkas':
                print('\n**************************************\nThe pasword you entered is wrong\nKindly input Correct Password or create your account in our Mart!!!')
                self.login()
        ## creating new account ###        
        elif self.x=='N' or self.x=='n':
            print('#### CUSTOMER ACCOUNT DETAILS #####\n\n')
            self.Name=input('Customer Name:')
            self.First=input('Customer First_Name:')
            self.Adress=input('Your place of living:')
            self.Password=input('Password of your mart Account:')
            data_collection=[self.Adress,self.Name,self.Password,self.First,str(datetime.datetime.now())]
            LOGIN.datalist.append(data_collection)
            self.datafile(LOGIN.datalist)
            print('   *      WELCOME TO  WILLY WONKAS SHOPPING WEAR  0*^__^*0         *')
            print('   *  Fashion as Unique as You Are                                 *')
            self.customer_login()
            self.customer_choice()
           
        else:
            print('\nKindly enter correct option!!!!\nThe input is invalid!!\n')
            self.login()
    def datafile(self,Logindata):
        '''Stores Customer Login data that are logged in uptill now'''
        f=open('customerlogindata.txt','a')
        for item in Logindata:
            f.write(str(item)+'\n')
        f.close()    
                
        
               
               
    ########### MAIN PROGRAM #############


L=LOGIN()
L.login()
        
