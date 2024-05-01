## Task 2: Create database and table in your MySQL server

● INSERT a new row to the member table where name, username and password must
be set to test. INSERT additional 4 rows with arbitrary data.
```
INSERT INTO member (id, name, username, password, follower_count, time) 
VALUES (1, 'test', 'test', 'test', 0, NOW());
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/f5d48140-83eb-459f-a22b-30d12662acc6)

```
INSERT INTO member (id, name, username, password, follower_count, time)
    -> VALUES
    -> (2, 'Charles', 'lion', '123qwe', 10, NOW()),
    -> (3, 'Jocelyn', 'cat', 'ewq321', 15, NOW()),
    -> (4, 'Belle', 'dog', 'rte321', 40, NOW()),
    -> (5, 'Sherry', 'rabbit', 'hippo421', 30, NOW());
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/e0cc56e3-95e0-4f36-a601-ed1b7b53f5bd)


● SELECT all rows from the member table.
```
SELECT * FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/f41ab32e-5a40-4396-81e4-0dce37d0b8e0)


● SELECT all rows from the member table, in descending order of time.
```
SELECT * FROM member ORDER BY time DESC;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/7b16fbab-2a8e-45b6-a2f7-1f93da3bbb18)


● SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/57619fdf-95d4-457b-9ff4-2fb11687d099)

● SELECT rows where username equals to test.
```
SELECT * FROM member WHERE username = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/fa2c4b1c-0f0f-4afa-95e3-cded8571a6ba)


● SELECT rows where name includes the es keyword.
```
SELECT * FROM member WHERE name LIKE '%es%';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/eb352c12-0493-4747-bda8-929de854a742)

● SELECT rows where both username and password equal to test.
```
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/80d5de1f-4de9-44b4-8d69-b22c3bc12d48)


● UPDATE data in name column to test2 where username equals to test.
```
UPDATE member SET name = 'test2' WHERE username = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/8276e873-63d0-419f-aa91-5288d73e8b1a)


## Task 4: SQL Aggregation Functions

● SELECT how many rows from the member table.
```
SELECT COUNT(*) FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/e1c46322-1b0b-4afd-86ac-09b7fbcc3aaa)

● SELECT the sum of follower_count of all the rows from the member table.
```
SELECT SUM(follower_count) FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/b3a71649-3d1f-4fa8-ac33-7641741b1f40)


● SELECT the average of follower_count of all the rows from the member table.
```
SELECT AVG(follower_count) FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/c3f370ca-01df-40eb-806e-ad0ad8dd4db7)


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
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/461b29d0-5f1f-40fe-bf3d-c0773133984e)

