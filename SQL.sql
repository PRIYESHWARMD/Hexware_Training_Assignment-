create database HMBank;
use HMBank;
-- Customers table
create table Customers
(customer_id int primary key,
 first_name varchar(20) not null,
 last_name varchar(20), DOB date not null, 
 email varchar(50) unique,
 phone_number int unique, 
 address varchar(20));
alter table Customers modify phone_number varchar(10);
alter table customers modify address varchar(50);
insert into Customers (customer_id, first_name, last_name, DOB, email, phone_number, address) values
(1, 'Steven', 'King', '1970-01-15', 'sking@example.com', '9001110001', '123 Elm Street LA'),
(2, 'Neena', 'Kochhar', '1975-05-20', 'nkochhar@example.com', '9001110002', '456 Oak Avenue New York'),
(3, 'Lex', 'De Haan', '1980-03-30', 'ldehaan@example.com', '9001110003', '789 Pine Road texas'),
(4, 'Alexander', 'Hunold', '1982-07-12', 'ahunold@example.com', '9001110004', '321 Maple Lane LA'),
(5, 'Bruce', 'Ernst', '1979-11-25', 'bernst@example.com', '9001110005', '654 Cedar Street LA');
insert into Customers (customer_id, first_name, last_name, DOB, email, phone_number, address) values
(6, 'David', 'Austin', '1984-06-18', 'daustin@example.com', '9001110006', '987 Birch Blvd new york LA'),
(7, 'Valli', 'Pataballa', '1987-02-14', 'vpatabal@example.com', '9001110007', '222 Spruce Circle LA'),
(8, 'Diana', 'Lorentz', '1990-09-05', 'dlorentz@example.com', '9001110008', '333 Redwood Drive new york'),
(9, 'Nancy', 'Greenberg', '1981-04-10', 'ngreenbe@example.com', '9001110009', '555 Willow Way new york'),
(10, 'Daniel', 'Faviet', '1983-08-23', 'dfaviet@example.com', '9001110010', '888 Sycamore Lane new york');

-- Accounts table
create table Accounts
(account_id int primary key auto_increment, 
customer_id int references Customers(coustomer_id), 
account_type enum('savings', 'current','zero_balance'), 
balance decimal(10,2) check(balance>=0));
alter table Accounts auto_increment=100;
insert into Accounts(customer_id, account_type, balance) values
 (1, 'savings',100000),
 (2,'current',200000),
 (3,'zero_balance',0),
 (4,'savings',50000),
 (5,'current',500000);
 
insert into Accounts (customer_id, account_type, balance) values
 (6, 'savings', 75000),
 (7, 'current', 300000),
 (8, 'zero_balance', 0),
 (9, 'savings', 120000),
 (10, 'current', 450000);

-- Transactions table
create table Transactions
 (transaction_id int primary key auto_increment,
 account_id int references Accounts(account_id),
 transaction_type enum('deposit','withdrawal','transfer'),
 amount decimal(10,2) check(amount>=0),
 transaction_date date not null);
alter table Transactions auto_increment=10001;
insert into Transactions (account_id, transaction_type, amount, transaction_date) values
(100, 'transfer', 54321, '2025-04-12'),
(101,'withdrawal',49579,'2023-03-21'),
(102,'deposit',2000,'2025-01-31'),
(103, 'withdrawal', 15000, '2024-06-10'),
(104, 'deposit', 30000, '2025-02-15'),
(105, 'transfer', 25000, '2023-11-20'),
(106, 'deposit', 4000, '2024-09-25'),
(107, 'deposit', 1200, '2025-03-05'),
(108, 'withdrawal', 5000, '2025-05-01'),
(109, 'transfer', 1800, '2023-12-18');
select * from transactions;
select * from accounts;
select * from customers;

-- Task 1
-- 1 Write a SQL query to retrieve the name, account type and email of all customers.
select concat(first_name,' ',last_name) 'Name',email,account_type
from Accounts,customers
where Accounts.customer_id=Customers.customer_id;
 
 -- 2 Write a SQL query to list all transaction corresponding customer.
 select concat(first_name,' ',last_name) 'Name',balance,transaction_type,amount
 from Accounts,Customers,Transactions
 where Accounts.customer_id=Customers.customer_id and Accounts.account_id=Transactions.account_id;

-- 3  Write a SQL query to increase the balance of a specific account by a certain amount.
update accounts set balance=51000 where balance= 50000;

-- 4 Write a SQL query to Combine first and last names of customers as a full_name.
select concat(first_name,' ',last_name) 'full_name'
from Customers;

-- 5 Write a SQL query to remove accounts with a balance of zero where the account type is savings.
update accounts set account_type='savings' where balance=0 and account_id=102;
delete from transactions 
where account_id in (select account_id from accounts 
where account_type='savings'and balance=0);
delete from Accounts
where account_type = 'savings' AND balance = 0;

-- 6 Write a SQL query to Find customers living in a specific city.
select * from customers 
where address like'%texas';

-- 7 Write a SQL query to Get the account balance for a specific account.
select balance from accounts
where account_id= 103;

-- 8 Write a SQL query to List all current accounts with a balance greater than $1,000.
select * from accounts
where balance>1000 and account_type='current';

-- 9 Write a SQL query to Retrieve all transactions for a specific account.
select * from transactions
where account_id=109;

-- 10 Write a SQL query to Calculate the interest accrued on savings accounts based on a given interest rate.
select *,balance*.10 'Interest'from accounts
where account_type='savings';

-- 11 Write a SQL query to Identify accounts where the balance is less than a specified overdraft limit.
select * from accounts
where balance< 75000;

-- 12 Write a SQL query to Find customers not living in a specific city.
select * from customers 
where address not like'%New York';

-- Task 3
-- 1. Write a SQL query to Find the average account balance for all customers.
select avg(balance) 'Avg Balance'
from accounts;

-- 2. Write a SQL query to Retrieve the top 10 highest account balances.
select balance from accounts
order by 1 desc;

-- 3. Write a SQL query to Calculate Total Deposits for All Customers in specific date.
select sum(amount) from transactions
where transaction_type='deposit' and transaction_date='2025-02-15';

-- 4. Write a SQL query to Find the Oldest and Newest Customers.
select concat(first_name,' ',last_name) 'Full_Name',DOB from customers
where dob= (select min(dob) from customers);

select concat(first_name,' ',last_name) 'Full_Name',DOB from customers
where dob= (select max(dob) from customers);

-- 5. Write a SQL query to Retrieve transaction details along with the account type.
select transaction_id,account_id,account_type,transaction_type,amount,transaction_date
from transactions join accounts using (account_id); 

-- 6. Write a SQL query to Get a list of customers along with their account details.
select account_id, customer_id, account_type,balance,concat(first_name,' ',last_name) 'Full_Name'
from accounts join customers using(customer_id);

-- 7. Write a SQL query to Retrieve transaction details along with customer information for a specific account.
select * 
from customers join accounts using(customer_id) join transactions using(account_id)
where customer_id=7;

-- 8. Write a SQL query to Identify customers who have more than one account.
insert into Accounts(customer_id, account_type, balance) values
 (2, 'savings',10000);
 select customer_id,count(account_id) from accounts
 group by customer_id
 having count(account_id)>1;
 
 -- 9. Write a SQL query to Calculate the difference in transaction amounts between deposits and withdrawals.
 select
 (select sum(amount) from transactions where transaction_type='deposit')'Total_deposit',
 (select sum(amount) from transactions where transaction_type='withdrawal')'Total_withdrawal',
 (select sum(amount) from transactions where transaction_type='deposit')- (select sum(amount) from transactions where transaction_type='withdrawal')'Difference';
 
-- 10. Write a SQL query to Calculate the average daily balance for each account over a specified period.
select account_id,balance,(balance/ count(distinct transaction_date))
from accounts join transactions using(account_id)
where transaction_date between '2025-02-15' and ' 2025-04-12'
group by account_id;

-- 11. Calculate the total balance for each account type.
select account_type,sum(balance) from accounts
group by account_type;

-- 12. Identify accounts with the highest number of transactions order by descending order.
select account_id,count(transaction_id) from transactions
group by account_id
order by 2 desc;
-- 13. List customers with high aggregate account balances, along with their account types.
select concat(first_name,' ',last_name) 'Full_Name', C.customer_id, group_concat(distinct A.account_type) as account_type,max(A.balance)
from customers C join  accounts A on C.customer_id=A.customer_id
group by C.customer_id
order by 4 desc;

-- 14. Identify and list duplicate transactions based on transaction amount, date, and account.
insert into Transactions (account_id, transaction_type, amount, transaction_date) values
(100, 'transfer', 54321, '2025-04-12');
select transaction_type,amount,transaction_date,count(*) from transactions
group by transaction_type,amount,transaction_date
having count(*)>1;


-- Task 4

-- 1. Retrieve the customer(s) with the highest account balance.
select concat(first_name,' ',last_name) 'Full_Name',balance
from customers join accounts using(customer_id) where balance =
(select max(balance) from accounts); 

-- 2. Calculate the average account balance for customers who have more than one account.
select customer_id, avg(balance) from accounts
where customer_id in (select customer_id from accounts group by customer_id having count(account_id)>1)
group by customer_id;

-- 3. Retrieve accounts with transactions whose amounts exceed the average transaction amount.
select * from transactions
where amount > (select avg(amount) from transactions); 

-- 4. Identify customers who have no recorded transactions.
select concat(first_name,' ',last_name) 'Full_Name' from customers 
where customer_id in(select customer_id from accounts 
where account_id not in(select account_id from transactions));

-- 5. Calculate the total balance of accounts with no recorded transactions.
select account_id,sum(balance) from accounts
where account_id not in (select account_id from transactions)
group by account_id;

-- 6. Retrieve transactions for accounts with the lowest balance.
select t.* from transactions t join accounts a using (account_id)
where a.balance=(select min(balance) from accounts) ;

-- 7. Identify customers who have accounts of multiple types.
select concat(first_name,' ',last_name) 'Full_Name' from customers 
where customer_id in (select customer_id from accounts group by customer_id having count(distinct account_type)>1);

-- 8. Calculate the percentage of each account type out of the total number of accounts.
select account_type,count(account_type)*100/(select count(account_id) from accounts) 'Percentage' from accounts
group by account_type;

-- 9. Retrieve all transactions for a customer with a given customer_id.
select concat(first_name,' ',last_name) 'Full_Name',t.* from customers join accounts using (customer_id) join transactions t using(account_id)
where customer_id=2;

select (select concat(first_name,' ',last_name) from customers where customer_id=2)'Full_Name' , t.* from transactions t
where account_id in (select account_id from accounts where customer_id=2);

-- 10. Calculate the total balance for each account type, including a subquery within the SELECT clause. 
select 
account_type,
  (select SUM(balance) from accounts as a2
   where a2.account_type = a1.account_type) as total_balance from accounts as a1;
