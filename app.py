from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

feedback_list = []


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('Phone Number')
        message = request.form.get('message')
        subject = request.form.get('Subject')
        phone = request.form.get('phone')
        telno = request.form.get('telNo')
        mail = request.form.get('mail')

        if not name or not email or not message:
            flash('All fields are required!', 'error')
        else:
            feedback_list.append({
                'name': name,
                'email': email,
                'number': number,
                'message': message,
                'subject': subject,
                'phone': phone,
                'telNo': telno,
                'mail': mail
            })
            flash('Thank you for your feedback!', 'success')
            return redirect(url_for('contact'))

    return render_template('contact.html', feedback=feedback_list)

if __name__ == '__main__':
    app.run(debug=True)