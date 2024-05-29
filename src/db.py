from peewee import PostgresqlDatabase, Model

db = PostgresqlDatabase('hookah_shop', **{'user': 'postgres', 'password': '2510ru80'})


class BaseModel(Model):
    class Meta:
        database = db
