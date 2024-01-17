use frostlink;
#drop database frostlink;

CREATE TABLE frostlink.values (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	handshake INT NOT NULL, 
	message VARCHAR(45), 
	capacity INT NOT NULL, 
    temp1 FLOAT(7, 4) NOT NULL, 
    temp2 FLOAT(7, 4) NOT NULL, 
    temp3 FLOAT(7, 4) NOT NULL, 
    temp4 FLOAT(7, 4) NOT NULL, 
	active_alarm_count INT NOT NULL
    );

select * from frostlink.values;