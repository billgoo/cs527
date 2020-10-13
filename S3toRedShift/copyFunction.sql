copy aisles from 's3://instacartredshiftcs527/load/aisles' 
credentials 'aws_access_key_id=AKIA3VE67DUA3KYOGRM7;aws_secret_access_key=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' 
csv;
copy departments from 's3://instacartredshiftcs527/load/departments' 
credentials 'aws_access_key_id=AKIA3VE67DUA3KYOGRM7;aws_secret_access_key=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' 
csv;
copy orders from 's3://instacartredshiftcs527/load/orders' 
credentials 'aws_access_key_id=AKIA3VE67DUA3KYOGRM7;aws_secret_access_key=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' 
csv;
copy products from 's3://instacartredshiftcs527/load/products' 
credentials 'aws_access_key_id=AKIA3VE67DUA3KYOGRM7;aws_secret_access_key=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' 
csv;
copy order_products from 's3://instacartredshiftcs527/load/order_products' 
credentials 'aws_access_key_id=AKIA3VE67DUA3KYOGRM7;aws_secret_access_key=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' 
csv;