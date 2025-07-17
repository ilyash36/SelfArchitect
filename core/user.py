from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class User:
    """Represents a SelfArchitect user."""

    name: str
    email: str
    goals: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Serialize the user to a dictionary."""
        return {
            "name": self.name,
            "email": self.email,
            "goals": self.goals,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "User":
        """Create a User instance from a dictionary."""
        return cls(
            name=data.get("name", ""),
            email=data.get("email", ""),
            goals=list(data.get("goals", [])),
        )