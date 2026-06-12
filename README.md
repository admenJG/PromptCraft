# PromptCraft

[![CI](https://github.com/admenJG/PromptCraft/actions/workflows/ci.yml/badge.svg)](https://github.com/admenJG/PromptCraft/actions)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/promptcraft-py.svg)](https://pypi.org/project/promptcraft-py/)
[![Downloads](https://img.shields.io/pypi/dm/promptcraft-py.svg)](https://pypi.org/project/promptcraft-py/)
[![Platform](https://img.shields.io/badge/platform-win%20%7C%20macos%20%7C%20linux-lightgrey.svg)]()

**A lightweight Python toolkit for prompt engineering, optimization, and evaluation.**

PromptCraft helps developers build, test, and refine prompts for LLMs with a clean, composable API.

## Features

- **Prompt Builder** - Chain instructions, examples, and variables with a fluent API
- **Template System** - Reusable prompt templates with variable interpolation
- **Optimizer** - Automatically refine prompts using scoring and iteration
- **Evaluator** - Score prompt quality across clarity, specificity, and completeness
- **Multi-provider** - Works with OpenAI, Anthropic, and any OpenAI-compatible API
- **Zero dependencies** - Core library has no external dependencies

## Platform Support

| Platform                             | Architecture          | Status          |
| ------------------------------------ | --------------------- | --------------- |
| Windows 10/11                        | x86_64                | Fully Supported |
| macOS 12+                            | Intel & Apple Silicon | Fully Supported |
| Linux (Ubuntu, Debian, Fedora, etc.) | x86_64, ARM64         | Fully Supported |
| Docker                               | Any                   | Fully Supported |

**Requirements:** Python 3.8 or higher

## Quick Start

`ash
pip install promptcraft-py
`

`python
from promptcraft import PromptBuilder, Template

# Build a prompt

prompt = (
PromptBuilder()
.system("You are a helpful coding assistant.")
.instruction("Explain the following concept clearly.")
.variable("concept", "dependency injection")
.examples([
{"input": "What is recursion?", "output": "Recursion is when a function calls itself..."}
])
.build()
)

print(prompt)
`

### Using Templates

`python
from promptcraft import Template

review_template = Template(
name="code_review",
system="You are a senior code reviewer.",
instruction="Review the following {language} code for bugs and improvements.",
variables=["language", "code"]
)

prompt = review_template.render(language="Python", code="def add(a, b): return a")
`

### Optimizing Prompts

`python
from promptcraft import Optimizer

optimizer = Optimizer(metric="relevance", iterations=5)
optimized = optimizer.optimize(
prompt="Explain {topic}",
test_cases=[{"topic": "quantum computing", "expected_keywords": ["qubit"]}]
)
print(f"Score: {optimized.initial_score:.2f} -> {optimized.final_score:.2f}")
`

### Evaluating Prompts

`python
from promptcraft import Evaluator

evaluator = Evaluator()
result = evaluator.score(
prompt="Write a function that sorts a list",
criteria=["clarity", "specificity", "completeness"]
)
print(f"Overall: {result.overall:.2f}")
`

## LangChain Integration

Convert a LangChain PromptTemplate to a PromptCraft Template:

```python
from langchain_core.prompts import PromptTemplate
from promptcraft import from_langchain

lc_prompt = PromptTemplate(
    template="Explain {topic}",
    input_variables=["topic"]
)

pc_template = from_langchain(lc_prompt)
```

Convert a PromptCraft Template to a LangChain PromptTemplate:

```python
from promptcraft import Template, to_langchain

template = Template(
    name="example",
    instruction="Explain {topic}",
    variables=["topic"]
)

lc_prompt = to_langchain(template)
```

### CLI Usage

`ash
promptcraft eval "Explain recursion clearly"
promptcraft score "You are a helpful assistant"
promptcraft optimize "Explain {topic}"
`

## Installation

### Windows

`cmd
pip install promptcraft-py
`

### macOS

`ash
pip3 install promptcraft-py
`

### Linux (Ubuntu/Debian)

`ash
sudo apt update && sudo apt install python3-pip
pip3 install promptcraft-py
`

### From Source

`ash
git clone https://github.com/admenJG/PromptCraft.git
cd PromptCraft
pip install -e .
`

## Running Tests

`ash
pytest
pytest --cov=promptcraft --cov-report=term-missing
`

## Documentation

- [Getting Started](docs/getting-started.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
