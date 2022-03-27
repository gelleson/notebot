-- upgrade --
ALTER TABLE "users" ADD "roles" VARCHAR(5) NOT NULL  DEFAULT 'user';
-- downgrade --
ALTER TABLE "users" DROP COLUMN "roles";
