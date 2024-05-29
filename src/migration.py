from playhouse.migrate import PostgresqlMigrator, migrate

from db import db
from models import HookahSize


migrator = PostgresqlMigrator(db)
migrate(
    migrator.drop_column('hookahsize', 'new_test'),
    migrator.drop_column('hookahsize', 'abc'),
    migrator.drop_column('hookahsize', 'def'),


)
