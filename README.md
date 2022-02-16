# dog-vs-cat-flask-api

<p align="center"><img src = 'https://github.com/lobvh/dog-vs-cat-flask-api/blob/main/readme-image/cute-doggie.png?raw=true' width = 400 height = 400></p>


A responsive Flask API to showcase usage of pretrained model to make inference. A dog-cat classifier is already trained via transfer learning techniques and I skipped the nouances of that. Imported the model as 'pickle file'.

You can train and use your own dog-cat classifier (remember to change the variable names!) OR ask me to upload mine, since GitHub doesn't allows to upload larger files (25+ MB). 

Used Bootstrap to create visualy appealing API, fast-ai library to train a model and it's functionality for making predictions on pretrained model. 

To run this, cd to working directory and type 'python api.py'. You will be provided with a local server (ex. http://127.0.0.1:12000/). Follow that 'link'.

Be advised that if you put a picture of something that is not cat/dog you might get gibberish results. As expected, since layers hold the nouances of dogs and cats, and can't generalize.

Good luck, and feel free to ask me if you have any questions!
