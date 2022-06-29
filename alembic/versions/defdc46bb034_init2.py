"""init2

Revision ID: defdc46bb034
Revises: 
Create Date: 2022-06-21 23:15:08.364774

"""
from alembic import op
import sqlalchemy as sa
import geoalchemy2

# revision identifiers, used by Alembic.
revision = 'defdc46bb034'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mayoralties',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nomgeo', sa.String(), nullable=True),
    sa.Column('cve_mun', sa.Integer(), nullable=True),
    sa.Column('cve_ent', sa.Integer(), nullable=True),
    sa.Column('cvegeo', sa.Integer(), nullable=True),
    sa.Column('geo_point_2d', sa.String(), nullable=True),
    sa.Column('geo_shape', geoalchemy2.types.Geometry(geometry_type='POLYGON', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('municipio', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transport_units',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_updated', sa.DateTime(), nullable=True),
    sa.Column('vehicle_id', sa.Integer(), nullable=True),
    sa.Column('vehicle_label', sa.Integer(), nullable=True),
    sa.Column('vehicle_current_status', sa.Integer(), nullable=True),
    sa.Column('position_latitude', sa.Float(), nullable=True),
    sa.Column('position_longitude', sa.Float(), nullable=True),
    sa.Column('geographic_point', geoalchemy2.types.Geometry(geometry_type='POINT', srid=4326, from_text='ST_GeomFromEWKT', name='geometry'), nullable=True),
    sa.Column('position_speed', sa.Integer(), nullable=True),
    sa.Column('position_odometer', sa.Integer(), nullable=True),
    sa.Column('trip_schedule_relationship', sa.Integer(), nullable=True),
    sa.Column('trip_id', sa.Integer(), nullable=True),
    sa.Column('trip_start_date', sa.Integer(), nullable=True),
    sa.Column('trip_route_id', sa.Integer(), nullable=True),
    sa.Column('mayoralty', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_transport_units_geographic_point', table_name='transport_units')
    op.drop_table('transport_units')
    op.drop_index('idx_mayoralties_geo_shape', table_name='mayoralties')
    op.drop_table('mayoralties')
    # ### end Alembic commands ###
