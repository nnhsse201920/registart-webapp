"""empty message

Revision ID: 5a2594e3f352
Revises: 
Create Date: 2020-04-21 21:57:53.784112

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a2594e3f352'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('assignments',
    sa.Column('organizerID', sa.Integer(), nullable=False),
    sa.Column('studentID', sa.Integer(), nullable=True),
    sa.Column('lastContact', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('medium', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('organizerID')
    )
    op.create_index(op.f('ix_assignments_lastContact'), 'assignments', ['lastContact'], unique=True)
    op.create_index(op.f('ix_assignments_medium'), 'assignments', ['medium'], unique=True)
    op.create_index(op.f('ix_assignments_status'), 'assignments', ['status'], unique=True)
    op.create_index(op.f('ix_assignments_studentID'), 'assignments', ['studentID'], unique=True)
    op.create_table('organizations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_organizations_name'), 'organizations', ['name'], unique=True)
    op.create_table('organizers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstN', sa.VARCHAR(length=255), nullable=True),
    sa.Column('lastN', sa.VARCHAR(length=255), nullable=True),
    sa.Column('username', sa.VARCHAR(length=255), nullable=True),
    sa.Column('organizationID', sa.Integer(), nullable=True),
    sa.Column('email', sa.VARCHAR(length=255), nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_organizers_email'), 'organizers', ['email'], unique=True)
    op.create_index(op.f('ix_organizers_firstN'), 'organizers', ['firstN'], unique=False)
    op.create_index(op.f('ix_organizers_lastN'), 'organizers', ['lastN'], unique=False)
    op.create_index(op.f('ix_organizers_organizationID'), 'organizers', ['organizationID'], unique=False)
    op.create_index(op.f('ix_organizers_password'), 'organizers', ['password'], unique=False)
    op.create_index(op.f('ix_organizers_username'), 'organizers', ['username'], unique=True)
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstN', sa.VARCHAR(length=255), nullable=True),
    sa.Column('lastN', sa.VARCHAR(length=255), nullable=True),
    sa.Column('targetID', sa.VARBINARY(length=255), nullable=True),
    sa.Column('organizationID', sa.Integer(), nullable=True),
    sa.Column('isOrganizer', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_students_firstN'), 'students', ['firstN'], unique=True)
    op.create_index(op.f('ix_students_isOrganizer'), 'students', ['isOrganizer'], unique=True)
    op.create_index(op.f('ix_students_lastN'), 'students', ['lastN'], unique=True)
    op.create_index(op.f('ix_students_organizationID'), 'students', ['organizationID'], unique=True)
    op.create_index(op.f('ix_students_targetID'), 'students', ['targetID'], unique=True)
    op.create_table('participants',
    sa.Column('organizer_id', sa.Integer(), nullable=True),
    sa.Column('activity_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['activity_id'], ['activity.id'], ),
    sa.ForeignKeyConstraint(['organizer_id'], ['organizers.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('participants')
    op.drop_index(op.f('ix_students_targetID'), table_name='students')
    op.drop_index(op.f('ix_students_organizationID'), table_name='students')
    op.drop_index(op.f('ix_students_lastN'), table_name='students')
    op.drop_index(op.f('ix_students_isOrganizer'), table_name='students')
    op.drop_index(op.f('ix_students_firstN'), table_name='students')
    op.drop_table('students')
    op.drop_index(op.f('ix_organizers_username'), table_name='organizers')
    op.drop_index(op.f('ix_organizers_password'), table_name='organizers')
    op.drop_index(op.f('ix_organizers_organizationID'), table_name='organizers')
    op.drop_index(op.f('ix_organizers_lastN'), table_name='organizers')
    op.drop_index(op.f('ix_organizers_firstN'), table_name='organizers')
    op.drop_index(op.f('ix_organizers_email'), table_name='organizers')
    op.drop_table('organizers')
    op.drop_index(op.f('ix_organizations_name'), table_name='organizations')
    op.drop_table('organizations')
    op.drop_index(op.f('ix_assignments_studentID'), table_name='assignments')
    op.drop_index(op.f('ix_assignments_status'), table_name='assignments')
    op.drop_index(op.f('ix_assignments_medium'), table_name='assignments')
    op.drop_index(op.f('ix_assignments_lastContact'), table_name='assignments')
    op.drop_table('assignments')
    op.drop_table('activity')
    # ### end Alembic commands ###