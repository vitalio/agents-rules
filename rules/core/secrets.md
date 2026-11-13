# Description: Progress reporting and strict credential/secret protection
- **Progress & secrets:** Report periodic progress on long-running operations. Never print credentials, secret files, or tokens, or enable command-trace logging around secrets; if a credential is ever exposed in chat, warn the user immediately to rotate it.
