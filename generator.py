from data import Person
from faker import Faker


fake = Faker()
Faker.seed()


def generated_person():
    yield Person(
        name=fake.first_name() + " " + fake.last_name(),
        email=fake.email(),
        phone=fake.msisdn(),
        subject=fake.company(),
        message=fake.simple_profile(),
    )
