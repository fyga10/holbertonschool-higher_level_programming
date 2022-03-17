-- List all the shows in the database.
SELECT sh.title, shgr.genre_id FROM tv_shows AS sh
       LEFT JOIN tv_show_genres AS shgr ON sh.id=shgr.show_id
       ORDER BY sh.title, shgr.genre_id ASC;
