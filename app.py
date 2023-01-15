from flask import Flask, render_template, url_for
from data import members
from jinja2 import Template

app = Flask(__name__, static_url_path='/static')

app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/members', defaults={'member_rank' : 'members'})            
@app.route('/members/<member_rank>')
def ranking(member_rank):
    if member_rank == 'members':
        return render_template('middle.html', member_rank=member_rank, members=members)
    elif member_rank == 'Leader':
        return render_template('individual.html', member=members[member_rank][0])
    else: 
        return render_template('members.html', member_rank=member_rank, members=members)


@app.route('/members/<member_rank>/<int:member_no>')
def member(member_rank, member_no):
     return render_template('individual.html', member=members[member_rank][member_no])

if __name__ == '__main__':
  app.run()