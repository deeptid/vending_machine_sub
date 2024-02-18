CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(256) NOT NULL,
  `role` varchar(256) NOT NULL,
  `password` char(60) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
);

CREATE TABLE `product` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_name` varchar(256) NOT NULL,
  `price` int NOT NULL,
  `seller` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
);

CREATE TABLE `purchase` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `amount` int NOT NULL,
  `buyer` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `deposit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` int NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`id`)
);

ALTER TABLE `product` ADD CONSTRAINT `product_seller_fkey` FOREIGN KEY (`seller`) REFERENCES `user`(`username`);

ALTER TABLE `purchase` ADD CONSTRAINT `purchase_product_fkey` FOREIGN KEY (`product_id`) REFERENCES `product`(`id`);

ALTER TABLE `purchase` ADD CONSTRAINT `purchase_buyer_fkey` FOREIGN KEY (`buyer`) REFERENCES `user`(`username`);