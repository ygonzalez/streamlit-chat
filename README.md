# QA Chatbot for DIP V2


## Setup


• Clone this repository to your local machine:
`git clone https://yvette_gonzalez@bitbucket.org/pwrlab/dip-chatbot.git`

• Create a .streamlit/secrets.toml file in the root directory of the cloned repository. This file will contain any necessary secrets or configurations for your app.



## Usage


• Start the Docker containers:
`docker-compose up`

• Once the containers are up and running, navigate to `localhost:8501` in your web browser.

• You will be presented with the Codebase QA App interface. Enter your questions related to the codebase in the provided input field and submit.

• The app will utilize the RAG model to retrieve relevant information from the codebase and generate answers to your questions.

• The answers will be displayed on the screen, providing you with valuable insights and understanding of the codebase.