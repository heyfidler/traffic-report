#!/usr/bin/python2.7

import psycopg2

DB_NAME = "news"


def print_popular_articles():
    """Prints out the three most popular articles."""
    print '\n'
    print 'The three most popular articles'
    conn = None
    try:
        conn = psycopg2.connect(database=DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            select articles.title,count(log) num
            from articles,log
            where log.path ~ articles.slug
            and log.status='200 OK'
            group by articles.title
            order by num desc
            limit 3;
        """)
        rows = cur.fetchall()
        print '{0:<40} {1:>20}'.format("title", "views")
        print '-------------------------------------------------------------'
        for row in rows:
            print '{0:<40} {1:>20}'.format(row[0], row[1])
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def print_popular_authors():
    """Prints out the most popular authors."""
    print '\n'
    print 'The most popular authors'
    conn = None
    try:
        conn = psycopg2.connect(database=DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            select authors.name,count(log) num
            from articles,log,authors
            where log.path ~ articles.slug
            and log.status='200 OK'
            and authors.id=articles.author
            group by authors.name
            order by num desc;
        """)
        rows = cur.fetchall()
        print '{0:<40} {1:>20}'.format("author", "views")
        print '-------------------------------------------------------------'
        for row in rows:
            print '{0:<40} {1:>20}'.format(row[0], row[1])
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def print_high_errors():
    """Prints out the days with errors > %1"""
    print '\n'
    print 'Days with errors > %1'
    conn = None
    try:
        conn = psycopg2.connect(database=DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            select sub1.day,
            round(
                sub2.bad_count::numeric/sub1.good_count::numeric*100,1
            ) as num
            from
            (
                    select time::date as day, count(*) as good_count
                    from log
                    where status='200 OK'
                    group by day
            ) sub1,
            (
                    select time::date as day, count(*) as bad_count
                    from log
                    where status!='200 OK'
                    group by day
            ) sub2
            where sub1.day=sub2.day
            and sub2.bad_count::numeric/sub1.good_count::numeric*100 > 1
            order by num desc;
        """)
        rows = cur.fetchall()
        print '{0:<40} {1:>20}'.format("date", "% error")
        print '-------------------------------------------------------------'
        for row in rows:
            print '{0:<40} {1:>20}'.format(str(row[0]), str(row[1]))
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


print_popular_articles()
print_popular_authors()
print_high_errors()
