# Description: Opt-in rule to omit internal task IDs from external updates and unit test names
- No internal task IDs in external text or test names: In commit messages,
  MR/PR descriptions, chat channels, and external status updates, describe
  changes in words without internal task IDs. Name and group unit test methods
  and classes strictly by domain behavior and component invariants (such as
  `test_bundle_table_hierarchy`, `test_fullscreen_info_part_cursor`,
  `test_clipboard_prompt_action`) without backlog task-ID prefixes
  (`test_f47_...`, `test_b11_...`), updating the component's domain test when a
  contract evolves rather than accumulating ticket-numbered test methods.
