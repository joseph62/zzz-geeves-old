from flask import Flask, request, jsonify
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

app = Flask(__name__)


PUBLIC_KEY = "111686b2c8f953055b729e68280fb2a4e8384db1a942f573d620466bbb7b4726"

VERIFY_KEY = VerifyKey(bytes.fromhex(PUBLIC_KEY))


def verify_request(signature, timestamp, body):
    try:
        VERIFY_KEY.verify(f"{timestamp}{body}".encode(), bytes.fromhex(signature))
    except BadSignatureError:
        abort(401, "invalid request signature")


@app.route("/", methods=["POST"])
def my_command():
    print(request.json)
    verify_request(
        request.headers["X-Signature-Ed25519"],
        request.headers["X-Signature-Timestamp"],
        request.data,
    )
    if request.json["type"] == 1:
        return jsonify({"type": 1})
