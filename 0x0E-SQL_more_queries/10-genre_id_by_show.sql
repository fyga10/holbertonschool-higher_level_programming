-- Import a database and list all the shows cointeined in it.
SELECT sh.title, shgr.genre_id FROM tv_shows AS sh
       JOIN tv_show_genres AS shgr ON sh.id=shgr.show_id
       ORDER BY sh.title, shgr.genre_id ASC;
