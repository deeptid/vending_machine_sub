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
  `price` int,
  `seller` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_name` (`product_name`)
);

CREATE TABLE `purchase` (
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` int NOT NULL,
  `quantity` int,
  `buyer` varchar(256) NOT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `deposit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(256) NOT NULL,
  `amount` int,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
);

ALTER TABLE `product` ADD CONSTRAINT `product_seller_fkey` FOREIGN KEY (`seller`) REFERENCES `user`(`username`);

ALTER TABLE `purchase` ADD CONSTRAINT `purchase_product_fkey` FOREIGN KEY (`product_id`) REFERENCES `product`(`id`);

ALTER TABLE `purchase` ADD CONSTRAINT `purchase_buyer_fkey` FOREIGN KEY (`buyer`) REFERENCES `user`(`username`);