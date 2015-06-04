import MySQLdb
import MySQLdb.cursors
import datetime


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
