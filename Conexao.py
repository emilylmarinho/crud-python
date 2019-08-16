import pymysql

class Conexao():

    def conecta():
        return pymysql.connect("localhost", "useraula", "senhaSQL", "aulaSQL")

    def criaCursor(self):
        return self.cursor()
