import csv

from flask import Flask, app, render_template, request,url_for,redirect

# Source - https://stackoverflow.com/a/23327352
# Posted by Martijn Pieters, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-14, License - CC BY-SA 4.0

app = Flask(__name__, template_folder='templates')  # still relative to module



@app.route("/")
def mysite():
    return render_template('index.html')




#Dynamic page loading 

@app.route('/<string:page_name>')
def serve_static(page_name):
    print(page_name)
    return render_template(page_name)

  
@app.route('/submit_form', methods=['GET', 'POST'])
def submit_form():  
    if request.method == 'POST':
        try:
            # Process the form data here
            data = request.form.to_dict()
            print(data)
            write_to_file(data)
            write_to_csv(data)
            return redirect('./thankyou.html')
        except Exception as e:
            print(e)
            return "Did not save to database!"
    else:
        return "something went wrong, Try again!"

def write_to_file(data):
    with open("database.txt", "a") as database:
        for key, value in data.items():
            database.write(f"{key}: {value}\n")

#method writes to a CSV file
def write_to_csv(data):
    with open("database.csv", "a") as database2:
        writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for key, value in data.items():
            writer.writerow([key, value])

""" @app.route('/about.html')
def about_html():
    return render_template('about.html')


@app.route("/contact.html")
def contact_html():
    return render_template("contact.html")

@app.route("/works.html")
def works_html():
    return render_template("works.html")
 """

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
