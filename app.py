from flask import Flask , request ,jsonify ,send_from_directory
from F import filmyzilla
from B import Bolly
from K import Kat
from M import MovieNation
from flask_cors import CORS
import json

app = Flask(__name__, static_folder='static')
CORS(app, origins="*") 

with open('baselinks.json', 'r') as file:
    base_urls = json.load(file)


# base_urls = {
#     'b':'https://bollyflix.army/',
#     'f':'https://www.filmyzilla15.com/',
#     'k':'https://katmoviehd.blue/',
#     'm':'https://moviesnation.onl/',
# }
@app.route('/')
def home():
    return "WELCOME to my api"

@app.route('/links/')
def show_links():
    return jsonify(base_urls)

@app.route('/search/')
def search():
    name = request.args.get('s')
    year = request.args.get('y')
    type_ = request.args.get('t')
    gen = request.args.get('g')

    f = filmyzilla(base_urls['f'])
    f_data = f.search(name,year,type_,gen)

    b = Bolly(base_urls['b'])
    b_data = b.search(name)

    k = Kat(base_urls['k'])
    k_data = k.search(name)

    m = MovieNation(base_urls['m'])
    m_data = m.search(name)
    final = {
        'filmyzilla':f_data,
        'boll':b_data,
        'kat':k_data,
        'movienation':m_data,
    }
    return jsonify(final)


@app.route('/config', methods=['POST'])
def config():
    data = request.get_json()
    print(data)
    for key,value in data.items():
        if key in base_urls:
            base_urls[key] = value
    
    with open('baselinks.json', 'w') as file:
        json.dump(base_urls,file)

    return jsonify({
        "status": "success",
        "received": base_urls,
    })



if __name__ == '__main__':
    app.run(debug=True)
