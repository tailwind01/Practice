CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  SET N=N-1;
  RETURN (
    Coalesce((Select distinct salary from Employee order by salary desc limit 1 offset N),null)
  );
END
