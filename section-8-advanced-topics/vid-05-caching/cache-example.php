#!/usr/bin/php
<?php

$document_id = '543f1ec50208373c53ba39b3';

// login and authenticate as read only user
$m = new MongoClient("mongodb://localhost:27200/statsdb");

// Prefer the nearest server with no tag preference
$m->setReadPreference(MongoClient::RP_NEAREST, array());

// get handle for statsdb and statistics collection
$db = $m->statsdb;
$statistics = $db->statistics;

$start_time = microtime(true);
// retrieve a record and display it
$statistical_record = $statistics->findOne(array("_id" => new MongoId($document_id)));
print "Found record with _id = {$statistical_record['_id']}.\n";
$stop_time = microtime(true);

// get the difference in seconds
$time_ms = ($stop_time - $start_time)*1000;
print "Elapsed time from MongoDB was $time_ms seconds.\n\n";

// cache document
apc_store ($document_id, $statistical_record);

$start_time = microtime(true);
// retrieve a record and display it
$statistical_record = apc_fetch($document_id);
print "Found record with _id = {$statistical_record['_id']}.\n";
$stop_time = microtime(true);

// get the difference in seconds
$time_ms = ($stop_time - $start_time)*1000;
PRINT "Elapsed time from cache was $time_ms seconds.\n\n";

?>