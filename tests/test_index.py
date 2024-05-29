from flask import render_template

from app import app, index


def test_1():
    assert True


def test_index():
    assert index() == render_template('index.html')