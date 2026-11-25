# Description: Strict credential, token, and secret protection
- Secrets & credentials: Never print credentials, secret files, or tokens, or
  enable command-trace logging around secrets; if a credential is ever exposed
  in chat or command output, warn the user immediately to rotate it.
