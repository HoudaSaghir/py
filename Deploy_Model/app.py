from flask import Flask, render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return (render_template('index.html'))

@app.route('/upload', methods=['POST'])
def upload_file():
    f = request.files['file']
    f.save("./static/img/" + f.filename)
    return "file uploaded"

app.run()




