import praw, random

reddit = praw.Reddit(client_id = 'lwcq_8ZSRdJQVQ',
                     client_secret = 'VZwCKZ6YSmjz_LyF4AiccgXSJes',
                     user_agent = 'meme_review',
                     username = 'blue_baby_yoshi__',
                     password = 'blue_baby_yoshi__')
subreddit = reddit.subreddit('memes')
top_subreddit = subreddit.top()
for submission in subreddit.top(limit = 10):
    print(submission.url)