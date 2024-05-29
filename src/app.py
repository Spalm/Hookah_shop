from functools import reduce
import operator

from flask import Flask, render_template, redirect, url_for, request

from cli import register_cli_commands
from catalog.hookah.hookah_form import HookahFilter
from models import (
    ClientCategory, Client,
    EmployeePosition, Employee,
    PaymentType, Order, Producer, Hookah,
    OrderProduct, Supplier, Stock, HookahSize,
    models
)

app = Flask(__name__)
register_cli_commands(app)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/base_page')
def base_page():
    return render_template('base_page.html')


@app.get('/base_page_2')
def base_page_2():
    return render_template('base_page_2.html')


@app.get('/hookahs')
@app.get('/hookahs/<int:n>')
def hookahs(n: int = 0):
    print(request.args)
    brand = request.args.get('brand')
    sizes = request.args.get('sizes')    # 1,3,4
    expressions = []
    if brand is not None:
        expressions.append(Hookah.producer == int(brand))
    if sizes is not None:
        size_ids = [int(x) for x in sizes.split(',')]
        expressions.append(Hookah.size.in_(size_ids))

    if expressions:
        query_filter = reduce(operator.and_, expressions)
        hookahs = Hookah.select().where(query_filter)
    else:
        hookahs = Hookah.select()
    hookahs = hookahs.order_by(Hookah.id).limit(6).offset(n * 6)

    form = HookahFilter()
    context = {
        'form': form,
        'hookahs': hookahs,
        'n': n,
        'args': request.args
    }

    return render_template('hookah_catalog.html', **context)


@app.get('/product')
def product():
    return render_template('product_page.html')


@app.post('/filter_hookahs')
def filter_hookahs():
    form = HookahFilter(request.form)

    print(
        form['brand'].data, form['size'].data,
        form['connector_type'].data, form['diffuser'].data
    )
    brand = form['brand'].data
    sizes = ','.join(form['size'].data)
    connector_type = form['connector_type'].data
    diffuser = form['diffuser'].data
    args = {
        'brand': brand,
        'connector_type': connector_type,
        'diffuser': diffuser,
    }
    if sizes != '':
        args['sizes'] = sizes

    return redirect(url_for('hookahs', **args))


if __name__ == '__main__':
    app.run()
