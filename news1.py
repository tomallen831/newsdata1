#!/usr/bin/env python3


import psycopg2
DB_NAME = "news"


# Connect to database
def connect_db(question):
    db = psycopg2.connect(database=DB_NAME)
    c = db.cursor()
    c.execute(question)
    results = c.fetchall()
    db.close()
    return results


# 1. What are the most popular three articles of all time?
question_1 = """select title, views
                    from popular_articles_view limit 3"""


# 2. Who are the most popular article authors of all time?
question_2 = """select authors.name, sum(popular_articles_view.views) as views
                    from popular_articles_view, authors
                    where authors.id = popular_articles_view.author
                    group by authors.name
                    order by views desc"""


# 3. On which days did more than 1% of requests lead to errors?
question_3 = """select * from error_days_view
                    where \"Error Percentage\" > 1"""


# Print questions
def print_question(title):
    print("\n" + title + "\n")


# Print 1. Who are the most popular article authors of all time?
def popular_articles():
    popular_articles = connect_db(question_1)
    print_question("1. What are the most popular three articles of all time?")

    for title, num in popular_articles:
        print(" \"{}\" -- {} views".format(title, num))


# Print 2. On which days did more than 1% of requests lead to errors?
def popular_authors():
    popular_authors = connect_db(question_2)
    print_question("2. Who are the most popular article authors of all time?")

    for name, num in popular_authors:
        print(" {} -- {} views".format(name, num))


# Print 3. On which days did more than 1% of requsets lead to errors?
def error_days():
    error_days = connect_db(question_3)
    print_question("3. On which days did more than
                    1% of requests lead to errors?")
    for day, errorpercentage in error_days:
        print("""{0:%B %d, %Y} -- {1:.2f} % errors""".
                format(day, errorpercentage))


if __name__ == '__main__':
    popular_articles()
    popular_authors()
    error_days()
