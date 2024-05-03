## Task 2: Create database and table in your MySQL server

> 2.1 Create a new database named website.
```sql
CREATE DATABASE website;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/0148d262-df96-469b-bf4a-c986c05ca908)


> 2.2 Create a new table named member, in the website database

```sql
CREATE TABLE member (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    follower_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/467b6405-245a-47a8-9dbb-aa6cf00a1f86)


## Task 3: SQL CRUD

> 3.1 INSERT a new row to the member table where name, username and password mustbe set to test. INSERT additional 4 rows with arbitrary data.
```sql
INSERT INTO member (name, username, password) 
VALUES ('test', 'test', 'test');
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/fed7feb1-9ddb-4051-81f7-da8005d29e7f)


```sql
INSERT INTO member (name, username, password, follower_count)
VALUES
  ('Charles', 'lion', '123qwe', 10),
  ('Jocelyn', 'cat', 'ewq321', 15),
  ('Belle', 'dog', 'rte321', 40),
  ('Sherry', 'rabbit', 'hippo421', 30);
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/013b6987-dbcd-4fab-b7e0-38f2ef6566a7)


> 3.2 SELECT all rows from the member table.
```sql
SELECT * FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/eccb539a-8e51-45b4-8572-4ae61c87a00a)


> 3.3 SELECT all rows from the member table, in descending order of time.
```sql
SELECT * FROM member ORDER BY time DESC;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/e7ac2a66-2f18-4d35-aadb-1f512aba35be)


> 3.4 SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
```sql
SELECT * FROM member ORDER BY time DESC LIMIT 3 OFFSET 1;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/9a0f9475-bb73-46ea-950a-648b9bebeea6)


> 3.5 SELECT rows where username equals to test.
```sql
SELECT * FROM member WHERE username = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/1fe89ef3-dc0c-415b-8306-fd30c730c904)


> 3.6 SELECT rows where name includes the es keyword.
```sql
SELECT * FROM member WHERE name LIKE '%es%';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/31c6f982-0c78-4c24-93cf-4333394f5630)


> 3.7 SELECT rows where both username and password equal to test.
```sql
SELECT * FROM member WHERE username = 'test' AND password = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/7b1c6570-2d45-4dd4-830b-545859b3218f)


> 3.8 UPDATE data in name column to test2 where username equals to test.
```sql
UPDATE member SET name = 'test2' WHERE username = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/eaa2f481-b196-4f07-a5f3-cf80a9ffa79e)


## Task 4: SQL Aggregation Functions

> 4.1 SELECT how many rows from the member table.
```sql
SELECT COUNT(*) FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/ff4fcad3-7201-421f-881f-8c5f6d978285)


> 4.2 SELECT the sum of follower_count of all the rows from the member table.
```sql
SELECT SUM(follower_count) FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/0b064547-426a-47d8-ac55-84b0a717b853)


> 4.3 SELECT the average of follower_count of all the rows from the member table.
```sql
SELECT AVG(follower_count) FROM member;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/a99dd5e5-13a9-4427-a542-c21247016c33)


> 4.4 SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
```sql
SELECT AVG(follower_count) 
FROM (
    SELECT follower_count 
    FROM member 
    ORDER BY follower_count DESC 
    LIMIT 2
) AS top_two;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/a48311f3-d30d-45f6-ad2e-608f7f426b90)


## Task 5: SQL JOIN

> 5.1 Create a new table named message, in the website database.
```sql
CREATE TABLE message (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    member_id BIGINT NOT NULL, FOREIGN KEY (member_id) REFERENCES member(id),
    content VARCHAR(255) NOT NULL,
    like_count INT UNSIGNED NOT NULL DEFAULT 0,
    time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/e73df384-564e-403f-a402-6cff716a88e1)


> 5.2 SELECT all messages, including sender names. We have to JOIN the member table to get that.
```sql
SELECT message.id, message.content, message.like_count, message.time,
       member.id AS sender_id
FROM message
JOIN member ON message.member_id = member.id;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/898b4d5a-6cab-44d0-9485-7e5cb9993fd1)


> 5.3 SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
```sql
SELECT message.id, message.content, message.like_count, message.time, 
       member.name AS sender_name
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/62d2bbbe-21ae-4902-a0cf-ed792663f9ba)


> 5.4 Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
```sql
SELECT AVG(message.like_count) AS average_like_count
FROM message
JOIN member ON message.member_id = member.id
WHERE member.username = 'test';
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/d417bf82-270c-408c-8cc0-66b76823be87)


> 5.5 Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.
```sql
SELECT member.username AS sender_username, AVG(message.like_count) AS average_like_count
FROM message
JOIN member ON message.member_id = member.id
GROUP BY member.username;
```
![image](https://github.com/bibbygreen/wehelp_5th/assets/54356660/9ab0b5bf-4930-4d27-a5f9-8d52d278b10e)


> mysqldump — A Database Backup Program
```powershell
mysqldump -u [username] -p [database_name] > [output_file.sql]
```

Use the `--result-file` option, which creates the output in ASCII format
```powershell
mysqldump [options] --result-file=dump.sql
```

直接指定mysqldump完整路徑
```powershell
"C:\Program Files\MySQL\MySQL Server 8.3\bin\mysqldump" -u root -p website > data.sql
```