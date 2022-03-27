-- upgrade --
ALTER TABLE "notes" DROP COLUMN "tags";
CREATE TABLE IF NOT EXISTS "tags" (
    "name" VARCHAR(255) NOT NULL  PRIMARY KEY
);-- downgrade --
ALTER TABLE "notes" ADD "tags" VARCHAR(255);
DROP TABLE IF EXISTS "tags";
