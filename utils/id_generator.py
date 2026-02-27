import uuid

def generate_id(prefix="lng"):
    """
    Generate a unique ID with an optional prefix.
    """
    unique_part = uuid.uuid4().hex[:8]
    return f"{prefix}_{unique_part}"