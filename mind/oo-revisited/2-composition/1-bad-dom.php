<?php

use Something\Bad\Create as C;

$form = new C\Element('form');
$form->setAttr(new C\AttrArr([
    'action' => 'action.php',
    'method' => 'post'
]));

$form->setInner(new C\InnerObj($inputFirstName));
$form->setInner(new C\InnerObj($inputSubmit));
echo $form->getElement();
/*
<form action="action.php" method="post">
<input type="text" name="firstName" class="form" required />
<input name="submit" type="submit" value="ok" />
</form>
*/
