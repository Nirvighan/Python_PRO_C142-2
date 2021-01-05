# IMPORT MODULES
from flask import Flask,jsonify,request
import csv
from demographic_filtering import df_main
from content_filtering import get_recommendations
import itertools

# READ THE DATA
all_articles = []
with open(r"D:\PythonProjects\PRO_C142\article.csv",'r',encoding="utf8") as f:
    csvreader = csv.reader(f)
    data = list(csvreader)
    all_articles = data[1:]
    
liked_articles = []
disliked_articles = []

# CREATE THE FLASK APP
app = Flask(__name__)


# GET THE FIRST ARTICLE
@app.route("/get-first-article")
def get_first_article():
    article_data = {
        "timestamp": all_articles[0][1],
        "eventType": all_articles[0][2],
        "contentId":all_articles[0][3] ,
        "authorPersonId":all_articles[0][4] ,
        "authorSessionId":all_articles[0][5] ,
        "authorUserAgent":all_articles[0][6] ,
        "authorRegion":all_articles[0][7] ,
        "authorCountry":all_articles[0][8] ,
        "contentType":all_articles[0][9] ,
        "url":all_articles[0][10] ,
        
        "title":all_articles[0][11] ,
        "lang":all_articles[0][12] ,
        "total_events":all_articles[0][13] 
    }
    return jsonify({
        "data": article_data,
        "status": "success"
    })

# CREATE AN API FOR LIKED ARTICLES
@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

# CREATE AN API FOR DILIKED ARTICLES
@app.route("/disliked-article", methods=["POST"])
def disliked_article():
    article = all_articles[0]
    disliked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

# CREATE AN API FOR POPULAR ARTICLES
@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in df_main:
        data = {
            "timestamp": all_articles[0][1],
            "eventType": all_articles[0][2],
            "contentId":all_articles[0][3] ,
            "authorPersonId":all_articles[0][4] ,
            "authorSessionId":all_articles[0][5] ,
            "authorUserAgent":all_articles[0][6] ,
            "authorRegion":all_articles[0][7] ,
            "authorCountry":all_articles[0][8] ,
            "contentType":all_articles[0][9] ,
            "url":all_articles[0][10] ,
        
            "title":all_articles[0][11] ,
            "lang":all_articles[0][12] ,
            "total_events":all_articles[0][13] 
        }
        article_data.append(data)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

# CREATE AN API FOR RECOMMENDED ARTICLES
@app.route("/recommended-articles")
def recommended_movies():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_articles[2])
        for data in output:
            all_recommended.append(data)

    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        data = {
            "timestamp": all_articles[0][1],
            "eventType": all_articles[0][2],
            "contentId":all_articles[0][3] ,
            "authorPersonId":all_articles[0][4] ,
            "authorSessionId":all_articles[0][5] ,
            "authorUserAgent":all_articles[0][6] ,
            "authorRegion":all_articles[0][7] ,
            "authorCountry":all_articles[0][8] ,
            "contentType":all_articles[0][9] ,
            "url":all_articles[0][10] ,
        
            "title":all_articles[0][11] ,
            "lang":all_articles[0][12] ,
            "total_events":all_articles[0][13] 
        }
        article_data.append(data)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200


# RUN THE FLASK API
if __name__ == "__main__":
  app.run()




