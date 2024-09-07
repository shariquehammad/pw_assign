from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
db = SQLAlchemy(app)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    salary = db.Column(db.Float)
    city = db.Column(db.String(100))



@app.route('/')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        employee_email = request.form['employee_email']
        employee_salary = request.form['employee_salary']
        employee_city = request.form['employee_city']

        if employee_name:
            new_employee = Employee(name=employee_name, email=employee_email, salary=employee_salary, city=employee_city)
            db.session.add(new_employee)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('add_employee.html')


@app.route('/edit_employee/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    employee = Employee.query.get(employee_id)
    if request.method == 'POST':
        employee.name = request.form['employee_name']
        employee.email = request.form['employee_email']
        employee.salary = request.form['employee_salary']
        employee.city = request.form['employee_city']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', employee=employee)

@app.route('/delete_employee/<int:employee_id>')
def delete_employee(employee_id):
    employee = Employee.query.get(employee_id)
    db.session.delete(employee)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context(): 
        db.create_all()
    app.run(debug=True)
    

    

