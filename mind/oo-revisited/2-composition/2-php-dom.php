<?php

$submit = new DomElement('input');
$submit->setAttribute('type', 'submit');
$submit->setAttribute('value', 'ok');

$name = new DomElement('input');
$name->setAttribute('type', 'text');
$name->setAttribute('name', 'firstName');
$name->setAttribute('class', 'form');
$name->setAttribute('required', 'required');

$form = new DomElement('form');
$form->setAttribute('action', 'action.php');
$form->setAttribute('method', 'POST');
$form->appendChild($name);
$form->appendChild($name);
