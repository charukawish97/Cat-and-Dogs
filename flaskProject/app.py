from flask import Flask, render_template, request

from keras.models import load_model

from keras.utils import img_to_array, load_img

app = Flask(__name__)

dic = {0: 'Cat', 1: 'Dog'}
model = load_model('model.h5')

model.make_predict_function()



def predict_label(filename):
    # load the image
    img = load_img(filename, color_mode="grayscale" , interpolation='nearest')
    # convert to array
    img = img_to_array(img)
    # reshape into a single sample with 1 channel
    img = img.reshape(2, 200, 50, 1)
    # prepare pixel data
    img = img.astype('float32')
    img = img / 255.0
    return img


@app.route("/", methods=['GET', 'POST'])
def main():
    return render_template("index.html")


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route("/submit", methods=['GET', 'POST'])
def get_output():
    global img_path, p
    if request.method == 'POST':
        img = request.files['my_image']

        img_path = "static/" + img.filename
        img.save(img_path)

        p = predict_label(img_path)

    return render_template("index.html", prediction=p, img_path=img_path)


@app.route("/about")
def about_page():
    return "Please subscribe  Artificial Intelligence Hub..!!!"


if __name__ == '__main__':
    app.run()
