import csv
import requests
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, Float, MetaData


CSV_URL = 'https://uploads.kodilla.com/bootcamp/ds/06/clean_stations.csv'


with requests.Session() as s:
    download = s.get(CSV_URL)

    decoded_content = download.content.decode('utf-8')

    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    """
    for row in my_list:
        print(row)
    """
engine = create_engine('sqlite:///database2.db')

meta = MetaData()

clean_stations = Table(
    'clean_stations', meta,
    Column('station', String, primary_key=True),
   Column('latitude', Float),
   Column('longitude', Float),
   Column('elevation',Float),
   Column('name',String),
   Column('country',String),
   Column('state',String),
)

meta.create_all(engine)
print(engine.table_names())

ins = clean_stations.insert()
for row in my_list[-9:]:
    ins=clean_stations.insert().values(station=row[0], latitude=row[1],longitude=row[2], elevation=row[3], name=row[4],country=row[5],state=row[6] )
    conn = engine.connect()
    result = conn.execute(ins)

result1=conn.execute("SELECT * FROM clean_stations LIMIT 5")
print(result1.fetchall())







