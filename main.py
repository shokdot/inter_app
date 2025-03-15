from flask import Flask, render_template, request

app = Flask(__name__, template_folder='src/templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    name = request.args.get('name', '')
    return (render_template('search.html', name=name))


if __name__ == '__main__':
    app.run(port=7000)