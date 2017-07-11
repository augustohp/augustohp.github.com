<?php

namespace Respect\Validation\Rules;

use Respect\Validation;

class AllOf implements Validation\Validatable
{
    private $rules = [];

    public function __construct(Validation\Rule ...$rules)
    {
        $this->rules = $rules;
    }

    public function isValid($mixed)
    {
        foreach ($this->rules as $rule) {
            if (false === $rule->isValid($mixed)) {
                return false;
            }
        }

        return true;
    }
}
