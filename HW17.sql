-- 1. Write SQL queries for table creation for a data model that you created for prev homework (Airbnb model)

-- 2. Write 3 rows (using INSERT queries) for each table in the data model

-- 3. Create the next analytic queries:

--       1. Find a user who had the biggest amount of reservations. Return user name and user_id


CREATE TABLE user_host (
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
);

CREATE TABLE user_guest (
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
);

CREATE TABLE available_rooms (
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
);

CREATE TABLE room_amenities (
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
);

CREATE TABLE room (
    id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (id)
    FOREIGN KEY (user_host_id) REFERENCES user_host(id)
    FOREIGN KEY (room_amenities_id) REFERENCES room_amenities(id)
);

CREATE TABLE reservation (
    reservation_id int NOT NULL AUTO_INCREMENT,
    PRIMARY KEY (reservation_id)
    FOREIGN KEY (user_host_id) REFERENCES user_host(id)
    FOREIGN KEY (user_guest_id) REFERENCES user_guest(id)
    FOREIGN KEY (room_id) REFERENCES room(id)
);

INSERT INTO user_host (name, surname, city) VALUES ('Anna', 'Green', 'London'), ('John', 'Deer', 'New York'), ('Ben', 'Muller', 'Berlin')
INSERT INTO user_guest (name, surname, city) VALUES ('Ann', 'Brown', 'Manchester'), ('Eva', 'Grey', 'Washington'), ('Kate', 'Carpenter', 'Budapest')

SELECT COUNT (reservation_id), user_guest_id
FROM reservation
GROUP BY user_guest_id;


