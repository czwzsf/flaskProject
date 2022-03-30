from datetime import datetime

from exts import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    # repassword = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(30))
    isdelete = db.Column(db.Boolean, default=False)  # 使用逻辑删除，避免从物理意义上硬盘删除
    rdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username


class UserRoot(db.Model):
    id1 = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    # repassword = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(30))
    isdelete = db.Column(db.Boolean, default=False)  # 使用逻辑删除，避免从物理意义上硬盘删除
    rdatetime = db.Column(db.DateTime, default=datetime.now)

    def __str__(self):
        return self.username


class Mis(db.Model):
    num_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    chassis_number = db.Column(db.String(255))
    Engine_number = db.Column(db.String(255))
    Claim_No = db.Column(db.String(255))
    Claim_filing_month = db.Column(db.String(255))
    TDS = db.Column(db.String(255))
    engine_type = db.Column(db.String(255))
    Engine_production_date = db.Column(db.String(255))
    Vehicle_production_date = db.Column(db.String(255))
    Date_of_sale = db.Column(db.String(255))
    Date_of_failure = db.Column(db.String(255))
    Actual_vehicle_mileage = db.Column(db.String(255))
    Actual_use_month_of_vehicle = db.Column(db.String(255))
    Vehicle_early_claim_information = db.Column(db.String(255))
    Date_of_replacing_the_third_stage = db.Column(db.String(255))
    Actual_mileage_of_valve = db.Column(db.String(255))
    Actual_service_month_of_valve = db.Column(db.String(255))
    Fault_Province = db.Column(db.String(255))
    Driving_route_and_road_conditions = db.Column(db.String(255))
    Fault_description_and_analysis = db.Column(db.String(255))
    Number_of_failed_valve_cylinders = db.Column(db.String(255))
    Failure_mode = db.Column(db.String(255))
    Engine_phase = db.Column(db.String(255))
    Vehicle_factory = db.Column(db.String(255))
    service_station = db.Column(db.String(255))

    def __str__(self):
        return self.chassis_number
