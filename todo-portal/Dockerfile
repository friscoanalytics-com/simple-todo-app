# Dockerfile (Frontend)
FROM node:16-alpine

# Set working directory
WORKDIR /app

# Install dependencies
COPY package.json yarn.lock ./
RUN yarn install

# Copy project files
COPY . .

ARG REACT_APP_API_URL
ENV REACT_APP_API_URL=${REACT_APP_API_URL}

# Build the project
RUN yarn build

# Serve with a lightweight web server
RUN yarn global add serve

# Expose port
EXPOSE 3000

# Start the web server
CMD ["serve", "-s", "build", "-l", "3000"]
