from flask import Flask, render_template, url_for
import os

app = Flask(__name__, static_folder='static')
COUNTER_FILE = 'counter.txt'

def get_counter():
    # Initialize counter file if it doesn't exist
    if not os.path.exists(COUNTER_FILE):
        with open(COUNTER_FILE, 'w') as f:
            f.write('0')
        return 0
    # Read the current counter value
    with open(COUNTER_FILE, 'r') as f:
        try:
            return int(f.read())
        except ValueError:
            return 0

def update_counter():
    # Increment the hit counter
    count = get_counter() + 1
    with open(COUNTER_FILE, 'w') as f:
        f.write(str(count))
    return count

@app.route('/')
def index():
    hits = update_counter()  # Update and get current hit count
    return render_template("index.html", hits=hits)

if __name__ == '__main__':
    app.run(debug=True)
