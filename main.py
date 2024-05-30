from flask import Flask, request 

app = Flask(__name__)

@app.get("/")
def home() -> str:
    user_ip = request.remote_addr
    return { "ip_address" : user_ip }

if __name__ == "__main__":
    app.run(
        debug = True,
        host="0.0.0.0",
        port=443,
        ssl_context = "adhoc"
    )