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
    resText = formatRes(predict(str(inputText)))
    return render_template('index.html', input_text = inputText, res_text = resText)

def formatRes(textList):
  return '<p>' + '</p><p>'.join(textList) + '</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
