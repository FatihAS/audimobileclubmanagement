import json
from app.conn.conn import mysql

class db:
    def getAllTuyul():
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT tu.id "id" ,tu.username "username", tu.nick "nickname", password, ti.nama_title "title", ruby FROM tuyuls tu inner JOIN titles ti on ti.id = tu.title')
        data = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        for result in data:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)
    
    def getTuyul(id):
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT tu.id "id" ,tu.username "username", tu.nick "nickname", password, ti.nama_title "title", ruby FROM tuyuls tu inner JOIN titles ti on ti.id = tu.title where tu.id='+id)
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
            cursor.execute("UPDATE `tuyuls` SET username = '"+ data['username'] +"', nick = '"+ data['nickname'] +"', password = '"+ data['password'] +"', title = '"+ data['title'] +"', ruby = '"+ data['ruby'] +"' WHERE `tuyuls`.`id` = '"+ data['id'] +"';")
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
            cursor.execute("INSERT INTO `tuyuls` (`id`, `username`, `nick`, `password`, `title`, `ruby`) VALUES (NULL, '"+ str(data['username']) +"', '"+ str(data['nickname']) +"' , '"+ str(data['password']) +"', '"+ str(data['title']) +"', '"+ str(data['ruby']) +"');")
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

    def getAllPusher():
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT tuyuls.id "id", pusher.id "id_pusher", tuyuls.username "username", tuyuls.nick "nickname", tuyuls.password, titles.nama_title "title", members.nick "nick_pusher", tuyuls.ruby FROM tuyuls INNER JOIN pusher on tuyuls.id = pusher.id_tuyul INNER JOIN titles on tuyuls.title = titles.id INNER JOIN members on members.id = pusher.id_member')
        data = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        for result in data:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)

    def getAllAvailableTuyul():
        cursor = mysql.connection.cursor()

        cursor.execute('SELECT tuyuls.id "id", tuyuls.username, tuyuls.nick "nickname", titles.nama_title "title", tuyuls.password, tuyuls.ruby from tuyuls LEFT OUTER JOIN pusher on pusher.id_tuyul = tuyuls.id INNER JOIN titles on titles.id = tuyuls.title where pusher.id_member is null')
        data = cursor.fetchall()
        row_headers=[x[0] for x in cursor.description]
        json_data=[]
        for result in data:
                json_data.append(dict(zip(row_headers,result)))
        return json.dumps(json_data)

    def addPusher(data):
        ret = {}
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("INSERT INTO pusher (pusher.id_member, pusher.id_tuyul) SELECT members.id, tuyuls.id FROM tuyuls, members WHERE tuyuls.username = '"+ data['username'] +"' and members.nick='"+ data['pushername'] +"'")
            mysql.connection.commit()
            ret['status'] = True
            return json.dumps(ret)
        except Exception as e:
            ret['status'] = False
            ret['message'] = str(e)
            return json.dumps(ret)
    
    def delPusher(id):
        ret = {}
        try:
            cursor = mysql.connection.cursor()
            cursor.execute("DELETE FROM pusher where id="+id)
            mysql.connection.commit()
            ret['status'] = True
            return json.dumps(ret)
        except Exception as e:
            ret['status'] = False
            ret['message'] = str(e)
            return json.dumps(ret)