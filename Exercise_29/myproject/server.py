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
        # Process the form data here
        data = request.form.to_dict()
        print(data)
        write_to_file(data)
        return redirect('./thankyou.html')
    else:
        return "something went wrong, Try again!"

def write_to_file(data):
    with open("database.txt", "a") as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")

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
