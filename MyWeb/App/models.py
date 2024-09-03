from .exts import db


class User(db.Model):
    # 表名
    __tablename__ = 'db_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, index=True)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.Boolean, default=True)
    salary = db.Column(db.Float, default=1000, nullable=False)
    # 定义 columns


class AirportData(db.Model):
    # 表名
    __tablename__ = 'airport_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_name = db.Column(db.String(255), unique=True, index=True)
    airport_code_3 = db.Column(db.String(20), unique=True, index=True)
    airport_code_4 = db.Column(db.String(20), unique=True, index=True)
    airport_name_cn = db.Column(db.String(255), unique=True, index=True)
    airport_name_en = db.Column(db.String(255), unique=True, index=True)


# flight schedule
class FlightSchedule(db.Model):
    # 表名
    __tablename__ = 'flight_schedule'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_number = db.Column(db.String(255), unique=True, index=True)
    start_city = db.Column(db.String(20), unique=True, index=True)
    end_city = db.Column(db.String(20), unique=True, index=True)

    start_timing = db.Column(db.String(20), unique=True, index=True)
    end_timing = db.Column(db.String(20), unique=True, index=True)


# 供应商数据表: supplier_data_table
class SupplierData(db.Model):
    # 表名
    __tablename__ = 'supplier_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 创建时间
    create_date = db.Column(db.DateTime, index=True)
    # 最后更新日期 (last_updated)： 记录数据最后一次更新的时间，帮助保持数据的时效性。
    last_updated = db.Column(db.DateTime, index=True)

    # 供应商名字
    name = db.Column(db.String(255), index=True)
    # 供应商 地址
    address = db.Column(db.String(255), index=True)
    # 供应商联系信息
    contact_info = db.Column(db.String(255), index=True)
    # 供应商 联系人
    contact_person = db.Column(db.String(20), index=True)

    # 可以用来表示供应商是否处于活跃状态，例如：active、inactive，方便管理。
    status = db.Column(db.String(20), default='active', index=True)

    # 国家和地区 (country, region)：
    country = db.Column(db.String(50), index=True)
    region = db.Column(db.String(50), index=True)

    # 供应商评级或评价 (rating)：对供应商的服务或产品进行评级或评价，用于供应商管理的参考
    rating = db.Column(db.Float, index=True)

    # 备注 (notes)： 用于记录额外的供应商信息或与供应商的交互历史。
    notes = db.Column(db.Text)


# 旅游产品数据表: tour_product_data_table
class TourProductData(db.Model):
    # 表名
    __tablename__ = 'tour_product_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


# 系统账号数据表: system_account_data_table
class SystemAccountData(db.Model):
    # 表名
    __tablename__ = 'system_account_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
