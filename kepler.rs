/// Kepler orbit calculator
struct Kepler {
    a: f64, ///< semi-major axis
    e: f64, ///< eccentricity
    i: f64, ///< inclination
    Omega: f64, ///< longitude of the ascending node
    omega: f64, ///< argument of perihelion
    E: f64, ///< eccentric anomaly
}

impl Kepler {
    fn new(a: f64, e: f64, i: f64, Omega: f64, omega: f64, f: f64) -> Self{
        Self {
            a,
            e,
            i,
            Omega,
            omega,
            f
        }
    }
}

/*Satelite position vector*/
fn satpos (kepler: &Kepler) -> (f64, f64, f64) {
    let xhi= kepler.a*(cos(kepler.E)-kepler.e);
    let eta= kepler.a*sqrt(1-kepler.e.pow(2))*sin(kepler.E);
    let zeta = 0;
    (xhi, eta, zeta)
}