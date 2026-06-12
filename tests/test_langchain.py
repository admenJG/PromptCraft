from promptcraft.template import Template
from promptcraft.langchain import (
    from_langchain,
    to_langchain,
)

from langchain_core.prompts import PromptTemplate


class TestLangChainIntegration:

    def test_langchain_to_promptcraft(self):
        lc_prompt = PromptTemplate(
            template="Explain {topic}",
            input_variables=["topic"],
        )

        pc_template = from_langchain(lc_prompt)

        assert pc_template.instruction == "Explain {topic}"
        assert pc_template.variables == ["topic"]

    def test_promptcraft_to_langchain(self):
        pc_template = Template(
            name="test",
            instruction="Explain {topic}",
            variables=["topic"],
        )

        lc_prompt = to_langchain(pc_template)

        assert lc_prompt.template == "Explain {topic}"
        assert lc_prompt.input_variables == ["topic"]

    def test_round_trip_conversion(self):
        original = PromptTemplate(
            template="Explain {topic}",
            input_variables=["topic"],
        )

        converted = from_langchain(original)
        restored = to_langchain(converted)

        assert restored.template == original.template
        assert restored.input_variables == original.input_variables