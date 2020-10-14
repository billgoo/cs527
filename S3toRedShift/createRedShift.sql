CREATE TABLE aisles (
	aisle_id INT NOT NULL, aisle VARCHAR(256) NOT NULL,
	PRIMARY KEY (aisle_id)
);
CREATE TABLE departments (
	department_id INT NOT NULL,
	department VARCHAR (256) NOT NULL,
	PRIMARY KEY (department_id)
);
CREATE TABLE orders (
	order_id INT NOT NULL,
	user_id INT NOT NULL,
    order_number INT NOT NULL,
    order_dow INT NOT NULL,
    order_hour_of_day INT NOT NULL,
    days_since_prior_order INT NOT NULL,
    PRIMARY KEY (order_id)
);
CREATE TABLE products (
	product_id INT NOT NULL,
	product_name VARCHAR (256) NOT NULL,
	aisle_id INT NOT NULL,
	department_id INT NOT NULL,
	PRIMARY KEY (product_id),
	CONSTRAINT pd_aidfk_1 FOREIGN KEY (aisle_id) REFERENCES aisles(aisle_id),
	CONSTRAINT pd_didfk_1 FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
CREATE TABLE order_products (
	order_id INT NOT NULL,
	product_id INT NOT NULL,
	add_to_cart_order INT NOT NULL,
	reordered INT NOT NULL,
	PRIMARY KEY ( product_id, order_id ),
	CONSTRAINT opd_pidfk_1 FOREIGN KEY (product_id) REFERENCES products(product_id),
	CONSTRAINT opd_oidfk_1 FOREIGN KEY (order_id) REFERENCES orders(order_id)
);