# Backend Task - Clean Architecture

This project is a very naive implementation of a simple shop system. It mimics in its structure a real world example of a service that was prepared for being split into microservices and uses the current Helu backend tech stack.

## Goals

Please answer the following questions:

1. Why can we not easily split this project into two microservices?

Use cases directly talking to FastAPI stuff like HTTPException, and they're tightly coupled with SQLAlchemy, they expect a Session object everywhere.
Repositories aren’t abstracted. So if you ever wanted to switch to an in-memory store or move some logic into a different service, you'd have to refactor a lot of code.
Also, even though the project is split by feature (item, user, etc.), it’s still not layered properly. There’s no clear separation between domain logic, infrastructure, and API. So slicing it into microservices feels more like tearing it apart than unplugging modules.

2. Why does this project not adhere to the clean architecture even though we have seperate modules for api, repositories, usecases and the model?

Main issue: wrong direction of dependencies. The core logic (use cases) depends on things it really shouldn’t (DB models, schemas, and repository implementations).
Also, throwing HTTPException inside the use cases, thts controller logic leaking into business logic.
The domain isn't “clean” because it drags around infrastructure concerns (every function expects a Session, so now you’re tied to SQLAlchemy forever).

3. What would be your plan to refactor the project to stick to the clean architecture?

Easy to say, harder to do, but here’s the SUPER plan:

Define interfaces (ItemRepository, CustomerRepository, etc...) in your domain layer.
Let use cases work with those interfaces (no knowledge of FastAPI, no DB stuff).
Push all SQLAlchemy models and DB logic to the infrastructure layer.
Wire things up in the app layer, maybe using dependency injection.
And definitely move all HTTP exceptions to the API layer.

4. How can you make dependencies between modules more explicit?

Use abstract base classes or Protocols to define your expectations (save, find_by_email, etc.).
Inject concrete implementations from the outside (no import db_stuff inside domain).
Don’t let inner layers call outer ones. Like, your use case shouldn’t know FastAPI even exists.
This structure, should be way easier to swap pieces in and out (even split things into microservices later with less pain).


*Please do not spend more than 2-3 hours on this task.*

Stretch goals:
* Fork the repository and start refactoring
* Write meaningful tests
* Replace the SQL repository with an in-memory implementation

## References
* [Clean Architecture by Uncle Bob](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)
* [Clean Architecture in Python](https://www.youtube.com/watch?v=C7MRkqP5NRI)
* [A detailed summary of the Clean Architecture book by Uncle Bob](https://github.com/serodriguez68/clean-architecture)

## How to use this project

If you have not installed poetry you find instructions [here](https://python-poetry.org/).

1. `docker-compose up` - runs a postgres instance for development
2. `poetry install` - install all dependency for the project
3. `poetry run schema` - creates the database schema in the postgres instance
4. `poetry run start` - runs the development server at port 8000
5. `/postman` - contains an postman environment and collections to test the project

## Other commands

* `poetry run graph` - draws a dependency graph for the project
* `poetry run tests` - runs the test suite
* `poetry run lint` - runs flake8 with a few plugins
* `poetry run format` - uses isort and black for autoformating
* `poetry run typing` - uses mypy to typecheck the project

## Specification - A simple shop

* As a customer, I want to be able to create an account so that I can save my personal information.
* As a customer, I want to be able to view detailed product information, such as price, quantity available, and product description, so that I can make an informed purchase decision.
* As a customer, I want to be able to add products to my cart so that I can easily keep track of my intended purchases.
* As an inventory manager, I want to be able to add new products to the system so that they are available for customers to purchase.


# Shop Clean Architecture - Refactored Version

This project is a refactored version of the original `be-task-ca` repository with improved modularity and testability using Clean Architecture principles.

## 🔄 Key Improvements

- **Domain-driven structure**: Separation of concerns between entities, use cases, repositories, and delivery.
- **Clean Architecture alignment**: Core logic is decoupled from frameworks like FastAPI and ORMs like SQLAlchemy.
- **Pluggable infrastructure**: Easily switch between SQL-based and in-memory repositories.
- **Swagger docs**: Auto-generated API docs available for testing via FastAPI.

## 🚀 How to Run

### ▶️ With In-Memory Repositories (no DB required)

```bash
USE_IN_MEMORY=true poetry run start
```

This mode is great for local development, prototyping, or running tests.

### 🗃️ With SQLAlchemy + PostgreSQL/SQLite

Make sure you’ve configured your database and run:

```bash
poetry run start
```

## 🔍 Swagger API Docs

Once the app is running, navigate to:

👉 [http://localhost:8000/docs](http://localhost:8000/docs)

You can test all endpoints (customers, items, carts) interactively.

## 🧪 Tests

```bash
poetry run test
```

Includes unit tests for use cases and API integration tests.

---