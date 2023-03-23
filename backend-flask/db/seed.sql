-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Ame Hi','amehi@gmail.com' , 'amehi' ,'MOCK'),
  ('Sam Iam','4of5khalils@gmail.com','sami','MOCK'),


INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'amehi' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )