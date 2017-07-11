---
title: Exceptions e o PHP
layout: post
date: 2017-07-01
category:
---

Existe uma diferença (um pouco grande) entre erros e excessões. É essa diferença
que justifica [linguagens sem excessões][1], não usar *excessões para controlar
o fluxo da aplicação*. Mas o que isso significa, na prática?

    <?php

    namespace MyApp\Controllers;

    use MyApp\Http;
    use MyApp\Promotion;
    use Respect\Validation\Validator as v;

    class Promotion
    {
        public function voucherValidation(Http\Request $req, Http\Response $res)
        {
            $params = $req->queryStringParameters();
            if (empty($params['voucher_code'])) {
                return $res->withClientErrorMessage(
                    '"voucher_code" parameter is required.'
                );
            }

            if (empty($params['customer_id'])) {
                return $res->withClientErrorMessage(
                    '"customer_id" parameter is required.'
                );
            }

            try {
                $customerId = $req->getFromQueryString('customer_id');
                $voucherCode = $req->getFromQueryString('voucher_code');
                $customer = $this->customers->findOneById($customerId);
                $promotion = $this->promotions->findOneByVoucher($voucherCode);
                
                $promotion->isApplicableTo($customer);
            } catch (Promotion\Exception\NotFound $e) {
                return $res->withError($e);
            } catch (Promotion\Exception\ExpiredVoucherCode $e) {
                return $res->withError($e);
            } catch (Promotion\Exception\NotApplicableToCustomer $e) {
                return $res->withError($e);
            }
        }
    }

Como ele poderia ser:

    <?php

    namespace MyApp\Controllers;

    use MyApp\Http;
    use MyApp\Promotion;
    use Respect\Validation\Validator as v;

    class Promotion
    {
        public function voucherValidation(Http\Request $req, Http\Response $res)
        {
            $query = $req->queryStringParameters(['voucher_code', 'customer_id]);

            $usageAttempt = Promotion\Factory::voucherUsageAttempt($query);
            $reservation = $usageAttempt->reserve($this->promotions);
            if ($reservation->wasUnsuccessfull()) {
                return $res->withError(
                    $reservation->explainProblem()
                );
            }

            $res->success(
                $reservation->explainDiscount()
            );
        }
    }

[1]: https://golang.org/doc/faq#exceptions "Why Go does not have exceptions?"

<!--
vim: spell spelllang=pt
-->
