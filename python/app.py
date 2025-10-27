import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def root():
    return jsonify({
        "method": request.method,
        "headers": dict(request.headers),
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "json": request.get_json(silent=True),
        "remote_addr": request.remote_addr,
        "url": request.url,
        "path": request.path
    })

if __name__ == "__main__":
    app.run(debug=True, port=5000)
