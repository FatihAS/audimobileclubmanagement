import json
from app.conn.conn import mysql

class db:
    def getAllTuyul():
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT tu.id "id" ,tu.username "username", password, ti.nama_title "title", ruby FROM tuyuls tu inner JOIN titles ti on ti.id = tu.title')
        data = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        for result in data:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    
    def getTuyul(id):
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT tu.id "id" ,tu.username "username", password, ti.nama_title "title", ruby FROM tuyuls tu inner JOIN titles ti on ti.id = tu.title where tu.id='+id)
        data = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        for result in data:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    
    def editTuyul(data):
        ret = {}
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("UPDATE `tuyuls` SET username = '"+ data['username'] +"', password = '"+ data['password'] +"', title = '"+ data['title'] +"', ruby = '"+ data['ruby'] +"' WHERE `tuyuls`.`id` = '"+ data['id'] +"';")
            mysql.connection.commit()
            ret['status'] = True
            return json.dumps(ret)
        except Exception as e:
            ret['status'] = False
            ret['message'] = str(e)
            return json.dumps(ret)

    def delTuyul(id):
        ret = {}
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM tuyuls where id="+id)
            mysql.connection.commit()
            ret['status'] = True
            return json.dumps(ret)
        except Exception as e:
            ret['status'] = False
            ret['message'] = str(e)
            return json.dumps(ret)

    def addTuyul(data):
        ret = {}
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO `tuyuls` (`id`, `username`, `password`, `title`, `ruby`) VALUES (NULL, '"+ str(data['username']) +"', '"+ str(data['password']) +"', '"+ str(data['title']) +"', '"+ str(data['ruby']) +"');")
            mysql.connection.commit()
            ret['status'] = True
            return json.dumps(ret)
        except Exception as e:
            ret['status'] = False
            ret['message'] = str(e)
            return json.dumps(ret)

    def getAllTitle():
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT * FROM titles')
        data = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        for result in data:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
