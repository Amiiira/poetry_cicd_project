from .app import app

import pytest
import json

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_tasks_empty(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == {'tasks': []}

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Task 1'})
    assert response.status_code == 201
    assert response.json['title'] == 'Task 1'

def test_get_tasks_with_task(client):
    client.post('/tasks', json={'title': 'Task 1'})
    response = client.get('/tasks')
    assert response.status_code == 200
    assert len(response.json['tasks']) == 1
    assert response.json['tasks'][0]['title'] == 'Task 1'

def test_get_task(client):
    response_create = client.post('/tasks', json={'title': 'Task 1'})
    task_id = response_create.json['id']
    response_get = client.get(f'/tasks/{task_id}')
    assert response_get.status_code == 200
    assert response_get.json['title'] == 'Task 1'

def test_get_nonexistent_task(client):
    response = client.get('/tasks/999')
    assert response.status_code == 404
    assert response.json['message'] == 'Task not found'

def test_create_task_missing_title(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 400
    assert response.json['message'] == 'Title is required'
