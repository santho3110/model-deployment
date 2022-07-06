FROM 

WORKDIR /

# copies the training code to the docker image
COPY trainer /trainer

# Sets up entry point to invoke the training
ENTRYPOINT ["python", "-m", "trainer.train"]