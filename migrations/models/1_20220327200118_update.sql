-- upgrade --
ALTER TABLE "users" ADD "language" VARCHAR(10) NOT NULL;
-- downgrade --
ALTER TABLE "users" DROP COLUMN "language";
