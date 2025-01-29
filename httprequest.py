from flask import Flask, request
import pyautogui

app = Flask(__name__)

# Mapeamento de teclas
KEY_MAPPING = {
    "right": "right",
    "left": "left",
}

@app.route('/press', methods=['GET'])
def press_key():
    key = request.args.get("key", "").lower()  # Obtém a tecla da URL

    if key in KEY_MAPPING:
        pyautogui.press(KEY_MAPPING[key])
        return {"status": "success", "message": f"Key '{key}' pressed"}, 200
    else:
        return {"status": "error", "message": "Invalid key"}, 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
