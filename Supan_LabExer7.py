from tkinter import *

root = Tk()
root.title('Calculator')

Label(root,text="Standard").grid(row=0, column=0, sticky='w', columnspan=12)
Entry(root).grid(row=1,column=0,padx=2,pady=2,sticky='we', columnspan=12, ipady=10)


Button(root, text="MC").grid(row=2,column=0,padx=2,pady=2,sticky='we', columnspan=2, ipadx=5, ipady=4)
Button(root, text="MR").grid(row=2,column=2,padx=2,pady=2,sticky='we', columnspan=2, ipadx=5, ipady=4)
Button(root, text="M+").grid(row=2,column=4,padx=2,pady=2,sticky='we', columnspan=2, ipadx=5, ipady=4)
Button(root, text="M-").grid(row=2,column=6,padx=2,pady=2,sticky='we', columnspan=2, ipadx=5, ipady=4)
Button(root, text="MS").grid(row=2,column=8,padx=2,pady=2,sticky='we', columnspan=2, ipadx=5, ipady=4)
Button(root, text="M*").grid(row=2,column=10,padx=2,pady=2,sticky='we', columnspan=2, ipadx=5, ipady=4)


Button(root, text="%").grid(row=3,column=0,padx=2,pady=2,sticky='we', columnspan=2,  ipady=4)
Button(root, text="CE").grid(row=3,column=3,padx=2,pady=2,sticky='we', columnspan=2,  ipady=4)
Button(root, text="C").grid(row=3,column=6,padx=2,pady=2,sticky='we', columnspan=2, ipady=4)
Button(root, text="BS").grid(row=3,column=9,padx=2,pady=2,sticky='we', columnspan=2, ipady=4)

Button(root, text="1/X").grid(row=4,column=0,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="x^2").grid(row=4,column=3,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="sqr").grid(row=4,column=6,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="/").grid(row=4,column=9,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)

Button(root, text="7").grid(row=5,column=0,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="8").grid(row=5,column=3,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="9").grid(row=5,column=6,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="*").grid(row=5,column=9,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)

Button(root, text="4").grid(row=6,column=0,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="5").grid(row=6,column=3,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="6").grid(row=6,column=6,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="-").grid(row=6,column=9,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)

Button(root, text="1").grid(row=7,column=0,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="2").grid(row=7,column=3,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="3").grid(row=7,column=6,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="+").grid(row=7,column=9,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)

Button(root, text="+/-").grid(row=8,column=0,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="0").grid(row=8,column=3,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text=".").grid(row=8,column=6,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="=").grid(row=8,column=9,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)

Button(root, text="%").grid(row=3,column=0,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="CE").grid(row=3,column=3,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="C").grid(row=3,column=6,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
Button(root, text="BS").grid(row=3,column=9,padx=2,pady=2,sticky='we', columnspan=3, ipady=4)
root.mainloop()








