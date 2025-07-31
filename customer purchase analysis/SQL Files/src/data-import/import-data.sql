BULK INSERT CustomerData
FROM 'D:\Study\Projects\Data Analytics Projects\customer purchase analysis\Customer_Data.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    CODEPAGE = '65001',
    DATAFILETYPE = 'char',
    TABLOCK
);

BULK INSERT PurchaseHistory
FROM 'D:\Study\Projects\Data Analytics Projects\customer purchase analysis\Cleaned_Purchase_History.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    CODEPAGE = '65001',
    DATAFILETYPE = 'char',
    TABLOCK,
    ERRORFILE = 'D:\Study\Projects\Data Analytics Projects\customer purchase analysis\BulkError_PurchaseHistory.txt',
    MAXERRORS = 100
);



BULK INSERT BrowsingHistory
FROM 'D:\Study\Projects\Data Analytics Projects\customer purchase analysis\Cleaned_Browsing_History.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    CODEPAGE = '65001',
    DATAFILETYPE = 'char',
    TABLOCK,
    ERRORFILE = 'D:\Study\Projects\Data Analytics Projects\customer purchase analysis\BulkError_PurchaseHistory.txt',
    MAXERRORS = 100
);

BULK INSERT ProductReviews
FROM 'D:\Study\Projects\Data Analytics Projects\customer purchase analysis\Cleaned_Product_Reviews.csv'
WITH (
    FIRSTROW = 2,
    FIELDTERMINATOR = ',',
    CODEPAGE = '65001',
    DATAFILETYPE = 'char',
    TABLOCK,
    ERRORFILE = 'D:\Study\Projects\Data Analytics Projects\customer purchase analysis\BulkError_PurchaseHistory.txt',
    MAXERRORS = 100
);
