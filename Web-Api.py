#Erstellung einer Web-Api
from flask import Flask,render_template

# initialisiere Flask-Server
app = Flask(__name__)


# to open/create a new html file in the write mode 

# definiere Route für Hauptseite
@app.route('/')
def index():
    # gebe Antwort an aufrufenden Client zurück
    return render_template('index.html')

@app.route('/outgoing', methods = ['GET'])
def outgoing():
    # gebe Antwort an aufrufenden Client zurück
     return render_template('outgoing.html')

@app.route('/incoming',methods = ['POST'])
def incoming():
    # gebe Antwort an aufrufenden Client zurück
    return render_template('incoming.html')

if __name__ == '__main__':
# starte Flask-Server
    app.run(host='0.0.0.0', port=5000)


        