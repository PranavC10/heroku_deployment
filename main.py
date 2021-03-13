from flask import Flask, request, render_template
import pickle as pk
import numpy as np

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        presentprice = request.form.get("presentprice")
        # getting input with name = lname in HTML form
        KmsDriven = float(request.form.get("KmsDriven"))
        Past_Owners = float(request.form.get("Past_Owners"))
        age = float(request.form.get("Age"))
        Transmission = request.form.get("Transmission")
        SellerType = request.form.get("SellerType")
        fueltype = request.form.get("fueltype")
        filename = 'finalized_model.pk'
        loaded_model = pk.load(open(filename, 'rb'))
        if Transmission=="Manual":
            man=1;
            aut0=0;
        else:
            man=0;
            aut0=1;

        if SellerType == "Individual":
            indi=1
        else:
            indi=0

        if fueltype == "Petrol":
            petrol = 1
            diesel=0
        elif fueltype == "Disel":
            petrol=0
            diesel=1
        else :
            petrol=0
            diesel=0

        predictionresult = loaded_model.predict([[presentprice,KmsDriven,Past_Owners,age,diesel,petrol,indi,man]])

        return "selling price is " + str(np.round(predictionresult[0],decimals=2)) + "Lakhs"
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)