# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)

with app.app_context():
    import views
    app.add_url_rule(
        '/', view_func=views.IndexView.as_view('index'), endpoint='index')
    app.add_url_rule(
        '/filemanager/', view_func=views.GetInfoView.as_view('get_info'),
        endpoint='get_info')
    app.add_url_rule(
        '/filemanager/dirlist/', view_func=views.DirListView.as_view('dir_list'),
        endpoint='dir_list')

if __name__ == '__main__':
    app.run(debug=True)
