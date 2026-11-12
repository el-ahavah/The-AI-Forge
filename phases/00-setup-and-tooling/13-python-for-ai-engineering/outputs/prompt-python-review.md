---
name: prompt-python-review
description: Review AI and data Python code for silent bugs, reproducibility, data leakage, and performance
phase: 0
lesson: 13
---

Review the Python file or code supplied by the user. Focus on correctness before style.

Check these categories:

1. **Shared mutable objects**
   - Names that unexpectedly refer to the same list, dictionary, or set.
   - Nested lists created with `[[value] * columns] * rows`.
   - Mutable function defaults such as `items=[]` or `cache={}`.
   - Dataclass mutable fields without `field(default_factory=...)`.

2. **Iterators and generators**
   - A generator, iterator, `zip`, or `map` object that is consumed more than once.
   - A generator reused across training epochs instead of being recreated.
   - A list built only to feed `sum`, `min`, `max`, `any`, or `all`.

3. **Reproducibility**
   - Random operations with no fixed seed when repeatability is required.
   - Global random state changed inside reusable library code.
   - A split function that shuffles the caller's input list in place.

4. **Train/test separation**
   - Feature means, standard deviations, vocabularies, or other preprocessing statistics calculated using test data.
   - Records that appear in both train and test splits.

5. **Files and parsing**
   - Files opened without a context manager or explicit UTF-8 encoding.
   - CSV parsed with `line.split(",")` instead of the `csv` module.
   - Numeric CSV values used without conversion.
   - Missing or unexpected columns silently accepted.

6. **Exceptions and numeric safety**
   - Broad exception handlers that hide errors.
   - Division by zero or zero standard deviation.
   - Vectors with mismatched lengths silently truncated by `zip`.

7. **Performance**
   - Large pure-Python numerical loops where NumPy vectorization would be appropriate.
   - Unnecessary intermediate lists.
   - Timing based on one run rather than repeated measurements.

Report findings in this format:

| Location | Problem | Why it matters | Suggested fix |
|---|---|---|---|

Order findings by risk: incorrect results, reproducibility, data leakage, performance, then maintainability. Provide paste-ready fixes. Do not invent facts about data size or runtime environment; ask when those facts are necessary.

Finish with one command or small test that verifies the most important correction.
