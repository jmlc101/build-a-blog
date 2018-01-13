from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config['DEBUG'] = True
# Note: the connection string after :// contains the following info:
# user:password@server:portNumber/databaseName
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:1234@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

    def __init__(self, title, body):
        self.title = title
        self.body = body


@app.route('/', methods=['POST', 'GET'])
def index():
    blog_titles = []
    bodys = []
    blogs = Blog.query.filter(Blog.id > 0).all()
    for blog in blogs:
        blog_titles.append(blog.title)
        bodys.append(blog.body)
    return render_template('blog.html',title="Build A Blog!", blogs=blogs, blog_titles=blog_titles, bodys=bodys)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    # TODO - If either the blog title or blog body is left empty in the new post form, 
    #           the form is rendered again, with a helpful error message and 
    #           any previously-entered content in the same form inputs
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        new_blog = Blog(title, body)
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect('/')
    return render_template('newpost.html', title="Build A Blog!")



if __name__ == '__main__':
    app.run()