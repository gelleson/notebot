-- upgrade --
ALTER TABLE "notes" ALTER COLUMN "tags" DROP NOT NULL;
-- downgrade --
ALTER TABLE "notes" ALTER COLUMN "tags" SET NOT NULL;
