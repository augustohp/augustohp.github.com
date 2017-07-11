<?php

namespace Respect\Validation;

use Respect\Validation\Exceptions\ComponentException;
use Respect\Validation\Rules\AllOf;

class Validator extends AllOf
{
    public static $factory = null;

    private static function getFactory()
    {
        if (!static::$factory instanceof Factory) {
            static::$factory = new Factory();
        }

        return static::$factory;
    }

    public static function __callStatic($ruleName, $arguments)
    {
        if ('allOf' === $ruleName) {
            return static::buildRule($ruleName, $arguments);
        }

        $validator = new static();

        return $validator->__call($ruleName, $arguments);
    }

    public static function buildRule($ruleSpec, $arguments = [])
    {
        try {
            return static::getFactory()->rule($ruleSpec, $arguments);
        } catch (\Exception $exception) {
            throw new ComponentException($exception->getMessage(), $exception->getCode(), $exception);
        }
    }

    public function __call($method, $arguments)
    {
        return $this->addRule(static::buildRule($method, $arguments));
    }
}
