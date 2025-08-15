
#criar player de video
    #baixar o video 

#criar opiciao conversa nos comentarios
    #criar sistema de inputs com os nomes de quem enviou
    #indentificar quem escreveu a menssagen

#criar layout de conversa (enviar e receber mensagens)
#criar o 'catalogo' de 'contatos' com quem ja conversou
#salvar videos ,comentarios e conversas no mysql
#criar a admin que vai poder enviar videos

from flask import Flask,render_template,flash,session,url_for,request,redirect

app= Flask(__name__)
app.secret_key='skibid1sigma2mewing3'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html',title='login',method='get')
    if request.method=='POST':
        Nome=request.form['text']
        Email=request.form['email']
        Senha=request.form['password']
        session['user']=Nome
        print(Nome)
        print(Email)
        print(Senha)
        print(session['user'])
        return redirect(url_for('video'))
    
comentarios=[]
@app.route('/video',methods=['GET','POST'])
def video():
    if "user" in session and not session["user"] == None:
        video=url_for('static', filename='static/video alcool.mp4')
        if request.method=='GET':
            return render_template('video.html',video=video,title='video')
        if request.method=='POST':
            comentario=request.form['comentarios']
            comentarios.append(comentario)
            return render_template('video.html',video=video,comentarios=comentarios,title='video')
    else:
        return redirect(url_for('login'))

@app.route('/conversas',methods=['GET','POST'])
def conversas():
    return render_template('conversa.html',title='conversas')

@app.route('/menssagens',methods=['GET','POST'])
def menssagens():
    outro=''
    return render_template('messagens.html',title='menssagens')

app.run(port=5000,debug=True)
