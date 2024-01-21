import psycopg2

username = 'student01'
password = '1'
database = 'lab4'
host = 'localhost'
port = '5432'

query_1 = '''
select c.name,c.type,r.rating_score,r.date,c.sugar,c.calories,c.protein,c.fat
from rating r
join cereal c on r.cereal_id=c.cereal_id
where c.fat=0 and r.rating_score>30 
'''
query_2 = '''select c.name,m.manufacturer_name,c.sugar,c.calories,c.protein,c.fat
from cereal c
join manufacturer m on m.manufacturer_id=c.manufacturer_id
where c.protein>1 and manufacturer_name='Kelloggs';
'''

query_3 = '''select c.name,m.manufacturer_name,r.rating_score,r.date,c.sugar,c.calories,c.protein,c.fat
from rating r
join cereal c on r.cereal_id=c.cereal_id
join manufacturer m on m.manufacturer_id=c.manufacturer_id
where c.sugar<10 and manufacturer_name='General Mills' and r.rating_score >30

'''


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
                       
    print ("Database opened successfully")
    cur = conn.cursor()
    print('1.  \n')

    cur.execute(query_1)

    for row in cur:
        print(row)
    print ("Database opened successfully")
    cur = conn.cursor()
    print('1.  \n')


    cur.execute(query_2)

    for row in cur:
        print(row)
    

    for row in cur:
        print(row)
    print ("Database opened successfully")
    cur = conn.cursor()
    print('1.  \n')

    cur.execute(query_3)

    for row in cur:
        print(row)
