
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk




UI_FILE = "UserInterface.glade"




class GUI:
    entry = dict()
    values = dict()


    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)
        opts=Gtk.ListStore(int,str)
        options = ["High","Medium","Low"]
        for o in options:
            opts.append([None,o])
        self.entry[9] = self.builder.get_object("entry9") #access level
        self.entry[9].set_model(opts)
        self.entry[9].set_entry_text_column(1)
        self.window = self.builder.get_object('window')
        self.window.show_all()








    def on_window_destroy(self, window):
        Gtk.main_quit()








    def home_clicked (self, button):
        stack = self.builder.get_object('stack')
        home_button = self.builder.get_object('home_button')
        stack.set_visible_child(home_button)









    def button_clicked (self, button):
        stack = self.builder.get_object('stack')
        notebook_box = self.builder.get_object('notebook_box')
        stack.set_visible_child(notebook_box)








    def applicationFormOpenButton(self,button):
        infoLabel = self.builder.get_object('infoLabel')
        infoLabel.set_text('Application Form is being opened.')
        stack = self.builder.get_object('stack')
        applicationForm = self.builder.get_object('ApplicationFormBox')
        stack.set_visible_child(applicationForm)








    def queryButton(self,button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('Querying Data for '+str(value))
            dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Queried data for "+str(value))
            result = 'some text' # insert your querying data command here after formatting it as required
            dialog.format_secondary_text(result)
            dialog.run()
            dialog.destroy()









    def revokeButton(self,button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('Revoking data access of '+str(value)+'.')








    def deleteDataButton(self,button):
        entry = self.builder.get_object('usernameEntry')
        infoLabel = self.builder.get_object('infoLabel')
        value = str(entry.get_text())
        if value == '':
            infoLabel.set_text('Username field is empty')
        else:
            infoLabel.set_text('Deleting data for '+str(value)+'. This user has been forgotten.')







    def applicationFormSubmitButton(self,button):
        self.entry[1] = self.builder.get_object('entry1') #userID
        self.entry[2] = self.builder.get_object('entry2') #Src
        self.entry[3] = self.builder.get_object('entry3') #Name
        self.entry[4] = self.builder.get_object('entry4') #Date
        self.entry[5] = self.builder.get_object('entry5') #phone
        self.entry[6] = self.builder.get_object('entry6') #creditcard
        self.entry[7] = self.builder.get_object('entry7') #aadhar
        self.entry[8] = self.builder.get_object('entry8') #email
        noticeLabel = self.builder.get_object('noticeLabel')
        emptyCheck = True
        for i in range(1,9):
            if i == 4 :
                continue
            self.values[i] = str(self.entry[i].get_text())
            if(self.values[i] == ''):
                emptyCheck = True
                notice = "\n Entry field "+str(i)+" is empty."
                print(notice)
                noticeLabel.set_text(notice)
                break
            emptyCheck = False
        if(emptyCheck == False):
            file = open("result.txt","w")
            for i in range(1,10):
                print(i)
                if i == 4 :
                    date = self.entry[4].get_date()
                    val = str(date[2])+'-'+str(date[1])+'-'+str(date[0])
                elif i == 9 :
                    access = self.entry[9].get_model()[self.entry[9].get_active()]
                    val = access[1]
                else:
                    val = self.entry[i].get_text()
                self.values[i] = str(val)
                print(self.values[i])
                file.write(self.values[i]+"\n")
            file.write(" ")
            file.close()
            dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO,Gtk.ButtonsType.OK, "Application Form")
            result = 'Submitted Successfully'
            dialog.format_secondary_text(result)
            dialog.run()
            dialog.destroy()
            # r = os.popen('./scripts/initLedger.sh').read()
            # print(r)
            for i in range(1,9):
                if i == 4 :
                    continue
                elif i == 9 :
                    continue
                else :
                    self.entry[i].set_text('')
            stack = self.builder.get_object('stack')
            notebook_box = self.builder.get_object('notebook_box')
            stack.set_visible_child(notebook_box)








app = GUI()
Gtk.main()