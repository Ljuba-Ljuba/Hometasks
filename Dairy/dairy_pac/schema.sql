CREATE TABLE IF NOT EXISTS dairy (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  task_name TEXT NOT NULL,
  task_description TEXT NOT NULL DEFAULT '',
  task_status TEXT NOT NULL DEFAULT '1111',
  task_craeted DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  task_realizer TEXT NOT NULL DEFAULT 'Liubov',
  task_time DATETIME NOT NULL DEFAULT CURRENT_DATE


)
