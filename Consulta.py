# import packages
import psycopg2
from datetime import datetime

import sys
import os

import configparser


class Consulta:

  def consulta(self, rfc):

    result_sql = []
    result= {}
    config = configparser.ConfigParser()
    config.read('configFile.ini')

    database = os.getenv('PG_DB')
    user = os.getenv('PG_USER')
    password = os.getenv('PG_PASSWORD')
    host = os.getenv('PG_HOST')
    port = os.getenv('PG_PORT')
    schema = os.getenv('PG_SCHEMA')

    # establish connections
    conn_string = f'postgresql://{user}:{password}@{host}/{database}?options=-csearch_path%3D{schema}'

    conn1 = psycopg2.connect(
      database = database,
      user = user,
      password = password, 
      host = host, 
      port = port,
      options = f'-c search_path={schema}'
    )

    conn1.autocommit = True  
    cursor = conn1.cursor()

    tablas = [
        {
          "table_name": "cancelados",
          "name": "Cancelados"
        },
        {
          "table_name": "cancelados0715",
          "name": "Cancelados Artículo 146A del 01 de enero de 2007 al 04 de mayo de 2015"
        },
        {
          "table_name": "condonados0715",
          "name": "Condonados del 01 de enero de 2007 al 04 de mayo de 2015"
        },
        {
          "table_name": "condonadosart146bcff",
          "name": "Condonados de concurso mercantil (Artículo 146B del Código Fiscal de la Federación)"
        },
        {
          "table_name": "condonadosart21cff",
          "name": "Reducción de recargos (Artículo 21 del Código Fiscal de la Federación)"
        },
        {
          "table_name": "condonadospordecreto",
          "name": "Condonados por decreto (Del 22 de enero y 26 de marzo de 2015)"
        },
        {
          "table_name": "exigibles",
          "name": "Exigibles"
        },
        {
          "table_name": "firmes",
          "name": "Firmes"
        },
        {
          "table_name": "nolocalizados",
          "name": "No localizados"
        },
        {
          "table_name": "reduccionart74cff",
          "name": "Reducción de multas (Artículo 74 del Código Fiscal de la Federación)"
        },
        {
          "table_name": "retornoinversiones",
          "name": "Retorno de inversiones"
        },
        {
          "table_name": "sentencias",
          "name": "Sentencias"
        }
    ]


    # Valida si hay información en la tabla con la fecha a insertar
    count = 0
    for tabla in tablas:
      sql = f'select count(*) from {tabla["table_name"]} where "RFC" = \'{rfc}\';'
      cursor.execute(sql)
      result_exec = cursor.fetchall()
      string_res = str(result_exec)
      if int(string_res[2:3]) > 0:
        count += 1
        result_sql.append(
          tabla["name"]
        )

    conn1.close()

  
    result = {
      "count": count,
      "desc": result_sql
    }
    
    return result

    

    
