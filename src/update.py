from controller import *
# path = '/Users/swain/Desktop/software_engineering/database/parking_file/parking_file'
# now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
res = requests.get("http://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f")
data = res.json()
sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=2)
def timed_job():
	# 因架設在heroku上，時區需要+8
	query = "SELECT parkId, avg(star) as avgStar FROM comment GROUP BY parkid"
	star = getMysqlData(lab_cur_mysql,query)
	now = datetime.datetime.now() + datetime.timedelta(hours=8)
	now = now.strftime("%Y-%m-%d %H:%M:%S")
	for row in data['parkingLots']:
		# print(row)
		for rank in star:
			if rank['parkId'] == row['parkId']:
				row['star'] = float(rank['avgStar'])
		if len(row) == 12:
			query = "UPDATE ParkingInfo SET surplusSpace = '%s', star = '%s' ,update_dt = '%s' WHERE parkId = '%s'"%(row['surplusSpace'], row['star'] ,now ,row['parkId'])
		else:
			query = "UPDATE ParkingInfo SET surplusSpace = '%s', update_dt = '%s' WHERE parkId = '%s'"%(row['surplusSpace'], now ,row['parkId'])
		print(query)
		msg = insertMysql(lab_cur_mysql, query)

sched.start()