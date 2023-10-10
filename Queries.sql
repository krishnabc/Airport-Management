create database airport; 
use airport; 
-- --------------------------------------------------------------------------------------------------------------------------------------------------------
-- FLIGHT TABLES
SHOW TABLES;
desc userdetails;
desc users;

create table FLIGHT_DETAILS
(
FLIGHT_ID varchar(20) NOT NULL PRIMARY KEY,
DEPARTURE_TIME TIME NOT NULL,
ARRIVAL_TIME TIME NOT NULL,
PRICE INT NOT NULL,
`DATE` DATE NOT NULL,
AIRLINE VARCHAR(20)
);
-- select airport_name from source_dest where airport_id = "nag";
-- desc FLIGHT_DETAILS;
-- desc FLIGHT_ids;
-- SELECT * FROM FLIGHT_DETAILS;
-- select * from FLIGHT_ids;
-- select * from source_dest;
select * from userdetails;
select * from users;
-- truncate users;
-- truncate userdetails;
INSERT INTO FLIGHT_DETAILS(FLIGHT_ID,DEPARTURE_TIME,ARRIVAL_TIME,PRICE,`DATE`,AIRLINE) 
VALUES('6E5234','10:15','11:40',3750,'2023-06-12','INDIGO'),
('6E6475','13:15','14:35',4250,'2023-06-08','AIRINDIA'),
('6E7638','10:00','11:15',6550,'2023-06-9','JET_AIRWAYS'),
('6E7975','2:15','3:25',4250,'2023-06-5','INDIGO'),
('6E8845','12:15','14:40',5250,'2023-06-13','AIRINDIA'),
('6E6984','9:15','11:40',6550,'2023-06-15','JET_AIRWAYS'),
('6E7529','15:15','16:40',4550,'2023-06-11','INDIGO');

ALTER TABLE users AUTO_INCREMENT=100;

-- update flight_details set AIRLINE = 'INDIGO';
-- select md5(password) from users where username = "hrishi@gmail.com";
-- select md5("hrishi123");
CREATE TABLE FLIGHT_IDS
(	
	FLIGHT_ID VARCHAR(15),
    SOURCE_ID VARCHAR(10),
    DESTINATION_ID VARCHAR(10),
    FOREIGN KEY (FLIGHT_ID) REFERENCES FLIGHT_DETAILS(FLIGHT_ID),
	FOREIGN KEY (SOURCE_ID) REFERENCES SOURCE_DEST(AIRPORT_ID),
	FOREIGN KEY (DESTINATION_ID) REFERENCES SOURCE_DEST(AIRPORT_ID)
);

SELECT * FROM FLIGHT_IDS;

INSERT INTO FLIGHT_IDS(FLIGHT_ID,SOURCE_ID,DESTINATION_ID)
VALUES('6E5234','BOM','NAG'),
('6E6475','JAI','BLR'),
('6E6984','DEL','BLR'),
('6E7529','NAG','DEL'),
('6E7638','NAG','PNQ'),
('6E7975','NAG','BLR'),
('6E8845','DEL','MAA');


create table source_dest 
(
airport_id varchar(20) primary KEY, 
airport_name varchar(100), 
city varchar(25)
);
 
 select * from source_dest; 
 
insert into source_dest (airport_id, airport_name , city) values 
('DEL','Indira Gandhi International Airport','delhi'),
('BOM','Chhatrapati Shivaji International Airport','Mumbai'),
('MAA','Chennai International Airport','Chennai'),				
('BLR','Kempegowda International Airport','Bangalore'),				
('COK','Cochin International Airport','Kochi'),				
('HYD','Rajiv Gandhi International Airport','Hyderabad'),				
('TRV','Trivandrum International Airport','Thiruvananthapuram'),				
('CCU','Netaji Subhash Chandra Bose International Airport','Kolkata'),				
('CCJ','Calicut International Airport','Calicut'),			
('GOI','Dabolim Airport','Vasco da Gama'),				
('ATQ','Sri Guru Ram Dass Jee International Airport','Amritsar'),				
('AMD','Sardar Vallabhbhai Patel International Airport','Ahmedabad'),				
('JAI','Jaipur International Airport','Jaipur'),				
('LKO','Chaudhary Charan Singh International Airport','Lucknow'),				
('CJB','Coimbatore International Airport','Coimbatore'),				
('TRZ','Tiruchirapally Civil Airport Airport','Tiruchirappally'),				
('PNQ','Pune Airport','Pune'),				
('IXB','Bagdogra Airport','Siliguri'),				
('GAU','Lokpriya Gopinath Bordoloi International Airport','Guwahati'),				
('IXM','Madurai Airport','Madurai'),				
('NAG','Dr. Babasaheb Ambedkar International Airport','Naqpur'),			
('IXC','Chandigarh Airport','Chandigarh'),			
('IXJ','Jammu Airport','Jammu'),				
('SXR','Sheikh ul Alam Airport','Srinagar'),				
('IXE','Mangalore International Airport','Mangalore'),				
('IXZ','Vir Savarkar International Airport','Port Blair'),				
('IDR','Devi Ahilyabai Holkar Airport','Indore'),				
('IXA','Agartala Airport','Agartala'),				
('PAT','Lok Nayak Jayaprakash Airport','Patna'),				
('IXR','Birsa Munda Airport','Ranchi');

-- ---------------------------------------------------------------------------------------------------
-- User Tables
set foreign_key_checks = 0; 
set foreign_key_checks = 1; 
create table `users` (
username varchar(50) primary key, 
`password` varchar(255),
`user_id` int(10),
FOREIGN KEY (user_id) REFERENCES userdetails(id));

create table `userdetails` (`id` int(10) primary key AUTO_INCREMENT, 
`name` varchar(50) not null, 
phone VARCHAR(10) unique key not null, 
`email` varchar(40) not null
); 

-- drop table userdetails;
-- drop table users;
------------------------

-- ---------------------------------------------------------------------

-- QUERIES

select fd.flight_id,fd.departure_time,fd.arrival_time,fd.price,fd.date,fd.airline from flight_details fd inner join 
flight_ids fid on fd.flight_id=fid.flight_id where
(fid.source_id="NAG" and fid.destination_id="BLR") and fd.date="";

-- FOR ALL DETAILS 
SELECT * FROM FLIGHT_DETAILS F1 INNER JOIN FLIGHT_IDS F2 ON F1.FLIGHT_ID=F2.FLIGHT_ID
INNER JOIN SOURCE_DEST S ON F2.SOURCE_ID=S.AIRPORT_ID
INNER JOIN SOURCE_DEST S1 ON F2.DESTINATION_ID=S1.AIRPORT_ID;

-- TO FETCH SPECIFIC DETAILS
SELECT * FROM FLIGHT_DETAILS F1 INNER JOIN FLIGHT_IDS F2 ON F1.FLIGHT_ID=F2.FLIGHT_ID
INNER JOIN SOURCE_DEST S ON F2.SOURCE_ID=S.AIRPORT_ID
INNER JOIN SOURCE_DEST S1 ON F2.DESTINATION_ID=S1.AIRPORT_ID WHERE F1.FLIGHT_ID= '??';

-- ------------------------------------------------------------------------

-- Stored Procedure Insert
DELIMITER $$
CREATE PROCEDURE Insert_Flight_Details(IN F_ID varchar(10),IN D_Time time,IN A_Time time,IN PRC VARCHAR(50),IN DATE_From date,IN AIRLINE_name VARCHAR(50),
IN S_ID VARCHAR(50),IN D_ID VARCHAR(50))
BEGIN
	IF NOT EXISTS (SELECT * FROM flight_details WHERE flight_id=f_id) THEN
		INSERT INTO FLIGHT_DETAILS(FLIGHT_ID,DEPARTURE_TIME,ARRIVAL_TIME,PRICE,`DATE`,AIRLINE) VALUES(f_id,D_TIME,A_TIME,PRC,DATE_From,AIRLINE_name);
		INSERT INTO FLIGHT_IDS (FLIGHT_ID,SOURCE_ID,DESTINATION_ID) VALUES (F_ID,S_ID,D_ID);
    ELSE
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT='Flight Details already exists';
	END IF;
END;
$$
DELIMITER ;
-- Stored Function Delete
DELIMITER $$
CREATE FUNCTION delete_flight_details(f_id VARCHAR(20))
RETURNS VARCHAR(50)
Deterministic
BEGIN
	IF EXISTS(SELECT * FROM flight_details WHERE flight_id=(SELECT flIGHT_ID FROM flight_ids WHERE flight_id=f_id)) THEN
		DELETE FROM Flight_ids WHERE flight_id=f_id;
		DELETE FROM Flight_details WHERE flight_id=f_id;
	RETURN "Flight Details Deleted Successfully";
	
    ELSE
	RETURN "WRONG FLIGHT DETAILS";
	END IF;
END
$$
DELIMITER ;
