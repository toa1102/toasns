from flask import Flask, render_template, request
from flaskr.forms import LikeAnimeForm

app = Flask(__name__)

#@app.routeの引数にmethods=['GET', 'POST']を追加
#これはユーザからフォームを介して変数を取得するので、
#HTTPメソッドとしてPOSTを許可するという意味。
@app.route('/', methods=['GET', 'POST'])
def home():
    #フォームはform = LikeAnimeForm(request.form)という形で記述
    #そのため、forms.pyからLikeAnimeFormとflaskライブラリからrequestをimportする必要がある。
    #requestというのは、ユーザから送信された変数を取得するメソッドであり、
    #フォームからの場合はrequest.formというプロパティを取得することになる。
    form = LikeAnimeForm(request.form)
    name = like_anime = rate = None
    #ここから下でそれぞれフォームから取得した値を変数として宣言している。
    #ここで作成した変数をrender_templateの引数でそれぞれ再びindex.htmlに返している。
    if request.method == 'POST':
        name = form.name.data
        like_anime = form.like_anime.data
        rate = form.rate.data
        return render_template('index.html', form=form, name=name, like_anime=like_anime, rate=rate)
    return render_template('index.html', form=form, name=name, like_anime=like_anime, rate=rate)
