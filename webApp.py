from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from flask_behind_proxy import FlaskBehindProxy

app = Flask(__name__)
proxied = FlaskBehindProxy(app)  # Handle proxy headers

# Secret key for form security
app.config['SECRET_KEY'] = 'your_secret_key_here'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page', text='This is the second page')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")