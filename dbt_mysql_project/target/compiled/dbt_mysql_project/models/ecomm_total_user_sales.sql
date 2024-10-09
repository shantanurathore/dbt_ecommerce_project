WITH user_totals AS (
    SELECT
        user_id,
        product_category,
        SUM(purchase_amount) AS total_sales
    FROM `ecomm_transactions_db`.`ecomm_transactions`
    GROUP BY 1,2
),
sales_by_category AS (
SELECT
    user_id,
    SUM(CASE WHEN product_category = 'App' THEN total_sales ELSE 0 END)AS app_sales,
    SUM(CASE WHEN product_category = 'Game' THEN total_sales ELSE 0 END) AS game_sales,
    SUM(CASE WHEN product_category = 'In-app Purchases' THEN total_sales ELSE 0 END) AS inapp_sales
FROM user_totals
GROUP BY 1
)
SELECT
    user_id,
    app_sales AS app_sales,
    game_sales AS game_sales,
    inapp_sales AS inapp_sales,
    app_sales + game_sales + inapp_sales AS total_sales
FROM sales_by_category