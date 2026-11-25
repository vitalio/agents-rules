# Description: Mirrored modular test layout, domain-behavior test naming, offline in-process & fixture-cloned execution, and live dot-progress
- Mirrored test layout & domain naming: Split unit tests across modular test
  files mirroring the project's source modules rather than accumulating all
  tests into a single monolithic test file. Name and group test cases and
  suites strictly by domain behavior and component invariants (such as
  `test_bundle_table_hierarchy`, `test_clipboard_prompt_action`) without
  backlog task-ID prefixes (`test_f47_...`, `test_b11_...`), updating the
  component's domain test when a contract evolves rather than accumulating
  ticket-numbered test methods.
- Offline, in-process & fixture-efficient tests: Tests must run completely
  offline without touching the network (replace external clients with
  in-memory stubs or mocks) and isolate all filesystem writes inside temporary
  directories without mutating the repository working tree or user
  environment. Exercise same-runtime modules and CLI dispatch in-process
  rather than spawning child interpreter processes per test case. Build
  expensive multi-step directory fixtures once per suite or class and clone
  them into per-test working directories (or initialize them lazily only in
  tests that use them), and reuse a single temporary directory across
  read-only parameterized checks rather than allocating one per iteration.
- Live dot-progress test execution: Run the project test suite so it emits
  compact live `.` progress indicators per test followed by the summary line
  when all tests pass, and prints full diagnostics and tracebacks whenever any
  test fails. Never pipe test runner output through `tail`, `head`, or `grep`
  or suppress it via output redirection (which buffers live progress and
  truncates failure tracebacks).
