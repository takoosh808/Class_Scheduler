-- CREATE DATABASE courseapp;
-- CREATE USER admin WITH PASSWORD 'Cpts322';
-- GRANT ALL PRIVILEGES ON DATABASE courseapp TO admin;

-- CREATE TABLE Student (
--     id_number VARCHAR(8) PRIMARY KEY,
--     first_name VARCHAR(50),
--     last_name VARCHAR(50),
--     password VARCHAR(50)
-- );

-- CREATE TABLE Courses (
--     Courseid VARCHAR(8) PRIMARY KEY,
--     CourseName VARCHAR(10),
--     CourseTime VARCHAR(4),
--     CourseDate VARCHAR(3)
-- );

-- -- CREATE TABLE Prerequisites (
-- --     Studentid VARCHAR(8) REFERENCES Student(id_number),
-- --     Courseid VARCHAR(8) REFERENCES Courses(Courseid),
-- -- );

-- CREATE TABLE Cart(
--     cart_id SERIAL PRIMARY KEY,
--     student_id VARCHAR(8) REFERENCES Student(id_number),
--     time_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE CartItem(
--     item_id SERIAL PRIMARY KEY,
--     cart_id INTEGER REFERENCES Cart(cart_id),
--     course_id VARCHAR(8) REFERENCES Courses(Courseid),
--     quantity INTEGER DEFAULT 1
-- );

-- insert into StudentCourses (Studentid, Courseid) values ('49103962', '1000');

insert into Student (id_number, first_name, last_name, password) values ('00123456','Jawn','Bautista','GYAT1234');
insert into Student (id_number, first_name, last_name, password) values ('00140997', 'Arlen', 'Kreuzer', 'Vgzh5349');
insert into Student (id_number, first_name, last_name, password) values ('00157714', 'Abbot', 'Guilleton', 'zHF2457');
insert into Student (id_number, first_name, last_name, password) values ('00130075', 'Elladine', 'McCaw', 'mBlb7588');
insert into Student (id_number, first_name, last_name, password) values ('00168486', 'Linda', 'Beric', 'FhZCu1619');
insert into Student (id_number, first_name, last_name, password) values ('00152806', 'Milka', 'Gruby', 'Q9546');
insert into Student (id_number, first_name, last_name, password) values ('00150210', 'Katherina', 'Haresnaip', 'QBzeM4753');
insert into Student (id_number, first_name, last_name, password) values ('00185176', 'Fidelity', 'Calcut', 'nS4567');
insert into Student (id_number, first_name, last_name, password) values ('00109708', 'Florie', 'McMurthy', 'csCki0749');
insert into Student (id_number, first_name, last_name, password) values ('00191671', 'Obediah', 'Stannislawski', 'QRq2211');
insert into Student (id_number, first_name, last_name, password) values ('00115735', 'Rodrigo', 'Hebdon', 'DCyL6494');
insert into Student (id_number, first_name, last_name, password) values ('00137010', 'Hedvig', 'Giffen', 'CpxH4400');
insert into Student (id_number, first_name, last_name, password) values ('00106324', 'Pris', 'Palin', 'KD0957');
insert into Student (id_number, first_name, last_name, password) values ('00115957', 'Ulrick', 'Welberry', 'epakh8827');
insert into Student (id_number, first_name, last_name, password) values ('00195324', 'Vonnie', 'Sterley', 'SDDIH4292');
insert into Student (id_number, first_name, last_name, password) values ('00131210', 'Christine', 'Sheran', 'bHQHU6570');
insert into Student (id_number, first_name, last_name, password) values ('00125348', 'Darryl', 'Messenger', 'cUR3718');
insert into Student (id_number, first_name, last_name, password) values ('00177405', 'Donna', 'Ianittello', 'BZ1746');
insert into Student (id_number, first_name, last_name, password) values ('00122129', 'Devinne', 'Tesoe', 'm4206');
insert into Student (id_number, first_name, last_name, password) values ('00139270', 'Selle', 'Duckfield', 'wAZfw1306');
insert into Student (id_number, first_name, last_name, password) values ('00179431', 'Kattie', 'Durham', 'jHS9017');
insert into Student (id_number, first_name, last_name, password) values ('00193862', 'Kyrstin', 'Sinderson', 'dIH7923');
insert into Student (id_number, first_name, last_name, password) values ('00113627', 'Teri', 'Wadlow', 'O9266');
insert into Student (id_number, first_name, last_name, password) values ('00146815', 'Marline', 'Heibl', 'C6827');
insert into Student (id_number, first_name, last_name, password) values ('00109125', 'Terrie', 'Liddyard', 'iEHC8995');
insert into Student (id_number, first_name, last_name, password) values ('00161478', 'Aldwin', 'Pardy', 'lGhaH1855');
insert into Student (id_number, first_name, last_name, password) values ('00114508', 'Thibaud', 'Cromb', 'v4660');
insert into Student (id_number, first_name, last_name, password) values ('00193953', 'Inez', 'Lidington', 'JJY4322');
insert into Student (id_number, first_name, last_name, password) values ('00158572', 'Karee', 'Borrill', 'L0341');
insert into Student (id_number, first_name, last_name, password) values ('00188269', 'Jen', 'Burkin', 's5103');
insert into Student (id_number, first_name, last_name, password) values ('00174550', 'Garrard', 'Kopelman', 'FzcV2372');
insert into Student (id_number, first_name, last_name, password) values ('00181193', 'Ginger', 'Tribe', 'sTC7091');
insert into Student (id_number, first_name, last_name, password) values ('00189002', 'Blayne', 'Oxby', 'xWpH1605');
insert into Student (id_number, first_name, last_name, password) values ('00151231', 'Ellsworth', 'Corby', 'qjA9258');
insert into Student (id_number, first_name, last_name, password) values ('00120490', 'Sully', 'Osanne', 'Gv1119');
insert into Student (id_number, first_name, last_name, password) values ('00118027', 'Lew', 'Ivashkov', 'jwCL2828');
insert into Student (id_number, first_name, last_name, password) values ('00110095', 'Carri', 'Wraggs', 'UWyFa3304');
insert into Student (id_number, first_name, last_name, password) values ('00189905', 'Angelo', 'Calbert', 'rqmP7459');
insert into Student (id_number, first_name, last_name, password) values ('00107112', 'Shem', 'Lippi', 'xZPbI3687');
insert into Student (id_number, first_name, last_name, password) values ('00189205', 'Nydia', 'Laterza', 'c3847');
insert into Student (id_number, first_name, last_name, password) values ('00131018', 'Honoria', 'Burnep', 'vW2427');
insert into Student (id_number, first_name, last_name, password) values ('00192951', 'Nikkie', 'Sellen', 'jqxDJ4687');
insert into Student (id_number, first_name, last_name, password) values ('00127134', 'Brandais', 'Gyngell', 'k3182');
insert into Student (id_number, first_name, last_name, password) values ('00143296', 'Rollie', 'Gockelen', 'eTH2728');
insert into Student (id_number, first_name, last_name, password) values ('00160059', 'Cord', 'Pedrocco', 'xeHge1350');
insert into Student (id_number, first_name, last_name, password) values ('00160588', 'Sky', 'Doret', 'tpQ9155');
insert into Student (id_number, first_name, last_name, password) values ('00113523', 'Lorrie', 'Abley', 'rWUA0057');
insert into Student (id_number, first_name, last_name, password) values ('00139846', 'Gasper', 'Ribou', 'a0000');
insert into Student (id_number, first_name, last_name, password) values ('00108752', 'Lammond', 'Icom', 'PXzuS0420');
insert into Student (id_number, first_name, last_name, password) values ('00191361', 'Ileana', 'Lorenc', 'FAXbC2287');
insert into Student (id_number, first_name, last_name, password) values ('00151915', 'Petronilla', 'Madine', 'JUC0224');
insert into Student (id_number, first_name, last_name, password) values ('00139376', 'Josephina', 'Aronowicz', 'ynvX7070');
insert into Student (id_number, first_name, last_name, password) values ('00169509', 'Aloise', 'Boick', 'vUEX5253');
insert into Student (id_number, first_name, last_name, password) values ('00174377', 'Morton', 'Leavy', 'Xb1687');
insert into Student (id_number, first_name, last_name, password) values ('00198266', 'Sybille', 'Pettiford', 'bVsDH7774');
insert into Student (id_number, first_name, last_name, password) values ('00132279', 'Stephan', 'Gladebeck', 'wdUSg2175');
insert into Student (id_number, first_name, last_name, password) values ('00129266', 'Kendrick', 'Coleridge', 'J7184');
insert into Student (id_number, first_name, last_name, password) values ('00137101', 'Benn', 'Maymond', 'sh0321');
insert into Student (id_number, first_name, last_name, password) values ('00196001', 'Florella', 'Bortolazzi', 'Dm5515');
insert into Student (id_number, first_name, last_name, password) values ('00192422', 'Felic', 'Piche', 'OtRf9962');
insert into Student (id_number, first_name, last_name, password) values ('00133786', 'Corette', 'Dowthwaite', 'VFVC2272');
insert into Student (id_number, first_name, last_name, password) values ('00101879', 'Cecily', 'Verity', 'i0262');
insert into Student (id_number, first_name, last_name, password) values ('00130851', 'Vilma', 'Debrett', 'SMK8713');
insert into Student (id_number, first_name, last_name, password) values ('00169179', 'Ky', 'Rowlson', 'Q1052');
insert into Student (id_number, first_name, last_name, password) values ('00146643', 'Mirilla', 'Pinkney', 'cqXC1317');
insert into Student (id_number, first_name, last_name, password) values ('00126813', 'Cordula', 'Durtnall', 'ni1236');
insert into Student (id_number, first_name, last_name, password) values ('00133137', 'Mordecai', 'McGowran', 'zv4442');
insert into Student (id_number, first_name, last_name, password) values ('00188541', 'Shirl', 'Maddocks', 'jysW8903');
insert into Student (id_number, first_name, last_name, password) values ('00114543', 'Berkie', 'Mugridge', 'RNkHb9006');
insert into Student (id_number, first_name, last_name, password) values ('00120091', 'Demetris', 'Barrie', 'kZ3448');
insert into Student (id_number, first_name, last_name, password) values ('00160776', 'See', 'Primarolo', 'aD4572');
insert into Student (id_number, first_name, last_name, password) values ('00175413', 'Heindrick', 'Issacson', 'uW9265');
insert into Student (id_number, first_name, last_name, password) values ('00140994', 'Marjie', 'Butterly', 'wcRA1222');
insert into Student (id_number, first_name, last_name, password) values ('00140583', 'Griswold', 'Bamb', 'J6993');
insert into Student (id_number, first_name, last_name, password) values ('00151317', 'Ammamaria', 'Dantesia', 'APfe3781');
insert into Student (id_number, first_name, last_name, password) values ('00194183', 'Layton', 'Bagnell', 'Nm1033');
insert into Student (id_number, first_name, last_name, password) values ('00194818', 'Alric', 'Ablewhite', 'tdz2671');
insert into Student (id_number, first_name, last_name, password) values ('00158623', 'Rosie', 'Rodgers', 'JDMB5722');
insert into Student (id_number, first_name, last_name, password) values ('00170524', 'Zenia', 'Haggerty', 'U5573');
insert into Student (id_number, first_name, last_name, password) values ('00116913', 'Vanni', 'Wetherby', 'xay7375');
insert into Student (id_number, first_name, last_name, password) values ('00199351', 'Betty', 'Sherry', 'pFrlg2573');
insert into Student (id_number, first_name, last_name, password) values ('00129481', 'Rosanne', 'Nias', 'nw9019');
insert into Student (id_number, first_name, last_name, password) values ('00145824', 'Boris', 'Hilldrup', 'Wx8940');
insert into Student (id_number, first_name, last_name, password) values ('00175458', 'Carling', 'Furlow', 'Mm6018');
insert into Student (id_number, first_name, last_name, password) values ('00114109', 'Wilbert', 'Kinastan', 'P1469');
insert into Student (id_number, first_name, last_name, password) values ('00130754', 'Lucie', 'Gunson', 'Bp7359');
insert into Student (id_number, first_name, last_name, password) values ('00165576', 'Grant', 'Dodridge', 'QJzS9830');
insert into Student (id_number, first_name, last_name, password) values ('00116425', 'Rolph', 'Abdey', 'k6922');
insert into Student (id_number, first_name, last_name, password) values ('00196721', 'Basilio', 'Tarling', 'h2057');
insert into Student (id_number, first_name, last_name, password) values ('00130177', 'Jedd', 'Deelay', 'E5435');
insert into Student (id_number, first_name, last_name, password) values ('00113374', 'Lorrayne', 'Cairns', 'dtWO2658');
insert into Student (id_number, first_name, last_name, password) values ('00157156', 'Camel', 'Gerleit', 'XQv4713');
insert into Student (id_number, first_name, last_name, password) values ('00176488', 'Benoite', 'Burde', 'jhm8781');
insert into Student (id_number, first_name, last_name, password) values ('00165868', 'Rosemary', 'Rathbone', 'fIzg1963');
insert into Student (id_number, first_name, last_name, password) values ('00104573', 'Dotti', 'Mazey', 'wJu1152');
insert into Student (id_number, first_name, last_name, password) values ('00102652', 'Agustin', 'Dunkerley', 'au7158');
insert into Student (id_number, first_name, last_name, password) values ('00189255', 'Fielding', 'Aimeric', 'EiT7390');
insert into Student (id_number, first_name, last_name, password) values ('00165660', 'Izabel', 'Pittendreigh', 'Lgksr9349');
insert into Student (id_number, first_name, last_name, password) values ('00148731', 'Heidi', 'Jakubowsky', 'dbao7686');
insert into Student (id_number, first_name, last_name, password) values ('00148197', 'Jarrod', 'Romanet', 'qQ6029');
insert into Student (id_number, first_name, last_name, password) values ('00182315', 'Evin', 'Rubes', 'C3224');
insert into Student (id_number, first_name, last_name, password) values ('00193760', 'Germaine', 'Amys', 'B8549');
insert into Student (id_number, first_name, last_name, password) values ('00158850', 'Klaus', 'Akenhead', 'mvn2383');
insert into Student (id_number, first_name, last_name, password) values ('00128957', 'Dani', 'Bellay', 'yJawA2587');
insert into Student (id_number, first_name, last_name, password) values ('00163762', 'Haze', 'Pybus', 'vSZV3627');
insert into Student (id_number, first_name, last_name, password) values ('00160434', 'Bradley', 'Teml', 'vc1230');
insert into Student (id_number, first_name, last_name, password) values ('00102408', 'Agretha', 'Dudny', 'hDKg8689');
insert into Student (id_number, first_name, last_name, password) values ('00158329', 'Bertine', 'Gow', 'tm1053');
insert into Student (id_number, first_name, last_name, password) values ('00126478', 'Sheree', 'Biaggiotti', 'vEyi0940');
insert into Student (id_number, first_name, last_name, password) values ('00190551', 'Cal', 'Pechard', 'hw2151');
insert into Student (id_number, first_name, last_name, password) values ('00123105', 'Paulina', 'Radin', 'KnZbG4039');
insert into Student (id_number, first_name, last_name, password) values ('00189562', 'Kiele', 'Gitting', 'vam1154');
insert into Student (id_number, first_name, last_name, password) values ('00132632', 'Alvinia', 'Freeland', 'h3002');
insert into Student (id_number, first_name, last_name, password) values ('00137240', 'Moreen', 'Boggish', 'jQZ4215');
insert into Student (id_number, first_name, last_name, password) values ('00176767', 'Frieda', 'Lewendon', 'FfVWW4142');
insert into Student (id_number, first_name, last_name, password) values ('00166372', 'Ericka', 'Dillamore', 'MhXEi0107');
insert into Student (id_number, first_name, last_name, password) values ('00112689', 'Carey', 'Rockingham', 'YHHe2205');
insert into Student (id_number, first_name, last_name, password) values ('00176158', 'Batholomew', 'Torel', 'RfUhe4937');
insert into Student (id_number, first_name, last_name, password) values ('00189417', 'Daphne', 'Ambler', 'rflLg0996');
insert into Student (id_number, first_name, last_name, password) values ('00157363', 'Allister', 'Cowpe', 'Z1291');
insert into Student (id_number, first_name, last_name, password) values ('00150437', 'Annabell', 'Cabble', 'PJR0312');
insert into Student (id_number, first_name, last_name, password) values ('00126620', 'Kirsten', 'Valois', 'dbIT2231');
insert into Student (id_number, first_name, last_name, password) values ('00101217', 'Dody', 'Darree', 'U6499');
insert into Student (id_number, first_name, last_name, password) values ('00113802', 'Dalila', 'Drayn', 'lcRZ9983');
insert into Student (id_number, first_name, last_name, password) values ('00135032', 'Bucky', 'Pinney', 'UhE0226');
insert into Student (id_number, first_name, last_name, password) values ('00191296', 'Eldredge', 'Bassom', 'ff7207');
insert into Student (id_number, first_name, last_name, password) values ('00150320', 'Koo', 'Arlett', 'kRQ7160');
insert into Student (id_number, first_name, last_name, password) values ('00167031', 'Ines', 'Pinkerton', 'QvxiU1860');
insert into Student (id_number, first_name, last_name, password) values ('00154886', 'Jessamine', 'McArd', 'glgy0511');
insert into Student (id_number, first_name, last_name, password) values ('00151677', 'Andrej', 'Lindholm', 'DLLXZ2732');
insert into Student (id_number, first_name, last_name, password) values ('00123595', 'Marena', 'Stannus', 'BV9224');
insert into Student (id_number, first_name, last_name, password) values ('00121661', 'Gawen', 'Synan', 'S4739');
insert into Student (id_number, first_name, last_name, password) values ('00196667', 'Alejoa', 'Form', 'yX5724');
insert into Student (id_number, first_name, last_name, password) values ('00165110', 'Maisey', 'Tolley', 'nu9480');
insert into Student (id_number, first_name, last_name, password) values ('00148489', 'Conrad', 'Clapson', 'xyCS4861');
insert into Student (id_number, first_name, last_name, password) values ('00165556', 'Latashia', 'Ambrogini', 'dwts2607');
insert into Student (id_number, first_name, last_name, password) values ('00171611', 'Devina', 'Colvine', 'bv1635');
insert into Student (id_number, first_name, last_name, password) values ('00174508', 'Jori', 'Pritchitt', 'masYR3551');
insert into Student (id_number, first_name, last_name, password) values ('00144903', 'Helenka', 'Tee', 'gmpV4083');
insert into Student (id_number, first_name, last_name, password) values ('00160124', 'Vallie', 'Helbeck', 'TI0775');
insert into Student (id_number, first_name, last_name, password) values ('00192318', 'Fabien', 'Gepson', 'U2840');
insert into Student (id_number, first_name, last_name, password) values ('00149131', 'Theo', 'Ors', 'wZXO3182');
insert into Student (id_number, first_name, last_name, password) values ('00100737', 'Anatol', 'Poulden', 'FI4896');
insert into Student (id_number, first_name, last_name, password) values ('00123318', 'Talbot', 'Auten', 'GZB7191');
insert into Student (id_number, first_name, last_name, password) values ('00172815', 'Barb', 'Minelli', 'j7244');
insert into Student (id_number, first_name, last_name, password) values ('00116793', 'Aurel', 'Halse', 'xZu6082');
insert into Student (id_number, first_name, last_name, password) values ('00121807', 'Bryant', 'Rubroe', 'nYqw9383');
insert into Student (id_number, first_name, last_name, password) values ('00129604', 'Bianca', 'Tankin', 'RVGb6625');
insert into Student (id_number, first_name, last_name, password) values ('00191339', 'Charmine', 'Papaminas', 'uow2906');
insert into Student (id_number, first_name, last_name, password) values ('00180295', 'Broddie', 'Winsley', 'dYkp0310');
insert into Student (id_number, first_name, last_name, password) values ('00177510', 'Dino', 'Osichev', 'PDL3782');
insert into Student (id_number, first_name, last_name, password) values ('00196747', 'Donetta', 'Storrs', 'rqWG5637');
insert into Student (id_number, first_name, last_name, password) values ('00104311', 'Stephenie', 'Burling', 'GmX6649');
insert into Student (id_number, first_name, last_name, password) values ('00130285', 'Darleen', 'Trenfield', 'braAg3817');
insert into Student (id_number, first_name, last_name, password) values ('00106995', 'Boote', 'Veldman', 'GY6095');
insert into Student (id_number, first_name, last_name, password) values ('00131765', 'Paxon', 'Askam', 'Ug3395');
insert into Student (id_number, first_name, last_name, password) values ('00122622', 'Yves', 'Matokhnin', 'Nbh8796');
insert into Student (id_number, first_name, last_name, password) values ('00164207', 'Tonia', 'Haldane', 'dKN7182');
insert into Student (id_number, first_name, last_name, password) values ('00197401', 'Dorri', 'Hegerty', 'f7941');
insert into Student (id_number, first_name, last_name, password) values ('00141181', 'Roselle', 'Clulee', 'Ko3122');
insert into Student (id_number, first_name, last_name, password) values ('00136722', 'Calypso', 'Lawranson', 'wRq7286');
insert into Student (id_number, first_name, last_name, password) values ('00123836', 'Karina', 'Wynch', 'IrJC6155');
insert into Student (id_number, first_name, last_name, password) values ('00125332', 'Floyd', 'Ackrill', 'oOC1779');
insert into Student (id_number, first_name, last_name, password) values ('00105792', 'Gillian', 'Lammerts', 'Nna6410');
insert into Student (id_number, first_name, last_name, password) values ('00170684', 'Shirlene', 'Earlam', 'GUX3569');
insert into Student (id_number, first_name, last_name, password) values ('00177129', 'Wyatan', 'Readshall', 'ZUdB3049');
insert into Student (id_number, first_name, last_name, password) values ('00180373', 'Layne', 'Jailler', 'PA3990');
insert into Student (id_number, first_name, last_name, password) values ('00193652', 'Bellanca', 'Stidever', 'jiTn4377');
insert into Student (id_number, first_name, last_name, password) values ('00103885', 'Norry', 'Arrundale', 'kv3844');
insert into Student (id_number, first_name, last_name, password) values ('00158290', 'Tomkin', 'Todman', 'qAiTT8033');
insert into Student (id_number, first_name, last_name, password) values ('00114539', 'Mable', 'MacGilmartin', 'MVc7200');
insert into Student (id_number, first_name, last_name, password) values ('00197767', 'Shaylynn', 'Gonnely', 'R0506');
insert into Student (id_number, first_name, last_name, password) values ('00136205', 'Fawn', 'Biaggiotti', 'rpRfx5414');
insert into Student (id_number, first_name, last_name, password) values ('00139856', 'Geri', 'Tomkys', 'PXQ6955');
insert into Student (id_number, first_name, last_name, password) values ('00179456', 'Angeline', 'Doey', 'fE5853');
insert into Student (id_number, first_name, last_name, password) values ('00154481', 'Modesty', 'Mulcaster', 'Ze5840');
insert into Student (id_number, first_name, last_name, password) values ('00120225', 'Randall', 'Bradd', 'TAzl4430');
insert into Student (id_number, first_name, last_name, password) values ('00179209', 'Theda', 'Tenwick', 'DxjLB9349');
insert into Student (id_number, first_name, last_name, password) values ('00151597', 'Pepito', 'O''Collopy', 'vUk1213');
insert into Student (id_number, first_name, last_name, password) values ('00121663', 'Warner', 'Bowcock', 'qwBk5848');
insert into Student (id_number, first_name, last_name, password) values ('00156783', 'Reta', 'Ackery', 'lQN9263');
insert into Student (id_number, first_name, last_name, password) values ('00162435', 'Shawna', 'Sarjeant', 'fRKXI8721');
insert into Student (id_number, first_name, last_name, password) values ('00192287', 'Melany', 'Este', 'kDpr5872');
insert into Student (id_number, first_name, last_name, password) values ('00177287', 'Callida', 'Giacomelli', 'P8301');
insert into Student (id_number, first_name, last_name, password) values ('00122382', 'Cathe', 'Adolthine', 'FM9335');
insert into Student (id_number, first_name, last_name, password) values ('00124015', 'Redd', 'Dizlie', 'akcl9621');
insert into Student (id_number, first_name, last_name, password) values ('00172688', 'Dick', 'Aslin', 's9887');
insert into Student (id_number, first_name, last_name, password) values ('00155866', 'Rogerio', 'Denington', 'ge4671');
insert into Student (id_number, first_name, last_name, password) values ('00168107', 'Coleman', 'Hazelhurst', 'A4338');
insert into Student (id_number, first_name, last_name, password) values ('00177224', 'Melloney', 'Mateescu', 'ry2732');
insert into Student (id_number, first_name, last_name, password) values ('00138386', 'Aloise', 'Carlens', 'W1916');
insert into Student (id_number, first_name, last_name, password) values ('00185675', 'Joan', 'Divina', 'G0495');
insert into Student (id_number, first_name, last_name, password) values ('00130955', 'Paige', 'Maddie', 'S0937');
insert into Student (id_number, first_name, last_name, password) values ('00146048', 'Gottfried', 'Kimbury', 'HX5464');
insert into Student (id_number, first_name, last_name, password) values ('00105782', 'Saloma', 'Olford', 'z1156');
insert into Student (id_number, first_name, last_name, password) values ('00106074', 'Madelyn', 'Grastye', 'LEDEw6770');
insert into Student (id_number, first_name, last_name, password) values ('00136314', 'Lauri', 'Kidwell', 'HMCU6466');
insert into Student (id_number, first_name, last_name, password) values ('00137601', 'Daile', 'MacLachlan', 'DnNW2681');
insert into Student (id_number, first_name, last_name, password) values ('00104503', 'Marybeth', 'Cater', 'PG3816');
insert into Student (id_number, first_name, last_name, password) values ('00111501', 'Fey', 'Keiley', 'wCbuX7656');
insert into Student (id_number, first_name, last_name, password) values ('00138903', 'Othilie', 'Ferruzzi', 'HQs5009');
insert into Student (id_number, first_name, last_name, password) values ('00191943', 'Laurens', 'Davydzenko', 'x7481');
insert into Student (id_number, first_name, last_name, password) values ('00143148', 'Stephenie', 'Koop', 'vOkw6744');
insert into Student (id_number, first_name, last_name, password) values ('00128267', 'Si', 'Minghella', 'CBrh2320');
insert into Student (id_number, first_name, last_name, password) values ('00156222', 'Graig', 'McElmurray', 'Ud6101');
insert into Student (id_number, first_name, last_name, password) values ('00104451', 'Antone', 'Lacoste', 'LlJKj4140');
insert into Student (id_number, first_name, last_name, password) values ('00143228', 'Egbert', 'Ciciotti', 'pUo6517');
insert into Student (id_number, first_name, last_name, password) values ('00100090', 'Kettie', 'Blakeden', 'RTP3699');
insert into Student (id_number, first_name, last_name, password) values ('00107535', 'Alex', 'Baton', 'zJH2454');
insert into Student (id_number, first_name, last_name, password) values ('00131164', 'Frederich', 'MacKartan', 'dzG3774');
insert into Student (id_number, first_name, last_name, password) values ('00188975', 'Catlin', 'Oboy', 'I3734');
insert into Student (id_number, first_name, last_name, password) values ('00100300', 'Ashely', 'Stacey', 'q9815');
insert into Student (id_number, first_name, last_name, password) values ('00113352', 'Marmaduke', 'Sommersett', 'yCJw9857');
insert into Student (id_number, first_name, last_name, password) values ('00180182', 'Wilmette', 'Dimond', 'GgIYh4126');
insert into Student (id_number, first_name, last_name, password) values ('00104007', 'Alexandrina', 'Thumim', 'Rvt7172');
insert into Student (id_number, first_name, last_name, password) values ('00181240', 'Deedee', 'Shere', 'sYz4665');
insert into Student (id_number, first_name, last_name, password) values ('00159501', 'Sanders', 'Minithorpe', 'v4637');
insert into Student (id_number, first_name, last_name, password) values ('00116206', 'Lindi', 'Boult', 'OZ2930');
insert into Student (id_number, first_name, last_name, password) values ('00145476', 'Grenville', 'Silverston', 'nJAdW4652');
insert into Student (id_number, first_name, last_name, password) values ('00187361', 'Kyle', 'Blankman', 'EBMh0629');
insert into Student (id_number, first_name, last_name, password) values ('00171628', 'Tracy', 'Thomasson', 'aQdW0256');
insert into Student (id_number, first_name, last_name, password) values ('00170530', 'Clemence', 'Bracknell', 'XjSsG1772');
insert into Student (id_number, first_name, last_name, password) values ('00109139', 'Clovis', 'O'' Molan', 'NkXEL0874');
insert into Student (id_number, first_name, last_name, password) values ('00124382', 'Sonny', 'Crookshanks', 'D1101');
insert into Student (id_number, first_name, last_name, password) values ('00138287', 'Brett', 'Oxnam', 'Ivvw0752');
insert into Student (id_number, first_name, last_name, password) values ('00104951', 'Adella', 'Gribble', 'tEg2814');
insert into Student (id_number, first_name, last_name, password) values ('00139870', 'Cara', 'Fozzard', 'U2782');
insert into Student (id_number, first_name, last_name, password) values ('00134426', 'Arielle', 'Clutheram', 'XKk3571');
insert into Student (id_number, first_name, last_name, password) values ('00144341', 'Wynne', 'Lamplugh', 'wOm1515');
insert into Student (id_number, first_name, last_name, password) values ('00190636', 'Evvie', 'Singleton', 'qAtk1275');
insert into Student (id_number, first_name, last_name, password) values ('00188641', 'Haroun', 'Ganley', 'x0350');
insert into Student (id_number, first_name, last_name, password) values ('00128048', 'Jdavie', 'Hardiker', 'hh7603');
insert into Student (id_number, first_name, last_name, password) values ('00196748', 'Clerissa', 'Allpress', 'VmzYW9421');
insert into Student (id_number, first_name, last_name, password) values ('00132112', 'Joell', 'Minogue', 'A0610');
insert into Student (id_number, first_name, last_name, password) values ('00183527', 'Hymie', 'Kyttor', 'bj3990');
insert into Student (id_number, first_name, last_name, password) values ('00190595', 'Gretna', 'Sarginson', 'lM0163');
insert into Student (id_number, first_name, last_name, password) values ('00147410', 'Pammie', 'Abrahami', 'i6358');
insert into Student (id_number, first_name, last_name, password) values ('00128655', 'Berthe', 'McMonies', 'L6752');
insert into Student (id_number, first_name, last_name, password) values ('00120669', 'Brandtr', 'Wolffers', 'z7379');
insert into Student (id_number, first_name, last_name, password) values ('00145623', 'Damara', 'Golightly', 'PK3664');
insert into Student (id_number, first_name, last_name, password) values ('00105021', 'Roddy', 'Winson', 'sys2701');
insert into Student (id_number, first_name, last_name, password) values ('00138839', 'Emiline', 'Ceaplen', 'XQ9155');
insert into Student (id_number, first_name, last_name, password) values ('00186724', 'Gwynne', 'Kiff', 'THCi9694');
insert into Student (id_number, first_name, last_name, password) values ('00195901', 'Truman', 'Cleen', 'JQ6039');
insert into Student (id_number, first_name, last_name, password) values ('00198856', 'Torry', 'Gounin', 'uT7565');
insert into Student (id_number, first_name, last_name, password) values ('00185849', 'Lynelle', 'Leftwich', 'ftP1327');
insert into Student (id_number, first_name, last_name, password) values ('00179368', 'Cal', 'Jeffryes', 'NXYfg9780');
insert into Student (id_number, first_name, last_name, password) values ('00137240', 'Verine', 'Innott', 'SERhe2003');
insert into Student (id_number, first_name, last_name, password) values ('00194521', 'Laverne', 'Eglese', 'HdrUa9774');
insert into Student (id_number, first_name, last_name, password) values ('00172267', 'Glynnis', 'Splaven', 'JEm5997');
insert into Student (id_number, first_name, last_name, password) values ('00180826', 'Grantham', 'Silvers', 'si7327');



-- insert into Courses (Courseid, CourseName, CourseTime, CourseLocation, CourseDate) values ('1000', 'Math 101', '3:15:00','MWF');
-- insert into Courses (Courseid, CourseName, CourseTime, CourseLocation, CourseDate) values ('1001', 'English 101', '3:15:00','MWF');
-- insert into Courses (Courseid, CourseName, CourseTime, CourseLocation, CourseDate) values ('1002', 'Cpts 101', '3:15:00','TTH');
-- insert into Courses (Courseid, CourseName, CourseTime, CourseLocation, CourseDate) values ('1003', 'Chemistry 101', '3:15:00','MWF');
