<?php

namespace Respect\Validation\Rules;

use Respect\Validation;

class StringType implements Validation\Validatable
{
    public function isValid($mixed)
    {
        return is_string($mixed);
    }
}
