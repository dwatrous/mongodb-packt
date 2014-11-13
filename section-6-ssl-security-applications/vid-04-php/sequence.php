#!/usr/bin/php
<?php

// context
$ctx = stream_context_create(array(
    "ssl" => array(
        "local_cert"        => "/etc/ssl/mongo-client.pem",
        "verify_peer"       => true,
        "cafile"            => "/etc/ssl/mongod.pem",
    ),
));

// connect to MongoDB and authenticate as read write user
$m = new MongoClient("mongodb://statsdb_rw:secret@localhost:16687/statsdb", array("ssl" => true), array("context" => $ctx));

// get handle for statsdb and statistics collection
$db = $m->statsdb;
$statistics = $db->statistics;

// create a document to insert
$stats_doc = array(
    "request_ip" => "0.0.0.0",
    "owner" => new MongoId('543f227c0208373c53ba4b28'),
    "request_date" => new MongoDate(),
    "request_method" => "GET",
    "request_uri" => "api.myapplication.com/v1/document/f9b09e246.php",
    "action" => "VIEW",
    "request_time_milliseconds" => 12,
    "loc" => array( -121.89, 37.3378),
    "cookies" => array("php")
);

// insert a document
$statistics->insert($stats_doc);

// query for the new document
$new_statistical_record = $statistics->findOne(array("request_ip" => "0.0.0.0"));
var_dump($new_statistical_record);

?>
