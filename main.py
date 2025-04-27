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
