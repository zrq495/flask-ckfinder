# -*- coding:utf-8 -*-

from flask import (
    request, render_template, views, jsonify)

from logic import CkFinder


class DirListView(views.MethodView):

    def post(self):
        ckfinder = CkFinder()
        return ckfinder.dir_list(request)


class IndexView(views.MethodView):

    def get(self):
        return render_template('index.html')


class GetInfoView(views.MethodView):

    def post(self):
        ckfinder = CkFinder()
        upload_path = request.form.get('currentpath', '')
        new_file = request.files['newfile']
        return ckfinder.upload(upload_path, new_file)

    def get(self):
        ckfinder = CkFinder()
        action = request.args.get('mode', '')
        if "getinfo" == action:
            info = ckfinder.get_info(request.args.get("path", ""))
            return jsonify(info)

        elif "getfolder" == action:
            return jsonify(ckfinder.get_dir_file(request.args.get("path", "")))

        elif "rename" == action:
            old_name = request.args.get("old", "")
            new_name = request.args.get("new", "")
            return ckfinder.rename(old_name, new_name)

        elif "delete" == action:
            path = request.args.get("path", "")
            return ckfinder.delete(path)

        elif "addfolder" == action:
            path = request.args.get("path", "")
            name = request.args.get("name", "")
            return ckfinder.addfolder(path, name)

        else:
            return "fail"
