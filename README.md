# CS5356Final
Building and deploying an API that does one thing: given a URL of an image, it returns the number of colors in that image
### Requirements

The app must be able to handle any common image format: JPEG, PNG, etc.

The number of colors needs to be returned as an integer as plain text...no HTML tags, JSON, additional wording, etc.

Use the following ImageMagick command to get the number of colors: `identify -format %k <filename>`

ImageMagick unfortunately seems to return slightly different answers on different machines, so it will be checked with a 5% tolerance.

The application is deployed to AWS EC2.

Use only `t2.micro` instance types.

Don’t use more than four instances.

For a request to be considered “successful” by the scoring system, it must complete in under 15 seconds.
