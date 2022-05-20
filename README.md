# model-deployment
Machine Learning Pipline Deployment

## Custom Model Deployment - Vertex AI

Step 1: Containerize the code
- Download the code
- Create Dockerfile
    - https://cloud.google.com/deep-learning-containers/docs/choosing-container
        
Step 2: Create a bucket to export the trained model 
- gsutil mb -l us-central1 gs://bucket-name
    

Step 3: Setup the project
- Create the folder structure as mentioned in the Dockerfile
    - mkdir trainer
    - touch trainer/train.py
- Add the training code to the train.py file
    
Step 4: Build & Register
- build the docker image
    - IMAGE_URI="gcr.io/gcp-onsite-training/diabetes:v1"
    - docker build ./ -t $IMAGE_URI
- Run and test the build
    `- docker run $IMAGE_URI`
- Push the container to Google container registry
    `- docker push $IMAGE_URI`
    
Step 5: Kick-off the cutom model training job in VertexAI
