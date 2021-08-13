from flask import Flask

app=Flask('First App')

@app.route('/')
def welcome():
    return 'Hi, this is Abhijeet. Hmm..Hmmm'

if __name__=='__main__':
    app.run(debug=True)
