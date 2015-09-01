#!/usr/bin/env/ python
# encoding: utf-8

__author__ = 'aldur'

import unittest

import matasano.public


class PublicTestCase(unittest.TestCase):
    def test_dh(self):
        f = matasano.public.dh_keys
        p = 23
        g = 5

        _, _, priv, pub = f(p=p, g=g)
        self.assertEqual(
            pow(g, priv, p), pub
        )

    def test_dh_default(self):
        f = matasano.public.dh_keys

        p, g, priv, pub = f()
        self.assertEqual(
            pow(g, priv, p), pub
        )

    def test_dh_protocol(self):
        alice = matasano.public.DHEntity()
        bob = matasano.public.DHEntity()

        alice.dh_protocol(bob)
        self.assertEqual(
            alice._session_key,
            bob._session_key
        )

    def test_dh_message(self):
        alice = matasano.public.DHEntity()
        bob = matasano.public.DHEntity()
        alice.dh_protocol(bob)

        message = b"MessageInABottle"
        answer = alice.send_and_receive(bob, message)
        self.assertEqual(
            message,
            answer
        )


if __name__ == '__main__':
    unittest.main()
