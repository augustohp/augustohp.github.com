<?php

namespace Respect\Validation;

use Respect\Validation\Exceptions\ComponentException;
use Respect\Validation\Rules\AllOf;

class Validator extends AllOf {
    protected static $factory;

    protected static function getFactory() {
        if (!static::$factory instanceof Factory) {
            static::$factory = new Factory();
        }

        return static::$factory;
    }

    public static function setFactory($factory) {
        static::$factory = $factory;
    }

    public static function with($rulePrefix, $prepend = false) {
        if (false === $prepend) {
            self::getFactory()->appendRulePrefix($rulePrefix);
        } else {
            self::getFactory()->prependRulePrefix($rulePrefix);
        }
    }

    public static function buildRule($ruleSpec, $arguments = []) {
        try {
            return static::getFactory()->rule($ruleSpec, $arguments);
        } catch (\Exception $exception) {
            throw new ComponentException(
                $exception->getMessage(),
                $exception->getCode(),
                $exception
            );
        }
    }
}
