from flask import Flask, app,render_template,url_for,Response
from flask.sessions import NullSession
import pose_Detection,cr1
app= Flask(__name__)
app.jinja_env.auto_reload = True
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/feed')
def open_camera():
    return Response(pose_Detection.running(),mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':    
    app.run()

    

