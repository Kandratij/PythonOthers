import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Date
USR ='lider'
PWD = 'master'
DB  = 'orcl'
engine = create_engine(f"oracle+cx_oracle://{USR}:{PWD}@{DB}?encoding=UTF-8&nencoding=UTF-8")
pool = cx_Oracle.SessionPool(
    user="lider", password="master", dsn="orcl",
    min=2, max=5, increment=1, threaded=True,
    encoding="UTF-8", nencoding="UTF-8"
)
conn = engine.connect()

metadata_obj = MetaData()
users = Table('users', metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('fullname', String(50)),
    Column('birthdate', Date)
)

metadata_obj.create_all(engine)

ins = users.insert().values(id = 1, name='fill', fullname='Jones')
result = conn.execute(ins)