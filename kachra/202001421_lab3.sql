CREATE OR REPLACE function "rail_db"."ticket_amt_gt_2000"() 
RETURNS TABLE(a integer, b integer, c character(30)) 
LANGUAGE 'plpgsql' 
AS $BODY$
BEGIN 
RETURN QUERY EXECUTE format ('SELECT ticket_id, amount, status FROM "rail_db".ticket where amount > 2000'); 
END;
$BODY$

SELECT * from ticket;

select "rail_db"."ticket_amt_gt_2000"();

ALTER TABLE ticket ADD total_amount FLOAT;
SELECT * from ticket;

CREATE OR REPLACE function "rail_db"."calc_tot_amt"() 
returns integer
LANGUAGE 'plpgsql' 
AS $BODY$
BEGIN 
UPDATE "rail_db".ticket set total_amount = amount + 0.12*amount;
return 0;
END;
$BODY$

select  "rail_db"."calc_tot_amt"();
SELECT * FROM ticket;



CREATE OR REPLACE TRIGGER pantry_check_item_id_trigger
  BEFORE INSERT
  ON pantry
  EXECUTE PROCEDURE pantry_check_item_id();
  
 SELECT * FROM pantry;
select c = count(*) FROM pantry WHERE item_id = 1;
RAISE NOTICE '%c', c;
 INSERT INTO pantry VALUES('1', 'samosa', '252' ,'No', 'online', '99');