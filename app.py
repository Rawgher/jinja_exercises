import stories
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    questions = stories.story.prompts
    return render_template('home.html', questions=questions)


@app.route('/story')
def story():
    newStory = stories.story.generate(request.args)

    return render_template('story.html', story=newStory)