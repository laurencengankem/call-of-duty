from flaskext.mysql import MySQL
from app import app
import click

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'instadb.cmjk7a4sjre6.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'instadb'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hahahaha'

mysql.init_app(app)

flag = True


def new_search(username):
    cur = mysql.get_db().cursor()
    select_query = "SELECT USERNAME FROM analytics_search"
    cur.execute(select_query)
    results = cur.fetchall()
    for result in results:
        if flag:
            click.secho(
                " [searched]\t\t%s"%result,
                fg="blue",
            )
    if username in str(results):
        update_query = "UPDATE analytics_search SET counter = counter +1 WHERE (username = '%s' )" % username
        cur.execute(update_query)
        mysql.get_db().commit()
        print("already in")
    else:
        insert_query = "INSERT INTO analytics_search(username, counter) VALUES ('%s', '%s')" % (username, 1)
        cur.execute(insert_query)
        mysql.get_db().commit()
