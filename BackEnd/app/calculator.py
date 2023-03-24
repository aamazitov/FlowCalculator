from app.data import Data
from app import db
from app.tables import Calculation, Radius, Time, Pressure, Temperature


class Calculator:
    def __init__(self, n, m):
        self.N = n
        self.M = m
        self.data = None

    def get_data(self):
        return self.data

    def calc(self) -> dict:
        self.data = Data()

        calculation = Calculation(name="my_calc")
        db.session.add(calculation)

        N = self.N
        M = self.M
        tk = 86400  # s
        R = 100  # m
        rw = 0.102  # m
        k = 10e-12  # m^-1
        mu = 1.1 * 10e-3  # попробовать 3
        fi = 0.2
        c = 1.58 * 10e-9
        P0 = 25331250
        Pr = 30397500

        cp = 1.4  # МДж/(м3*К)
        lam = 0.6  # Вт/(м*К)
        eps = 3.947693066864051e-7  # К/Па  0.04 K/атм
        nu = 3.158154453491241e-7  # К/Па 0.032 K/атм
        T0 = 363.15  # К
        Tr = 368.15  # К
        # фиктивные ячейки - посмотреть

        h = (R - rw) / (N - 1)
        tau = tk / M

        radius4db = []
        time4db = []

        P = []
        T = []
        r = []

        time = 0

        time_db = Time(value=time, calc=calculation)
        time4db.append(time_db)

        i = 1
        while i < N + 1:
            P.append(P0)
            T.append(T0)
            r.append(rw + (i - 1) * h)
            radius_db = Radius(value=rw + (i - 1) * h, calc=calculation)
            db.session.add(radius_db)
            radius4db.append(radius_db)
            pressure_db = Pressure(value=P0, radius=radius_db, time=time_db)
            db.session.add(pressure_db)
            temperature_db = Temperature(value=T0, radius=radius_db, time=time_db)
            db.session.add(temperature_db)
            i = i + 1

        self.data.init_radius(r)
        self.data.append_time(time)
        self.data.append_pressure(P)

        while tk > time:
            time = time + tau
            time_db = Time(value=time, calc=calculation)
            db.session.add(time_db)
            time4db.append(time_db)

            alpha = []
            beta = []

            alpha.append(1.0)  # alpha[0]
            beta.append(0.0)  # beta[0]

            i = 2

            while i < N:
                A_i = ((k / mu) * (2 * rw + 2 * i * h - h)) / ((h * h) * (2 * rw + 2 * i * h - 2 * h))
                C_i = ((k / mu) * (2 * rw + 2 * i * h - 3 * h)) / ((h * h) * (2 * rw + 2 * i * h - 2 * h))
                B_i = A_i + C_i + fi * c / tau
                F_i = (-1) * (fi * c * P[i - 1]) / tau
                alpha.append(A_i / (B_i - C_i * alpha[i - 2]))
                beta.append((C_i * beta[i - 2] - F_i) / (B_i - C_i * alpha[i - 2]))
                i = i + 1

            P[N - 1] = Pr
            pressure_db = Pressure(value=Pr, radius=radius4db[N - 1], time=time_db)
            db.session.add(pressure_db)

            i = N - 2
            while i >= 0:
                P[i] = alpha[i] * P[i + 1] + beta[i]
                pressure_db = Pressure(value=P[i], radius=radius4db[i], time=time_db)
                db.session.add(pressure_db)
                i = i - 1

            self.data.append_time(time)
            self.data.append_pressure(P)

        time = 0

        self.data.append_temperature(T)

        j = 1
        while tk > time:
            time = time + tau

            alpha = []
            beta = []

            alpha.append(1.0)  # alpha[0]
            beta.append(0.0)  # alpha[0]

            i = 2

            while i < N:
                u_i = (-1) * k * mu * self.data.get_der_p_r(time, i, h)
                A_i = lam / ((h * h) * (rw + (i - 1) * h))
                C_i = lam / ((h * h) * (rw + (i - 1) * h))
                B_i = (2 * lam) / ((h * h) * (rw + (i - 1) * h)) + (cp * (u_i + 1)) / tau
                F_i = cp * u_i * eps * self.data.get_der_p_r(time, i, h) - nu * fi * cp * self.data.get_der_p_t(time, i,
                                                                                                              tau) \
                      - cp * T[i - 1] / tau - cp * u_i * T[i - 1] / tau
                alpha.append(A_i / (B_i - C_i * alpha[i - 2]))
                beta.append((C_i * beta[i - 2] - F_i) / (B_i - C_i * alpha[i - 2]))
                i = i + 1

            T[N - 1] = Tr

            temperature_db = Temperature(value=Tr, radius=radius4db[N - 1], time=time4db[j])
            db.session.add(temperature_db)

            i = N - 2
            while i >= 0:
                T[i] = alpha[i] * T[i + 1] + beta[i]
                temperature_db = Temperature(value=T[i], radius=radius4db[i], time=time4db[j])
                db.session.add(temperature_db)
                i = i - 1

            self.data.append_temperature(T)

            j = j + 1

        db.session.commit()

        return {"calc_id": calculation.id, "radius_id": radius4db[N - 1].id, "time_id": time4db[M].id}
