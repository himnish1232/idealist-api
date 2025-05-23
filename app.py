from flask import Flask, request, jsonify
from idealist import Idealist

app = Flask(__name__)
idealist = Idealist()

@app.route('/generate', methods=['GET'])
def generate():
    prompt = request.args.get('prompt', '')
    idea = idealist.generate(prompt) if prompt else idealist.generate()
    return jsonify({'idea': idea})

if __name__ == '__main__':
    app.run(debug=True)
