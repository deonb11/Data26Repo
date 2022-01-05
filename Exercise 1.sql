--EXERCISE 1
--1.1
SELECT CustomerID, CompanyName, Address, City, PostalCode
FROM Customers
WHERE City = 'London'or City ='Paris';

--1.2
SELECT ProductName
FROM Products
WHERE QuantityPerUnit LIKE '%bottles%'

--1.3
SELECT ProductName,s.CompanyName, s.Country
FROM Products p
JOIN Suppliers s
ON p.SupplierID =s.SupplierID
WHERE QuantityPerUnit LIKE '%bottles%'

--1.4
SELECT c.CategoryName, COUNT(p.ProductName) AS 'No. of Products'
FROM Categories c
LEFT JOIN Products p
ON p.CategoryID =c.CategoryID
GROUP BY c.CategoryID, c.CategoryName
ORDER BY [No. of Products] DESC;

--1.5
SELECT TitleOfCourtesy +' '+FirstName +' '+ LastName AS 'FullName', City
FROM Employees
WHERE Country= 'UK'

SELECT*FROM Territories
SELECT*FROM Region
SELECT*FROM [Order Details] 
SELECT*FROM Orders
SELECT*FROM EmployeeTerritories

--1.6
SELECT FORMAT(Sum((od.UnitPrice*od.Quantity)),'C0') AS 'Sales Totals', r.RegionDescription
FROM [Order Details] od 
JOIN Orders o 
    ON od.OrderID =o.OrderID
JOIN EmployeeTerritories e
    ON o.EmployeeID =e.EmployeeID
JOIN Territories t 
    ON e.TerritoryID =t.TerritoryID
JOIN Region r 
    ON t.RegionID=r.RegionID

GROUP BY  r.RegionDescription
HAVING Sum((od.UnitPrice*od.Quantity)) > 1000000 
-- filtering for >1000000


--1.7
SELECT COUNT(*)
FROM Orders
WHERE Freight>100
AND ShipCountry IN  ('UK','USA');


--1.8
--SELECT TOP 5 OrderID, FORMAT((UnitPrice*Quantity) * Discount,'C') AS 'Total Discount'
--FROM [Order Details]
--ORDER By [Total Discount] DESC


SELECT TOP 5 OrderID, ((UnitPrice*Quantity) * Discount) AS 'Total Discount'
FROM [Order Details]
ORDER By [Total Discount] DESC


--2.0

USE Deon_db
DROP TABLE IF EXISTS Spartans

CREATE TABLE Spartans(
    SpartanID int IDENTITY PRIMARY KEY NOT NULL,
    Title VARCHAR(20) NOT NULL, 
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    University_attend VARCHAR (50),
    Course VARCHAR(50),
    Grade VARCHAR (50)
)

INSERT INTO Spartans 
VALUES 
('Mr', 'Allan', 'Elias', 'University of Birmingham', 'Electrical and Electronic Engineering', 'First'),
('Mr', 'Jordan', 'Baldwin', 'Swansea University', 'Computer Science', 'First'),
('Mr','Deon', 'Bepe', 'University of Essex', 'Actuarial Science', 'Upper Second'),
('Mr','Mohamad Jad', 'AL Khalil', 'University of Essex', 'Electrical Engineering', 'First'),
('Mr','Aidan', 'Jones', 'Univeristy of Sheffield', 'Aerospace Engineering', 'First'),
('Mr','Jacob', 'Baker', 'Univeristy of Essex', 'Electronic Engineering', 'Upper Second'),
('Miss','Mariam', 'Sengo', 'Univeristy of East London', 'Civil Engineering', 'Second'),
('Mr','Yi', 'Chen', 'Univeristy of Bath', 'Integrated Mechanical & Electrical Engineering', 'Upper Second'),
('Mr','Ali', 'Matten', 'Goldsmiths University of London', 'Computer Science', 'First'),
('Mr','Cameron', 'Mclean', 'Univeristy of Nottingham', 'Physics', 'Second')

--3.1
USE Northwind
SELECT*
FROM Employees e


SELECT e2.EmployeeID, e2.FirstName, e2.LastName, e1.employeeID, e1.FirstName +' '+e1.LastName AS 'Reports To'
FROM Employees e2
JOIN Employees e1
    ON e2.ReportsTo =e1.EmployeeID

