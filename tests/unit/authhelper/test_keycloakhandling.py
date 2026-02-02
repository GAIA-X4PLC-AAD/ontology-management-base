#!/usr/bin/env python3
"""
Unit tests for src.tools.authhelper.keycloakhandling.
"""

import importlib

import pytest


class _StubKeycloak:
    def __init__(self):
        self.last_user = None
        self.last_password = None

    def token(self, user, password):
        self.last_user = user
        self.last_password = password
        return {"access_token": "stub-token"}


def test_get_auth_header_returns_bearer(monkeypatch):
    pytest.importorskip("keycloak.keycloak_openid")
    module = importlib.import_module("src.tools.authhelper.keycloakhandling")

    stub = _StubKeycloak()
    monkeypatch.setattr(module, "KEYCLOAK_OPENID", stub)
    monkeypatch.setattr(module, "KEYCLOAK_USER", "user")
    monkeypatch.setattr(module, "KEYCLOAK_PASSWORD", "pass")

    header = module.get_auth_header()
    assert header["Authorization"] == "Bearer stub-token"
    assert stub.last_user == "user"
    assert stub.last_password == "pass"
