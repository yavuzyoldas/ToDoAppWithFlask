FROM python:3.6

RUN apt-get update && \
    apt-get install -y jq && \
    apt-get install -y grep && \
    apt-get install -y netcat

# Set the working directory to /app
WORKDIR /app

ADD requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
ADD . /app

# Make port 80 available to the world outside this container
EXPOSE 5802

# Run app.py when the container launches
CMD ["python","todo.py"]
