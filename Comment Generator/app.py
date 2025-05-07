from flask import Flask, render_template_string, request
from pytube import YouTube
import random

app = Flask(__name__)

# Comment templates and emojis
COMMENT_TEMPLATES = [
    "Loved this video on '{title}'! {emoji}",
    "Wow, '{title}' was so interesting! {emoji}",
    "This deserves way more views! {emoji}",
    "Great content as always on '{title}' {emoji}",
    "I learned a lot from '{title}'. Thanks for sharing! {emoji}",
    "Awesome job! '{title}' was amazing {emoji}",
    "Keep making videos like '{title}' {emoji}",
    "Very helpful video on '{title}', much appreciated {emoji}",
    "Super engaging — '{title}' kept me hooked! {emoji}",
    "Brilliant editing on '{title}'! {emoji}"
]

EMOJIS = ["🔥", "😍", "💥", "👏", "👍", "🙌", "💯", "🤩", "🎉", "😊"]

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>YouTube Comment Generator</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #6a11cb, #2575fc);
            color: #fff;
            padding: 50px;
            text-align: center;
        }
        h1 {
            font-size: 36px;
            margin-bottom: 30px;
        }
        input, button {
            padding: 15px;
            width: 70%;
            margin: 10px 0;
            border-radius: 8px;
            border: none;
            font-size: 18px;
        }
        input {
            background-color: #fff;
            color: #333;
        }
        button {
            background-color: #2575fc;
            color: #fff;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #6a11cb;
        }
        .comment {
            background-color: #fff;
            color: #333;
            padding: 15px;
            margin: 10px 0;
            border-radius: 8px;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
            font-size: 18px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .comment span {
            font-style: italic;
        }
        .copy-btn {
            background-color: #28a745;
            color: #fff;
            font-size: 14px;
            padding: 8px 12px;
            border-radius: 5px;
            cursor: pointer;
            border: none;
        }
        .copy-btn:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>
    <h1>YouTube Comment Generator 🚀</h1>
    <form method="post">
        <input type="text" name="link" placeholder="Paste YouTube video link" required>
        <button type="submit">Generate Comments</button>
    </form>
    {% if title %}
        <h2>Video Title: {{ title }}</h2>
        <h3>Generated Comments:</h3>
        <div id="commentsContainer">
            {% for comment in comments %}
                <div class="comment">
                    <span>{{ comment }}</span>
                    <button class="copy-btn" onclick="copyComment('{{ comment | escape }}')">Copy</button>
                </div>
            {% endfor %}
        </div>
    {% endif %}
    
    <script>
        function copyComment(commentText) {
            // Create a temporary textarea element to copy the text
            var tempInput = document.createElement('textarea');
            tempInput.value = commentText;
            document.body.appendChild(tempInput);
            tempInput.select();
            try {
                // Copy the text
                document.execCommand('copy');
                alert('Comment copied to clipboard!');
            } catch (e) {
                alert('Unable to copy comment.');
            }
            document.body.removeChild(tempInput);
        }
    </script>
</body>
</html>
"""



def fetch_video_title(link):
    try:
        yt = YouTube(link)
        return yt.title
    except Exception as e:
        print(f"Error fetching title: {e}")
        if 'watch?v=' in link:
            return f"Video {link.split('v=')[-1]}"
        else:
            return "your video"

def generate_comments(title):
    comments = []
    for _ in range(50):  # generate 50 comments
        template = random.choice(COMMENT_TEMPLATES)
        emoji = random.choice(EMOJIS)
        comment = template.format(title=title, emoji=emoji)
        comments.append(comment)
    return comments

@app.route('/', methods=['GET', 'POST'])
def index():
    title = None
    comments = []
    if request.method == 'POST':
        link = request.form['link']
        title = fetch_video_title(link)
        comments = generate_comments(title)
    return render_template_string(HTML_TEMPLATE, title=title, comments=comments)

if __name__ == '__main__':
    app.run(debug=True)
