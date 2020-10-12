from flask import Flask, render_template, request

from mysql import buildQueryFromInput, connect_mysql

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mysql', methods = ['POST'])
def queryMysql():
    raw_query = request.form['query']
    # return render_template('index.html', query=raw_query)
    q = buildQueryFromInput(raw_query)

    connection = connect_mysql(host='cs527project1group5.cnpt9dsbfddc.us-east-1.rds.amazonaws.com',
                               user='admin',
                               password='cs527project1',
                               db='')

    col_name, res, query_time = connection.run_query(q)
    return render_template('index.html',
                           col_name=col_name,
                           res=res,
                           query_time=query_time,
                           query=raw_query)

if __name__ == '__main__':
    app.run()
