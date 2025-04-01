#!/usr/bin/env python3
import os
import datetime
import argparse
from pathlib import Path

def create_jekyll_post(title, categories=None, tags=None, author=None, draft=False):
    """
    Create a new Jekyll post with proper front matter and file naming.
    
    Args:
        title (str): Title of the post
        categories (list, optional): List of categories. Defaults to None.
        tags (list, optional): List of tags. Defaults to None.
        author (str, optional): Author name. Defaults to None.
        draft (bool, optional): Whether to create as draft. Defaults to False.
    """
    
    # Set timezone to GMT+7
    tz = datetime.timezone(datetime.timedelta(hours=7))
    today = datetime.datetime.now(tz)
    
    # Format the filename according to Jekyll conventions
    slug = title.lower().replace(' ', '-').replace('?', '').replace('!', '').replace(':', '')
    filename = f"{today.strftime('%Y-%m-%d')}-{slug}.md"
    
    # Determine the directory based on draft status
    if draft:
        directory = "_drafts"
    else:
        directory = "_posts"
    
    # Create directory if it doesn't exist
    Path(directory).mkdir(exist_ok=True)
    
    # Create the file path
    filepath = os.path.join(directory, filename)
    
    # Create front matter
    front_matter = "---\n"
    front_matter += f"title: \"{title}\"\n"
    front_matter += f"date: {today.strftime('%Y-%m-%d %H:%M:%S %z')}\n"  # Now includes GMT+7
    
    if author:
        front_matter += f"author: {author}\n"
    
    if categories:
        front_matter += "categories:\n"
        for category in categories:
            front_matter += f"  - {category}\n"
    
    if tags:
        front_matter += "tags:\n"
        for tag in tags:
            front_matter += f"  - {tag}\n"
    
    front_matter += "---\n\n"
    front_matter += "Your post content goes here.\n"
    
    # Write the file
    with open(filepath, 'w') as f:
        f.write(front_matter)
    
    print(f"Created new Jekyll post at: {filepath}")
    return filepath

def main():
    parser = argparse.ArgumentParser(description='Create a new Jekyll post.')
    parser.add_argument('title', help='Title of the post')
    parser.add_argument('--categories', nargs='+', help='List of categories')
    parser.add_argument('--tags', nargs='+', help='List of tags')
    parser.add_argument('--author', help='Author name')
    parser.add_argument('--draft', action='store_true', help='Create as draft')
    
    args = parser.parse_args()
    
    create_jekyll_post(
        title=args.title,
        categories=args.categories,
        tags=args.tags,
        author=args.author,
        draft=args.draft
    )

if __name__ == "__main__":
    main()
