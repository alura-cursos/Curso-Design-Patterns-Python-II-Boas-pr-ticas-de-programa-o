# -*- coding: utf-8 -*-
import MySQLdb

class Connection_factory(object):

    def get_connection(self):
        # tratamento de erro omitido
        return MySQLdb.connect(host="localhost", 
            user='root', 
            passwd='',
            db='alura')