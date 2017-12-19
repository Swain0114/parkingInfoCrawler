from controller import *

path = '/Users/swain/Desktop/software_engineering/database/parking_file/parking_file'
# def writeToJsonFile(path, fileName, data):
# 	filePathNameWExt = './' + path + '/' + fileName + '.json'
# 	with open(filePathNameWExt, 'w') as outfile:
# 		json.dump(data, outfile)
# 	return 
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#URL： http://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f
res = requests.get("http://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f")
data = res.json()
# datas = []
# df = pd.read_json('桃園-路外停車資訊.json')
# pprint.pprint(data)
# data_titles = ['address','areaId','areaName','introduction','parkId','parkName','payGuide','surplusSpace','totalSpace','wgsX','wgsY']
# pprint.pprint(data['parkingLots'])
# print(len(data['parkingLots']))
target = '小時'
target2 = '時'
target3 = '次'
target4 = '元'
seq = 0
for lot in data['parkingLots']:
	# pprint.pprint(lot)
	# pprint.pprint(lot['payGuide'])
	# print(lot['payGuide'].find(target))
	# print(lot['payGuide'][:lot['payGuide'].find(target)+2])
	result = lot['payGuide'][:lot['payGuide'].find(target)+2]
	# pprint.pprint(result)
	if '/' not in result:
		# print(lot['payGuide'])
		# pprint.pprint(lot['payGuide'][:lot['payGuide'].find(target2)+1])
		result = lot['payGuide'][:lot['payGuide'].find(target2)+1]
		# pprint.pprint(result)
		if target3 in lot['payGuide']:
			# pprint.pprint(lot['payGuide'])
			result = lot['payGuide'][:lot['payGuide'].find(target3)+1]
			# pprint.pprint(result)
		# elif target2 in lot['payGuide']:
			# pprint.pprint(lot['payGuide'][:lot['payGuide'].find(target4)+1])

	seq = seq + 1
	query = "INSERT INTO ParkingInfo(id,areaId,areaName,parkName,totalSpace,surplusSpace,payGuide,introduction,address,wgsX,wgsY,parkId) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(seq,lot['areaId'],lot['areaName'],lot['parkName'],lot['totalSpace'],lot['surplusSpace'],result,lot['introduction'],lot['address'],lot['wgsX'],lot['wgsY'],lot['parkId'])
	print(query)
	msg = insertMysql(lab_cur_mysql, query)
	



''' SQL
INSERT INTO ParkingInfo(
id,areaId,areaName,parkName,totalSpace,surplusSpace,payGuide,introduction,address,wgsX,wgsY,parkId)
VALUES(
1,1,'桃園區','府前地下停車場',344,89,'停車費率:30 元/小時。停車時數未滿一小時者，以一小時計算。逾一小時者，其超過之不滿一小時部分，如不逾三十分鐘者，以半小時計算；如逾三十分鐘者，仍以一小時計算收費。','桃園市政府管轄之停車場','桃園區縣府路一號',121.3011,24.9934,'P-TY-001'
);
'''

# pprint.pprint(datas)
# print(datas[0])