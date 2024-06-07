
from newsfeed.models import News

def main():
    news_items = News.objects.all()
    for news_item in news_items:
        print(news_item)

if __name__ == "__main__":
    main()
