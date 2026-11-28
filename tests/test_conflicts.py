"""
Tests du module de détection de conflits.
Règles testées :
1. Enseignant occupé sur deux séances au même créneau
2. Salle occupée sur deux séances au même créneau
3. Groupe déjà en cours
4. Salle trop petite pour l'effectif

Ce fichier est écrit en TDD (Test-Driven Development) :
les tests définissent le comportement attendu AVANT que le code n'existe.
Alyssa doit coder app/services/conflict_detector.py pour faire passer ces tests.
"""
import pytest

# Import protégé : le module n'existe peut-être pas encore (TDD)
try:
    from app.services.conflict_detector import detect_conflicts
    CONFLICT_MODULE_AVAILABLE = True
except ImportError:
    CONFLICT_MODULE_AVAILABLE = False

pytestmark = pytest.mark.skipif(
    not CONFLICT_MODULE_AVAILABLE,
    reason="Module conflict_detector pas encore implémenté (TDD)"
)


def test_no_conflict_when_all_free():
    """Cas nominal : aucune séance en conflit."""
    seances = [
        {"enseignant_id": 1, "salle_id": 1, "groupe_id": 1, "creneau_id": 1},
        {"enseignant_id": 2, "salle_id": 2, "groupe_id": 2, "creneau_id": 2},
    ]
    conflicts = detect_conflicts(seances, new_seance=seances[0])
    assert conflicts == []


def test_enseignant_occupe():
    """Conflit : même enseignant, même créneau."""
    seances = [
        {"enseignant_id": 1, "salle_id": 1, "groupe_id": 1, "creneau_id": 1},
    ]
    nouvelle = {"enseignant_id": 1, "salle_id": 2, "groupe_id": 2, "creneau_id": 1}
    conflicts = detect_conflicts(seances, new_seance=nouvelle)
    assert any("enseignant" in c.lower() for c in conflicts)


def test_salle_occupee():
    """Conflit : même salle, même créneau."""
    seances = [
        {"enseignant_id": 1, "salle_id": 1, "groupe_id": 1, "creneau_id": 1},
    ]
    nouvelle = {"enseignant_id": 2, "salle_id": 1, "groupe_id": 2, "creneau_id": 1}
    conflicts = detect_conflicts(seances, new_seance=nouvelle)
    assert any("salle" in c.lower() for c in conflicts)


def test_groupe_deja_en_cours():
    """Conflit : même groupe, même créneau."""
    seances = [
        {"enseignant_id": 1, "salle_id": 1, "groupe_id": 1, "creneau_id": 1},
    ]
    nouvelle = {"enseignant_id": 2, "salle_id": 2, "groupe_id": 1, "creneau_id": 1}
    conflicts = detect_conflicts(seances, new_seance=nouvelle)
    assert any("groupe" in c.lower() for c in conflicts)


def test_salle_trop_petite():
    """Conflit : effectif groupe > capacité salle."""
    salles = {1: {"capacite": 20}}
    groupes = {1: {"effectif": 30}}
    nouvelle = {"enseignant_id": 1, "salle_id": 1, "groupe_id": 1, "creneau_id": 1}
    conflicts = detect_conflicts([], new_seance=nouvelle, salles=salles, groupes=groupes)
    assert any("capacit" in c.lower() for c in conflicts)


def test_multiple_conflicts():
    """Cas limite : plusieurs conflits simultanés."""
    seances = [
        {"enseignant_id": 1, "salle_id": 1, "groupe_id": 1, "creneau_id": 1},
    ]
    nouvelle = {"enseignant_id": 1, "salle_id": 1, "groupe_id": 1, "creneau_id": 1}
    conflicts = detect_conflicts(seances, new_seance=nouvelle)
    assert len(conflicts) >= 2


def test_no_conflict_different_creneau():
    """Pas de conflit si créneaux différents."""
    seances = [
        {"enseignant_id": 1, "salle_id": 1, "groupe_id": 1, "creneau_id": 1},
    ]
    nouvelle = {"enseignant_id": 1, "salle_id": 1, "groupe_id": 1, "creneau_id": 2}
    conflicts = detect_conflicts(seances, new_seance=nouvelle)
    assert conflicts == []
