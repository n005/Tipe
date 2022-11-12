/// Kepler orbit calculator
pub struct Kepler {
    a: f64, ///< semi-major axis
    e: f64, ///< eccentricity
    i: f64, ///< inclination
    omega: f64, ///< longitude of the ascending node
    pomega: f64, // argument of perihelion
}

impl Kepler {
    pub fn new(a: f64, e: f64, i: f64, omega: f64, pomega: f64) -> Self{
        Self {
            a,
            e,
            i,
            omega,
            pomega,
        }
    }
}

/*Satelite position vector*/
pub fn satpos (kepler: &Kepler, E: &f64) -> (f64, f64, f64) { ///< with E eccentric anomaly
    let xhi= kepler.a*(E.cos()-kepler.e);
    let eta= kepler.a*(1.0-kepler.e.powf(2.0)).sqrt()*E.sin();
    let zeta = 0f64;
    (xhi, eta, zeta)
}


/*Mean motion */
fn mean_motion (kepler: &Kepler) -> f64 {
    let mu = 3.986005e14;
    let a = kepler.a;
    (mu/a.powf(3.0)).sqrt()
}

/*Mean anomaly */
fn mean_anomaly (kepler: &Kepler, t: f64, t0: f64) -> f64 { ///< with t & t0 time
    let n = mean_motion(kepler);
    let t = t - t0;
    n*t
}

/*eccentric anomaly */
pub fn eccentric_anomaly (kepler: &Kepler, n: f64) -> f64 { ///< with n mean anomaly
    let e = kepler.e;
    n+e*n.sin()
}

/*True anomaly */
fn true_anomaly (kepler: &Kepler, E: f64) -> f64 { ///< with E eccentric anomaly
    let e = kepler.e;
    (((1.0-e.powf(2.0)).sqrt()*E.sin())/(E.cos()-e)).atan()
}

/* r norm */
fn r_norm (kepler: &Kepler, E: f64) -> f64 { ///< with E eccentric anomaly
    let e = kepler.e;
    kepler.a*(1.0-e*E.cos())
}

/*Cartesian coordinate */
pub fn cartesian (kepler: &Kepler, E: f64) -> (f64, f64, f64) { ///< with E eccentric anomaly
    let r = r_norm(kepler, E);
    let f = true_anomaly(kepler, E);
    let x = r*f.cos();
    let y = r*f.sin();
    let z = 0f64;
    (x, y, z)
}
