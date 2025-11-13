import mysql.connector
from datetime import datetime

connection=None
cursor=None

def createUserDetails(userDetails):
    global connection
    global cursor
    try:
        connection=mysql.connector.connect(host='localhost',
                                           database='python_db',
                                           user='root',
                                           password='root',
                                           auth_plugin='mysql_native_password')
        sql_insert_qry="insert into user_details (First_Name,Last_Name, Email, Address1, Address2, City, State, Pincode, Password) values ("
        sql_insert_qry += "'" + userDetails["Fname"] + "', "
        sql_insert_qry += "'" + userDetails["Lname"] + "', "
        sql_insert_qry += "'" + userDetails["Email"] + "', "
        sql_insert_qry += "'" + userDetails["Addr1"] + "', "
        sql_insert_qry += "'" + userDetails["Addr2"] + "', "
        sql_insert_qry += "'" + userDetails["City"] + "', "
        sql_insert_qry += "'" + userDetails["State"] + "', "
        sql_insert_qry += userDetails["Pin"] + ", "
        sql_insert_qry += "'" + userDetails["Pwd"] + "')"
        cursor = connection.cursor()
        cursor.execute(sql_insert_qry)
        connection.commit()
        print(cursor.rowcount," Records inserted successfully")
        cursor.close()
        return "Registration Successful"
    except mysql.connector.Error as e:
        print("Failed to insert record into user_details table {}".format(e))
        return "Registration Failed...Try later"
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

def updateUserProfile(userDetails):
    global connection
    global cursor
    try:
        print("Before try inside update user profile")
        connection=mysql.connector.connect(host='localhost',
                                           database='python_db',
                                           user='root',
                                           password='root',
                                           auth_plugin='mysql_native_password')
        print("after connection")
        sql_update_qry="update user_details set "
        sql_update_qry +="First_Name = '" + userDetails["Fname"] +"',"
        sql_update_qry +="Last_Name = '" + userDetails["Lname"] + "',"
        sql_update_qry +="Address1 = '" + userDetails["Addr1"] + "',"
        sql_update_qry +="Address2 = '" + userDetails["Addr2"] + "',"
        sql_update_qry +="City = '" + userDetails["City"] + "',"
        sql_update_qry +="State = '" + userDetails["State"] + "',"
        sql_update_qry +="Pincode = " + userDetails["Pin"] + " "
        sql_update_qry +="where Email = '" + userDetails["Email"] + "'"
        print("update profile query")
        print(sql_update_qry)
        cursor = connection.cursor()
        cursor.execute(sql_update_qry)
        connection.commit()
        print(cursor.rowcount," Details updated successfully")
        cursor.close()
        return "Updated Profile Successfully"
    except mysql.connector.Error as e:
        print("Failed to update record into user_details table {}".format(e))
        return "Update Failed...Try later"
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


def updateUserDetails(username,password):
    global connection
    global cursor
    #print("inside update user details")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='python_db',
                                             user='root',
                                             password='root',
                                             auth_plugin='mysql_native_password')
        sql_update_qry = "update user_details set Password = '" + password + "' where Email = '" + username + "'"
        print(sql_update_qry)
        cursor = connection.cursor()
        cursor.execute(sql_update_qry)
        connection.commit()
        cursor.close()
        return "Password updated Successfully"
    except mysql.connector.Error as e:
        print("Failed to update record into user_details table {}".format(e))
        return "Update Password Failed...Try later"
    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

def getUserProfile(username):
    global connection
    global cursor
    print("user name inside user profile",username)
    try:
        connection=mysql.connector.connect(host='localhost',
                                       database='python_db',
                                       user='root',
                                       password='root',
                                        auth_plugin='mysql_native_password')
        sql_select_qry="select First_Name, Last_Name,Email, Address1, Address2, City, State, Pincode from user_details where Email='" + username + "'"
        cursor=connection.cursor()
        cursor.execute(sql_select_qry)
        records=cursor.fetchall()
        if username == "":
            rowcount=-1
        else:
            rowcount=cursor.rowcount;
        cursor.close()

        userProfile=[]
        for row in records:
            userProfile.append(row[0])
            userProfile.append(row[1])
            userProfile.append(row[2])
            userProfile.append(row[3])
            userProfile.append(row[4])
            userProfile.append(row[5])
            userProfile.append(row[6])
            userProfile.append(row[7])
            cursor.close()
            return userProfile
    except mysql.connector.Error as e:
        print ("Error = ", e)
        return "Error Occurred..Please Try again"

def getUserDetails(username,password):
    global connection
    global cursor
    try:
        connection=mysql.connector.connect(host='localhost',
                                       database='python_db',
                                       user='root',
                                       password='root',
                                        auth_plugin='mysql_native_password')
        sql_select_qry="select Password,User_ID from user_details where Email='" + username + "'"
        cursor=connection.cursor()
        cursor.execute(sql_select_qry)
        records=cursor.fetchall()
        if username == "":
            rowcount=-1
        else:
            rowcount=cursor.rowcount;
       #connection.close()
        cursor.close()

        if rowcount == 0:
            return "User ID not found...proceed to registration"
        elif rowcount == -1:
            return "Please fill all the values"
        else:
            for row in records:
                if(row[0] == password):
                    now=datetime.now()
                    dt_string=now.strftime("%Y-%m-%d %H:%M:%S")
                    print("date=",dt_string)
                    return "valid"
                    #try:
                    #    insert_query="insert into user_stats (user_id, Login_Dt_Time) values ("+str(row[1])+",'"+ dt_string + "')"
                    #    print(insert_query)
                    #    cursor=connection.cursor()
                    #    cursor.execute(insert_query)
                    #    connection.commit()
                    #    cursor.close()
                    #    return "valid"
                    #except mysql.connector.Error as e:
                    #    print("Error = ",e)
                    #    return "Error Occurred while inserting records into user statistics"
                else:
                    return "Invalid User Name Password combination"
    except mysql.connector.Error as e:
        print ("Error = ", e)
        return "Error Occurred..Please Try again"

def getAllUsers(caller):
    global connection
    global cursor
    try:
        connection=mysql.connector.connect(host='localhost',
                                       database='python_db',
                                       user='root',
                                       password='root',
                                        auth_plugin='mysql_native_password')
        if(caller=="login"):
            sql_select_qry="SELECT First_name,Last_Name,Login_Dt_Time from user_stats, user_details " \
                       "where user_stats.user_id=user_details.User_ID"
        elif(caller=="all"):
            sql_select_qry="SELECT Email,First_name,Last_Name from user_details"
        print(sql_select_qry)
        cursor=connection.cursor()
        cursor.execute(sql_select_qry)
        records=cursor.fetchall()
        cursor.close()
        return records
    except mysql.connector.Error as e:
        print ("Error = ", e)
        return "Error Occurred..Please Try again"

def getUserStats(user_name):
    global connection
    global cursor
    try:
        connection=mysql.connector.connect(host='localhost',
                                       database='python_db',
                                       user='root',
                                       password='root',
                                        auth_plugin='mysql_native_password')
        if("admin" in user_name):
            sql_select_qry="SELECT count(*) ,concat(First_name,'" + " ',Last_Name) from user_stats, user_details " \
                       "where user_stats.user_id=user_details.User_ID" \
                       " group by user_stats.user_id"
        else:
            sql_select_qry="SELECT count(*) ,CAST(Login_Dt_Time as DATE) " \
                            "from user_stats, user_details " \
                            "where user_stats.user_id=user_details.User_ID " \
                            "AND user_stats.user_id='2' " \
                            "group by CAST(Login_Dt_Time as DATE)"
        cursor=connection.cursor()
        cursor.execute(sql_select_qry)
        records=cursor.fetchall()
        cursor.close()
        userStats={}
        for row in records:
            userStats[row[1]] = row[0]
        print("user stats values")
        print(userStats)
        return userStats
    except mysql.connector.Error as e:
        print ("Error = ", e)
        return "Error Occurred..Please Try again"
