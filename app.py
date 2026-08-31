from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "DevSecOps CI/CD Pipeline"


@app.route("/health")
def health():
    return {"status": "healthy"}


@app.route("/api/message")
def message():
    return {
        "message": "Hello from the DevSecOps application",
        "version": "1.0"
    }


if __name__ == "__main__":
    app.run(debug=True)
