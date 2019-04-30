from Flask import Flask, Request, response, direct

app = Flask(__name__)

@app.route('/')
def main():
    return redirect('index.html')



if __name__ == "__main__":
    app.run(debug=True)