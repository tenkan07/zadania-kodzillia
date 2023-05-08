from flask import render_template, Flask, request, redirect
app = Flask(__name__)


@app.route('/')
def hello():
    my_name = "John"
    print(request.form)
    return f'Hello, {my_name}!'


@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        print("We received GET")
        return render_template("wizytówka_z_Flaskiem02.html")
    elif request.method == 'POST':
        print("We received POST")
        print(request.form)
        return redirect("/")
    
@app.route('/mypage/me', methods=['GET'])
def me():
    print("We received GET")
    return render_template("wizytówka_z_Flaskiem01.html")

