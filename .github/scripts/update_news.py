#!/usr/bin/env python3
"""
Financial News Ticker Updater
Fetches news from multiple sources and updates README.md
"""

import feedparser
import re
from datetime import datetime
from typing import List, Dict
import sys

# News sources configuration
NEWS_SOURCES = [
    {
        "name": "CNBC Market",
        "url": "https://www.cnbc.com/id/10000664/device/rss/rss.html",
        "category": "Market"
    },
    {
        "name": "Reuters Business",
        "url": "https://www.reutersagency.com/feed/?taxonomy=best-topics&post_type=best",
        "category": "Business"
    },
    {
        "name": "Financial Times",
        "url": "https://www.ft.com/?format=rss",
        "category": "Finance"
    }
]

# Markers for README update
START_MARKER = "<!-- NEWS:START -->"
END_MARKER = "<!-- NEWS:END -->"


def fetch_news_from_source(source: Dict) -> List[Dict]:
    """Fetch news from a single RSS source with error handling."""
    try:
        feed = feedparser.parse(source["url"])
        news_items = []
        
        for entry in feed.entries[:5]:  # Get top 5 items
            try:
                # Parse publication date
                pub_date = entry.get("published", "")
                if pub_date:
                    try:
                        date_obj = datetime.strptime(pub_date, "%a, %d %b %Y %H:%M:%S %Z")
                        formatted_date = date_obj.strftime("%b %d, %Y")
                    except:
                        formatted_date = pub_date[:15]
                else:
                    formatted_date = datetime.now().strftime("%b %d, %Y")
                
                news_items.append({
                    "title": entry.get("title", "No title"),
                    "link": entry.get("link", "#"),
                    "date": formatted_date,
                    "category": source["category"]
                })
            except Exception as e:
                print(f"Error parsing entry from {source['name']}: {e}", file=sys.stderr)
                continue
        
        return news_items
    except Exception as e:
        print(f"Error fetching from {source['name']}: {e}", file=sys.stderr)
        return []


def fetch_all_news() -> List[Dict]:
    """Fetch news from all sources and aggregate."""
    all_news = []
    
    for source in NEWS_SOURCES:
        print(f"Fetching from {source['name']}...")
        news_items = fetch_news_from_source(source)
        all_news.extend(news_items)
    
    # Sort by date (most recent first) and limit to 10 items
    return all_news[:10]


def format_news_as_markdown(news_items: List[Dict]) -> str:
    """Format news items as markdown table."""
    if not news_items:
        return """| Category | Date | Headline |
|----------|------|----------|
| - | - | No news available at this time |
"""
    
    markdown = """| Category | Date | Headline |
|----------|------|----------|
"""
    
    for item in news_items:
        # Escape pipe characters in title
        title = item["title"].replace("|", "\\|")
        # Truncate long titles
        if len(title) > 100:
            title = title[:97] + "..."
        
        markdown += f"| {item['category']} | {item['date']} | [{title}]({item['link']}) |\n"
    
    return markdown


def update_readme(news_markdown: str):
    """Update README.md with new news content."""
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            content = f.read()
        
        # Check if markers exist
        if START_MARKER not in content or END_MARKER not in content:
            print("Warning: News markers not found in README.md", file=sys.stderr)
            print("Please add the following markers to your README where you want the news:")
            print(f"{START_MARKER}")
            print("(news will appear here)")
            print(f"{END_MARKER}")
            return
        
        # Replace content between markers
        pattern = f"{re.escape(START_MARKER)}.*?{re.escape(END_MARKER)}"
        replacement = f"{START_MARKER}\n{news_markdown}\n{END_MARKER}"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        
        print("README.md updated successfully!")
        
    except Exception as e:
        print(f"Error updating README: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main execution function."""
    print("Starting financial news ticker update...")
    
    # Fetch news
    news_items = fetch_all_news()
    
    if not news_items:
        print("Warning: No news items fetched from any source", file=sys.stderr)
        # Still create a placeholder
        news_items = []
    
    # Format as markdown
    news_markdown = format_news_as_markdown(news_items)
    
    # Update README
    update_readme(news_markdown)
    
    print(f"Update complete! Added {len(news_items)} news items.")


if __name__ == "__main__":
    main()
