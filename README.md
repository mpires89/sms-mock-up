# Strategic SMS Delivery Service

This project implements a dynamic and extensible SMS delivery system utilizing Object-Oriented Programming (OOP) best practices in Python.

## Applied Patterns & Concepts
- **Dependency Inversion (SOLID):** Coupling is based on abstractions rather than concrete implementations.
- **Open/Closed Principle (SOLID):** Easily extensible to include new SMS providers without modifying existing code.
- **Simple Factory Pattern:** Centralizes the logic for instantiating the correct provider during the service's initialization.

## Code Structure
- `SMSProviderBase`: Abstract base class that enforces the `enviar_sms` contract via `NotImplementedError`.
- `PrimarySMSProvider` & `SecondarySMSProvider`: Concrete classes handling the actual SMS delivery logic.
- `ServicoSMS`: Service manager that dynamically injects the chosen provider using `match-case` in its constructor.

## Running the Tests
Ensure you have `pytest` installed, then run:
```bash
pytest test_provedores_sms.py