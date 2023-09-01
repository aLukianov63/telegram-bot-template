
CREATE TABLE IF NOT EXISTS "users" (
    "id" bigint NOT NULL,
    "username" text NOT NULL,
    "lang" text NOT NULL,
    "created_at" timestamp NOT NULL,
    CONSTRAINT "pk_user" PRIMARY KEY (
        "id"
    ),
    CONSTRAINT "uc_user_username" UNIQUE (
        "username"
    )
);