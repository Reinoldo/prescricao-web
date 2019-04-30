from flask import Flask, request, Response, redirect

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('index.html')



if __name__ == "__main__":
    app.run(debug=True)