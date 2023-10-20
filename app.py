from flask import Flask,render_template
app=Flask(__name__)


thumbnaillist=[{ "description":"This ia a video focused on frontend developement.This is create for absolute.we also have other videos. now we are replicating Youtuble UI",
            "channel":"Happy students",
            "views":"1M",
            "uploaded":"2days"},
            { "description":"This ia a video focused on frontend developement.This is create for absolute.we also have other videos. now we are replicating Youtuble UI",
            "channel":"Happy students",
            "views":"1M",
            "uploaded":"2days"},
            { "description":"This ia a video focused on frontend developement.This is create for absolute.we also have other videos. now we are replicating Youtuble UI",
            "channel":"Happy students",
            "views":"1M",
            "uploaded":"2days"},
            { "description":"This ia a video focused on frontend developement.This is create for absolute.we also have other videos. now we are replicating Youtuble UI",
            "channel":"Happy students",
            "views":"1M",
            "uploaded":"2days"},
            { "description":"This ia a video focused on frontend developement.This is create for absolute.we also have other videos. now we are replicating Youtuble UI",
            "channel":"Happy students",
            "views":"1M",
            "uploaded":"2days"},
            { "description":"This ia a video focused on frontend developement.This is create for absolute.we also have other videos. now we are replicating Youtuble UI",
            "channel":"Happy students",
            "views":"1M",
            "uploaded":"2days"},
            { "description":"This ia a video focused on frontend developement.This is create for absolute.we also have other videos. now we are replicating Youtuble UI",
            "channel":"Happy students",
            "views":"1M",
            "uploaded":"2days"},
            { "description":"This ia a video focused on frontend developement.This is create for absolute.we also have other videos. now we are replicating Youtuble UI",
            "channel":"Happy students",
            "views":"1M",
            "uploaded":"2days"}]




@app.route('/')
def home():
    return render_template("index.html",thumbnaillist1=thumbnaillist)
if __name__ =="__main__":
    app.run(debug=True)