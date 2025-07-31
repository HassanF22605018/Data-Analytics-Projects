DROP TABLE IF EXISTS CustomerData;

CREATE TABLE CustomerData (
    Unique_Customer_ID VARCHAR(100),
    Age INT,
    Gender VARCHAR(200),
    Location VARCHAR(200),
    Income INT
);

DROP TABLE IF EXISTS PurchaseHistory;
CREATE TABLE PurchaseHistory (
    Unique_Customer_ID VARCHAR(100),
    Date DATE,
    Category VARCHAR(200),
    Price DECIMAL(10, 2)
);

DROP TABLE IF EXISTS BrowsingHistory;
CREATE TABLE BrowsingHistory (
    Unique_Customer_ID VARCHAR(10),
    Category VARCHAR(50),
    BrowsingDateTime DATETIME,
    TimeOnSite_Minutes TIME
);
DROP TABLE IF EXISTS ProductReviews;

CREATE TABLE ProductReviews (
    Unique_Customer_ID VARCHAR(10),
    Reviews TEXT,
    Rating DECIMAL(2, 1)
);

GO