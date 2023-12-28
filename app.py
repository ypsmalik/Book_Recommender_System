from flask import Flask, render_template
import pickle
import pandas as pd

popular_df = pd.read_csv(r"C:\Users\Yashpriya Malik\Desktop\Machine_Learning\Book_Rec_Sys\popular.csv")   

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",
                           book_name = list(popular_df['Book-Title'].values),
                           author = list(popular_df['Book-Author'].values),
                           image = list(popular_df['Image-URL-M'].values),
                           votes = list(popular_df['no. of Ratings'].values),
                           rating = list(popular_df['Avg Ratings'].values)
                           )

if __name__ == '__main__':
    app.run(debug = True)