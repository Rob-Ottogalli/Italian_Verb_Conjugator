from flask import Flask, render_template, redirect
import Italian_Verb_Conjugator
import verb_scrape

# create instance of Flask app
app = Flask(__name__)

# create route that renders index.html template
@app.route("/")
def home():
    # Define variable to hold verb input data
    verb = Italian_Verb_Conjugator.conjugate("piovere", "lui", "present", "indicative")

    # Print to console
    print(f"Verb printed: {verb}")

    # Push conjugated verb to web page
    return render_template("index.html", verb=verb)

@app.route("/scrape")
def scrape():

    ## Call dictionary from verb_scrape
    # my_dict = verb_scrape.get_verb_info()
    
    # Set variables (verb, person, mood, tense) equal to dictionary values

    # # Define variable to hold verb input data
    # verb = Italian_Verb_Conjugator.conjugate("piovere", "lui", "present", "indicative")

    # # Print to console
    # print(f"Verb printed: {verb}")

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

