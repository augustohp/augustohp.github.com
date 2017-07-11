<?php

namespace Respect\Validation;

use ReflectionClass;
use Respect\Validation\Exceptions\ComponentException;

class Factory
{
  protected $rulePrefixes = ['Respect\\Validation\\Rules\\'];

  public function rule($ruleName, array $arguments = [])
  {
    if ($ruleName instanceof Validatable) {
      return $ruleName;
    }

    foreach ($this->rulePrefixes as $prefix) {
      $className = $prefix.ucfirst($ruleName);
      if (!class_exists($className)) {
        continue;
      }

      $reflection = new ReflectionClass($className);
      if ($reflection->isSubclassOf(Validatable::class)) {
        throw new ComponentException(
          sprintf('"%s" is not a rule.', $className)
        );
      }

      return $reflection->newInstanceArgs($arguments);
    }

    throw new ComponentException(
      sprintf('"%s" not found.', $ruleName)
    );
  }
}
