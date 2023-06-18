
import json, requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        Ilość = float(request.form['Ilość'])
        currency = request.form['currency']
        
        response = requests.get('http://api.nbp.pl/api/exchangerates/tables/C?format=json')
        data = response.json()
        with open('exchange_rates.json', 'w') as file:
            json.dump(data, file)

        for i in data[0]['rates']:
            if i['code']==currency:
                exhange=Ilość*i['bid']
        result = f" {exhange} zł"       
          
        return render_template('result.html', result=result,exhange=exhange)
    return render_template('form.html')

if __name__ == '__main__':
    app.run()