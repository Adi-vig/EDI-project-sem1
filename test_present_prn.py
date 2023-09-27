import pickle
import os
from datetime import datetime
import pymongo as pm

from collections import OrderedDict
from pathlib import Path
import pymongo as pm
import smtplib

final_file_prev= Path("final_presnt_prn.p")
if (final_file_prev.is_file()): 
    os.remove("final_presnt_prn.p")
loaded_prn_file = open("present.p", 'rb')
loaded_prn_list = pickle.load(loaded_prn_file)
loaded_prn_file.close()




non_duplicates =  list(OrderedDict.fromkeys(loaded_prn_list))

final_save_file = open("final_presnt_prn.p", 'wb')
pickle.dump(non_duplicates, final_save_file)
final_save_file.close()
non_duplicates=sorted(non_duplicates)



print("welcome to pymongo")
client_0 = pm.MongoClient("mongodb://localhost:27017")
print(client_0)


Base_db= client_0["Students_DB"]
base_col = Base_db["Students_Col"]






now = datetime.now()

dt_string = now.strftime("%d_%m_%Y %H:%M:%S")
print("date and time =", dt_string)
file_name= ("Attendance_db_"+dt_string)

attendance_db= client_0["Attendance_DB"]
attendance_col = attendance_db[file_name]


for i in non_duplicates: 
    curr_doc_present=base_col.find_one({'_id':int(i)})
    print("Present Studnets:")
    print(curr_doc_present['_id'])
    attendance_col.insert_one(curr_doc_present)



base_cur_= base_col.find()
present_DB_cur = attendance_col.find()



print("\n\n\n")



set_present = set(non_duplicates)

base_prn=[]
for i in base_cur_:
        base_prn.append(int(i['_id']))

set_base_prn=set(base_prn)
set_absent = set(set_base_prn-set_present)



server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login("<your email>", "<your password>")


for i in set_present:
    curr_doc=base_col.find_one({'_id':int(i)})
    message ='\n\n\n\nPRESENT \n\n\nAttendance status: PRESENT \nName: '+curr_doc['name']+ '\nRoll No: '+ str(curr_doc['rol_no'])
    # server.sendmail("sakharevig@gmail.com", curr_doc['email'], message)
    server.sendmail("sakharevig@gmail.com", "aditya2004cs@gmail.com", message)
    print("mail sent as present to ",i ," ", curr_doc['email'])
    

for i in set_absent:
    curr_doc=base_col.find_one({'_id':int(i)})
    message ='\n\n\n\nABSENT \n\n\nAttendance status: ABSENT \nName: '+curr_doc['name']+ '\nRoll No: '+ str(curr_doc['rol_no'])
    # server.sendmail("sakharevig@gmail.com", "aditya2004cs@gmail.com", message)
    # server.sendmail("sakharevig@gmail.com", curr_doc['email'], message)
    print("mail sent as absent to ",i," ", curr_doc['email'])
