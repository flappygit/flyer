import datetime
import gitpython


def getLatestReport(report_type, query_date=None):
	"""Given a report type, it tries to get the latest report for a given date."""
	if query_date is None:
		query_date = datetime.date.today()
	if report_type == 1:
		report_name = getOrgDevReportName(query_date)
		#get the Org dev Report
	elif report_type ==2:
		report_name = getPerfReportName(query_date)
		#get the Performance Report
	elif report_type == 3:
		report_name = getRewardsReportName(query_date)
		#get the Rewards reports

def getLastUpdateDetails(query_date=None):
	if query_date == None:
		query_date = datetime.date.today()

def createNewReport(report_type):
	if report_type == 1:
		#get the Org dev Report
	elif report_type ==2:
		#get the Performance Report
	elif report_type == 3:
		#get the Rewards reports

def getQuote():
	
	return quote, author

def getOrgDevReportName(query_date):
	return "OrgDevRep_%s.txt"%query_date.strftime("%Y%m%d")

def getPerfReportName(query_date):
	return "PerfRep_%s.txt" %query_date.strftime("%Y%m%d")

def getRewardsReportName(query_date):
	return "RewardsRep_%s.txt"%query_date.strftime("%Y%m%d")