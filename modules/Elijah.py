import MySQLdb
import MySQLdb.cursors
import datetime


def getFlyerConnector():
	conn = MySQLdb.connect(host="""111.118.215.156""",user="oinkwdop_orwell", 
					passwd="bigbrother",db="oinkwdop_oink",cursorclass=MySQLdb.cursors.DictCursor)
	return conn

def addReport(report_type, report_text, reportee_id):
	conn = getFlyerConnector()
	cursor = conn.cursor()
	sqlcmd = """INSERT INTO `hr_reports` (`report_type`, `report_text`, `reportee_id`) 
	VALUES ("%s", "%s", "%s");""" %(report_type, report_text, reportee_id)
	cursor.execute(sqlcmd)
	conn.commit()
	conn.close()

def fetchLatestReports(query_date):
	pass

def modifyReport(report_job_card, report_text):
	pass

