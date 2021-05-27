from flask import render_template
from app import app

@app.route('/')         # decoratore: crea un'associazione tra la URL argomento e la funzione
@app.route('/index')    # decoratore. In questo caso entrambi i decoratori sono associati alla stessa funzione: 
                        # quando nel browser viene richiesta una delle due URL avremo lo stesso risultato
def index():
    user = {'username': 'Andrea'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Andrea'},
            'body': 'Che palle!'
        }        
    ]
    return render_template('index.html', title='Home', user=user, posts=posts) # title='Home',
