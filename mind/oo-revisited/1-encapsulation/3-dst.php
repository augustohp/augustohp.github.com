<?php

$tz = 'America/Sao_Paulo';
date_default_timezone_set($tz);

$start = convertTz("20:00:00-02:00");
$end = convertTz("06:00:00-02:00");
if ($now >= $start &&
    $now <= $end) {
    // Here be dragons ...
}
