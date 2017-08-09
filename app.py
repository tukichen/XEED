import os
from flask import Flask, render_template, send_from_directory,request, redirect , url_for, Response
from flask_assets import Environment, Bundle
import flask
import bokeh
from bokeh.embed import components
from bokeh.layouts import gridplot
from bokeh.plotting import figure, show, output_file,save


#----------------------------------------------------------------------------
# initialization
app = Flask(__name__)
assets = Environment(app)
app.config.update(
    DEBUG = True,
)
js = Bundle('jquery.js', 'base.js', 'widgets.js',
            filters='jsmin', output='gen/packed.js')
assets.register('js_all', js)

# a dict to collect input data
app.vars = {}
app.vars['login'] =0
#----------------------------------------------------------------------------

#----------------------------------------------------------------------------

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
##########################################################################
@app.route('/')
def home():
    return redirect('/login')

@app.route('/resume')
def resume():
    return render_template('resume.html')  # render a template


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != '1' or request.form['password'] != '1':
            error = 'Invalid Credentials. Please try again.'
            return render_template('login.html', error=error)
        
        elif request.form['username'] == '1' and request.form['password'] == '1':
            app.vars['login'] = 1
            return render_template('index.html')
    elif request.method == 'GET':
        if app.vars['login'] ==1:
            return render_template('index.html')
        else:
            return render_template('login.html', error=error)

@app.route('/index')
def index():
    return redirect('/login')

@app.route('/plot')
def plots():
    script = ''
    div    = ''
    display= 'Plot Data'
    
    if request.method == 'GET':
        return render_template('plot.html', script=script, div=div, display = display, show_result= True)
    if request.method == 'POST':
        if request.form['username'] != '1' : pass

@app.route('/in_progress')
def in_progress():
    display  = 'Work in progress - Please check back later'
    script= '' ; div= ''
    return render_template("base.html",script=script, div=div,
                           display = display,show_result= True)


@app.route('/detect_walk')
def detect_walk():
    return render_template("Walking+Detection.html")

@app.route('/extract_feature')
def extract_feature():
    return render_template("Feature+Extraction+and+Visualization.html")

@app.route('/differentiate_PD_Cotrol')
def differentiate_PD_Cotrol():
    return render_template("Differentiate+Walking+Features+between+PD+Patients+and+Controls.html")

@app.route('/plot_feature')
def plot_feature():
    return render_template("plot_feature.html")

@app.route('/plot_signal')
def plot_signal():
    return render_template("plot_asymmetry.html")

@app.route('/plot_corr')
def plot_corr():
    return render_template("plot_corr.html")

#----------------------------------------------------------------------------

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
