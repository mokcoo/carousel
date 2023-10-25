from peewee import PostgresqlDatabase

# setting up the connection to the local database
db = PostgresqlDatabase("carousel",user='kong',password='kong',host='192.168.74.137')