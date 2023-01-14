INSERT INTO main.app_task
(user_id_id, status, place, total_hours, completed_hours, description, created_at, updated_at, worker_id_id)
VALUES ((select id from auth_user where username = 'student1'), 'TO_DO', 'Haifa', 200, 0, 'isarel ', datetime('now'),
        datetime('now'), (select id from auth_user where username = 'worker1'));