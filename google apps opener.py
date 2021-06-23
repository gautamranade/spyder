import webbrowser
p = 'http://jamboard.com' 
url='http://google.com'
d= 'http://googlemaps.com'
g='http://Netflix.com'

print (" welcome, I can open google apps!!!")
command=input ('press g to open google,press j to open jamboard,press m to open gmaps,press n to open netflix-')




if 'g' in command :
    print ('opening google............') 
    webbrowser.open(url) 


                 #end of google program#     





elif "j" in command :
      print('opening jam.........')
      webbrowser.open(p)
    

                 #end of jamboard#
    
elif "m" in command:
     print('opening gMaps..........')
     webbrowser.open(d)
    
    #end of maps#
    
    
elif "n" in command:
     print('opening playstore..........')
     webbrowser.open(g)      