#!/usr/bin/php
<?php

// login and authenticate as read only user
$m = new MongoClient("mongodb://localhost:27017/statsdb");

// Prefer the nearest server with no tag preference
$m->setReadPreference(MongoClient::RP_NEAREST, array());

// get handle for statsdb and statistics collection
$db = $m->statsdb;
$statistics = $db->statistics;

// retrieve a record and display it
$statistical_record = $statistics->findOne();
var_dump($statistical_record);

?>
