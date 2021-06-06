USE dbfinal;

LOAD DATA INFILE 'csv/bazaar_catalogue.csv'
INTO TABLE bazaar_catalogue
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'csv/bazaar_trade_history.csv'
INTO TABLE bazaar_trade_history
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'csv/bazaar_sell_summary.csv'
INTO TABLE bazaar_sell_summary
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE 'csv/bazaar_buy_summary.csv'
INTO TABLE bazaar_buy_summary
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';
