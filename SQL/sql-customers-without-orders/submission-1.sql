-- Write your query below
select c.name 
from customers c

-- join on orders 
LEFT JOIN orders o 
  ON c.id = o.customer_id
WHERE o.customer_id IS NULL;

