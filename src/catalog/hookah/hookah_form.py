from functools import cache

from wtforms import Form, DateField, BooleanField, StringField, IntegerField, SelectField, EmailField, PasswordField
from wtforms.validators import InputRequired

from forms import MultiCheckboxField
from models import (
    ClientCategory, Client,
    EmployeePosition, Employee,
    PaymentType, Order, Producer, Hookah,
    OrderProduct, Supplier, Stock, HookahSize,
    models, HookahConnectorType
)


class HookahFilter(Form):
    brand = SelectField('БРЕНД')
    size = MultiCheckboxField('РАЗМЕР')
    connector_type = SelectField('ТИП КОННЕКТОРА')
    diffuser = SelectField('ДИФФУЗОР')

    def __init__(self, formdata=None, obj=None, prefix="", data=None, meta=None, **kwargs):
        super().__init__(formdata, obj, prefix, data, meta, **kwargs)
        producers = Producer.select(Producer.id, Producer.name)
        brands = [(0, 'все')]
        brands.extend((producer.id, producer.name) for producer in producers)
        self.brand.choices = brands

        hookah_size = HookahSize.select(HookahSize.name).order_by(HookahSize.id)
        sizes = [(0, 'все')]
        sizes.extend(enumerate(size.name for size in hookah_size))
        self.size.choices = sizes

        hookah_connectors = HookahConnectorType.select(HookahConnectorType.name)
        connector_types = [(0, 'все')]
        connector_types.extend(enumerate(hookah.name for hookah in hookah_connectors))
        self.connector_type.choices = connector_types

        diffusers = [(0, 'все'), (1, 'есть'), (2, 'нет')]
        self.diffuser.choices = diffusers
