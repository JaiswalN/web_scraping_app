from mymodule import funproject2,funproject3,funproject4

inp= int(raw_input("which page do you want to see?? \n Press 1 for watching Mp4-Videos \n Press 2 for Groceries \n Press 3 for news"))
if inp==1:
    funproject2.main()
elif inp==2:
    funproject3.main()
elif inp==3:
    funproject4.main()
else:
    print "Invalid choice!!!"
