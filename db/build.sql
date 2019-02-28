CREATE TABLE `event` (
	`event_id` int NOT NULL AUTO_INCREMENT,
	`event_nm` varchar(255) NOT NULL,
	`date_st` DATETIME NOT NULL,
	`date_end` DATETIME NOT NULL,
	PRIMARY KEY (`event_id`)
);

CREATE TABLE `team` (
	`team_no` int NOT NULL,
	`team_nm` varchar(255) NOT NULL,
	PRIMARY KEY (`team_no`)
);

CREATE TABLE `match` (
	`match_id` int NOT NULL AUTO_INCREMENT,
	`event_id` int NOT NULL,
	`team_no` int NOT NULL,
	`scout` varchar(255) NOT NULL,
	`auto_move` varchar(1) NOT NULL,
	`auto_switch_cubes` int NOT NULL,
	`auto_scale_cubes` int NOT NULL,
	`auto_comm` varchar(2000) NOT NULL,
	`match_no` int NOT NULL,
	`tele_switch_cubes` int NOT NULL,
	`tele_scale_cubes` int NOT NULL,
	`hang` varchar(1) NOT NULL,
	`tele_comm` varchar(2000) NOT NULL,
	`rate` int NOT NULL,
	PRIMARY KEY (`match_id`)
);

CREATE TABLE `event_team_xref` (
	`event_id` int NOT NULL,
	`team_no` int NOT NULL
);


CREATE TABLE `pit` (
	`pit_id` int NOT NULL AUTO_INCREMENT,
	`team_no` int NOT NULL,
	`event_id` int NOT NULL,
	`drivetrain` varchar(2000) NOT NULL,
	`auto` varchar(2000) NOT NULL,
	`fast` varchar(500) NOT NULL,
	`pickup` varchar(2000) NOT NULL,
	`scale` varchar(1) NOT NULL,
	`switch` varchar(1) NOT NULL,
	`hang` varchar(1) NOT NULL,
	`climbpart` varchar(500) NOT NULL,
	`defense` varchar(1) NOT NULL,
	PRIMARY KEY (`pit_id`)
);

ALTER TABLE `match` ADD CONSTRAINT `match_fk0` FOREIGN KEY (`event_id`) REFERENCES `event`(`event_id`);

ALTER TABLE `match` ADD CONSTRAINT `match_fk1` FOREIGN KEY (`team_no`) REFERENCES `team`(`team_no`);

ALTER TABLE `event_team_xref` ADD CONSTRAINT `event_team_xref_fk0` FOREIGN KEY (`event_id`) REFERENCES `event`(`event_id`);

ALTER TABLE `event_team_xref` ADD CONSTRAINT `event_team_xref_fk1` FOREIGN KEY (`team_no`) REFERENCES `team`(`team_no`);

ALTER TABLE `pit` ADD CONSTRAINT `pit_fk0` FOREIGN KEY (`team_no`) REFERENCES `team`(`team_no`);

ALTER TABLE `pit` ADD CONSTRAINT `pit_fk1` FOREIGN KEY (`event_id`) REFERENCES `event`(`event_id`);