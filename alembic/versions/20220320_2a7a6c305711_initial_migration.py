"""Initial migration

Revision ID: 2a7a6c305711
Revises: 
Create Date: 2022-03-20 15:57:32.668113

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from ums.sima.classes import Program

# revision identifiers, used by Alembic.
revision = '2a7a6c305711'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gui_access_level',
    sa.Column('ID', sa.INTEGER(), nullable=False),
    sa.Column('login', sa.VARCHAR(length=16), nullable=True),
    sa.Column('password', sa.VARCHAR(length=32), nullable=True),
    sa.Column('level', sa.SMALLINT(), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_gui_access_level_login'), 'gui_access_level', ['login'], unique=False)
    op.create_table('programs',
    sa.Column('ID', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=False),
    sa.Column('author', sa.VARCHAR(length=64), nullable=False),
    sa.Column('describe', sa.TEXT(), nullable=True),
    sa.Column('marker', sa.VARCHAR(length=8), nullable=True),
    sa.Column('size1', sa.NUMERIC(precision=3, scale=1), nullable=True),
    sa.Column('size2', sa.NUMERIC(precision=3, scale=1), nullable=True),
    sa.Column('size3', sa.NUMERIC(precision=3, scale=1), nullable=True),
    sa.Column('def_obs_period', sa.NUMERIC(precision=3, scale=1), nullable=True),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_programs_ID'), 'programs', ['ID'], unique=True)
    op.create_index(op.f('ix_programs_author'), 'programs', ['author'], unique=False)
    op.create_index(op.f('ix_programs_name'), 'programs', ['name'], unique=False)
    op.create_table('objects',
    sa.Column('ID', sa.INTEGER(), nullable=False),
    sa.Column('_Program', sa.INTEGER(), nullable=True),
    sa.Column('type', sa.VARCHAR(length=1), nullable=True),
    sa.Column('main_id', sa.VARCHAR(length=32), nullable=False),
    sa.Column('name_list', postgresql.ARRAY(sa.VARCHAR(length=32)), nullable=False),
    sa.Column('ra_2000', sa.VARCHAR(length=16), nullable=True),
    sa.Column('dec_2000', sa.VARCHAR(length=16), nullable=True),
    sa.Column('ra_pm', sa.NUMERIC(precision=8, scale=3), nullable=True),
    sa.Column('dec_pm', sa.NUMERIC(precision=8, scale=3), nullable=True),
    sa.Column('gmag', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('bmag', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('vmag', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('rmag', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('imag', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('jmag', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('hmag', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('kmag', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('sptype', sa.VARCHAR(length=32), nullable=True),
    sa.Column('parallax', sa.NUMERIC(precision=7, scale=4), nullable=True),
    sa.Column('period', sa.NUMERIC(precision=7, scale=4), nullable=True),
    sa.Column('status', sa.BOOLEAN(), nullable=True),
    sa.Column('describe', sa.TEXT(), nullable=True),
    sa.Column('posN', sa.SMALLINT(), nullable=True),
    sa.Column('orbN', sa.SMALLINT(), nullable=True),
    sa.ForeignKeyConstraint(['_Program'], ['programs.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_objects_ID'), 'objects', ['ID'], unique=True)
    op.create_index(op.f('ix_objects__Program'), 'objects', ['_Program'], unique=False)
    op.create_index(op.f('ix_objects_main_id'), 'objects', ['main_id'], unique=False)
    op.create_index(op.f('ix_objects_status'), 'objects', ['status'], unique=False)
    op.create_index(op.f('ix_objects_type'), 'objects', ['type'], unique=False)
    op.create_table('journal',
    sa.Column('ID', sa.INTEGER(), nullable=False),
    sa.Column('_Object', sa.INTEGER(), nullable=True),
    sa.Column('ra_start', sa.VARCHAR(length=16), nullable=True),
    sa.Column('dec_start', sa.VARCHAR(length=16), nullable=True),
    sa.Column('utc_date_start', sa.DateTime(), nullable=True),
    sa.Column('lst_date_start', postgresql.TIME(), nullable=True),
    sa.Column('z_start', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('par_ang_start', sa.NUMERIC(precision=5, scale=2), nullable=True),
    sa.Column('ra_end', sa.VARCHAR(length=16), nullable=True),
    sa.Column('dec_end', sa.VARCHAR(length=16), nullable=True),
    sa.Column('utc_date_end', sa.DateTime(), nullable=True),
    sa.Column('lst_date_end', postgresql.TIME(), nullable=True),
    sa.Column('z_end', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('par_ang_end', sa.NUMERIC(precision=5, scale=2), nullable=True),
    sa.Column('filt', sa.VARCHAR(length=16), nullable=True),
    sa.Column('gain', sa.SMALLINT(), nullable=True),
    sa.Column('mag', sa.SMALLINT(), nullable=True),
    sa.Column('focus', sa.NUMERIC(precision=5, scale=2), nullable=True),
    sa.Column('par_ang_mean', sa.NUMERIC(precision=5, scale=2), nullable=True),
    sa.Column('t_in', sa.NUMERIC(precision=4, scale=1), nullable=True),
    sa.Column('t_out', sa.NUMERIC(precision=4, scale=1), nullable=True),
    sa.Column('t_mir', sa.NUMERIC(precision=4, scale=1), nullable=True),
    sa.Column('press', sa.NUMERIC(precision=4, scale=1), nullable=True),
    sa.Column('wind', sa.NUMERIC(precision=4, scale=2), nullable=True),
    sa.Column('comment', sa.TEXT(), nullable=True),
    sa.Column('lines', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['_Object'], ['objects.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_journal_ID'), 'journal', ['ID'], unique=True)
    op.create_table('journal_name_equal',
    sa.Column('ID', sa.INTEGER(), nullable=False),
    sa.Column('_Object', sa.INTEGER(), nullable=True),
    sa.Column('journal_line', sa.TEXT(), nullable=True),
    sa.Column('params', postgresql.JSON(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['_Object'], ['objects.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_journal_name_equal_ID'), 'journal_name_equal', ['ID'], unique=True)
    op.create_table('orbits',
    sa.Column('ID', sa.INTEGER(), nullable=False),
    sa.Column('_Object', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.VARCHAR(length=16), nullable=False),
    sa.Column('P', sa.NUMERIC(precision=7, scale=4), nullable=False),
    sa.Column('T0', sa.NUMERIC(precision=8, scale=4), nullable=False),
    sa.Column('a', sa.NUMERIC(precision=8, scale=4), nullable=False),
    sa.Column('e', sa.NUMERIC(precision=5, scale=4), nullable=False),
    sa.Column('W', sa.NUMERIC(precision=7, scale=4), nullable=False),
    sa.Column('w', sa.NUMERIC(precision=7, scale=4), nullable=False),
    sa.Column('i', sa.NUMERIC(precision=7, scale=4), nullable=False),
    sa.Column('P_err', sa.NUMERIC(precision=6, scale=4), nullable=True),
    sa.Column('T0_err', sa.NUMERIC(precision=6, scale=4), nullable=True),
    sa.Column('a_err', sa.NUMERIC(precision=6, scale=4), nullable=True),
    sa.Column('e_err', sa.NUMERIC(precision=6, scale=4), nullable=True),
    sa.Column('W_err', sa.NUMERIC(precision=6, scale=4), nullable=True),
    sa.Column('w_err', sa.NUMERIC(precision=6, scale=4), nullable=True),
    sa.Column('i_err', sa.NUMERIC(precision=6, scale=4), nullable=True),
    sa.Column('first_author', sa.VARCHAR(length=16), nullable=True),
    sa.Column('author', sa.TEXT(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=256), nullable=True),
    sa.Column('year', sa.SMALLINT(), nullable=True),
    sa.Column('journal', sa.VARCHAR(length=256), nullable=True),
    sa.Column('doi', sa.VARCHAR(length=128), nullable=True),
    sa.Column('comment', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['_Object'], ['objects.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_orbits_ID'), 'orbits', ['ID'], unique=True)
    op.create_table('position_parameters',
    sa.Column('ID', sa.INTEGER(), nullable=False),
    sa.Column('_Object', sa.INTEGER(), nullable=False),
    sa.Column('type', sa.VARCHAR(length=16), nullable=False),
    sa.Column('epoch', sa.NUMERIC(precision=10, scale=6), nullable=False),
    sa.Column('rho', sa.NUMERIC(precision=8, scale=4), nullable=False),
    sa.Column('rho_err', sa.NUMERIC(precision=6, scale=4), nullable=True),
    sa.Column('theta', sa.NUMERIC(precision=7, scale=4), nullable=False),
    sa.Column('theta_err', sa.NUMERIC(precision=6, scale=4), nullable=True),
    sa.Column('theta_ambiguity', sa.BOOLEAN(), nullable=True),
    sa.Column('dm', sa.NUMERIC(precision=5, scale=3), nullable=True),
    sa.Column('dm_err', sa.NUMERIC(precision=4, scale=3), nullable=True),
    sa.Column('filter', sa.VARCHAR(length=16), nullable=True),
    sa.Column('first_author', sa.VARCHAR(length=16), nullable=False),
    sa.Column('author', sa.TEXT(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=256), nullable=True),
    sa.Column('year', sa.SMALLINT(), nullable=True),
    sa.Column('journal', sa.VARCHAR(length=256), nullable=True),
    sa.Column('doi', sa.VARCHAR(length=128), nullable=True),
    sa.Column('comment', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['_Object'], ['objects.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    op.create_index(op.f('ix_position_parameters_ID'), 'position_parameters', ['ID'], unique=True)
    op.create_index(op.f('ix_position_parameters_first_author'), 'position_parameters', ['first_author'], unique=False)
    op.create_index(op.f('ix_position_parameters_type'), 'position_parameters', ['type'], unique=False)
    # ### end Alembic commands ###

    bind = op.get_bind()
    session = sa.orm.Session(bind=bind)
    session.add(Program(name='Without program', author='Unknown', describe='Stars without program', marker='%?%'))
    session.commit()



def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_position_parameters_type'), table_name='position_parameters')
    op.drop_index(op.f('ix_position_parameters_first_author'), table_name='position_parameters')
    op.drop_index(op.f('ix_position_parameters_ID'), table_name='position_parameters')
    op.drop_table('position_parameters')
    op.drop_index(op.f('ix_orbits_ID'), table_name='orbits')
    op.drop_table('orbits')
    op.drop_index(op.f('ix_journal_name_equal_ID'), table_name='journal_name_equal')
    op.drop_table('journal_name_equal')
    op.drop_index(op.f('ix_journal_ID'), table_name='journal')
    op.drop_table('journal')
    op.drop_index(op.f('ix_objects_type'), table_name='objects')
    op.drop_index(op.f('ix_objects_status'), table_name='objects')
    op.drop_index(op.f('ix_objects_main_id'), table_name='objects')
    op.drop_index(op.f('ix_objects__Program'), table_name='objects')
    op.drop_index(op.f('ix_objects_ID'), table_name='objects')
    op.drop_table('objects')
    op.drop_index(op.f('ix_programs_name'), table_name='programs')
    op.drop_index(op.f('ix_programs_author'), table_name='programs')
    op.drop_index(op.f('ix_programs_ID'), table_name='programs')
    op.drop_table('programs')
    op.drop_index(op.f('ix_gui_access_level_login'), table_name='gui_access_level')
    op.drop_table('gui_access_level')
    # ### end Alembic commands ###