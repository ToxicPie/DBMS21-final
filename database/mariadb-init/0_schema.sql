-- CREATE DATABASE dbfinal;
-- USE dbfinal;

-- CREATE TABLE bazaar_catalogue (
--     product_id  VARCHAR(50) NOT NULL,
--     name        VARCHAR(100),
--     PRIMARY KEY (product_id)
-- );

CREATE TABLE bazaar_sell_summary (
    product_id VARCHAR(50) NOT NULL,
    summary_index BIGINT NOT NULL,
    fetched_on DATETIME NOT NULL,
    amount BIGINT,
    price_per_unit FLOAT,
    orders BIGINT,
    PRIMARY KEY (product_id, summary_index, fetched_on)
);

load data local infile '/file/bazaar_sell_summary.csv'
into table bazaar_sell_summary
fields terminated by ','
lines terminated by '\n';

create table bazaar_buy_summary (
    product_id VARCHAR(50) NOT NULL,
    summary_index BIGINT NOT NULL,
    fetched_on DATETIME NOT NULL,
    amount BIGINT,
    price_per_unit BIGINT,
    orders BIGINT,
    PRIMARY KEY (product_id, summary_index, fetched_on)
);

load data local infile '/file/bazaar_buy_summary.csv'
into table bazaar_buy_summary
fields terminated by ','
lines terminated by '\n';
--
CREATE TABLE bazaar_trade_history (
    product_id  VARCHAR(50) NOT NULL,
    fetched_on  DATETIME NOT NULL,
    buy_price   FLOAT,
    buy_volume  BIGINT,
    sell_price  FLOAT,
    sell_volume BIGINT,
    PRIMARY KEY (product_id, fetched_on)
);


load data local infile '/file/bazaar_trade_history.csv'
into table bazaar_trade_history
fields terminated by ','
lines terminated by '\n';
