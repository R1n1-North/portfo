
from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__) # __name__ == __main__


@app.route("/")
def home_route():
    return render_template('index.html') # looks for folders that are in a templates folder


@app.route("/<string:page>") # <string:page> means that we can input the name of the page without repeating code below!
def about(page):  #we accept page as the input # created a static folder , which doesn't change.. flask recognizes folders template and static
    return render_template(page)#returns the page we want

def write_to_file(data):
    with open('database2.txt', 'a+') as database: # database 2 method
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}') # you can decide which database is good for you!


def write_to_csv(data): #csv stands for comma seperated values
    with open('database.csv', 'a', newline='') as csv_database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(csv_database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def Submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            with open('database.txt', mode='a+') as base: # Database 1 method
                base.seek(0)
                if len(base.read(100)) > 0:
                    base.write("\n")
                base.write(str(data))
            print(data)
            return redirect('/thankyou.html')
        except:
                return 'did not save to database'
    else:
        return 'something went wrong. Try again!'








# @app.route("/components.html")
# def components(): # created a static folder , which doesn't change.. flask recognizes folders template and static
#     return render_template('components.html')

# @app.route("/contact.html")
# def contact(): # created a static folder , which doesn't change.. flask recognizes folders template and static
#     return render_template('contact.html')

# @app.route("/work.html")
# def work(): # created a static folder , which doesn't change.. flask recognizes folders template and static
#     return render_template('work.html')


# @app.route("/works.html")
# def works(): # created a static folder , which doesn't change.. flask recognizes folders template and static
#     return render_template('works.html')


# @app.route("/blog/doggo")
# def blog(): # created a static folder , which doesn't change.. flask recognizes folders template and static
#     return '<p>This is my dog</p>'


# @app.route("/favicon.ico")  #favicon is the icon on the tab --allows users to differentiate between websites at a glance
# def favicon():                # actually don't need this function can delete, but won't coz has notes
#     return "<p>This is my thoughts on the matter</p>"
