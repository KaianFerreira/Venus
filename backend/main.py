from app import create_app

app = create_app()
app.config['SECRET_KEY'] = 'ndsadanjdnscn'
app.run(host = '0.0.0.0', port ='8080',debug=True)