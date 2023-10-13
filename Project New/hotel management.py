import pickle
print('='*15,'Welcome To TGC Hotel','='*15,'\n')
print('Please enter your personal details')
n=input('Enter the name:')
a=input('Enter the address:')
ci=int(input('Enter check-in ID:'))
co=int(input('Enter check-out ID:'))
rn=int(input('Enter the room number:'))
print('')
f=open(n+'-'+str(ci)+'_data'+'.bin','wb')
data={'Name':n,'Address':a,'Check-in ID':ci,'Check-out ID':co,'Room No.':rn}
data1={}
pickle.dump(data,f)
f.close()
print('')
while True:
    print('\nWhat would you like to do?\n')
    print('1.) Calculate room rent')
    print('2.) Calculate restaurant bill')
    print('3.) Calculate laundry bill')
    print('4.) Show total cost')
    print('5.) Exit\n')
    c=int(input('Enter your choice:'))
    if c==1:
        print('The following rooms are available:')
        print('1.) Basic Suite ---> RS 3000 per night')
        print('2.) Executive Suite ---> RS 4000 per night')
        print('3.) Luxury Suite ---> RS 5000 per night')
        rr=int(input('Enter your choice:'))
        ns=int(input('Enter nights stayed:'))
        print('')
        if rr==1:
            tr=3000*ns
            print('Total room rent is: Rs',tr)
            print('')
        elif rr==2:
            tr=4000*ns
            print('Total room rent is: Rs',tr)
            print('')
        elif rr==3:
            tr=5000*ns
            print('Total room rent is: Rs',tr)
            print('')
        dtr={'Total Rent':tr}
        data1.update(dtr)
        f=open(n+'-'+str(ci),'wb')
        pickle.dump(data1,f)
        f.close()
    elif c==2:
        print('1.) Breakfast')
        print('2.) Lunch')
        print('3.) Dinner')
        rc=int(input('Choose your menu:'))
        print('')
        bcost=0
        lcost=0
        dcost=0
        if rc==1:
            print('='*5,'BREAKFAST','='*5)
            print('1.) Omelette (RS 100)')
            print('2.) Corn Flakes (RS 50)')
            print('3.) Aloo Parantha (RS 80)')
            print('4.) Paneer Parantha (RS 75)')
            bcost=0
            while True:
                bchoice=int(input('Please enter your choice (in RS):'))
                if bchoice==100 or bchoice==80 or bchoice==75 or bchoice==50:
                    bcost+=bchoice
                else:
                    print('Invalid Choice')
                con1=input('Would you like to order more items? (y/n):')
                if con1.lower()=='n':
                    break    
        elif rc==2:
            print('='*5,'LUNCH','='*5)
            print('1.) Rajma Rice (RS 75)')
            print('2.) Dal Makhani (RS 50)')
            print('3.) Chole Bhature (RS 80)')
            print('4.) Burger (RS 100)')
            lcost=0
            while True:
                lchoice=int(input('Please enter your choice (in RS):'))
                if lchoice==100 or lchoice==80 or lchoice==75 or lchoice==50:
                    lcost+=lchoice
                else:
                    print('Invalid Choice')
                con2=input('Would you like to order more items? (y/n):')
                if con2.lower()=='n':
                    break
        elif rc==3:
            print('='*5,'DINNER','='*5)
            print('1.) Pasta (RS 75)')
            print('2.) Pizza (RS 80)')
            print('3.) Kadhai Paneer (RS 50)')
            print('4.) Tandoori Platter (RS 100)')
            dcost=0
            while True:
                dchoice=int(input('Please enter your choice (in RS):'))
                if dchoice==100 or dchoice==80 or dchoice==75 or dchoice==50:
                    dcost+=dchoice
                else:
                    print('Invalid Choice')
                con3=input('Would you like to order more items? (y/n):')
                if con3.lower()=='n':
                    break
        dfc={'Food Cost':bcost+lcost+dcost}
        data1.update(dfc)
        f=open(n+'-'+str(ci),'wb')
        pickle.dump(data1,f)
        f.close()
    elif c==3:
        print('')
        print('='*5,'Laundry Charges','='*5)
        print('1.) Light Clothes (T-shirts, Shirts, Light Jackets, Trousers, Shorts, Pyjamas, etc.) (RS 4 Per Garment)')
        print('2.) Heavy Clothes (Coats, Jeans, Windcheaters, Hoodies, Pullovers, etc.) (RS 5 Per Garment)')
        lacost=0
        while True:
            lachoice=int(input('Please enter your choice (in RS):'))
            if lachoice==4 or lachoice==5:
                lacost+=lachoice
            else:
                print('Invalid Choice')
            con4=input('Would you like to add more garments? (y/n):')
            if con4.lower()=='n':
                break
        dla={'Laundry Cost':lacost}
        data1.update(dla)
        f=open(n+'-'+str(ci),'wb')
        pickle.dump(data1,f)
        f.close()
    elif c==4:
        tn=input('Enter your name:')
        tci=int(input('Enter your check-in ID:'))
        print('')
        f=open(n+'-'+str(ci)+'_data'+'.bin','rb')
        g=open(tn+'-'+str(tci),'rb')
        dic=pickle.load(f)
        dic1=pickle.load(g)
        tcost=0
        for i in dic.keys():
            print(i,':',dic[i])
        for j in dic1.keys():
            print(j,':',dic1[j])
            tcost+=int(dic1[j])
        print('Total charges for your stay:',tcost)
        print('')
    elif c==5:
        break
        
    
        
        
        
        
    
        
    
    
        
    
