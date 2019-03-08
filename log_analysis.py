#!/usr/bin/env python3.7.1
import psycopg2


def run_query_view(query):
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    cur.execute('select * from {}'.format(query))
    results = cur.fetchall()
    cur.close()
    db.close()
    return results


def top_three_articles():
    articles = run_query_view('popular_articles')
    text = ['\nTop three articles of all time are:\n']
    article_no = 1

    if articles is not None:
        for article in articles:
            article_info = '{}. {} - {} views'.format(
                article_no, article[0], str(article[1]))
            text.append(article_info)
            article_no += 1

        print('\n'.join(text))


def most_popular_authors():
    authors = run_query_view('popular_authors')
    text = ['\nThe most popular article authors of all time are:\n']
    author_no = 1

    if authors is not None:
        for author in authors:
            author_formatted = '{}. {} - {} views'.format(
                author_no, author[0], str(author[1]))
            text.append(author_formatted)
            author_no += 1

        print('\n'.join(text))


def dates_with_more_errors():
    dates = run_query_view('days_with_more_than_one_percent_errors')
    text = ['\nOn following dates more than 1% of requests lead to errors:\n']

    if dates is not None:
        for date in dates:
            formated_date = date[0].strftime('%B %d, %Y')
            text.append('{} - {}% errors'.format(formated_date, str(date[1])))

        print('\n'.join(text))


def main():
    top_three_articles()
    most_popular_authors()
    dates_with_more_errors()

if __name__ == '__main__':
    main()
