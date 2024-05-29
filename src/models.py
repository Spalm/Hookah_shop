from peewee import CharField, DateField, ForeignKeyField, BooleanField, FloatField, IntegerField

from db import db, BaseModel


# from flask_login import UserMixin


class ClientCategory(BaseModel):
    title = CharField()


class Client(BaseModel):
    category = ForeignKeyField(ClientCategory)
    name = CharField()
    phone = CharField()
    date_added = DateField()


class EmployeePosition(BaseModel):
    title = CharField()


class Employee(BaseModel):
    employee_position = ForeignKeyField(EmployeePosition)
    name = CharField()
    phone = CharField(unique=True)
    date_added = DateField()


class PaymentType(BaseModel):
    title = CharField()


class Order(BaseModel):
    client = ForeignKeyField(Client)
    payment_type = ForeignKeyField(PaymentType)
    total = FloatField()
    delivered = DateField()
    paid = FloatField()


class Producer(BaseModel):
    name = CharField()
    date_added = DateField()
    phone = CharField(unique=True)


class HookahSize(BaseModel):
    name = CharField()


class HookahConnectorType(BaseModel):
    name = CharField()


class Hookah(BaseModel):
    producer = ForeignKeyField(Producer)
    name = CharField()
    price = FloatField()
    cost = FloatField()
    img = CharField()
    size = IntegerField(HookahSize)
    connector_type = IntegerField(HookahSize)
    diffuser = BooleanField()


class OrderProduct(BaseModel):
    product = ForeignKeyField(Hookah)
    order = ForeignKeyField(Order)


# TODO: что добавлять в foreignKey продукта


class Supplier(BaseModel):
    name = CharField()
    phone = CharField(unique=True)
    date_added = DateField()


class Stock(BaseModel):
    product = ForeignKeyField(Hookah)
    supplier = ForeignKeyField(Supplier)
    date_added = DateField()


# TODO: что добавлять в foreignKey продукта

models = [
    ClientCategory, Client, EmployeePosition, Employee,
    PaymentType, Order, Producer, Hookah,
    OrderProduct, Supplier, Stock, HookahSize,
    HookahConnectorType
]

# db.drop_tables(models)
db.create_tables(models)
