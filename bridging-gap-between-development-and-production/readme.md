
# Basic Housing Web App

## For 1-simple-housing-app-without-ml-model
#### 1. Build docker image for backend
```bash
docker build --network=host -t housing-backend-app-without-ml-model ./3-backend/.
```
#### 2. Run the application
```bash
docker compose up -d
```
#### 3. Access the application
```bash
http://localhost

or

http:<you-ip>
```

## For 2-simple-housing-app-with-ml-model
#### 1. Build docker image for backend
```bash
docker build --network=host -t housing-backend-app-with-ml-model ./3-backend/.
```
#### 2. Build docker image for ai-model-service
```bash
docker build --network=host -t housing-ai-model-service ./4-ai-model-service/.
```
#### 3. Run the application
```bash
docker compose up -d
```
#### 4. Access the application
```bash
http://localhost

or

http:<you-ip>
```
#### 5. Access the application backend
```bash
http://localhost:5000 

or 

http:<you-ip>:5000
```
#### 5. AI model service API endpoints
```bash
http://localhost:8000/docs

or

http:<you-ip>:8000/docs
```
