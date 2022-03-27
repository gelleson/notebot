-- upgrade --
ALTER TABLE "users" ADD "full_name" VARCHAR(250) NOT NULL;
-- downgrade --
ALTER TABLE "users" DROP COLUMN "full_name";
