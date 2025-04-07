from dataclasses import dataclass

@dataclass
class Customer:
    id: int | None
    first_name: str
    last_name: str
    email: str
    password_hash: str
    shipping_address: str
