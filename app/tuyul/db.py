import json
from app.conn.conn import mysql

class db:
    def getAllTuyul():
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT tu.id "id" ,tu.username "username", password, ti.nama_title "title", ruby FROM tuyuls tu inner JOIN titles ti on ti.id = tu.id')
        data = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        for result in data:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)