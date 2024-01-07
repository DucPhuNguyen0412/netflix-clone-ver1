# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /code/
COPY . /code/

# Collect static files
RUN python manage.py collectstatic --no-input

# Make sure the entrypoint script is executable
COPY entrypoint.sh /code/
RUN chmod +x /code/entrypoint.sh

# Set the entrypoint script to be executed
ENTRYPOINT ["/code/entrypoint.sh"]

# Run the application
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "netflix_site.wsgi:application"]
