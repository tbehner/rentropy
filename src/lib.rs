use entropy::shannon_entropy;

use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

#[pyfunction]
/// Formats the sum of two numbers as string
fn eta(inp: Vec<u8>) -> PyResult<f32> {
    Ok(shannon_entropy(&inp))
}

/// This module is a python module implemented in Rust.
#[pymodule]
fn rentropy(py: Python, m: &PyModule) -> PyResult<()> {
    m.add_wrapped(wrap_pyfunction!(eta))?;

    Ok(())
}

#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        assert_eq!(2 + 2, 4);
    }
}
