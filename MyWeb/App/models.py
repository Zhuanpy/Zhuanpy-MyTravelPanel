from .exts import db


class AirportData(db.Model):
    # 表名
    __tablename__ = 'airport_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    airport_IATA = db.Column(db.String(3), unique=True, index=True)  # IATA 代码一般为3个字符
    city_name = db.Column(db.String(100), index=True)  # 假设城市名不会超过100个字符
    airport_name_cn = db.Column(db.String(100))  # 假设中文机场名称不会超过100个字符
    airport_name_en = db.Column(db.String(100))  # 假设英文机场名称不会超过100个字符


# flight schedule
class FlightSchedule(db.Model):
    # 表名
    __tablename__ = 'flight_schedule'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flight_number = db.Column(db.String(10), unique=True, index=True)
    airline_code = db.Column(db.String(10))
    airline_num = db.Column(db.String(10))

    schedule_city = db.Column(db.String(20))
    schedule_timing = db.Column(db.String(15))


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

    # 主键 ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 产品名称
    name = db.Column(db.String(100), nullable=False)

    # 产品描述
    description = db.Column(db.Text, nullable=False)

    # 目的地
    destination = db.Column(db.String(100), nullable=False)

    # 出发日期
    departure_date = db.Column(db.Date, nullable=False)

    # 返回日期
    return_date = db.Column(db.Date, nullable=False)

    # 产品价格
    price = db.Column(db.Float, nullable=False)

    # 可用座位数
    available_seats = db.Column(db.Integer, nullable=False)

    # 创建时间
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # 更新时间
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<TourProductData {self.name}>'


# 系统账号数据表: system_account_data_table
class SystemAccountData(db.Model):
    # 表名
    __tablename__ = 'system_account_data'

    # 主键 ID
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # 用户名
    username = db.Column(db.String(50), unique=True, nullable=False)

    # 密码（建议存储加密后的密码）
    password_hash = db.Column(db.String(128), nullable=False)

    # 电子邮件
    email = db.Column(db.String(100), unique=True, nullable=False)

    # 用户角色（如管理员、普通用户等）
    role = db.Column(db.String(20), nullable=False)

    # 账号状态（如激活、禁用等）
    status = db.Column(db.String(20), nullable=False, default='active')

    # 创建时间
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # 更新时间
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<SystemAccountData {self.username}>'
