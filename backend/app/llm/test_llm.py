from app.llm.client import generate
from app.llm.prompts import simple_test_prompt
from app.llm.parser import parse_json


def main():

    prompt = simple_test_prompt()

    print("\nPrompt\n")
    print(prompt)

    print("\nCalling Ollama...\n")

    response = generate(prompt)

    print(response)

    print("\nParsed JSON\n")

    parsed = parse_json(response)

    print(parsed)


if __name__ == "__main__":
    main()