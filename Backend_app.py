from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.method == 'POST':
        # Assuming form fields for user inputs
        miles_driven = float(request.form['miles'])
        electricity_consumed = float(request.form['electricity'])
        waste_generated = float(request.form['waste'])

        # Carbon footprint calculation (example formula, adjust as needed)
        carbon_footprint = miles_driven * 0.4 + electricity_consumed * 0.2 + waste_generated * 0.1

        return render_template('result.html', footprint=carbon_footprint)

if __name__ == '__main__':
    app.run(debug=True)

