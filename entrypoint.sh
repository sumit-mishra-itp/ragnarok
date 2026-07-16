#!/bin/bash
set -e

# Only run flask db upgrade if migrations/ directory was shipped with the image.
if [ -d "migrations" ]; then
    flask db upgrade || echo "WARNING: flask db upgrade failed, continuing anyway..."
else
    # No migrations shipped — auto-generate from model definitions and apply.
    # Requires ENV FLASK_APP=app.py to be set.
    flask db init || true
    flask db migrate -m "initial" || true
    flask db upgrade || echo "WARNING: flask db upgrade failed, continuing anyway..."
fi

exec "$@"