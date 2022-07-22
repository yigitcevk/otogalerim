import psycopg2

conn = psycopg2.connect(database = "otogaleri", user = "postgres", password = "enes1324", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

cur.execute('''create table if not EXISTS BRAND (
    brand_id varchar(30) NOT NULL,
    brand_name varchar(30),
    primary key(brand_id)
);''')

cur.execute('''create table if not EXISTS MODEL(
    model_id varchar(30) NOT NULL,
    model_name varchar(30),
    brand_id varchar(30) NOT NULL,
    primary key(model_id),
    foreign key(brand_id) references BRAND(brand_id)
);''')

cur.execute('''insert into brand
values ('1', 'Alfa Romeo');
insert into brand
values ('2', 'Audi');
insert into brand
values ('3', 'BMW');
insert into brand
values ('4', 'Citroen');
insert into brand
values ('5', 'Dacia');
insert into brand
values ('6', 'Fiat');
insert into brand
values ('7', 'Ford');
insert into brand
values ('8', 'Honda');
insert into brand
values ('9', 'Hyundai');
insert into brand
values ('10', 'Jeep');
insert into brand
values ('11', 'Kia');
insert into brand
values ('12', 'Mercedes-Benz');
insert into brand
values ('13', 'Nissan');
insert into brand
values ('14', 'Opel');
insert into brand
values ('15', 'Peugeot');
insert into brand
values ('16', 'Renault');
insert into brand
values ('17', 'Seat');
insert into brand
values ('18', 'Skoda');
insert into brand
values ('19', 'Subaru');
insert into brand
values ('20', 'Toyota');
insert into brand
values ('21', 'Volkswagen');
insert into brand
values ('22', 'Volvo');

insert into model
values('1', 'Giulietta', '1');
insert into model
values('2', 'A1', '2');
insert into model
values('3', 'A3', '2');
insert into model
values('4', 'A4', '2');
insert into model
values('5', 'A6', '2');
insert into model
values('6', 'Q2', '2');
insert into model
values('7', '1 Serisi', '3');
insert into model
values('8', '2 Serisi', '3');
insert into model
values('9', '3 Serisi', '3');
insert into model
values('10', '4 Serisi', '3');
insert into model
values('11', 'X1', '3');
insert into model
values('12', 'C-Elysee', '4');
insert into model
values('13', 'C3', '4');
insert into model
values('14', 'C3 AirCross', '4');
insert into model
values('15', 'C4', '4');
insert into model
values('16', 'C4 Cactus', '4');
insert into model
values('17', 'Duster', '5');
insert into model
values('18', 'Lodgy', '5');
insert into model
values('19', 'Sandero', '5');
insert into model
values('20', 'Sandro Stepway', '5');
insert into model
values('21', '500', '6');
insert into model
values('22', '500C', '6');
insert into model
values('23', '500L', '6');
insert into model
values('24', 'Egea', '6');
insert into model
values('25', 'Linea', '6');
insert into model
values('26', 'Punto', '6');
insert into model
values('27', 'Focus', '7');
insert into model
values('28', 'EcoSport', '7');
insert into model
values('29', 'Kuga', '7');
insert into model
values('30', 'Mondeo', '7');
insert into model
values('31', 'Puma', '7');
insert into model
values('32', 'CR-V', '8');
insert into model
values('33', 'City', '8');
insert into model
values('34', 'Civic', '8');
insert into model
values('35', 'Elantra', '9');
insert into model
values('36', 'i10', '9');
insert into model
values('37', 'i20', '9');
insert into model
values('38', 'i20 Active', '9');
insert into model
values('39', 'i30', '9');
insert into model
values('40', 'Tucson', '9');
insert into model
values('41', 'Renegade', '10');
insert into model
values('42', 'Rio', '11');
insert into model
values('43', 'Ceed', '11');
insert into model
values('44', 'Sportage', '11');
insert into model
values('45', 'Stonic', '11');
insert into model
values('46', 'A', '12');
insert into model
values('47', 'C', '12');
insert into model
values('48', 'E', '12');
insert into model
values('49', 'Juke', '13');
insert into model
values('50', 'Micra', '13');
insert into model
values('51', 'Qashqai', '13');
insert into model
values('52', 'Astra', '14');
insert into model
values('53', 'Corsa', '14');
insert into model
values('54', 'Crossland', '14');
insert into model
values('55', 'Crossland X', '14');
insert into model
values('56', 'Insignia', '14');
insert into model
values('57', '2008', '15');
insert into model
values('58', '208', '15');
insert into model
values('59', '3008', '15');
insert into model
values('60', '301', '15');
insert into model
values('61', 'Taliant', '16');
insert into model
values('62', 'Symbol', '16');
insert into model
values('63', 'Megane', '16');
insert into model
values('64', 'Kadjar', '16');
insert into model
values('65', 'Fluence', '16');
insert into model
values('66', 'Clio', '16');
insert into model
values('67', 'Captur', '16');
insert into model
values('68', 'Arona', '17');
insert into model
values('69', 'Ateca', '17');
insert into model
values('70', 'Ibiza', '17');
insert into model
values('71', 'Leon', '17');
insert into model
values('72', 'Fabia', '18');
insert into model
values('73', 'Kamiq', '18');
insert into model
values('74', 'Karoq', '18');
insert into model
values('75', 'Octavia', '18');
insert into model
values('76', 'Scala', '18');
insert into model
values('77', 'Rapid', '18');
insert into model
values('78', 'Kodiaq', '18');
insert into model
values('79', 'XV', '19');
insert into model
values('80', 'Corolla', '20');
insert into model
values('81', 'Yaris', '20');
insert into model
values('82', 'Beetle', '21');
insert into model
values('83', 'CC', '21');
insert into model
values('84', 'Golf', '21');
insert into model
values('85', 'Jetta', '21');
insert into model
values('86', 'Passat', '21');
insert into model
values('87', 'Passat Variant', '21');
insert into model
values('88', 'Polo', '21');
insert into model
values('89', 'T-Roc', '21');
insert into model
values('90', 'Tiguan', '21');
insert into model
values('91', 'S60', '22');''')

conn.commit()
conn.close()