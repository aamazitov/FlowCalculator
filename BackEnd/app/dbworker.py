from app import db
from app.tables import Calculation, Radius, Time, Temperature, Pressure


def get_calculations() -> list:
    calculations = Calculation.query.all()
    result = []

    for calc in calculations:
        result.append({"calc_id": calc.id, "calc_name": calc.name, "calc_date": calc.calc_date})

    return result


def get_radiuses(calc_id) -> list:
    radiuses = db.session.execute(db.Select(Radius).filter_by(calc_id=calc_id)).scalars()

    result = []

    for radius in radiuses:
        result.append({"radius_id": radius.id, "radius_value": radius.value})

    return result


def get_times(calc_id) -> list:
    times = db.session.execute(db.Select(Time).filter_by(calc_id=calc_id)).scalars()

    result = []

    for time in times:
        result.append({"time_id": time.id, "time_value": time.value})

    return result


def get_pressure_by_radius(radius_id) -> list:
    pressures = db.session.execute(db.Select(Pressure).filter_by(radius_id=radius_id)).scalars()

    result = []

    for pressure in pressures:
        result.append({"time_id": pressure.time_id, "pressure_value": pressure.value})

    return result


def get_pressure_by_time(time_id) -> list:
    pressures = db.session.execute(db.Select(Pressure).filter_by(time_id=time_id)).scalars()

    result = []

    for pressure in pressures:
        result.append({"radius_id": pressure.radius_id, "pressure_value": pressure.value})

    return result


def get_temperature_by_radius(radius_id) -> list:
    temperatures = db.session.execute(db.Select(Temperature).filter_by(radius_id=radius_id)).scalars()

    result = []

    for temperature in temperatures:
        result.append({"time_id": temperature.time_id, "temperature_value": temperature.value})

    return result


def get_temperature_by_time(time_id) -> list:
    temperatures = db.session.execute(db.Select(Temperature).filter_by(time_id=time_id)).scalars()

    result = []

    for temperature in temperatures:
        result.append({"radius_id": temperature.radius_id, "temperature_value": temperature.value})

    return result
