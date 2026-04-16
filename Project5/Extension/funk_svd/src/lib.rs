use ndarray::Array2;
use numpy::PyArrayMethods;
use numpy::{PyArray2, PyReadonlyArray2};
use pyo3::prelude::*;

#[pymodule]
mod funk_svd {

    use super::*;

    #[pyfunction]
    fn fit<'py>(
        py: Python<'py>,
        a: PyReadonlyArray2<'py, f64>,
        u: &Bound<'py, PyArray2<f64>>,
        i_mat: &Bound<'py, PyArray2<f64>>,
        step: f64,
        n_iter: usize,
        reg: f64,
    ) -> PyResult<()> {
        let a = a.as_array();
        let mut u = unsafe { u.as_array_mut() };
        let mut i_mat = unsafe { i_mat.as_array_mut() };

        let (n_rows, n_cols) = a.dim();
        let k = u.shape()[1];

        // precompute nonzero indices
        let mut indices: Vec<(usize, usize)> = Vec::new();
        for i in 0..n_rows {
            for j in 0..n_cols {
                if a[[i, j]] != 0.0 {
                    indices.push((i, j));
                }
            }
        }

        for _ in 0..n_iter {
            for &(i, j) in &indices {
                // compute prediction
                let pred: f64 = (0..k).map(|f| u[[i, f]] * i_mat[[f, j]]).sum();
                let e = a[[i, j]] - pred;

                // freeze current values
                let u_row: Vec<f64> = (0..k).map(|f| u[[i, f]]).collect();
                let i_col: Vec<f64> = (0..k).map(|f| i_mat[[f, j]]).collect();

                for f in 0..k {
                    u[[i, f]] -= step * -(e * i_col[f] - reg * u_row[f]);
                    i_mat[[f, j]] -= step * -(e * u_row[f] - reg * i_col[f]);
                }
            }
        }

        Ok(())
    }
}
