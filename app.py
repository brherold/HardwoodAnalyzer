from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.append('scripts')
from pygameAnaylzer import gameAnaylzer
from pygameSearcher import gameSearcher


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        code = request.form['code']
        if len(code) > 4:
            url = code
            #return redirect(url_for('game_analyzer', url=url))

            sample_data = gameAnaylzer(url)
            return render_template('gameAnalyzer.html',data = sample_data)
            

        else:
            return redirect(url_for('seasonAnalyzerYear', code=code))
    return render_template('home.html')
'''
@app.route('/gameAnalyzer')
def game_analyzer(url):
    # Handle game analysis based on the code parameter
    sample_data = gameAnaylzer(url)
    return render_template('gameAnalyzer.html',data = sample_data)
'''



@app.route('/seasonAnalyzerYear/<code>', methods=['GET', 'POST'])
def seasonAnalyzerYear(code):
    if request.method == 'POST':
        year = request.form['year']
        return redirect(url_for('seasonAnalyzer', code=code, year=year))
    return render_template('seasonAnalyzerYear.html', code=code)

@app.route("/seasonAnalyzer/<code>/<year>/<game_type>")
@app.route("/seasonAnalyzer/<code>/<year>", defaults={'game_type': 'Total'})
def seasonAnalyzer(code, year, game_type):
    sample_data = gameSearcher(code, year, game_type)
    
    if sample_data == "No Games Played":
        errorMsg = "No Games Played"
        return render_template('error.html', error_message=errorMsg)
    
    return render_template('seasonAnalyzer.html', data=sample_data,year=year,game_type=game_type)

if __name__ == '__main__':
    app.run()
