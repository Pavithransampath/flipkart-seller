from flask import Flask,request,render_template
import requests
import json 


app=Flask(__name__)

@app.route("/",methods=["POST","GET"])
def home1():
    if request.method=="POST":
        image=request.form.get("image")
        product_name=request.form.get("product_name")
        description=request.form.get("description")
        price=request.form.get("price")
        quantity=request.form.get("quantity")
        dict1={}
        dict1.update({"image":image})
        dict1.update({"product_name":product_name})
        dict1.update({"description":description})
        dict1.update({"price":price})
        dict1.update({"quantity":quantity})
        url="http://127.0.0.1:5000/mobiles"
        response=requests.post(url,json=dict1)
        return{"data":"response"}
    return render_template("index.html")





if __name__ =="__main__":
    app.run(debug=True,port=5001)