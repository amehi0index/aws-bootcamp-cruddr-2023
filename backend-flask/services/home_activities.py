from datetime import datetime, timedelta, timezone
from lib.db import pool, query_wrap_array

# Acquire tracer tobe sent to HoneyComb
from opentelemetry import trace
tracer = trace.get_tracer("home.activities")

class HomeActivities:
  # def run(logger):
  #   logger.info("HomeActivities")
  def run(cognito_user_id=None):
    # Create span, name span that will appear in list of stories
    with tracer.start_as_current_span("home-activities-mock-data"):
      #Set span attribute
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()
      span.set_attribute("app.now", now.isoformat())

      #sql heredoc
      sql = query_wrap_array("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
      """)
      print("==SQL--")
      print(sql)
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          json = cur.fetchone()
      print("-1--------")
      print(json[0])
      return json[0]
      return results
   