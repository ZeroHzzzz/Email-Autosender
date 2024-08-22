from flask import Flask, render_template, request
import yaml

def read_config(config_path='config.yaml'):
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config

app = Flask(__name__)

@app.after_request
def set_headers(response):
    response.headers["Referrer-Policy"] = 'no-referrer'
    return response

@app.route('/email', methods=['GET', 'POST'])
def quote():
    data = request.get_json()
    return render_template('templates.html', data_list=data)

if __name__ == '__main__':
    config = read_config()
    port = config.get('backend', {}).get('port', 5000)  # 读取 backend.port 配置项，默认值为 5000
    app.run(host='0.0.0.0', port=port)
