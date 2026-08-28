
DROP TABLE IF EXISTS insurance_loss_stat;
DROP TABLE IF EXISTS insurance_contract_stat;
DROP TABLE IF EXISTS coverage_master;
DROP TABLE IF EXISTS insurance_product;
DROP TABLE IF EXISTS car_value_factor;
DROP TABLE IF EXISTS car_master;
DROP TABLE IF EXISTS coverage_master;

CREATE TABLE car_master (
    car_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    maker_name VARCHAR(50) NOT NULL,
    model_name VARCHAR(100) NOT NULL,
    origin_type VARCHAR(10) NOT NULL,
    body_type VARCHAR(10) NOT NULL,
    vehicle_class VARCHAR(10) NOT NULL,
    base_price INT NOT NULL,
    eco_flag CHAR(1) NOT NULL DEFAULT 'N',
    eco_fuel_type VARCHAR(30) NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT uq_car_master UNIQUE (maker_name, model_name),

    CONSTRAINT ck_car_master_origin_type
        CHECK (origin_type IN ('국산', '외산')),

    CONSTRAINT ck_car_master_body_type
        CHECK (body_type IN ('승용', '승합')),

    CONSTRAINT ck_car_master_vehicle_class
        CHECK (vehicle_class IN ('소형', '중형', '대형', '다인승')),

    CONSTRAINT ck_car_master_eco_flag
        CHECK (eco_flag IN ('Y', 'N')),

    CONSTRAINT ck_car_master_base_price
        CHECK (base_price >= 0)
);

CREATE TABLE car_value_factor (
    origin_type VARCHAR(10) NOT NULL,
    body_type VARCHAR(10) NOT NULL,
    model_year INT NOT NULL,
    residual_value_rate DECIMAL(6,4) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    PRIMARY KEY (origin_type, body_type, model_year),

    CONSTRAINT ck_car_value_factor_origin_type
        CHECK (origin_type IN ('국산', '외산')),

    CONSTRAINT ck_car_value_factor_body_type
        CHECK (body_type IN ('승용', '승합')),

    CONSTRAINT ck_car_value_factor_model_year
        CHECK (model_year >= 1900),

    CONSTRAINT ck_car_value_factor_rate
        CHECK (residual_value_rate >= 0 AND residual_value_rate <= 1)
);

CREATE TABLE insurance_product (
    insurance_product_id INT AUTO_INCREMENT PRIMARY KEY,
    insurance_product_name VARCHAR(20) NOT NULL,

    CONSTRAINT uq_insurance_product_name UNIQUE (insurance_product_name),

    CONSTRAINT ck_insurance_product_name
        CHECK (insurance_product_name IN ('개인용', '업무용', '영업용'))
);

CREATE TABLE coverage_master (
    coverage_id INT AUTO_INCREMENT PRIMARY KEY,
    coverage_name VARCHAR(30) NOT NULL,
    coverage_group VARCHAR(10) NOT NULL,

    CONSTRAINT uq_coverage_name UNIQUE (coverage_name),

    CONSTRAINT ck_coverage_group
        CHECK (coverage_group IN ('인담보', '물담보'))
);

CREATE TABLE insurance_contract_stat (
    contract_stat_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    stat_year_month CHAR(6) NOT NULL,
    insurance_product_id INT NOT NULL,
    coverage_id INT NOT NULL,
    gender_code CHAR(1) NOT NULL,
    age_group VARCHAR(20) NOT NULL,
    origin_type VARCHAR(10) NOT NULL,
    vehicle_class VARCHAR(10) NOT NULL,
    join_count BIGINT NOT NULL,
    earned_premium_amount BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_contract_stat_insurance_product
        FOREIGN KEY (insurance_product_id)
        REFERENCES insurance_product (insurance_product_id),

    CONSTRAINT fk_contract_stat_coverage
        FOREIGN KEY (coverage_id)
        REFERENCES coverage_master (coverage_id),

    CONSTRAINT uq_contract_stat UNIQUE (
        stat_year_month,
        insurance_product_id,
        coverage_id,
        gender_code,
        age_group,
        origin_type,
        vehicle_class
    ),

    CONSTRAINT ck_contract_stat_gender_code
        CHECK (gender_code IN ('M', 'F')),

    CONSTRAINT ck_contract_stat_age_group
        CHECK (
            age_group IN (
                '20대 이하',
                '30대',
                '40대',
                '50대',
                '60대',
                '70대 이상'
            )
        ),

    CONSTRAINT ck_contract_stat_origin_type
        CHECK (origin_type IN ('국산', '외산')),

    CONSTRAINT ck_contract_stat_vehicle_class
        CHECK (vehicle_class IN ('소형', '중형', '대형', '다인승')),

    CONSTRAINT ck_contract_stat_join_count
        CHECK (join_count >= 0)
);

CREATE TABLE insurance_loss_stat (
    loss_stat_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    stat_year_month CHAR(6) NOT NULL,
    insurance_product_id INT NOT NULL,
    coverage_id INT NOT NULL,
    vehicle_class VARCHAR(10) NOT NULL,
    loss_amount BIGINT NOT NULL,
    injury_partial_count BIGINT NOT NULL,
    death_total_loss_count BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT fk_loss_stat_insurance_product
        FOREIGN KEY (insurance_product_id)
        REFERENCES insurance_product (insurance_product_id),

    CONSTRAINT fk_loss_stat_coverage
        FOREIGN KEY (coverage_id)
        REFERENCES coverage_master (coverage_id),

    CONSTRAINT uq_loss_stat UNIQUE (
        stat_year_month,
        insurance_product_id,
        coverage_id,
        vehicle_class
    ),

    CONSTRAINT ck_loss_stat_vehicle_class
        CHECK (vehicle_class IN ('소형', '중형', '대형', '다인승'))
);
