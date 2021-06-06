# Send to single device.
from pyfcm import FCMNotification
import pyodbc
import traceback
from datetime import datetime,timedelta


now = now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %I:%M %p")


def get_token_list(user_ids):
    conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                        "Server=192.168.100.75;"
                        "Database=DCR;"
                        "Trusted_Connection=no;"
                        "UID=sa;"
                        "PWD=dataport;")
    cursor = conn.cursor()
    
    format_strings = ','.join(['?'] * len(user_ids))
    #cursor.execute("select Tocket From UserTocken WHERE UserId IN (%s)" % format_strings,tuple(user_ids))
    cursor.execute(
        "WITH TOPTWO AS (\
            SELECT Tocket ,ROW_NUMBER()\
            over (\
                PARTITION BY [UserId] \
                order by [EntryDate] DESC\
            ) AS RowNo \
            FROM [UserTocken]\
            WHERE UserId IN (%s) \
        ) SELECT * FROM TOPTWO WHERE RowNo <= 3" % format_strings,tuple(user_ids)
    )

    final_result = [item[0] for item in cursor.fetchall()]
    #print(final_result)
    return final_result

def send_notification_to_multiple_device(registration_ids,message_title,message_body):
    print(registration_ids)
    data_message = {
        "title" : message_title,
        "body"  : message_body,
        "Room"  : "RxUpdate"
    }
    # harvester key
    #registration_ids = ['cBv17BFKSw6M8xVw5IYIxu:APA91bE3d4yUF7yxAMHzKXwmA-Xms7SkAac9c1X-ulZKO3D1TDOImCtapUgUAvw75uoTzNiTLAj8tLTs-eWgukyutirs2o7FS_U6VQG27heqapF2DwLdEBlWQIwSwCJMfXiKDFuISiKn']
    #push_service = FCMNotification(api_key="AAAApQJqMHs:APA91bF9tP2h3mf4q1jcNc_tXuR1iwf55uG9w3YiABK8ER1FQBIizo7L2SCrDHC9Rf3DB8gQCa66v-qzbaBj-Ljz5RBfwrlSjxY2P-rL9oRAr0A3fVlMkxFbgeimeMFkhH03pxsSHSLR")
    #harvester key end
    push_service = FCMNotification(api_key="AAAAXZYbxLQ:APA91bFEjqKFYm-LU8-NBlumM_Djl2oHngxlK8x49JrU3wrlWdJqVE48z0lhaJDXm6u7VzWYJI70nIOUq0gBSMIIOprMC201c4hpUcT0g4taevC9N0JO_H9CZVuKhO6xba0FNWt9bdxm")
    #result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)
    result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body, data_message=data_message)
    print(result)
    return result


def send_nofification_to_users(business,user_ids,message_title,message_body):
    registration_ids = get_token_list(user_ids)
    #send notiification
    try:
        result = send_notification_to_multiple_device(registration_ids,message_title,message_body) 
        #with open("logs/notification_logs/"+business+"_success.txt", "a") as text_file:
        #    text_file.write(dt_string + " Notification SENT ->" +','.join(str(x) for x in user_ids)+'\n'+ str(result) )        
    except Exception as e:
        s = str(e)
        s += str(traceback.format_exc())
        print(s)
        #with open("logs/notification_logs/"+business+"_failed.txt", "a") as text_file:
        #    text_file.write(dt_string + "->" + s + '\n') 
    


#send_nofification_to_users('test',['YCB14'],'Neoronta (Rx Update)','this is test notification')
