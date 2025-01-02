# reddit_scraper.py

import praw
from prawcore.exceptions import RequestException, ServerError, ResponseException, Forbidden
import os
import time
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def wait_and_retry(func, *args, retries=5, backoff_factor=2, **kwargs):
    """
    Retry a function if a rate limit or server error occurs.
    """
    attempt = 0
    while attempt < retries:
        try:
            return func(*args, **kwargs)
        except (RequestException, ServerError, ResponseException) as e:
            attempt += 1
            wait_time = backoff_factor ** attempt
            print(f"Error: {e}. Retrying in {wait_time} seconds...")
            time.sleep(wait_time)
        except Forbidden:
            print("Access forbidden. Skipping...")
            return None
    print(f"Failed after {retries} attempts.")
    return None

def scrape_reddit_user(username, task_id, tasks):
    """
    Scrape Reddit user data and update the tasks dict with progress.
    """
    output_data = ""
    try:
        tasks[task_id]['progress'] = 'Fetching user information...'
        # Get user object
        user = wait_and_retry(reddit.redditor, username)
        if not user:
            print(f"Unable to fetch data for user: {username}")
            tasks[task_id]['progress'] = 'Failed to fetch user data.'
            tasks[task_id]['status'] = 'Failed'
            return None

        output_data += f"# Reddit User: {username}\n\n## 📝 Posts:\n\n"

        # Count posts and comments
        tasks[task_id]['progress'] = 'Counting total posts and comments...'
        total_posts = wait_and_retry(lambda: sum(1 for _ in user.submissions.new(limit=None)))
        total_comments = wait_and_retry(lambda: sum(1 for _ in user.comments.new(limit=None)))
        tasks[task_id]['total_posts'] = total_posts
        tasks[task_id]['total_comments'] = total_comments
        tasks[task_id]['progress'] = f"Total Posts: {total_posts}, Total Comments: {total_comments}\n"

        # Initialize scraped counts
        tasks[task_id]['scraped_posts'] = 0
        tasks[task_id]['scraped_comments'] = 0

        # Scrape posts
        tasks[task_id]['progress'] = 'Scraping posts...'
        submissions = wait_and_retry(user.submissions.new, limit=None)
        if submissions:
            for post in submissions:
                try:
                    post_data = (
                        f"### Title: {post.title}\n"
                        f"**Subreddit:** {post.subreddit}\n"
                        f"**URL:** {post.url}\n"
                        f"**Content:** {post.selftext or 'No Content'}\n\n"
                    )
                    output_data += post_data
                    tasks[task_id]['scraped_posts'] += 1
                    tasks[task_id]['progress'] = f"Scraping posts... ({tasks[task_id]['scraped_posts']}/{tasks[task_id]['total_posts']})"
                except Exception as post_error:
                    print(f"Error with post: {post_error}")

        # Add section for comments
        output_data += "\n## 💬 Comments:\n\n"

        # Scrape comments
        tasks[task_id]['progress'] = 'Scraping comments...'
        comments = wait_and_retry(user.comments.new, limit=None)
        if comments:
            for comment in comments:
                try:
                    comment_data = (
                        f"### Comment:\n{comment.body}\n"
                        f"**Subreddit:** {comment.subreddit}\n"
                        f"**Post:** {comment.submission.title}\n"
                    )

                    # Add parent comment if replying
                    if not comment.is_root:
                        parent_comment = wait_and_retry(comment.parent)
                        if isinstance(parent_comment, praw.models.Comment):
                            comment_data += f"**Parent Comment:** {parent_comment.body}\n"

                    comment_data += "\n"
                    output_data += comment_data
                    tasks[task_id]['scraped_comments'] += 1
                    tasks[task_id]['progress'] = f"Scraping comments... ({tasks[task_id]['scraped_comments']}/{tasks[task_id]['total_comments']})"
                except Exception as comment_error:
                    print(f"Error with comment: {comment_error}")

        print("\nScraping completed!")
        tasks[task_id]['progress'] = 'Scraping completed. Processing data...'
        tasks[task_id]['status'] = 'Processing'
        return output_data
    
    except:
        pass