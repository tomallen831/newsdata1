This project covers postgresql and utilizes psycopg2

Download/Install:
  python
  Vagrant
  VirtualBox
  newsdata.sql

Open VirtualBox
Open Terminal
  $vagrant up
  $vagrant ssh
  cd /vagrant

Load newsdata.sql
  In VirtualBox enter:
    psql -d news -f newsdata.sql
    psql -d news

Create views
  a news=> opens up create a view by entering:

  create view popular_articles_view as select title, author, count(*) as views
  from articles, log where log.path like ('%', articles.slug) group by
  articles.title, articles.author order by views desc;

  create view error_days_view as select date(time),
  round(100.0 * sum(case log.status when '200 OK' then 0 else 1 end)
  /count(log.status),2) as "Error Percentage" from log group by date(time)
  order by "Error Percentage" desc;

  From VirtualBox run the news1.py file and save to .txt file
  /vagrant$ python news1.py > newsoutput.txt
