-- upgrade --
ALTER TABLE "users" RENAME COLUMN "roles" TO "role";
-- downgrade --
ALTER TABLE "users" RENAME COLUMN "role" TO "roles";
