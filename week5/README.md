## Task 2: Create database and table in your MySQL server

● INSERT a new row to the member table where name, username and password must
be set to test. INSERT additional 4 rows with arbitrary data.
```
INSERT INTO member (name, username, password) 
VALUES ('test', 'test', 'test');
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/fed7feb1-9ddb-4051-81f7-da8005d29e7f)


```
INSERT INTO member (name, username, password, follower_count)
VALUES
  ('Charles', 'lion', '123qwe', 10),
  ('Jocelyn', 'cat', 'ewq321', 15),
  ('Belle', 'dog', 'rte321', 40),
  ('Sherry', 'rabbit', 'hippo421', 30);
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/013b6987-dbcd-4fab-b7e0-38f2ef6566a7)



● SELECT all rows from the member table.
```
SELECT * FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/eccb539a-8e51-45b4-8572-4ae61c87a00a)



● SELECT all rows from the member table, in descending order of time.
```
SELECT * FROM member ORDER BY time DESC;
```



● SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```


● SELECT rows where username equals to test.
```
SELECT * FROM member WHERE username = 'test';
```


● SELECT rows where name includes the es keyword.
```
SELECT * FROM member WHERE name LIKE '%es%';
```


● SELECT rows where both username and password equal to test.
```
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```



● UPDATE data in name column to test2 where username equals to test.
```
UPDATE member SET name = 'test2' WHERE username = 'test';
```



## Task 4: SQL Aggregation Functions

● SELECT how many rows from the member table.
```
SELECT COUNT(*) FROM member;
```


● SELECT the sum of follower_count of all the rows from the member table.
```
SELECT SUM(follower_count) FROM member;
```



● SELECT the average of follower_count of all the rows from the member table.
```
SELECT AVG(follower_count) FROM member;
```



● SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table.
```
SELECT AVG(follower_count) 
FROM (
    SELECT follower_count 
    FROM member 
    ORDER BY follower_count DESC 
    LIMIT 2
) AS top_two;
```


