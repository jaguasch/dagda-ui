from flask import Flask,render_template

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/docker')
def showDocker():
    return render_template('docker.html')

@application.route('/vulndb')
def showvulnDB():
    return render_template('vulndb.html')

@application.route('/monitor')
def showMonitor():
    return render_template('monitor.html')

@application.route('/settings')
def showSettings():
    return render_template('settings.html')

@application.route('/reports')
def showReports():
    return render_template('reports.html')

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5001, debug=True)
