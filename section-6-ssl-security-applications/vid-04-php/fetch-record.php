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

// login and authenticate as read only user
$m = new MongoClient("mongodb://statsdb_ro:secret@localhost:16687/statsdb", array("ssl" => true), array("context" => $ctx));

// get handle for statsdb and statistics collection
$db = $m->statsdb;
$statistics = $db->statistics;

// retrieve a record and display it
$statistical_record = $statistics->findOne();
var_dump($statistical_record);

?>
