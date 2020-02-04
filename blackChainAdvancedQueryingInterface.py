from tkinter import *
import os

window = Tk()
window.title('Query Window')
mainframe = Frame(window)

def QueryData():
    print('Querying now ... please be patient')
    user = StringVar()
    userId = StringVar()
    user = userType.get().lower()
    userId = entry.get()
    r = os.popen('./scripts/queryAdv.sh 1 ' + user + ' ' + userId).read()
    print(r)


def RevokeConsent():
    print('Revoking Consent now ... they won\'t see what hit \'em')
    user = StringVar()
    userId = StringVar()
    user = userType.get().lower()
    userId = entry.get()
    r = os.popen('./scripts/queryAdv.sh 2 ' + user + ' ' + userId).read()
    print(r)


def PurgeData():
    print('Purging now ... it\'s judgement day')
    user = StringVar()
    userId = StringVar()
    user = userType.get().lower()
    userId = entry.get()
    r = os.popen('./scripts/queryAdv.sh 3 ' + user + ' ' + userId).read()
    print(r)


def setButtonVisibility(self):
    user = StringVar()
    user = userType.get()
    if(user == 'Users'):
        button1['state'] = 'normal'
        button2['state'] = 'normal'
        button3['state'] = 'normal'
    else:
        button1['state'] = 'normal'
        button2['state'] = 'disabled'
        button3['state'] = 'disabled'

userType = StringVar()
userOptions = {'Airport','CCD','Users'}
userType.set('User')
menu = OptionMenu(mainframe,userType,*userOptions,command=setButtonVisibility)
Label(mainframe,text='Organization : ').grid(row=0,column=0)
menu.grid(row = 0,column = 1)

Label(mainframe,text='User ID : ').grid(row=1,column=0)
entry = Entry(mainframe)
entry.grid(row = 1,column=1)

button1 = Button(mainframe,text='Query Data',command=QueryData)
button2 = Button(mainframe,text='Purge Data',command=PurgeData)
button3 = Button(mainframe,text='Revoke Consent',command=RevokeConsent)
button1.grid(row=2,column=1)
# button1['state'] = 'disabled'
button2.grid(row=3,column=0)
# button2['state'] = 'disabled'
button3.grid(row=3,column=2)
# button3['state'] = 'disabled'
mainframe.pack()
window.mainloop()
