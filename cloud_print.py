# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

def lpr(filename,print_time=1):
    command = 'lpr '+os.path.dirname(__file__)+'/static/uploads/'+filename+' -#'+str(print_time)
    try :
        print("hahah")
        result = os.popen(command)
        print("ghcxcdc")
    except Exception as e:
        print(e)

    #return  result.read()


@app.route('/', methods=['POST', 'GET'])
def uploads():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径

        time = request.form['myselect']
        print(time)

        print(f.filename)
        upload_path = os.path.join(basepath, 'static/uploads',(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        print(upload_path)
        f.save(upload_path)


        result = lpr(f.filename,time)
        #return result
        return redirect(url_for('uploads'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)