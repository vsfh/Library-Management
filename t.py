import cx_Oracle
import pandas as pd
import sqlalchemy

from sqlalchemy import create_engine 
engine = create_engine("oracle+cx_oracle://coder:coder@127.0.0.1:1521/orcl",encoding='utf-8', echo=True)
print("ok")
sql_a = "select * from book"
data = pd.read_sql(sql=sql_a,con=engine)
data.to_csv("sss.csv")

