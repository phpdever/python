import MySQLdb

conn = MySQLdb.connect(
	host = '127.0.01',
	user = 'root',
	passwd = '',
	db = 'tyf',
	port = 3306,
	charset = 'utf8'
)