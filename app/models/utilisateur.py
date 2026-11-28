from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base

class Utilisateur(Base):
    __tablename__ = "utilisateur"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    mot_de_passe_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)
    actif = Column(Boolean, default=True)
    groupe_id = Column(Integer, ForeignKey("groupe.id"), nullable=True)
    enseignant_id = Column(Integer, ForeignKey("enseignant.id"), nullable=True)