## Reddit is a community-driven link-sharing site. Users submit links to articles, photos, and other content. Other users upvote the submissions they like, and downvote the ones they dislike. Users can comment on submissions, and even upvote or downvote other people's comments. We'll get Reddit API and analyze some questions.


```python
import requests
import requests.auth
import pandas as pd
```


```python
# ger personal access token
# personal info marked as 'confidential'
client_auth = requests.auth.HTTPBasicAuth('confidential', 'confidential')
```


```python
post_data = {"grant_type": "password", "username": "confidential", "password": "confidential"}
```


```python
headers = {"User-Agent": "confidential"}
```


```python
token = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
```


```python
# replace your access token with accessToken
headers = {"Authorization": "bearer accessToken", "User-Agent": "confidential"}
params = {"t": "day"}

# python as subrreddit
response = requests.get("https://oauth.reddit.com/r/python/top", headers=headers, params=params)

python_top = response.json()
```

### 1. Find all the posts


```python
posts = [i['data']['title'] for i in python_top['data']['children']]
posts
```




    ['"Automate the Boring Stuff with Python" online course is free to sign up for the next few days with code JUL2020FREE',
     'Using only Python, I made a web dashboard to follow the coronavirus situation in Brazil',
     'PyCapsule; Yes, this website uses Python in the browser instead of JavaScript to client-side render',
     'A somewhat silly demonstration of table formatting in the console with Rich',
     'Maze Generation With Python!',
     'What is the core of the Python programming language? - Brett Cannon',
     'Introducing iommi',
     'Python Humble Bundle',
     'Lark 0.9 released: A parser built with a focus on ergonomics, performance and resilience',
     'Build Your Own Machine Learning Web Service with Django',
     'Web Comic viewer using Stream lit(https://github.com/jojo96/StreamLit-Apps)',
     'Built a simple guitar learning companion website',
     'Tutorial: Develop Your Python Docker Applications Faster',
     'I built an API for generating PDF documents from HTML or templates',
     "I made a Flask app based on XKCD's meta collecting comic!",
     'Asynchronous Task Queue with Django, Celery and AWS SQS',
     'Guietta! — Guietta is a tool that makes simple GUIs simple:',
     'I made a reddit bot script for anyone to use on their subreddit, with several of the most widely-used features bots are using right now. Any critiques/suggestions welcome!',
     'Python automation for homework',
     'Syntax And Numerical Operators',
     'A bot that emails me the disk usage in my home server every week and shows data from the past in a graph',
     'Python program accessible online',
     'Deploying Flask to AWS: Amazon Linux 2, PostgreSQL, Nginx and, uWSGI',
     'Youtube download with tkinter and youtube-dl (new to this)',
     'Does anybody know about a built-in function I can use that takes in three lists and outputs a filled-in contour plot?']



### 2. What is the post that received the most up votes?


```python
most_upvotes = 0
id_most_upvotes = ''
name_most_upvotes = ''

for i in python_top['data']['children']:
    if i['data']['ups'] >= most_upvotes:
        most_upvotes = i['data']['ups']
        id_most_upvotes = i['data']['id']
        name_most_upvotes = i['data']['title']
        
print(most_upvotes)
print(id_most_upvotes)
print(name_most_upvotes)
```

    846
    hjgvcz
    "Automate the Boring Stuff with Python" online course is free to sign up for the next few days with code JUL2020FREE


### 3. View all of its comments


```python
comments = requests.get("https://oauth.reddit.com/r/python/comments/hjgvcz", headers=headers)
comments
```




    <Response [200]>




```python
comments_read = comments.json()
```


```python
list_of_comments = [i['data']['body'] for i in comments_read[1]['data']['children']]
list_of_comments
```




    ['Dude, if you keep giving your stuff away for free, lots of people might learn valuable skills. The world could become a better place. Do you want that on your conscience?!',
     'Thank you, kind person',
     'I’m almost done with the book, having a lot of trouble with the files part tho :/',
     'Good stuff',
     'You earned our respect. 🙏',
     'Thank you!',
     'Many thanks!',
     'I’m an experienced PHP dev looking to learn python. I understand the basics of python syntax. Is this a good place for me to start with getting my hands dirty?',
     "I bought the 1st edition last year but didn't get around to using it beyond the first few chapters... just picked it up again today before checking out reddit and seeing theres a new version... Is the older edition still relevant/worthwhile, or would it be better just to use the online edition?\n\nEdit: Scratch that I'll check the blog post.",
     'Thank you',
     'Great course',
     "This is by far the best beginner class I've found online for learning Python. Thanks so much for putting this together and continually making it accessible!",
     'Thank you sir, for your continued contribution to the community, I also want to become as skilled as you(plural) someday, and contribute back !',
     'Great Stuff! I enjoyed the book and the online course completing all of the programming assignments.  Lots of learning! Thanks 😊',
     'Thanks a lot for sharing the coupon !\n++',
     'Thanks! It worked for me without any issues.',
     'Thanks for the update.',
     'This is a great course. Thanks for doing that mate',
     'Thanks Al, this is awesome!',
     "I only have one questions...\n\n&amp;#x200B;\n\n&gt; (until I get that automation script done). \n\n&amp;#x200B;\n\nWhy?  \n\n\n&amp;#x200B;\n\n&amp;#x200B;\n\nI also want to add thank you,  I got to chapter 9 and gave up on the book, doing jetbrains right now, I did some DataCamp, but your book made Python accessible and sparked that fire, I do intend to finish, but I rather go at it with a little more knowledge.  It's been a very fun two months so far, hopefully it changes my career trajectory.  \n\n\nI love the style the book is written in, makes learning code much less intimidating, and giving it away for free is far too kind.",
     'Thank you sir',
     'Thank you for making this course free. This has given me  some motivation to start learning to code in python once again.',
     'Thank you very much',
     'Thank you!!!',
     'Thank you sir, enrolled!',
     'Amazing! Thank you so much!',
     'So kind!! Thank you!!! #humansbeingbros',
     'Thank you',
     'I love reddit. Thank you so much for this!',
     'Thanks a lot. Worked!!',
     'Thank you!!',
     'Thank you, good sir!',
     'Thanks you so much, very generous of you!',
     'Amazing, thanks! I will do it for sure!',
     'Thanks a lot! : )',
     'Is this from the Author of the book with the same name?',
     'You are a good man. Thank you',
     'thank you kind sir, you are amazing!',
     'thank you!',
     "Yesterday i thought it's time to try again learning how to code, today i got notification about humblebundle python bundle, checked out this subreddit for the first time, and found this post. Coincidence? I think not...",
     'Thank you',
     "Isn't this always going free",
     'Ty! I enrolled!',
     'I should make a bot that upvotes Al Sweigart posts.',
     'Thank you!',
     'Thank you🙏',
     'Not valid for your location',
     'Wait so if I sign up free right now I have it for life? Or is it a trial that will end and eventually start charging?',
     'Did the course as a refresher in June, if you can get it for free its great value for your time',
     'What a great time to decide to learn Python with a practical foundation. Much appreciated!',
     'Just finished this last night.  Super easy to understand if you are new to programming.',
     'Wish I could give you gold, but all I can give you rn is respect man💯',
     'Thanks, great!']



### 4. What is the top-level comment that receives the most up votes?


```python
comments_upvotes = 0
body_most_upvotes = ''

for i in comments_read[1]['data']['children']:
    if i['data']['ups'] >= comments_upvotes:
        comments_upvotes = i['data']['ups']
        body_most_upvotes = i['data']['body']
        
print(comments_upvotes)
print(body_most_upvotes)
```

    76
    Dude, if you keep giving your stuff away for free, lots of people might learn valuable skills. The world could become a better place. Do you want that on your conscience?!

