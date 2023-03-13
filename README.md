## Getting Started
1. ```git clone https://github.com/maxim-shirokov547/user_notes```.
2. ``` cp .env.example .env```.
3. Fill .env file.
4. Run ```make``` command for production mode.
    1. Run ```make dev``` for development mode.
5. Open ```http://host:port/swagger-ui/``` to view docs.

## Struct project
```
├── src                           # Source files.
    ├── api         
    │    ├── internal             # Source code files.
    │    │    ├── models          # Files with models.
    │    │    ├── serializers     # Files with serializers .
    │    │    ├── views           # Files with views.
              └── ...
    │    ├── migrations           # Migration files .
    │    ├── pkg                  # Common files.
    │    ├── templates            # Templates files.
    │    ├── tests                # Test files.
         └── ...
    ├── config                    # Config files.
    └── ...
```    