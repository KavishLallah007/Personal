-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Theft at 10:15 am at Humphrey street bakery
SELECT description
FROM crime_scene_reports
WHERE year = 2021 AND month = 7 AND day = 28 AND street = 'Humphrey Street';


-- car left parking 10 minutes later look in bakery_security_logs
SELECT transcript
FROM interviews
WHERE year = 2021 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';


-- list of suspects who left parking lot 10 minutes after theft based on first transcript
SELECT name
FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10 AND minute <= 25 AND activity = 'exit';
-- suspects: Vanessa, Bruce, Barry, Luca, Sofia, Iman, Diana, Kelsey



-- new list of suspects who withdrew money based on second transcript
SELECT name
FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
JOIN atm_transactions ON atm_transactions.account_number = bank_accounts.account_number
WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';
-- suspects: Bruce, Diana, Brooke, Kenny, Iman, Luca, Taylor, Benista
--common suspects from transcript 1 and 2: Bruce, Iman, Diana, Luca


-- new list of suspects who took early flight the next day based on third transcript
SELECT name
FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id = (
    SELECT id
    FROM flights
    WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (
        SELECT id
        FROM airports
        WHERE city = 'Fiftyville'
    )
    ORDER by hour, minute
    LIMIT 1);
--suspect: Doris, Sofia, Bruce, Edward, Kelsey, Taylor, Kenny, Luca
--common suspects: Bruce, Luca


-- look for list of suspects based on phone calls of duraion less that 1 minute
SELECT name
FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60;
-- common suspects: Bruce
-- thief > Bruce


SELECT city
FROM airports
WHERE id = (
    SELECT destination_airport_id
    FROM flights
    WHERE year = 2021 AND month = 7 AND day = 29 AND origin_airport_id = (
        SELECT id
        FROM airports
        WHERE city = 'Fiftyville'
    )
    ORDER BY hour, minute
    LIMIT 1
);
-- Thief fled to New York City


-- get Bruce phone number (367) 555-5533
SELECT phone_number
FROM people
WHERE name = 'Bruce';

--get name of suspect Bruce contacted: Robin
SELECT name
FROM people
WHERE phone_number = (
    SELECT receiver
    FROM phone_calls
    WHERE year = 2021 AND month = 7 AND day = 28 AND duration < 60 AND caller = '(367) 555-5533'
);

