CREATE DATABASE dbfinal;
USE dbfinal;

-- CREATE TABLE bazaar_catalogue (
--     product_id  VARCHAR(50) NOT NULL,
--     name        VARCHAR(100),
--     PRIMARY KEY (product_id)
-- );

create table bazaar_sell_summary (
    product_id varchar(50) not null,
    summary_index bigint,
    amount bigint,
    pricePerUnit bigint,
    order bigint,
    primary key (product_id, summary_index)
)

load data local infile '/home/august/github/DBMS21-final/file/bazaar_sell_summary.csv'
into table bazaar_trade_history
fields terminated by ','
lines terminated by '\n';

CREATE TABLE bazaar_trade_history (
    product_id  VARCHAR(50) NOT NULL,
    fetched_on  DATETIME NOT NULL,
    buy_price   DECIMAL(12, 1),
    buy_volume  BIGINT,
    sell_price  DECIMAL(12, 1),
    sell_volume BIGINT,
    PRIMARY KEY (product_id, fetched_on)
);


load data local infile '/home/august/github/DBMS21-final/file/bazaar_trade_history.csv'
into table bazaar_trade_history
fields terminated by ','
lines terminated by '\n';
