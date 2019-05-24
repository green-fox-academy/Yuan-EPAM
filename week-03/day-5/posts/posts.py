from flask import Flask, render_template
import post_database as post_db

app = Flask(__name__)

def get_author_name(authors):
    author_name = {}
    for author in authors:
        author_name[author['id']] = author['name']
    return author_name

def get_post_liked(authors, author_name):
    post_liked = {}
    for author in authors:
        if len(author['likes']):
            for post_id in author['likes']:
                if post_id in post_liked.keys():
                    post_liked[post_id].append(author['name'])
                else:
                    post_liked[post_id] = list([author['name']])
        else:
            post_liked[author['id']] = []
    return post_liked

def transform_data(posts, authors):
    head = ['id', 'author', 'content', 'liked_by']
    author_name = get_author_name(authors)
    print(f'author name : {author_name}')
    post_liked = get_post_liked(authors, author_name)
    print(f'post liked : {post_liked}')
    processed_post = []
    for post in posts:
        post_tmp = post
        post_tmp.update({'author':author_name[post['author']]})
        if post['id'] in post_liked.keys():
            post_tmp['liked_by'] = post_liked[post['id']]
        else:
            post_tmp['liked_by'] = []
        processed_post.append(post_tmp)
    print(processed_post)
    return processed_post

@app.route('/posts')
def list_posts():
    authors = post_db.get_file_data('authors.json')
    posts = post_db.get_file_data('posts.json')
    transformed_posts = transform_data(posts, authors)
    return render_template('posts.html', posts=transformed_posts)

