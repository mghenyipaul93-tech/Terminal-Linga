
class DialectService:
    def __init__(self):
        self.dialects = {}
        self.counter = 1

    def _generate_id(self):
        dialect_id = self.counter
        self.counter += 1
        return dialect_id

    def create_dialect(self, name):
        if not name:
            raise ValueError("Dialect name cannot be empty.")

        dialect_id = self._generate_id()

        dialect = {
            "id": dialect_id,
            "name": name
        }

        self.dialects[dialect_id] = dialect
        return dialect

    def get_all_dialects(self):
        return list(self.dialects.values())

    def get_dialect_by_id(self, dialect_id):
        return self.dialects.get(dialect_id)