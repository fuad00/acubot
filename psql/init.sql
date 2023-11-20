/* ----------------------------- ACUBOT DATABASE MODEL ----------------------------- */

CREATE TABLE users (
    id           serial PRIMARY KEY,
    tgid         BIGINT NOT NULL UNIQUE,
    nickname     TEXT,
    first_name   TEXT,
    last_name    TEXT,
    is_banned    boolean NOT NULL DEFAULT false,
    is_admin     boolean NOT NULL DEFAULT false,
    created_at   TIMESTAMP NOT NULL DEFAULT NOW()
);


CREATE TABLE user_settings (
    id               serial PRIMARY KEY,
    tgid             BIGINT NOT NULL UNIQUE,
    notifyonsuccess  boolean NOT NULL DEFAULT 1,

);