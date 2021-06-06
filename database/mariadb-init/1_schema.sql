USE dbfinal;

CREATE TABLE bazaar_catalogue (
    product_id  VARCHAR(50)     NOT NULL,
    name        VARCHAR(100),
    enabled     BOOLEAN,
    PRIMARY KEY (product_id)
);

CREATE TABLE bazaar_trade_history (
    product_id  VARCHAR(50)     NOT NULL,
    fetched_on  DATETIME        NOT NULL,
    buy_price   DECIMAL(18, 1),
    buy_volume  BIGINT,
    sell_price  DECIMAL(18, 1),
    sell_volume BIGINT,
    PRIMARY KEY (product_id, fetched_on),
    FOREIGN KEY (product_id) REFERENCES bazaar_catalogue(product_id)
);

CREATE TABLE bazaar_sell_summary (
    product_id  VARCHAR(50)     NOT NULL,
    fetched_on  DATETIME        NOT NULL,
    order_index TINYINT         NOT NULL,
    price       DECIMAL(18, 1),
    volume      BIGINT,
    order_count BIGINT,
    PRIMARY KEY (product_id, fetched_on, order_index),
    FOREIGN KEY (product_id) REFERENCES bazaar_catalogue(product_id)
);

CREATE TABLE bazaar_buy_summary (
    product_id  VARCHAR(50)     NOT NULL,
    fetched_on  DATETIME        NOT NULL,
    order_index TINYINT         NOT NULL,
    price       DECIMAL(18, 1),
    volume      BIGINT,
    order_count BIGINT,
    PRIMARY KEY (product_id, fetched_on, order_index),
    FOREIGN KEY (product_id) REFERENCES bazaar_catalogue(product_id)
);
