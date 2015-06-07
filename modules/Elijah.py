import MySQLdb
import MySQLdb.cursors
import datetime
import codecs

def encryptRot13(text):
	"""Function to encrypt a given string using the rot13 cipher and return the encrypted string."""
	return str(codecs.encode(text, 'rot_13'))

def decryptRot13(text):
	"""Function to decrypt a given string using the rot13 cipher and return the decrypted string."""
	return str(codecs.decode(text, 'rot_13'))

def getFlyerConnector():
	"""This method returns a MySQLdb connector, create a cursor and use it."""
	conn = MySQLdb.connect(host="""111.118.215.156""",user="oinkwdop_orwell", 
					passwd="bigbrother",db="oinkwdop_oink",cursorclass=MySQLdb.cursors.DictCursor)
	return conn

def addReport(report_type, report_text, reportee_id):
	"""This function adds a new report, the report_types should be one of the following:
	"OrgDev", "Performance", "Rewards"
	In that order, the user_ids are "pavan","kc" and "satish"."""
	conn = getFlyerConnector()
	cursor = conn.cursor()
	sqlcmd = """INSERT INTO `hr_reports` (`report_type`, `report_text`, `reportee_id`) 
	VALUES ("%s", "%s", "%s");""" %(report_type, report_text, reportee_id)
	cursor.execute(sqlcmd)
	conn.commit()
	conn.close()

def fetchLatestReports():
	"""This method fetches all the latest reports in a list of dictionaries.
	The table column names are the dictionary keys.
	"""
	conn = getFlyerConnector()
	cursor = conn.cursor()
	sqlcmd = """(SELECT * from `hr_reports` WHERE 
		`time_stamp` = (SELECT MAX(`time_stamp`) from `hr_reports` WHERE `report_type`="Performance")) UNION
		(SELECT * from `hr_reports` WHERE 
		`time_stamp` = (SELECT MAX(`time_stamp`) from `hr_reports` WHERE `report_type`="OrgDev")) UNION
		(SELECT * from `hr_reports` WHERE 
		`time_stamp` = (SELECT MAX(`time_stamp`) from `hr_reports` WHERE `report_type`="Rewards"));"""
	cursor.execute(sqlcmd)
	data = cursor.fetchall()
	conn.close()
	return data

def modifyReport(report_type, reportee_id, query_date, new_report_text):
	"""Change the report text for a given date, report type and reportee_id."""
	conn = getFlyerConnector()
	cursor = conn.cursor()
	start_time_stamp = datetime.datetime(query_date.year, query_date.month, query_date.day, 0, 0, 0)
	end_time_stamp = datetime.datetime(query_date.year, query_date.month, query_date.day, 23, 59, 59)
	sqlcmd = """UPDATE `hr_reports` SET `report_text`="%s" WHERE 
		`reportee_id`="%s" AND `report_type`="%s" AND 
		`time_stamp` BETWEEN "%s" AND "%s";""" %(new_report_text, reportee_id, report_type, start_time_stamp, end_time_stamp)
	cursor.execute(sqlcmd)
	data = cursor.fetchall()
	conn.commit()
	conn.close()

def login(user_id, password):
	"""Check if a password matches a user_id. 
	Return True if it does, False either 
	if the password is incorrect or if there's no such user."""
	conn = getFlyerConnector()
	cursor = conn.cursor()
	sqlcmd = """SELECT `password` from `user_records` WHERE `user_id`="%s";"""%user_id
	cursor.execute(sqlcmd)
	data = cursor.fetchall()
	conn.close()
	if len(data) == 0:
		return False
	else:
		return (decryptRot13(data[0]["password"]) == password)

def getUserDetails(user_id):
	"""For a user_id, this gives the user_name and email. Returns false if such a user doesn't exist."""
	conn = getFlyerConnector()
	cursor = conn.cursor()
	sqlcmd = """SELECT `user_name`, `user_email_id` FROM `user_records` WHERE `user_id`="%s";""" %user_id
	cursor.execute(sqlcmd)
	data = cursor.fetchall()
	conn.close()
	if len(data) == 0:
		return False
	else:
		return data[0] #data is a tuple of dictionaries with len=1 in this case

def getEditableReports(user_id):
	"""Given a user_id and report type, this function returns true if a user can edit it or false if he can't."""
	conn = getFlyerConnector()
	cursor = conn.cursor()
	sqlcmd = """SELECT `editable_reports` FROM `user_records` WHERE `user_id` = "%s";""" %(user_id)
	cursor.execute(sqlcmd)
	data = cursor.fetchall()
	conn.close()
	if len(data) == 0:
		return "NA"
	else:
		reports = data[0]["editable_reports"]
		if reports == None:
			reports = []
			return reports
		else:
			return reports.split(',')

def changePassword(user_id, password):
	"""Given a user ID, this method modifies the password."""
	encrypted_password = encryptRot13(password)
	conn = getFlyerConnector()
	cursor = conn.cursor()
	sqlcmd = """UPDATE `user_records` SET `password`="%s" WHERE `user_id` = "%s";""" %(password, user_id)
	cursor.execute(sqlcmd)
	conn.commit()
	conn.close()
