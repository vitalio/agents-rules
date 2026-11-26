# Description: Mirrored modular test layout, domain-behavior test naming, offline in-process & fixture-cloned execution, and live dot-progress
- Mirrored test layout & domain naming: Split unit tests across modular test
  files mirroring the project's source modules. Name and group test cases and
  suites strictly by domain behavior and component invariants (such as
  `test_bundle_table_hierarchy`) without backlog task-ID prefixes
  (`test_f47_...`, `test_b11_...`), updating the component's domain test when a
  contract evolves rather than accumulating ticket-numbered test methods.
- Offline, in-process & fixture-efficient tests: Run tests completely offline
  (replacing external clients with in-memory stubs or mocks) and isolate
  filesystem writes inside temporary directories. Exercise same-runtime modules
  and CLI dispatch in-process rather than spawning child interpreter processes
  per test case. Build expensive multi-step directory fixtures once per suite
  or class and clone them into per-test working directories (or initialize them
  lazily), and share a single temporary directory across read-only
  parameterized checks.
- Live dot-progress test execution: Run the test suite so it emits compact live
  `.` progress indicators per test followed by the summary line on pass, and
  prints full diagnostics and tracebacks on failure. Never pipe test runner
  output through `tail`, `head`, or `grep` or suppress it via redirection.
