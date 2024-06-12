from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({'message': 'Task not found'}), 404

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    if 'title' not in data:
        return jsonify({'message': 'Title is required'}), 400
    task = {'id': len(tasks) + 1, 'title': data['title']}
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True)
