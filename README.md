## MongoDB Migrations for PyKlatchat

### Example usage:

#### apply migration
    pymongo-migrate migrate -u mongodb://username:password@host:port -d database_name
    
#### rollback migration
    pymongo-migrate downgrade -u mongodb://username:password@host:port -d database_name