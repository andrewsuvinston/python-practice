# Python Practice — Learning Repository

A working repository of Python projects I've built while learning software
engineering, with a focus on problems relevant to Electronics and
Communication Engineering (ECE), embedded systems, and robotics.

This is not a showcase repo — it's a **learning journal**. Some files here
are finished, some are exercises, some are experiments. The point is not
polish. The point is progress, documented commit-by-commit.

## Why this repo exists

I am a first-year ECE student. My long-term goals are:

- GATE EC with a strong rank
- Embedded systems and robotics
- AI engineering and research
- High-value internships
- A GitHub portfolio that shows real work, not tutorial copies

Every project in this repo is built with those goals in mind — even the
small ones. A resistor color code calculator is not exciting by itself,
but the debugging discipline it teaches carries over to firmware bring-up,
protocol analysis, and everything else in embedded work.

## The rules of this repo

1. **No copy-pasting finished code.** AI is used as a tutor and debugger
   (see "AI usage" below), not as a code generator.
2. **Every project is finished before a new one starts.** Half-built
   projects don't get merged. The whole point is to build the habit of
   finishing.
3. **Every project has tests.** Even if those tests are just a table in
   the README with input → expected output.
4. **Every commit is honest.** WIP commits are fine. "Cleared All the
   Error" is a real commit message in this repo. The history is the
   work.
5. **Documentation is part of the project.** Not an afterthought.

## Projects

### 1. Resistor Color Code Calculator — `resistor_color_code.py`

**Status:** Finished
**Concepts:** dictionaries, functions, parameters, string manipulation,
input validation, reverse lookups, exponential formulas, variable scope

A command-line tool that encodes and decodes 4-band resistor color codes,
with validation and a representability check that rejects values a 4-band
resistor physically cannot encode (e.g. `1234 Ω`).

**Run it:**

    python resistor_color_code.py

**Example:**

    Choose Mode:
    1.decode colors to resistance
    2.Encode resistance to colors
    Type the number : 2
    Enter the Resistance(Eg:4700): 4700
    Enter the Tolerance(if there is no tolerance then enter none): 5
    yellow violet red gold

**Highlights:**
- 19 real bugs documented in commit history, from `NameError` through
  `UnboundLocalError` to a silent wrong-answer bug on non-representable
  values
- Edge cases handled: 1 Ω (gold multiplier), no-tolerance resistors,
  garbage input, non-representable values
- Full bug log with symptom → cause → fix → lesson in the commit messages

**Known limitations:**
- 4-band only (no 5-band or 6-band)
- Interactive prompt only, no batch or file input
- Does not suggest nearest standard value for non-representable inputs
- Trailing space in output when tolerance is `none` (cosmetic)

### 2. Practice — `Practice.py`

**Status:** Exercises
**Concepts:** basic functions, parameters, arithmetic

Small practice functions (`square`, `cube`) written while learning how
function parameters actually work versus reading globals. Kept in the
repo as a record of early learning.

### 3. Basic Check Page — `Basic Check Page.py`

**Status:** [Fill in — describe what this file does and whether you plan
to keep or remove it. If it's leftover/obsolete, delete it from the repo
and remove this section.]

## How to run

All projects here are standalone Python scripts. Pick any file and run:

    python <filename>.py

Requires Python 3.8+. No external libraries used so far.

## Commit history

The commit log in this repo is the most honest record of what went into
these projects. You'll find:

- WIP commits before fixes
- Commit messages like "Cleared All the Error" and "Checked the code"
- Reverts and rewrites
- Days where the code was broken and got committed anyway

This is not a bug — it's the **point**. A clean repo with one commit per
project usually means someone pasted the code. A repo with thirty commits
across weeks means someone actually built it.

## Upcoming projects

These are planned but not started yet. Listed here to hold myself
accountable:

- [ ] **Bit Manipulation Toolkit** — set/clear/toggle/read bits, with
      binary and hex display. Foundation for embedded register writes.
- [ ] **LED Series Resistor Calculator** — Ohm's law applied to LED
      current-limiting resistor selection.
- [ ] **Intel HEX Parser** — parse and validate Intel HEX firmware files.
- [ ] **UART Packet Analyzer** — parse a hex stream, extract packets,
      validate XOR checksum.
- [ ] **GPIO Register Simulator** — simulate a microcontroller GPIO
      register in pure Python (later ported to C).

## AI usage policy

AI is used in this repo as a **mentor and debugger**, not a code
generator. Specifically:

- AI explains concepts, points at lines to investigate, and asks
  debugging questions — it does not write the finished solution.
- Every line of code in this repo was typed by me. Broken versions
  included.
- I run every test myself, read every traceback myself, and diagnose
  every error before fixing it.
- The commit history is the evidence: no one copy-pastes through 20
  debugging rounds across multiple weeks.

The goal is to develop independent problem-solving, not to ship a script
in the shortest possible time.

## About the author

First-year ECE student, building toward a career in embedded systems and
robotics. If you're reading this and want to talk shop, feel free to open
an issue on this repo.

## License

MIT