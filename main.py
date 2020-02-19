import os
from flask import Flask, request, render_template, Markup
from model import predict

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def recommendation1():
  if request.method == 'GET':
    return render_template('index.html', input_text ='', res_text ='')
  else:
    inputText = request.form.get("input_text")
    result_list = predict(str(inputText))
    result_text = Markup(formatRes(result_list))
    return render_template('index.html', input_text = inputText, res_text = result_text)

@app.route('/rec2.html', methods=['GET', 'POST'])
def recommendation2():
  if request.method == 'GET':
    return render_template('rec2.html', input_text = '', res_text = '')
  else:
    inputText = request.form.get("input_text")
    result_text = predict(str(inputText))
    return render_template('rec2.html', input_text = inputText, res_text = result_text)

@app.route('/rec3.html', methods=['GET', 'POST'])
def recommendation3():
  if request.method == 'GET':
    return render_template('rec3.html', input_text = '', res_text = '')
  else:
    inputText = request.form.get("input_text")
    result_list = predict(str(inputText))
    result_text = Markup(formatRes(result_list))
    return render_template('rec3.html', input_text = inputText, res_text = result_text)

@app.route('/rec4.html', methods=['GET', 'POST'])
def recommendation4():
  if request.method == 'GET':
    return render_template('rec4.html', input_text = '', res_text = '')
  else:
    inputText = request.form.get("input_text")
    result_list = predict(str(inputText))
    result_text = Markup(formatRes(result_list))
    return render_template('rec4.html', input_text = inputText, res_text = result_text)


def formatRes(textList):
  if not textList:
    print('没有这首歌的内部id')
    return '<p>没有这首歌的内部id，再看看其他歌吧~</p>'
  else:
    return '<p/>'.join(textList)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
