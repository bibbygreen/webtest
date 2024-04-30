##Task 2: Create database and table in your MySQL server

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
    -> (2, 'Lin', 'lion', '123qwe', 0, NOW()),
    -> (3, 'Jocelyn', 'cat', 'ewq321', 0, NOW()),
    -> (4, 'Belle', 'dog', 'rte321', 0, NOW()),
    -> (5, 'Sherry', 'rabbit', 'hippo421', 0, NOW());
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/7a576178-096f-40d4-86ec-814365d3b657)

● SELECT all rows from the member table.
```
SELECT * FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/583fe1c5-2748-4ae5-84f1-88fd5a600994)

● SELECT all rows from the member table, in descending order of time.
```
SELECT * FROM member ORDER BY time DESC;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/d97e2111-33d0-4459-b621-ec87644f0117)

● SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/57a86fba-876a-4977-a5ad-af6369a018ee)

● SELECT rows where username equals to test.
```
SELECT * FROM member WHERE username = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/baa60e16-3310-445b-9766-d9253ada9d89)


● SELECT rows where name includes the es keyword.
```
SELECT * FROM member WHERE name LIKE '%es%';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/ab3a0e00-c4cc-4b88-a7ac-1821b490521a)

● SELECT rows where both username and password equal to test.
```
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/7e93e292-dfe1-478e-81bc-c7926c4d05fd)

● UPDATE data in name column to test2 where username equals to test.
```
UPDATE member SET name = 'test2' WHERE username = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/b633f2dc-72ee-4f16-a89a-cab7955beda8)

##Task 4: SQL Aggregation Functions

● SELECT how many rows from the member table.
```
SELECT COUNT(*) FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/e1c46322-1b0b-4afd-86ac-09b7fbcc3aaa)

● SELECT the sum of follower_count of all the rows from the member table.
```
SELECT SUM(follower_count) FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/4651ed1d-cd5f-48e5-bfbb-cd1d135a2f19)

● SELECT the average of follower_count of all the rows from the member table.
```
SELECT AVG(follower_count) FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/9a60684c-1b58-4dde-9646-6f1cf42449e6)

● SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table.
