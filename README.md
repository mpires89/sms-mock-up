# Strategic SMS Delivery Service & API

This project implements a dynamic and extensible SMS delivery system utilizing Object-Oriented Programming (OOP) best practices in Python, exposed as a RESTful API using **FastAPI**.

## Applied Patterns & Concepts
- **Dependency Inversion (SOLID):** Coupling is based on abstractions rather than concrete implementations.
- **Open/Closed Principle (SOLID):** Easily extensible to include new SMS providers without modifying existing code.
- **Simple Factory Pattern:** Centralizes the logic for instantiating the correct provider during the service's initialization.

## Code Structure
- `sms_provider_base.py`: Abstract base class `SMSProviderBase` that enforces the `enviar_sms` contract.
- `primary_sms_provider.py` & `secondary_sms_provider.py`: Concrete classes handling the actual SMS delivery logic.
- `service_sms.py`: Service manager (`ServicoSMS`) that dynamically injects the chosen provider using `match-case` in its constructor.
- `main.py`: **FastAPI** application exposing the endpoint to trigger SMS dispatches via HTTP requests.

## Requirements
- Python 3.10+
- [Poetry](https://python-poetry.org/) for dependency management.

## Installation

Install the environment and dependencies using Poetry:
```bash
poetry install
```

## Running the Application

To run the API locally, execute the following command:
```bash
poetry run uvicorn main:app --reload
```
The application will be available at `http://127.0.0.1:8000`. You can access the interactive Swagger documentation at `http://127.0.0.1:8000/docs`.

### API Usage Example
Send a `POST` request to `/enviar-sms`:
```bash
curl -X POST "http://127.0.0.1:8000/enviar-sms" \
     -H "Content-Type: application/json" \
     -d '{"telefone": "11999999999", "mensagem": "Hello via API!", "provedor": "primary"}'
```

## Testing

It is critical that all functionalities are reliable. Thus, all functions, classes, and endpoints are covered by **unit tests**. We use `pytest` for the test suite, alongside `TestClient` for API assertions.

To run the complete test suite and verify all unit tests, execute:
```bash
poetry run pytest
```
This will automatically discover and run all tests located in the `test/` folder.