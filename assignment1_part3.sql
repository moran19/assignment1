mysql;

USE COMPANY1;

/* List all Employees whose salary is between 1,000 AND 2,000.
Show the Employee Name, Department and Salary */
SELECT ENAME, DEPTNO, SAL
FROM EMP
WHERE SAL BETWEEN 1000 AND 2000;

/* Count the number of people in department 30 who receive a salary */
SELECT COUNT(SAL) AS num_emp_salary
FROM EMP
WHERE DEPTNO = 30;

/* and the number of people who receive a commission */
SELECT COUNT(COMM) AS num_emp_commission
FROM EMP
WHERE DEPTNO = 30 AND COMM > 0;

/* Find the name and salary of employees in Dallas */
SELECT ENAME, SAL
FROM EMP
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO
WHERE LOC = 'DALLAS';

/* List all departments that do not have any employees */
SELECT DEPT.DEPTNO, DNAME
FROM DEPT
WHERE DEPT.DEPTNO NOT IN (SELECT EMP.DEPTNO FROM EMP);

/* List the department number and average salary of each department */
SELECT EMP.DEPTNO, AVG(SAL) AS avg_salary
FROM EMP
JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO
GROUP BY DEPT.DEPTNO;


/* Alternative code for question 2 */

/*Count the number of people in department 30 who receive a salary 
and the number of people who receive a commission*/
SELECT COUNT(SAL) AS num_emp_salary,
COUNT(CASE WHEN COMM > 0 THEN 1 END) AS num_emp_commission
FROM EMP
WHERE DEPTNO = 30;