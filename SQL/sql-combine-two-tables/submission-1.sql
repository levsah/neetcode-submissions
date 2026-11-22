-- Write your query below
-- take person table, join it on person_id on address table
select first_name, last_name, city, state
from person p
LEFT JOIN address a on p.person_id = a.person_id;





