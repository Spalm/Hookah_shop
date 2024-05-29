from flask import Flask
from flask.cli import AppGroup

from db import db
from models import (
    ClientCategory, Client,
    EmployeePosition, Employee,
    PaymentType, Order, Producer, Hookah,
    OrderProduct, Supplier, Stock, HookahSize,
    models
)

start_data = AppGroup('start_data')


@start_data.command('create_db')
def create_db():
    db.create_tables(models)


@start_data.command('reset_db')
def drop_db():
    db.drop_tables(models)
    db.create_tables(models)


@start_data.command('populate_db')
def populate_db():
    Producer.create(title="Alpha Hookah")
    Producer.create(title="Nano Smoke")
    Producer.create(title="Mamay")

    Hookah.create(producer=1, name='ORO', price=25000.00,
                  cost=20000.00, img=None, size='большой', connector_type='магнит',
                  diffuser=True)
    Hookah.create(producer=2, name='Box', price=3800.00,
                  cost=2500.00, img=None, size='маленький', connector_type='обычный',
                  diffuser=False)
    Hookah.create(producer=3, name='Flow', price=7500.00,
                  cost=5000.00, img=None, size='средний', connector_type='притирка',
                  diffuser=True)


def register_cli_commands(app: Flask) -> None:
    app.cli.add_command(start_data)
