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
    resText = Markup(formatRes(result_list))
    return render_template('index.html', input_text = inputText, result_text = resText)


def formatRes(textList):
  if not textList:
    print('没有这首歌的内部id')
    return '<p>没有这首歌的内部id，再看看其他歌吧~</p>'
  else:
    return '<p/>'.join(textList)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
