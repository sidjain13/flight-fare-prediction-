from flask import Flask,request,render_template,request
import pickle

app=Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict",methods=["POST","GET"])
def predict():
    if request.method=="POST":
        return request.method["dep_time"]
    

# model=pickle.load(open("flight.pkl","rb"))




if __name__ == "__main__":
    app.run(debug=True)
