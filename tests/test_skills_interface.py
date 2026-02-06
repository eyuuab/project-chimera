import pytest
from src.core.interfaces import SkillInterface

def test_skill_interface_compliance():
    """
    The Governor: Ensures all skills inherit from the base class.
    This enforces the 'execute(ctx, payload)' signature.
    """
    # We will try to import a skill that hasn't been written yet
    from src.skills.content_drafting import ContentDraftingSkill
    
    # Assert it inherits from the base interface
    assert issubclass(ContentDraftingSkill, SkillInterface)
    
    # Assert it has the required method
    assert hasattr(ContentDraftingSkill, "execute")