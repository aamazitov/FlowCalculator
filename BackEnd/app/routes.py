from app import app
from app.calculator import Calculator
from app.dbworker import get_calculations, get_radiuses, get_times, get_pressure_by_radius, get_pressure_by_time, \
    get_temperature_by_radius, get_temperature_by_time
from flask import jsonify

calculator = Calculator(10, 10)


@app.route("/")
@app.route("/index")
def index():
    return "Hello User!"


# Запускает расчет
@app.route("/calc")
def calc():
    # calculator.calc()
    # data = calculator.get_data()
    # return jsonify(
    #    radius=data.get_radius(),
    #    time=data.get_time(),
    # )
    return calculator.calc()


# Хуета
# @app.route("/result/time/<time>")
# def get_result_by_time(time=None):
#    return jsonify(
#        pressure=calculator.get_data().get_pressure_by_time(time=float(time)),
#        temperature=calculator.get_data().get_temperature_by_time(time=float(time)),
#    )
#
#
# @app.route("/result/radius/<radius>")
# def get_result_by_radius(radius=None):
#    return jsonify(
#        pressure=calculator.get_data().get_pressure_by_radius(radius=float(radius)),
#        temperature=calculator.get_data().get_temperature_by_radius(radius=float(radius)),
#    )


# Возвращает список расчетов
@app.route("/calculations")
def get_calcs():
    return get_calculations()


# Возвращает список радиусов по идентификатору расчета
@app.route("/calculations/<calc_id>/radiuses")
def get_rads(calc_id):
    return get_radiuses(calc_id)


# Возвращает список времен по идентификатору расчета
@app.route("/calculations/<calc_id>/times")
def get_time(calc_id):
    return get_times(calc_id)


# Возвращает давление по радиусу
@app.route("/radiuses/<radius_id>/pressures")
def get_pressure_radius(radius_id):
    return get_pressure_by_radius(radius_id=radius_id)


# Возвращает давление по времени
@app.route("/times/<time_id>/pressures")
def get_pressure_time(time_id):
    return get_pressure_by_time(time_id=time_id)


# Возвращает температуру по радиусу
@app.route("/radiuses/<radius_id>/temperatures")
def get_temperature_radius(radius_id):
    return get_temperature_by_radius(radius_id=radius_id)


# Возвращает температуру по времени
@app.route("/times/<time_id>/temperatures")
def get_temperature_time(time_id):
    return get_temperature_by_time(time_id=time_id)
