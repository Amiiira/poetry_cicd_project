import pytest
from .app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/add?a=1&b=2')
    assert response.status_code == 200
    assert response.json == {'result': 3}

def test_subtract(client):
    response = client.get('/subtract?a=5&b=3')
    assert response.status_code == 200
    assert response.json == {'result': 2}

def test_multiply(client):
    response = client.get('/multiply?a=4&b=3')
    assert response.status_code == 200
    assert response.json == {'result': 12}

def test_divide(client):
    response = client.get('/divide?a=10&b=2')
    assert response.status_code == 200
    assert response.json == {'result': 5}

def test_divide_by_zero(client):
    response = client.get('/divide?a=10&b=0')
    assert response.status_code == 400
    assert response.json == {'error': 'Division by zero'}

def test_factorial(client):
    response = client.get('/factorial?n=5')
    assert response.status_code == 200
    assert response.json == {'result': 120}

def test_factorial_negative(client):
    response = client.get('/factorial?n=-1')
    assert response.status_code == 400
    assert response.json == {'error': 'Factorial is not defined for negative numbers'}

def test_sqrt(client):
    response = client.get('/sqrt?x=16')
    assert response.status_code == 200
    assert response.json == {'result': 4}

def test_sqrt_negative(client):
    response = client.get('/sqrt?x=-1')
    assert response.status_code == 400
    assert response.json == {'error': 'Square root is not defined for negative numbers'}

def test_power(client):
    response = client.get('/power?a=2&b=3')
    assert response.status_code == 200
    assert response.json == {'result': 8}

def test_median(client):
    response = client.get('/median?values=1&values=3&values=5')
    assert response.status_code == 200
    assert response.json == {'result': 3}

def test_median_empty(client):
    response = client.get('/median')
    assert response.status_code == 400
    assert response.json == {'error': 'Missing parameters'}

def test_missing_parameters(client):
    response = client.get('/add?a=1')
    assert response.status_code == 400
    assert response.json == {'error': 'Missing parameters'}
