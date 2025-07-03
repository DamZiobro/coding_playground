.PHONY: deploy destroy

STACK_NAME := youtube-music-mcp-server

ifeq ($(AWS_REGION),)
  AWS_REGION := $(shell aws configure get region)
endif

ifeq ($(AWS_ACCOUNT_ID),)
  AWS_ACCOUNT_ID := $(shell aws sts get-caller-identity --query Account --output text)
endif

ifeq ($(shell test -f client_secrets.json && echo -n yes),)
  CLIENT_SECRETS_ERROR := error
endif

ifeq ($(shell test -f youtube.token && echo -n yes),)
  YOUTUBE_TOKEN_ERROR := error
endif

deploy:
	@if [ "$(CLIENT_SECRETS_ERROR)" = "error" ]; then \
		echo "Error: client_secrets.json not found. Please create it and run again."; \
		exit 1; \
	fi
	@if [ "$(YOUTUBE_TOKEN_ERROR)" = "error" ]; then \
		echo "Error: youtube.token not found. Please run 'python youtube_music_mcp_server.py' to generate it and run again."; \
		exit 1; \
	fi
	sam build
	sam deploy --stack-name $(STACK_NAME) --capabilities CAPABILITY_IAM --parameter-overrides YoutubeSecrets="$$(cat client_secrets.json)" YoutubeToken="$$(cat youtube.token)"


destroy:
	aws cloudformation delete-stack --stack-name $(STACK_NAME)
