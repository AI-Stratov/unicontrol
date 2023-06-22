-- Удалить задание для самостоятельной работы, которое было создано более года назад:
DELETE FROM Assignment
WHERE assignment_date <= NOW() - INTERVAL '1 year';

