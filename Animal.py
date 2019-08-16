from projetoConclusao.Conexao import Conexao
class Animal():
    def __init__(self):
        self.nome = ""
        self.tipo = ""
        self.mediaVida = 0


    def restartaTabela(self):
        conexao = Conexao.conecta()
        cursor = Conexao.criaCursor(conexao)

        sql = "DROP TABLE IF EXISTS ANIMAL"
        cursor.execute(sql)

        create = """
            CREATE TABLE ANIMAL(
            NOME CHAR(20) NOT NULL,
            TIPO CHAR(20),
            MEDIA_VIDA INT
            );
            """
        try:
            cursor.execute(create)
            conexao.commit()
        except:
            conexao.rollback()
            print("Erro ao criar tabela!")

        conexao.close()
        cursor.close()

    def insereDados(self, dicDados):
        conexao = Conexao.conecta()
        cursor = Conexao.criaCursor(conexao)

        self.nome = dicDados['nome']
        self.tipo = dicDados['tipo']
        self.mediaVida = dicDados['mediaVida']

        insert = """INSERT INTO ANIMAL (nome, tipo, media_vida)
        VALUE
        ('{}', '{}' , {})""".format(self.nome, self.tipo, self.mediaVida)

        try:
            cursor.execute(insert)
            conexao.commit()
        except:
            conexao.rollback()
            print("Erro ao inserir")

        conexao.close()
        cursor.close()

    def autalizaDados(self, dicDados):
        conexao = Conexao.conecta()
        cursor = Conexao.criaCursor(conexao)

        update = """ UPDATE ANIMAL SET {} = {} WHERE {} """.format(dicDados['campo'],
                                                                       dicDados['valor'],
                                                                       dicDados['condicional'])
        try:
            cursor.execute(update)
            conexao.commit()
        except:
            conexao.rollback()
            print("Erro ao atualizar")

        conexao.close()
        cursor.close()

    def deletaDados(self, dicDados):
        conexao = Conexao.conecta()
        cursor = Conexao.criaCursor(conexao)

        delete = """DELETE FROM ANIMAL WHERE {} = {} """.format(dicDados['campo'], dicDados['valor'])

        try:
            cursor.execute(delete)
            conexao.commit()
        except:
            conexao.rollback()
            print("Erro ao deletar")

        conexao.close()
        cursor.close()

    def selecionaDados(self, dicDados):
        conexao = Conexao.conecta()
        cursor = Conexao.criaCursor(conexao)

        select = """SELECT {} FROM ANIMAL""".format(dicDados['campos'])

        try:
            cursor.execute(select)
            resultado = cursor.fetchall()
            conexao.commit()
            return resultado
        except:
            conexao.rollback()
            print("Erro ao retornar dados!")

        cursor.close()
        conexao.close()