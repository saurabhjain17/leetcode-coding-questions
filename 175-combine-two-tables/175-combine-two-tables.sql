# Write your MySQL query statement below
select p.firstName,p.lastName,A.city,A.state from person p left outer join address A on p.personid=a.personid