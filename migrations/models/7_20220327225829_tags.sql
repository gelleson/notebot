-- upgrade --
CREATE TABLE IF NOT EXISTS "tag_notes" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "note_id" INT NOT NULL REFERENCES "notes" ("id") ON DELETE CASCADE,
    "tag_id" VARCHAR(255) NOT NULL REFERENCES "tags" ("name") ON DELETE CASCADE,
    CONSTRAINT "uid_tag_notes_tag_id_9d529f" UNIQUE ("tag_id", "note_id")
);
-- downgrade --
DROP TABLE IF EXISTS "tag_notes";
