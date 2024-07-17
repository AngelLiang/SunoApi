/*
 Navicat Premium Data Transfer

 Source Server         : sunoapi.db
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 17/07/2024 10:22:57
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for link
-- ----------------------------
DROP TABLE IF EXISTS "link";
CREATE TABLE "link" (
  "id" INTEGER NOT NULL,
  "label" TEXT(128) NOT NULL,
  "link" TEXT(128) NOT NULL,
  "status" TINYINT NOT NULL DEFAULT 0,
  PRIMARY KEY ("id")
);

-- ----------------------------
-- Table structure for music
-- ----------------------------
DROP TABLE IF EXISTS "music";
CREATE TABLE "music" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "aid" TEXT NOT NULL,
  "data" TEXT NOT NULL,
  "sid" TEXT,
  "name" TEXT,
  "image" TEXT,
  "title" TEXT,
  "tags" TEXT,
  "prompt" TEXT,
  "duration" TEXT,
  "created" TIMESTAMP NOT NULL DEFAULT (datetime('now', 'localtime')),
  "updated" TIMESTAMP NOT NULL DEFAULT (datetime('now', 'localtime')),
  "status" TEXT NOT NULL DEFAULT running,
  "private" TINYINT NOT NULL DEFAULT 0,
  "user_cookie" TEXT
);

-- ----------------------------
-- Table structure for session
-- ----------------------------
DROP TABLE IF EXISTS "session";
CREATE TABLE "session" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  "identity" TEXT(50) NOT NULL,
  "session" TEXT(50) NOT NULL,
  "cookie" TEXT(1500) NOT NULL,
  "token" TEXT(1000) NOT NULL,
  "created" TIMESTAMP NOT NULL DEFAULT (datetime('now', 'localtime')),
  "updated" TIMESTAMP NOT NULL DEFAULT (datetime('now', 'localtime')),
  "status" TEXT NOT NULL DEFAULT 200
);

-- ----------------------------
-- Table structure for sqlite_sequence
-- ----------------------------
DROP TABLE IF EXISTS "sqlite_sequence";
CREATE TABLE "sqlite_sequence" (
  "name",
  "seq"
);

-- ----------------------------
-- Indexes structure for table link
-- ----------------------------
CREATE UNIQUE INDEX "link_id"
ON "link" (
  "id" ASC
);

-- ----------------------------
-- Auto increment value for music
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 4399 WHERE name = 'music';

-- ----------------------------
-- Indexes structure for table music
-- ----------------------------
CREATE UNIQUE INDEX "music_aid"
ON "music" (
  "aid" ASC
);
CREATE UNIQUE INDEX "music_id"
ON "music" (
  "id" ASC
);
CREATE INDEX "music_title"
ON "music" (
  "title" ASC
);

-- ----------------------------
-- Auto increment value for session
-- ----------------------------
UPDATE "sqlite_sequence" SET seq = 5 WHERE name = 'session';

-- ----------------------------
-- Indexes structure for table session
-- ----------------------------
CREATE UNIQUE INDEX "session_id"
ON "session" (
  "id" ASC
);
CREATE UNIQUE INDEX "session_identity"
ON "session" (
  "identity" ASC
);

PRAGMA foreign_keys = true;
