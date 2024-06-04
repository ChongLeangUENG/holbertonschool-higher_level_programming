# Use the same Alpine base image as before
FROM alpine:latest

# Install curl package
RUN apk add --no-cache curl

# Copy the configuration file into the container
COPY config.txt /app/config.txt

# Define the default command to keep the container running
CMD ["sh"]

