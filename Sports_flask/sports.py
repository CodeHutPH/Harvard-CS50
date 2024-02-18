from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sports', methods=['GET', 'POST'])
def sports():
    if request.method == 'POST':
        selected_sport = request.form['sport']
        return render_template('sports_result.html', selected_sport=selected_sport)
    else:
        return render_template('sports.html')

if __name__ == '__main__':
    app.run(debug=True)
