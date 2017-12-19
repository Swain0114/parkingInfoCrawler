from controller import *
# path = '/Users/swain/Desktop/software_engineering/database/parking_file/parking_file'
# now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
res = requests.get("http://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f")
data = res.json()
sched = BlockingScheduler()
# 將資料寫至local file
# fd = open(path + str(now) + '-ParkingLotInfo.json', 'w')
# json.dump(data,fd,indent=1,ensure_ascii=False)
# pprint.pprint(data)
# query = "SELECT * FROM ParkingInfo"
# pprint.pprint(getMysqlData(gcp_cur_mysql,query))
@sched.scheduled_job('interval', minutes=3)
def timed_job():
	for row in data['parkingLots']:
		# print(row)
		query = "UPDATE ParkingInfo SET surplusSpace = '%s', update_dt = '%s' WHERE parkId = '%s'"%(row['surplusSpace'], now ,row['parkId'])
		print(query)
		msg = insertMysql(lab_cur_mysql, query)

sched.start()