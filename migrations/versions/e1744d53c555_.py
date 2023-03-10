"""empty message

Revision ID: e1744d53c555
Revises: 
Create Date: 2023-02-06 18:25:09.191534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1744d53c555'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=80), nullable=False),
    sa.Column('lname', sa.String(length=80), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fname', sa.String(length=80), nullable=False),
    sa.Column('lname', sa.String(length=80), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subjects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('assessments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['subject_id'], ['subjects.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('students_assessments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('assessment_id', sa.Integer(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['assessment_id'], ['assessments.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['students.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students_assessments')
    op.drop_table('assessments')
    op.drop_table('subjects')
    op.drop_table('students')
    op.drop_table('teachers')
    # ### end Alembic commands ###
