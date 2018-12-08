# coding:utf-8

from flask import Flask,render_template,request,redirect,url_for
from werkzeug.utils import secure_filename
import os
import time

app = Flask(__name__)
base_dir = os.path.dirname(os.path.abspath(__file__))
uploader_dir = base_dir + '/static/uploads/'

def conv2pdf_file(filename):
    """
    convert the words file to pdf and relay the liberoffice...
    :param filename:
    :return:
    """
    command = 'soffice --headless --invisible --convert-to pdf {}{} --outdir {}'
    os.popen(command.format(uploader_dir, filename, uploader_dir))
    # TODO: process need synchronization!
    time.sleep(10)


def lpr(filename, print_time=1):
    """
    use the unix command: `lpr`; U can search it in man manual for the usage.
    :param filename: str
    :param print_time: str
    :return: none
    """

    # `command`中的空格一个都不能随意更改
    command = 'lpr {}{} -#{}'
    finalFile = filename
    try:
        suffix = filename.split('.')[-1]
        if suffix == 'docx' or suffix == 'doc':
            conv2pdf_file(filename)
            # 转化完成后后缀应该是`*.pdf`

            finalFile = filename.split('.')[0] + '.pdf'

        result = os.popen(command.format(uploader_dir, finalFile, print_time))
    except Exception as e:
        print(e)

    #return  result.read()


@app.route('/', methods=['POST', 'GET'])
def uploads():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径

        times = request.form['myselect']


        print(f.filename)
        filehouzhui = f.filename.split('.')[-1]
        tempfile = str(int(time.time()%100))
        upload_path = os.path.join(basepath, 'static/uploads',((tempfile+'.'+filehouzhui)))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        print(upload_path)
        f.save(upload_path)


        lpr(tempfile+'.'+filehouzhui,times)

        # python使用os.pepon 来执行命令，也就是当前进程fork了个子进程来执行打印任务。
        # 也就是说当前需要有同步的方式，然而。。。
        # 硬核一点儿算了，直接sleep 200秒。希望你们能够优化。
        # 200 秒打印机应该已经打印完了吧。。。
        os.popen("sleep 200;rm %s" % uploader_dir + '*')

        return redirect(url_for('uploads'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='192.168.1.152' ,port=80)
