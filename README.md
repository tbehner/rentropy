# rentropy
A small wrapper around the rust [entropy crate](https://crates.io/crates/entropy) with [PyO3](https://github.com/PyO3/pyo3).

## Usage

```
    import rentropy
    rentropy.eta(b"Hello, world!")
```

calculates the [Shannon entropy](https://en.wikipedia.org/wiki/Entropy_(information_theory)) of `b"Hello, world!"`.

## Setup
```
    pip install rentropy
```

## Build
Use [just](https://crates.io/crates/just) to build wheels for CPython 3.5, 3.6
and 3.7 with manylinux.

```
    just build
```
