import webbrowser

tp = input('enter todays day:- ').lower()

url = ('http://classroom.google.com')

if tp == 'monday':
    print("period 1: geography")    
    print('period 2: english')   
    print("period 3: history")    
    print("period 4: computer")    
    print('period 5: maths')
    webbrowser.open(url)

elif tp == 'tuesday':
    print("period 1: maths")
    print('period 2: biology')
    print("period 3: english")
    print("period 4: physics")
    print('period 5: marathi')
    webbrowser.open(url)

elif tp == 'wednesday':
    print("period 1: maths")
    print('period 2: chemistry')
    print("period 3: english")
    print("period 4: hindi")
    print('period 5: maths')
    webbrowser.open(url)
    
elif tp == 'thursday':
    print('holiday,holiday,holiday!!!!')
    
elif tp == 'sunday':
    print('party,party,party!!!!!')    
    
    

elif tp == 'friday':
    print("period 1: maths")
    print('period 2: history')
    print("period 3: hindi")
    print("period 4: marathi")
    print('period 5: english')
    webbrowser.open(url)

elif tp == 'saturday':
    print("period 1: physics")
    print('period 2: maths')
    print("period 3: geography")
    print("period 4: chmistry")
    print('period 5: english')
    webbrowser.open(url)


else:
    print('please enter a valid day,if you have entered a valid day,try running the program again')
    