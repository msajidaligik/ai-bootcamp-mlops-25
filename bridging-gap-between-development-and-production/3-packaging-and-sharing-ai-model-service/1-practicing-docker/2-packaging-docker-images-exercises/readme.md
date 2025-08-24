
# Docker Image Exercises

## 1. Create a Python Docker Image FROM ubuntu

- Go to directory my-python
```bash
cd my-python
```
- Use the following Dockerfile instructions
```bash
# Use the official Ubuntu base image
FROM ubuntu

# Update and install dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set default Python alias
RUN ln -s /usr/bin/python3 /usr/bin/python

# Set working directory inside the container
WORKDIR /app

# Default command to run Python
CMD ["python"]

```

- Build docker image
```bash
docker build --network=host -t my-python .
```

- Create a local file
```bash
echo 'print("Hello, world!")' > hello.py
```

- Run container with volume
```bash
docker run -it --rm -v $(pwd)/hello.py:/app/hello.py my-python bash
```

- **Congratulations!** you have just created your own isloated python environment
```bash
docker run -it --rm -v $(pwd)/hello.py:/app/hello.py my-python bash
```

