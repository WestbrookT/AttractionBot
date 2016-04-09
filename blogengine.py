

from flask import Flask, render_template, url_for, request, redirect, flash
from flask import session
import os, datetime, json, re






app = Flask(__name__)


pageLocation = os.path.join(os.path.abspath(os.path.join(app.static_folder, '..')), 'pages')
import template
from admin import checkPassword

app.secret_key= os.urandom(24)




def checkCredentials(sessionInfo):
    try:
        timeDiff = (datetime.datetime.now() - sessionInfo['login_date']).days
        if sessionInfo['logged_in'] and timeDiff > 1:
            return False
        else:
            return True


    except:
        return False

def getPython(info):
    return json.loads(info)

def replacelink(text):
    print(text.group(0))
    info = text.group(0).split(";")
    link = '<a href="{}">{}</a>'.format(info[1][:len(info[1])-1], info[0][1:])
    print(link)
    return link

def convertLink(text):

    temp = re.sub(r'\([^/][^;]+;[^)]+\)', replacelink, text)
    while(text != temp):
        text = temp
        temp = re.sub(r'\([^/][^;]+;[^)]+\)', replacelink, temp)

    return text

@app.route('/')
def hello_world():

    return render_template('landing.html', f=globals(), conv=getPython)


@app.route('/pages/<name>')
def getPage(name):
    content = template.getPage(name)
    return render_template('post.html', post=content['content'], f=globals(), conv=getPython)

@app.route('/api/pages/<name>')
def apiGetPage(name):
    content = template.getPage(name)

    return render_template('apipost.html', post=content['content'], f=globals(), conv=getPython)

@app.route('/api/pages/<name>/meta')
def apiGetPageMeta(name):
    content = template.getPage(name)

    return json.dumps(content)

@app.route('/api/pages/<name>/meta/<tag>')
def apiGetTag(name, tag):
    page = template.getMeta(name)
    out = page[tag]
    return out

@app.route('/api/pages')
def apiGetPages():

    try:
        os.listdir(pageLocation)
    except:

        return '{}'

    return  json.dumps(os.listdir(pageLocation))



@app.route('/admin/create', methods=['POST', 'GET'])
def createPage():
    if not checkCredentials(session):
        return redirect(url_for('login'))
    if (request.method == 'POST'):
        r = list(dict(request.form).keys())[0]



        pageDict = json.loads(str(r))

        checkPage = template.createPage(pageDict)
        if checkPage != 'success':
            return checkPage
        return redirect(url_for('admin'))
    else:
        return 'You should not be here!'

@app.route('/admin/delete/<page>')
def deletePage(page):
    if not checkCredentials(session):
        return redirect(url_for('login'))
    return template.deletePage(page)




@app.route('/admin', methods=['POST', 'GET'])
def admin():

    if checkCredentials(session):
        pages = json.loads(apiGetPages())

        return render_template('panel.html', pages=pages)
    else:
        return redirect(url_for('logout'))

@app.route('/admin/help')
def adminHelp():
    return render_template('help.html')

@app.route('/login', methods=['POST', 'GET'])
def login():

    if (request.method == 'POST'):
        if checkPassword(request.form['password']):
            session['logged_in'] = True
            session['login_date'] = datetime.datetime.now()
            return redirect(url_for('admin'))
    return render_template('adminLogin.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/portal')
def portal():
    return render_template('portal.html')

@app.route('/auth', methods=['POST'])
def auth():
    fb_id = request.form['id']
    fb_token = request.form['token']
    os.system('/home/trase/PycharmProjects/AttractionBot/tind.py {} {}'.format(fb_id, fb_token))
    return redirect(url_for('hello_world'))


if __name__ == '__main__':
    app.run(debug=True)
