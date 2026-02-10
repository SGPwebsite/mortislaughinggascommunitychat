from flask import Flask, render_template, request, redirect
import datetime

app = Flask(__Mortis Community Web__)
messages = []

@app.route('/')
def home():
    return render_template('index.html', messages=messages)

@app.route('/send', methods=['POST'])
def send():
    username = request.form.get('username')
    message = request.form.get('message')
    timestamp = datetime.datetime.now().strftime('%H:%M')
    messages.append({'username': username, 'message': message, 'time': timestamp})
    return redirect('/')

if __Mortis Community Web__ == '__main__':
    app.run(debug=True)
```
