# APIs & Keys

Course lesson: [APIs & Keys](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/00-setup-and-tooling/04-apis-and-keys/docs/en.md)

**Date:** 2026-11-03  
**Quiz:** 3/3

## What I learned

An API lets one program send a request to a service and receive a response. An LLM request includes the endpoint, authentication, a model and message, and a token limit. The response includes generated content and usage information such as input and output token counts.

An API key is a credential that identifies the account and authorizes requests. Keep it out of source code and notebooks. For local development, store it in an environment variable or a `.env` file excluded by `.gitignore`. Check whether it is set without printing the key value.

An SDK handles request construction, authentication headers, JSON encoding and decoding, and API errors. A raw HTTP request makes those parts explicit. Current Anthropic documentation uses `Authorization: Bearer <key>`; the `x-api-key` header from the lesson example is also accepted.

## API errors

- **401:** The key is missing, invalid, expired, or revoked. Check that the environment variable is set and the key is valid; never print it while debugging.
- **403:** The key lacks permission for the requested resource.
- **429:** A rate or spending limit was reached. Check the error details and account limits before retrying.
- **400:** The request is malformed or uses an invalid model or message format.
- **5xx / 529:** The service has a temporary problem; wait and retry with backoff.
- **Timeout or connection error:** Check the network and endpoint, then reduce the request size or use streaming where appropriate.

## Exercise status

Compared SDK and raw HTTP request structures and completed the quiz with **3/3**. I do not have an Anthropic API key yet, so I did not create one or send a live request. The API call can be tried later after setting a key locally.

The Python and TypeScript examples are in [`code/first_api_call.py`](code/first_api_call.py) and [`code/first_api_call.ts`](code/first_api_call.ts). They default to an offline sample; pass an explicit live option only after setting a key privately.

The lesson troubleshooting artifact is in [`outputs/prompt-api-troubleshooter.md`](outputs/prompt-api-troubleshooter.md).
