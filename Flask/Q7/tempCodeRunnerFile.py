@app.route('/add_employee', methods=['GET','POST'])
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