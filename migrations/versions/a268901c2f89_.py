"""empty message

Revision ID: a268901c2f89
Revises: 
Create Date: 2022-03-29 16:45:28.818655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a268901c2f89'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mis', sa.Column('Vehicle_production_date', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Date_of_sale', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Date_of_failure', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Actual_vehicle_mileage', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Actual_use_month_of_vehicle', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Vehicle_early_claim_information', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Date_of_replacing_the_third_stage', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Actual_mileage_of_valve', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Actual_service_month_of_valve', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Fault_Province', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Driving_route_and_road_conditions', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Fault_description_and_analysis', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Number_of_failed_valve_cylinders', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Failure_mode', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Engine_phase', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('Vehicle_factory', sa.String(length=255), nullable=True))
    op.add_column('mis', sa.Column('service_station', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mis', 'service_station')
    op.drop_column('mis', 'Vehicle_factory')
    op.drop_column('mis', 'Engine_phase')
    op.drop_column('mis', 'Failure_mode')
    op.drop_column('mis', 'Number_of_failed_valve_cylinders')
    op.drop_column('mis', 'Fault_description_and_analysis')
    op.drop_column('mis', 'Driving_route_and_road_conditions')
    op.drop_column('mis', 'Fault_Province')
    op.drop_column('mis', 'Actual_service_month_of_valve')
    op.drop_column('mis', 'Actual_mileage_of_valve')
    op.drop_column('mis', 'Date_of_replacing_the_third_stage')
    op.drop_column('mis', 'Vehicle_early_claim_information')
    op.drop_column('mis', 'Actual_use_month_of_vehicle')
    op.drop_column('mis', 'Actual_vehicle_mileage')
    op.drop_column('mis', 'Date_of_failure')
    op.drop_column('mis', 'Date_of_sale')
    op.drop_column('mis', 'Vehicle_production_date')
    # ### end Alembic commands ###
