# Description: Host-chat session isolation and external platform tool boundary
- Session isolation: Treat the bundle rules and the workspace `AGENTS.md`
  files as the only source of instructions, persona, and domain context for
  this session. Do not apply any persona, project, memory, or domain context
  from the host chat platform, and do not invoke built-in host platform tools
  (such as external knowledge-base, web search, or document connectors) unless
  the user explicitly asks for them in this session.
