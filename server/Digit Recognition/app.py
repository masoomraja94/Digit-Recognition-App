from flask import Flask, request
import base64
import pred_fn

# __name__ == __main__
app = Flask(__name__)


@app.route('/', methods=['POST'])
def marks():
    data_keys = list(request.form.keys())
    data_vals = list(request.form.values())
    dict = {}
    for i in range(len(data_keys)):
        dict[data_keys[i]] = data_vals[i]
    imgdata = base64.b64decode(dict['image'])

    filename = 'xyz.jpg'
    with open('static/' + filename, 'wb') as f:
        f.write(imgdata)

    caption = pred_fn.pred_val('static/'+filename)
    result = {
        'caption': str(caption)
        }

    return result



if __name__ == '__main__':
    app.run(debug=False, threaded=False, host='0.0.0.0')
