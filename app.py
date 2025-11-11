from flask import Flask, send_file, request, render_template
import qrcode
import io

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/generate_qr")
def generate_qr():
    data = request.args.get("data", "")
    if not data:
        return "No data provided", 400

    qr = qrcode.QRCode()
    qr.add_data(data)
    img = qr.make_image()

    reg = io.BytesIO()
    img.save(reg, format="PNG")
    reg.seek(0)

    return send_file(reg, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
