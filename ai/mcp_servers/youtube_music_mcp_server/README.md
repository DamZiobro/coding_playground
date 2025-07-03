# YouTube Music MCP Server

This MCP server provides tools to interact with YouTube Music.

## Features

- **List my playlists containing selected word**: Find playlists in your YouTube Music library that contain a specific word in their title.
- **List the songs containing specified word**: Search for songs in your YouTube Music library that contain a specific word in their title.

## Deployment

This server is designed to be deployed to AWS Lambda and exposed via an API Gateway.

### Prerequisites

- AWS Account
- Python 3.10 or higher
- `pip` for installing packages
- AWS CLI configured

### Deployment Steps

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up YouTube API credentials:**
   - Follow the instructions [here](https://developers.google.com/youtube/v3/getting-started) to create a project and enable the YouTube Data API v3.
   - Create an OAuth 2.0 client ID and download the `client_secrets.json` file.
   - Place the `client_secrets.json` file in the root of the project directory.
   - Run the following command to authorize the application and generate a `youtube.token` file:
     ```bash
     python youtube_music_mcp_server.py
     ```
     This will open a browser window for you to authorize the application. After authorization, a `youtube.token` file will be created.

4. **Deploy to AWS:**
   ```bash
   make deploy
   ```

### Destroy the deployment

To remove the deployed stack from AWS, run:

```bash
make destroy
```

## Configuration with Gemini CLI

To use this MCP server with the Gemini CLI, you need to configure it in the `~/.gemini/config.json` file. Add the following to the `mcp_servers` section:

```json
{
  "mcp_servers": {
    "youtube_music": {
      "url": "YOUR_API_GATEWAY_URL",
      "headers": {
        "x-api-key": "YOUR_API_KEY"
      }
    }
  }
}
```

Replace `YOUR_API_GATEWAY_URL` with the URL of your deployed API Gateway and `YOUR_API_KEY` with the API key that is output from the `make deploy` command.

## Solution Architecture

The solution consists of the following components:

- **Gemini CLI**: The client that interacts with the MCP server.
- **Amazon API Gateway**: An HTTP API that acts as the entry point for the MCP server.
- **AWS Lambda**: A serverless compute service that hosts the MCP server logic.

The Gemini CLI sends requests to the API Gateway, which triggers the Lambda function. The Lambda function then interacts with the YouTube Music API to fulfill the request and returns the response to the Gemini CLI.

## AWS Resources

The following AWS resources will be created when you deploy this solution:

- **AWS::Serverless::Function**: The Lambda function that contains the MCP server logic.
- **AWS::ApiGatewayV2::Api**: The HTTP API Gateway that exposes the Lambda function.
- **AWS::ApiGatewayV2::Stage**: The default stage for the API Gateway.
- **AWS::ApiGatewayV2::Integration**: The integration between the API Gateway and the Lambda function.
- **AWS::Lambda::Permission**: The permission that allows the API Gateway to invoke the Lambda function.
- **AWS::IAM::Role**: The IAM role that grants the Lambda function permission to execute.

## Cost Estimation

This solution is designed to be very cost-effective and should fall within the AWS Free Tier for most use cases.

- **AWS Lambda**: The AWS Free Tier includes 1 million free requests per month and 400,000 GB-seconds of compute time per month. The Lambda function is configured with a low memory setting, so it is unlikely to exceed the free tier limits with normal usage.
- **Amazon API Gateway**: The AWS Free Tier for API Gateway includes 1 million HTTP API calls per month for up to 12 months. After that, the cost is very low.
- **AWS CloudFormation**: There is no additional charge for using AWS CloudFormation. You only pay for the AWS resources that you create.
- **YouTube Data API**: The YouTube Data API has a quota system. You can find more information about the quota usage [here](https://developers.google.com/youtube/v3/getting-started#quota).

**Disclaimer:** The actual cost will depend on your usage. Please refer to the official AWS pricing pages for the most up-to-date information.
