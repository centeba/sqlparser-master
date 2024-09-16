# Use the official PostgreSQL image for Windows
FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Set environment variables
ENV POSTGRES_USER=admin
ENV POSTGRES_PASSWORD=admin
ENV POSTGRES_DB=wma0_1
ENV POSTGRES_DIR=C:\Apps\Temp\PostgresQL\15

# Install PostgreSQL
RUN mkdir POSTGRES_DIR
WORKDIR C:/Apps/Temp/PostgresQL/15
ADD https://get.enterprisedb.com/postgresql/postgresql-14.1-1-windows-x64-binaries.zip POSTGRES_DIR
RUN Expand-Archive -Path POSTGRES_DIR\postgresql-14.1-1-windows-x64-binaries.zip -DestinationPath POSTGRES_DIR
RUN del POSTGRES_DIR\postgresql-14.1-1-windows-x64-binaries.zip

# Add PostgreSQL bin directory to the PATH
RUN setx /M PATH "%PATH%;POSTGRES_DIR\pgsql\bin"

# Initialize database
RUN initdb -D C:\Program Files\PostgresQL\15/data

# Expose PostgreSQL port
EXPOSE 5432

# Start PostgreSQL server
CMD ["postgres", "-D", "WORKDIR/data"]



docker run --name pgdev -e POSTGRES_PASSWORD -d -p 5432:5432 -v C:\apps\Docker\pgdev

# Python install

# Pull base image
FROM python:3.11.5-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV NAME World
ENV VIRTUAL_ENV=./venv

# Set work directory in the container
WORKDIR /code

# Switch on virtual environment
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "app.py"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
