use entropy::shannon_entropy;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
/// Computes the Shannon entropy of bytes
fn _eta(inp: Vec<u8>) -> PyResult<f32> {
    Ok(shannon_entropy(&inp))
}

/// This module is a python module implemented in Rust.
#[pymodule]
fn rentropy(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(_eta))?;

    Ok(())
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
