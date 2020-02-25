# Book-FlaskApp-03-AddStaicFilesAndTemplates

---

## Flask のインストール

仮想環境を用意して、Flask パッケージを(ローカル)インストールします。

```ps
PS C:\Users\y\Documents\GitHub\Book-FlaskApp-03-AddStaicFilesAndTemplates> py -m venv flaskenv
PS C:\Users\y\Documents\GitHub\Book-FlaskApp-03-AddStaicFilesAndTemplates> flaskenv\Scripts\activate
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-03-AddStaicFilesAndTemplates> py -m pip install Flask
```

## 静的なファイルを追加する

JavaScript ファイルや CSS ファイル、画像ファイル等を利用する場合、 `static` フォルダを作成し、その中にファイルを入れておくことで、 `/static/***` の URL で呼び出すことができます。

まず、 [icon.png](static/icon.png) を [static/](static/) フォルダに入れます。

次に、 [app.py](app.py) を作成し、以下のコードを書きます。 [app01.py](app01.py)

```py
from flask import Flask, redirect, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('static', filename='icon.png'))
    return app.send_static_file('icon.png')
```

環境変数 `FLASK_APP` にファイル名を設定し、実行します。

```ps
C:\Users\y\Documents\GitHub\Book-FlaskApp-03-AddStaicFilesAndTemplates> set FLASK_APP=app.py
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-03-AddStaicFilesAndTemplates> python -m flask run
```

ブラウザを開き、 [http://127.0.0.1:5000/](http://127.0.0.1:5000/) にアクセスして、画像が表示されることを確認します。

## テンプレートを利用する

HTML テキストを自分で組み立てて出力した場合、エスケープが漏れるなどのバグが発生する可能性があるため、Jinja2 テンプレートエンジンを利用して HTML テキストを生成します。

まず、 [templates/](templates/) フォルダの中に、 [hello.html](templates/hello.html) を作成し、以下のコードを書いて保存します。

```
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello, World!</h1>
{% endif %}
```

次に、 [app.py](app.py) を以下のコードに置き換えます。 [app02.py](app02.py)

```py
from flask import render_template

app = Flask(__name__)


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
```

環境変数 `FLASK_APP` にファイル名を設定し、実行します。

```ps
C:\Users\y\Documents\GitHub\Book-FlaskApp-03-AddStaicFilesAndTemplates> set FLASK_APP=app.py
(flaskenv) PS C:\Users\y\Documents\GitHub\Book-FlaskApp-03-AddStaicFilesAndTemplates> python -m flask run
```

ブラウザを開き、 [http://127.0.0.1:5000/hello/taro](http://127.0.0.1:5000/hello/taro) にアクセスして、 `Hello taro!` と表示されることを確認します。
