from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret' # you need to set a secret key for security purposes
# routing rules and rest of server.py below

import random # import the random module
# The random module has many useful functions. This is one that gives a random number in a range



# our index route will handle rendering our form
@app.route('/')
def index():
    # session['count'] += 1
    # print session['count']
    number = ''
    message = ''
    if 'randomnumb' in session and 'guess1' in session:
        print "yup"
        if session['guess1'] == session['randomnumb']:
            print "you got it"
            message = "exact"
            number = session['randomnumb']
            session.pop('randomnumb')
            session.pop('guess1')
        elif session['guess1'] > session['randomnumb']:
            print "too high"
            message = "high"
        elif session['guess1'] < session['randomnumb'] and session['guess1'] != None:
            print "too lowwwww"
            message = "low"
    else:
        session['randomnumb'] = random.randrange(0, 101) # random number between 0-100
    
        
        
    print session
    
    return render_template("index.html", message = message, number = number)


@app.route('/guess', methods=['POST'])
def guess():
        
        session['guess1'] = int(request.form['new_guess'])

        return redirect('/')



app.run(debug=True)