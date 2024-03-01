from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

tasks = []

# Create operation
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.form
    task = {
        'id': len(tasks) + 1,
        'title': data['title'],
        'description': data['description']
    }
    tasks.append(task)
    return jsonify({'message': 'Task created successfully', 'task': task}), 201

# Read operation (Get all tasks)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

# Delete operation
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({'message': 'Task deleted successfully'}), 200

# Render HTML page to display all tasks
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', tasks=tasks)

if __name__ == '__main__':
    app.run(debug=True)
