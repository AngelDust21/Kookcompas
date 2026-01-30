"""
Kookcompas - Database Connectie Module
======================================
Teamlid 1: Database Developer

Verantwoordelijkheden:
- Database connectie beheer
- Stored procedures uitvoeren
- Error handling voor database operaties
"""

import os
import sys

# Voeg parent directory toe aan path voor imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

_actieve_connectie = None


def maak_connectie():
    """
    Maakt een database connectie aan of hergebruikt bestaande.
    Returns: MySQL connectie object of None bij fout
    """
    global _actieve_connectie

    if _actieve_connectie is not None:
        try:
            if _actieve_connectie.is_connected():
                return _actieve_connectie
        except Error:
            _actieve_connectie = None

    try:
        _actieve_connectie = mysql.connector.connect(**DB_CONFIG)
        return _actieve_connectie
    except Error as database_fout:
        print(f"Kon geen verbinding maken met de database: {database_fout}")
        return None


def sluit_connectie():
    """
    Sluit de actieve database connectie netjes af.
    """
    global _actieve_connectie

    if _actieve_connectie is not None:
        try:
            if _actieve_connectie.is_connected():
                _actieve_connectie.close()
        except Error:
            pass
        finally:
            _actieve_connectie = None
