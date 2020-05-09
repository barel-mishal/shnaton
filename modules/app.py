from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
# def auth('/auth'):
#     flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
#     creds = flow.run_local_server(port=0)

if __name__ == "__main__":
    app.run(debug=True)