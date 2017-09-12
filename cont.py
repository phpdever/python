import MySQLdb
try:
	conn = MySQLdb.connect(
		host = '127.0.0.1',
		user = 'root',
		passwd = '',
		db = 'tyf',
		port = 3306,
		charset = 'utf8'
	)
	cursor = conn.cursor()

	cursor.execute('select * from weixin_user where id=23629')

	res = cursor.fetchone();

	print(res)

	conn.close()
	
except MySQLdb.Error as e:
	print('Error:%s'%e)