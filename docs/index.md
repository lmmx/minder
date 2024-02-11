---
title: Minder
---

`Minder` is a utility library that provides two context managers to coordinate the safe handling of
exception raising.

!!! tip "Goals"

    We want to ensure:

    :material-shield-lock: **Robustness**: No errors can be raised.

    :material-sword-cross: **Containment**: Any errors that occur are handled.

    :material-head-question: **Legibility**: Error handling does not make code hard to read.

For an overview of how to robustly handle code that could fail, see [Motivation](motivation.md).

For an example of how to use it in your program see [Usage](usage/index.md).
