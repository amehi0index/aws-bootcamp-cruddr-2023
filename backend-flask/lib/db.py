from psycopg_pool import ConnectionPool
import os  #for env variables

class Db:

  def __init__(self):
    self.init_pool()


  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)

  def print_sql(self, sql):
    cyan = '\033[96m'
    no_color = '\033[0m'
    print(f'{cyan} SQL STATEMENT-[{title}]------{no_color}')
    print(sql)

  #when we want to commit data such as an insert

  def query_commit():
    try: 
      conn = self.pool.connection()
      cur =  conn.cursor()
      cur.execute(sql)
      conn.commit()
    except Exception as err:
      self.print_sql_err(err)


    # try:
    #   with self.pool.connection() as conn:
    #     cur =  conn.cursor()
    #     cur.execute(sql,params)
    #     if is_returning_id:
    #       returning_id = cur.fetchone()[0]
    #     conn.commit() 
    #     if is_returning_id:
    #       return returning_id
    # except Exception as err:
    #   self.print_sql_err(err)

  # when we want to return a json object
  def query_array_json(self,sql):
    # self.print_sql('array',sql)

    wrapped_sql = self.query_wrap_array(sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        json = cur.fetchone()
        return json[0]

  # When we want to return an array of json objects
  def query_object_json(self,sql):

    self.print_sql('json',sql)
    # self.print_params(params)
    wrapped_sql = self.query_wrap_object(sql)

    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(wrapped_sql)
        json = cur.fetchone()
        # if json == None:
        #   "{}"
        # else:
        #   return json[0]
        return json[0]

  def query_value(self,sql):
    self.print_sql('value',sql)
    with self.pool.connection() as conn:
      with conn.cursor() as cur:
        cur.execute(sql)
        json = cur.fetchone()
        return json[0]    

  def query_wrap_object(self,template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {template}
    ) object_row);
    """
    return sql

  def query_wrap_array(self,template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql

  def print_sql_err(self,err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print ("\npsycopg ERROR:", err, "on line number:", line_num)
    print ("psycopg traceback:", traceback, "-- type:", err_type)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

db = Db()