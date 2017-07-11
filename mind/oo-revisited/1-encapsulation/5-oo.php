<?php

$utc = new DateTimezone('UTC');
$promotion = new Easy\Promotion(
    'Santander Meia Bandeira',
     new DateTime('2016-11-24 20:00:00', $utc),
     new DateTime('2016-11-25 06:00:00', $utc)
 );

if ($promotion->isValidFor($ride)) {
    // Here be beers!
}
