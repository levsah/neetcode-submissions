select 
    employee_id,
    Case 
        When employee_id % 2 != 0 AND name NOT LIKE 'M%' Then Salary
        Else 0
    End as bonus
From employees
order by employee_id;

