# webhook-repo

This is a repo to write the webhook end point code to capture changes done on action-repo.

## Installing required libraries

Use the below code snippet in your terminal to install all the required libraries
`pip install -r requirements.txt`

## Installing MongoDB

Use the link below to download MongoDB. This will be your Database.
`https://www.mongodb.com/try/download/community`

## Installing ngrok

Use the below link to download ngrok. This will you get your webapp online.
`https://ngrok.com/download`

Use the command `ngrok http <port>` in once you start ngrok to get your site online once you run the app.

Example:
`ngrok http 5000`

## Running the app

Run the `app.py` file in the repo and setup ngrok as explained above.

By default you will land on the Index page that says `HELLO`.

Use extension to your link as shown below you can read the data stored in the DB
`/read`
