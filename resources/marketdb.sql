PRAGMA foreign_keys = ON;

CREATE TABLE YEAR_TABLE (
    year_number INTEGER(4) PRIMARY KEY
);

CREATE TABLE MONTH_TABLE (
    id_month     INTEGER    PRIMARY KEY AUTOINCREMENT,
    month_number INTEGER(2) NOT NULL,
    year_number  INTEGER(4) NOT NULL REFERENCES YEAR_TABLE(year_number),
    UNIQUE(month_number, year_number)
);

CREATE TABLE SALE (
    id_sale      INTEGER       PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR (100) NOT NULL,
    value        NUMBER  (20)  NOT NULL,
    day          INTEGER (2)   NOT NULL,
    id_month     INTEGER       NOT NULL REFERENCES MONTH_TABLE(id_month)
);

CREATE TABLE PURCHASE (
    id_purchase  INTEGER       PRIMARY KEY AUTOINCREMENT,
    product_name VARCHAR (100) NOT NULL,
    value        NUMBER  (20)  NOT NULL,
    day          INTEGER (2)   NOT NULL,
    id_month     INTEGER       NOT NULL REFERENCES MONTH_TABLE(id_month)
);

CREATE UNIQUE INDEX id_month ON MONTH_TABLE (id_month);
CREATE UNIQUE INDEX id_sale ON SALE (id_sale);
CREATE UNIQUE INDEX id_purchase ON PURCHASE (id_purchase);