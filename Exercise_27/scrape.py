import requests
from bs4 import BeautifulSoup




def sort_by_score(items):
    return sorted(items, key=lambda x: x["score"], reverse=True)

def create_custom_item(links, votes, comments):
    hacker_news_items = []
    for index in range(len(links)):
        title = links[index].get_text() if index < len(links) else ""
        link = links[index]["href"] if index < len(links) else ""
        if len(votes) > index:
            score = int(votes[index].get_text().split()[0])
            if score > 99:
                hacker_news_items.append({
                    "title": title,
                    "link": link,
                    "score": score,
                })
    return hacker_news_items


for pagenum in range(1, 3):  # Scrape the first 3 pages
    response = requests.get(f"https://news.ycombinator.com/?p={pagenum}")
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.select(".athing .titleline a")
    votes = soup.select(".score")
    comments = soup.select(".subtext a:last-child")

    for item in sort_by_score(create_custom_item(links, votes, comments)):
        print(f"Title: {item['title']}")
        print(f"Link: {item['link']}")
        print(f"Score: {item['score']}" + " points")
        print("--------------------\n")




""" for item in soup.select(".athing"):
    title = item.select_one(".titleline a").get_text()
    link = item.select_one(".titleline a")["href"]
    score = item.select_one('.score')
    score = score.get_text() if score else "0 points"
    comments = item.select_one(".subtext a:last-child")
    comments = comments.get_text() if comments else "0 comments"
    print(f"Title: {title}")
    print(f"Link: {link}")
    print(f"Score: {score}")
    print(f"Comments: {comments}")
    print("--------------------\n") """

# Format and print the custom Hacker News items

for item in sort_by_score(create_custom_item(links, votes, comments)):
    print(f"Title: {item['title']}")
    print(f"Link: {item['link']}")
    print(f"Score: {item['score']}" + " points")
    print("--------------------\n")

print("\n\nFinished scraping Hacker News.\n")
