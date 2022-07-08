from hashlib import new
import json
from flask import Flask , render_template , request , redirect , url_for, jsonify
from flask_cors import cross_origin , CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://czqz@localhost:5432/QNA_db'
db = SQLAlchemy(app)
CORS(app)
#build a SQL database to store all the todo items

class Entries(db.Model):
    __tablename__ = 'QnA'
    id = db.Column(db.Integer , primary_key = True)
    question = db.Column(db.String() , nullable = False)
    answer = db.Column(db.String , nullable = True)

db.create_all()

@app.route('/Entries/delete/<id>' , methods=['DELETE'])
def delete(id):
    print(id)
    try:
        entry = Entries.query.get(id)
        db.session.delete(entry)
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    print(Entries.query.all())
    return jsonify(id)

@app.route('/Entries/answer' , methods=['POST'])
def answering():
    try:
        answer = request.get_json()['answer']
        id = request.get_json()['id']
        entry_to_answer = Entries.query.get(id)
        entry_to_answer.answer = answer
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()
    return jsonify({id , request.get_json()['answer']})

@app.route('/Entries/create' , methods=['POST'])
def create_listing():
    entry_info = request.get_json()
    new_entry = Entries(question = entry_info['question'] , answer = None , id = entry_info['id'])
    db.session.add(new_entry)
    db.session.commit()
    print(Entries.query.all())
    return jsonify({
    'question': new_entry.question
    })
@app.route('/Entries/obtain' , methods=['GET'])
def obtain():
    result = []
    for eachpart in Entries.query.all():
        each_entry = Entries.query.get(eachpart.id)
        result.append({
            "id": each_entry.id,
            "question": each_entry.question,
            "answer": each_entry.answer
        })
    return jsonify(result)

if __name__ == "__main__":
    print(Entries.query.all())
    app.run(debug=True)