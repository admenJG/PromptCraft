from promptcraft.template import Template
from typing import TYPE_CHECKING

try:
    from langchain_core.prompts import PromptTemplate
except ImportError:
    PromptTemplate = None

def from_langchain(prompt):
    """Convert a LangChain PromptTemplate to a PromptCraft Template."""

    return Template(
        name="langchain_template",
        instruction=prompt.template,
        variables=prompt.input_variables,
    )

def to_langchain(template):
    """Convert a PromptCraft Template to a LangChain PromptTemplate."""

    if PromptTemplate is None:
        raise ImportError(
            "langchain-core is required for LangChain integration"
        )

    return PromptTemplate(
        template=template.instruction,
        input_variables=template.variables,
    )

