"""Added models

Revision ID: 5e369ca9bd89
Revises: c00afc776eb6
Create Date: 2020-08-03 14:54:56.846853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e369ca9bd89'
down_revision = 'c00afc776eb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('bio', sa.Text(), nullable=True),
    sa.Column('imageURL', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('albums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('imageURL', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('imageURL', sa.String(length=50), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('album_id', sa.Integer(), nullable=False),
    sa.Column('songURL', sa.String(length=255), nullable=True),
    sa.Column('songLength', sa.Time(), nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playlistsongs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('playlist_id', sa.Integer(), nullable=False),
    sa.Column('song_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.id'], ),
    sa.ForeignKeyConstraint(['song_id'], ['songs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playlistsongs')
    op.drop_table('songs')
    op.drop_table('playlists')
    op.drop_table('albums')
    
    op.drop_table('artists')
    # ### end Alembic commands ###
