from dataclasses import dataclass


@dataclass
class Person:
    name: str = None
    email: str = None
    phone: str = None
    subject: str = None
    message: str = None
