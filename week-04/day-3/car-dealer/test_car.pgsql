SELECT ROUND(AVG(age.car_age), 2) AS avg_car_age
FROM (SELECT (2019 - year) AS car_age
      FROM car
      WHERE count != 0) AS age;
