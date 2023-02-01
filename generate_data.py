import csv
import random

import faker

writer = csv.writer(open("data.csv", "w"))
faker_instance = faker.Faker()
writer.writerow(["num", "longitude", "latitude", "temperature", "date"])
for i in range(1000):
    writer.writerow(
        [i, faker_instance.longitude(), faker_instance.latitude(), random.randint(-30, 40), faker_instance.date_time()])
