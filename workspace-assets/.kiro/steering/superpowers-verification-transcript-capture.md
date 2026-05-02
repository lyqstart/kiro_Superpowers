# Superpowers Verification Transcript Capture

## Purpose

Make verification evidence closer to Superpowers by preserving enough raw output to audit the claim.

## Transcript Location

When practical, save verification output to:

```text
.kiro/superpowers-runtime/verification/<timestamp>-<task-or-command>.log
```

If not writing a file, include a sufficient output excerpt in the response.

## Required Fields

- command
- working directory
- timestamp
- exit code
- pass count if available
- fail count if available
- skip count if available
- raw output path or excerpt
- conclusion

## Parsing Rule

If pass/fail/skip counts cannot be parsed, say how success was determined. Do not invent counts.

## Completion Rule

No COMPLETE without fresh verification evidence or explicit user-approved exception.
