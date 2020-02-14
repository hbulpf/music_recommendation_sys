import os
from flask import Flask, request, render_template, Markup
from model import predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def demo():
  if request.method == 'GET':
    return render_template('index.html', input_text = '', res_text = '')
  else:
    inputText = request.form.get("input_text")
    result_list = predict(str(inputText))
    return render_template('index.html', input_text = inputText,
                           song0 = result_list[0],
                           song1 = result_list[1],
                           song2 = result_list[2],
                           song3 = result_list[3],
                           song4 = result_list[4],
                           song5 = result_list[5],
                           song6 = result_list[6],
                           song7 = result_list[7],
                           song8 = result_list[8],
                           song9 = result_list[9],
                           song10 = result_list[10]
                           )

# def formatRes(textList):
#   return '<p>' + '</p><p>'.join(textList) + '</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
