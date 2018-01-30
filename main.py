from flask import Flask, request, redirect, render_template
from models import Blog
from app import app, db

@app.route('/', methods=['POST', 'GET'])
def index():
    blog_titles = []
    bodys = []
    blogs = Blog.query.filter(Blog.id > 0).all()
    
    # TODO - Try doing this a more complex way, as the bonus suggests.
    #flip blogs list around, the simple way
    flipped_blogs = []
    for blog in reversed(blogs):
        flipped_blogs.append(blog)

    for blog in blogs:
        blog_titles.append(blog.title)
        bodys.append(blog.body)
    return render_template('blog.html',title="Build A Blog!", blogs=flipped_blogs, blog_titles=blog_titles, bodys=bodys)


@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    # TODO - Need validation to make sure body is string under 2000 characters, ad db.Column specifies above.

    # TODO - If either the blog title or blog body is left empty in the new post form, 
    #           the form is rendered again, with a helpful error message and 
    #           any previously-entered content in the same form inputs
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        if (title == '') or (body == ''): # TODO - come up with better validation tech.
            error = 'Please enter "Title" and "Content" for new blog entry...'
            return render_template('newpost.html', title="Build A Blog!", error=error) # TODO - rewrite this using Flash Messages.
        else:
            new_blog = Blog(title, body)
            db.session.add(new_blog)
            db.session.commit()
            id = new_blog.id
            id = str(id)
            return redirect('/display?id='+id)
    return render_template('newpost.html', title="Build A Blog!")

@app.route('/display')
def display():
    id = request.args.get('id')
    blog = Blog.query.filter_by(id=id).first()
    blog_title = blog.title
    blog_body = blog.body
    return render_template('display.html', title="display blog here", blog_title=blog_title, blog_body=blog_body)




if __name__ == '__main__':
    app.run()