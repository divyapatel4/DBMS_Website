
SELECT ticket_id FROM ticket WHERE amount = (SELECT MAX(amount) FROM ticket);

SELECT name, passenger_id FROM passengerdetails WHERE gender = 'female' ORDER BY passenger_id DESC;

SELECT ticket_id from ticket WHERE amount in ( SELECT amount FROM ticket ORDER BY amount DESC LIMIT 2);

SELECT COUNT(distinct(passenger_id)) FROM pantry WHERE payment_mode = 'cash'; 

SELECT passenger_id ,gender from passengerdetails NATURAl JOIN ticket WHERE amount > (SELECT AVG(amount) FROM ticket); 

SELECT station_id, train_name FROM train JOIN station ON station.train_id = train.train_id;

SELECT COUNT(payment_mode), payment_mode FROM pantry GROUP BY payment_mode;

SELECT DISTINCT(tc_id ) FROM ticketcollector WHERE age < (SELECT AVG(age) FROM ticketcollector);

SELECT train_name FROM train JOIN station ON station.train_id = train.train_id WHERE hault = 'Yes' ORDER BY station.station_id;

CREATE OR REPLACE VIEW mx as SELECT MAX(amount) from ticket;

CREATE OR REPLACE VIEW station_details as (SELECT * from station);
INSERT INTO station_details VALUES('101','Z5T 3C4','08:45:00','106','Yes');
SELECT * FROM station_details WHERE station_id = 101;

CREATE OR REPLACE VIEW rate_details as (SELECT AVG(rate) from pantry);
SELECT *  FROM rate_details;
INSERT INTO pantry VALUES('9999', 'food1', '100', 'Yes', 'Online', '99');
INSERT INTO pantry VALUES('9998', 'food2', '100', 'Yes', 'Online', '102');
INSERT INTO pantry VALUES('9997', 'food3', '100', 'Yes', 'Online', '101');
INSERT INTO pantry VALUES('9996', 'food4', '100', 'Yes', 'Online', '100');
SELECT *  FROM rate_details;

CREATE OR REPLACE VIEW train_stat_detail as (SELECT station_id, train_name FROM train JOIN station ON station.train_id = train.train_id);
SELECT * FROM train_stat_detail;

CREATE OR REPLACE VIEW pass_food_detail as (SELECT * FROM pantry NATURAl JOIN passengerdetails WHERE payment_mode = 'Online' or payment_mode = 'online');
SELECT * FROM pass_food_detail;

SELECT name, ticket_id, age FROM passengerdetails JOIN train ON passengerdetails.train_id = train.train_id WHERE train.seats_available > 10 ORDER BY ticket_id DESC;
