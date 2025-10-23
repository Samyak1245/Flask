from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('main.html')

@app.route('/success/<float:score>')
def success(score):
    res = "PASS" if score >= 50 else "FAIL"
    return render_template('result.html', result=res, score=score)

@app.route('/result/<int:marks>')
def result(marks):
    if marks < 50:
        return redirect(url_for('success', score=marks))
    else:
        return redirect(url_for('success', score=marks))

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        physics = int(request.form['physics'])
        chemistry = int(request.form['chemistry'])
        maths = int(request.form['maths'])
        biology = int(request.form['biology'])

        total_score = (physics + chemistry + maths + biology) / 4

        return redirect(url_for('success', score=total_score))

if __name__ == "__main__":
    app.run(debug=True)
