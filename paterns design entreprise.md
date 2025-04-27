# Enterprise Design Patterns: Applying the Patterns from the "Catalog of Patterns of Enterprise Application Architecture"
In the world of enterprise application architecture, design patterns play a crucial role in structuring systems in a maintainable, scalable, and efficient way. The Catalog of Patterns of Enterprise Application Architecture presents a wide array of patterns that can be applied to various enterprise scenarios. Below, we’ll walk through some of the most important patterns and demonstrate how they can be implemented in Python code

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

1. Service Layer Pattern
The Service Layer Pattern is used to centralize business logic into a dedicated service layer. This pattern keeps the business logic separate from the rest of the application, making it easier to manage and maintain.

Explanation: The service layer provides a clean API for the business operations, acting as an intermediary between the user interface and the domain model. It consolidates operations that interact with the database, ensuring that the business logic is abstracted from both the UI and the data access layer.

Code Example:
```
class CustomerService:
    def __init__(self, repository):
        self.repository = repository

    def add_customer(self, name, email):
        customer = Customer(name, email)
        self.repository.save(customer)

    def get_customer(self, customer_id):
        return self.repository.get_by_id(customer_id)

```

2. Repository Pattern
The Repository Pattern abstracts the data access logic. It isolates the domain model from the data storage details, making it possible to change the data storage implementation without affecting the business logic.

Explanation: The repository acts as a middle layer between the service layer and the data source (database, in-memory storage, etc.). It provides methods for querying and saving domain objects, which makes data access more flexible and easier to modify.

Code Example:
```
class CustomerRepository:
    def __init__(self):
        self.customers = {}

    def save(self, customer):
        self.customers[customer.id] = customer

    def get_by_id(self, customer_id):
        return self.customers.get(customer_id)

    def remove(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]

```

3. Domain Model Pattern
The Domain Model Pattern represents the business entities in an application. It encapsulates both the data and the behavior associated with it, ensuring the business logic is contained within these objects.

Explanation: The domain model contains the core business logic for each entity, making it more than just a container for data. It can include validation, behavior, and transformations.

Code Example:
```
class Customer:
    def __init__(self, name, email):
        self.id = id(self)
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email})"

```
4. Separation of Concerns
The Separation of Concerns (SoC) principle states that different parts of the application should have distinct, well-defined responsibilities. By following SoC, you make the system more modular, easier to understand, and easier to maintain.

Explanation: In our application, each class has a clear responsibility:

CustomerService manages the business logic,

CustomerRepository handles data persistence, and

Customer defines the business entity.

This separation allows for better maintenance and scalability.

Code Example: 
```
The previous examples of CustomerService, CustomerRepository, and Customer already demonstrate the application of SoC. These classes don't overlap in functionality and each handles a specific task.
```
5. Centralized Business Logic
This pattern centralizes the business logic into a dedicated layer, preventing the logic from being spread across multiple parts of the application, making it easier to maintain and evolve over time.

Explanation: The logic related to customers (like adding and retrieving customers) is encapsulated within the CustomerService class. If the logic changes in the future (for example, adding more validations or operations), you only need to modify the service layer.

Code Example: Again, the CustomerService class is where the business logic is centralized. It is the place where all operations related to customers (such as adding and retrieving) are performed.

complete code :
```
# Domain Model Pattern: The Customer class represents the business entity
class Customer:
    def __init__(self, name, email):
        self.id = id(self)
        self.name = name
        self.email = email

    def __str__(self):
        return f"Customer(name={self.name}, email={self.email})"


# Repository Pattern: Handles data persistence
class CustomerRepository:
    def __init__(self):
        self.customers = {}

    def save(self, customer):
        self.customers[customer.id] = customer

    def get_by_id(self, customer_id):
        return self.customers.get(customer_id)

    def remove(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]


# Service Layer Pattern: Contains business logic
class CustomerService:
    def __init__(self, repository):
        self.repository = repository

    def add_customer(self, name, email):
        customer = Customer(name, email)
        self.repository.save(customer)

    def get_customer(self, customer_id):
        return self.repository.get_by_id(customer_id)


# Testing the implementation
if __name__ == "__main__":
    # Instantiate the repository
    customer_repository = CustomerRepository()

    # Instantiate the service layer with the repository
    customer_service = CustomerService(customer_repository)

    # Add a customer
    customer_service.add_customer("John Doe", "john.doe@example.com")
    customer_service.add_customer("Jane Smith", "jane.smith@example.com")

    # Retrieve and print customer by ID
    customer = customer_service.get_customer(1)  # In this case, we'll assume the customer id is 1
    if customer:
        print(customer)
    else:
        print("Customer not found.")
```

# Conclusion
By applying these enterprise design patterns, we achieve a clear, modular, and maintainable architecture for our application. Here's how these patterns contribute to the overall structure:

- Service Layer Pattern ensures that business logic is centralized, making it easy to maintain and update.

- Repository Pattern abstracts the data access layer, allowing for easier changes in how data is stored.

- Domain Model Pattern helps in encapsulating business data and logic within entities.

- Separation of Concerns ensures that each part of the application has a distinct responsibility, improving readability and maintainability.

>This pattern-based architecture makes it easier to scale and maintain the system as it grows, which is a key aspect of enterprise-level applications. You can use this code as a foundation and build more complex systems by adding new layers and patterns as needed

>Code example demonstrate how to implement Enterprise Design Patterns as described in the Catalog of Patterns of Enterprise Application Architecture. Each pattern contributes to a robust and maintainable software architecture that is scalable and easier to manage.
