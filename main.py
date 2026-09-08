import re

class SimpleAIAgent:
    """
    A simple AI agent that can process requests by selecting and using appropriate tools.
    This demonstrates the core concept of an agent perceiving, thinking, and acting,
    which is central to frameworks like DeerFlow.
    """
    def __init__(self):
        # Define available "tools" (functions) that the agent can use.
        # In a real framework like DeerFlow, these would be more complex modules or services.
        self.tools = {
            "add": self._add,
            "subtract": self._subtract,
            "greet": self._greet
        }

    def _add(self, num1, num2):
        """Tool: Adds two numbers."""
        return f"Result of addition: {num1 + num2}"

    def _subtract(self, num1, num2):
        """Tool: Subtracts two numbers."""
        return f"Result of subtraction: {num1 - num2}"

    def _greet(self, name="User"):
        """Tool: Greets a user."""
        return f"Hello, {name}! How can I assist you today?"

    def process_request(self, request: str):
        """
        The agent's core decision-making and action execution logic.
        It perceives the request, thinks about which tool to use, and then acts.
        """
        print(f"\nAgent received request: '{request}'")

        # --- PERCEPTION & THINKING (Decision Making) ---
        # This is where the agent analyzes the request to decide the best course of action.
        # In a real DeerFlow agent, this would involve LLMs, planning modules, etc.,
        # but here we use simple keyword matching.

        if "add" in request.lower() or "+" in request:
            match = re.search(r'(\d+)\s*[+\s]+\s*(\d+)', request)
            if match:
                num1, num2 = int(match.group(1)), int(match.group(2))
                print(f"Agent decided to use the 'add' tool for {num1} and {num2}.")
                # --- ACTION ---
                return self.tools["add"](num1, num2)
            else:
                return "Agent couldn't parse numbers for addition."

        elif "subtract" in request.lower() or "-" in request:
            match = re.search(r'(\d+)\s*[- ]\s*(\d+)', request)
            if match:
                num1, num2 = int(match.group(1)), int(match.group(2))
                print(f"Agent decided to use the 'subtract' tool for {num1} and {num2}.")
                # --- ACTION ---
                return self.tools["subtract"](num1, num2)
            else:
                return "Agent couldn't parse numbers for subtraction."

        elif "hello" in request.lower() or "hi" in request.lower() or "greet" in request.lower():
            name_match = re.search(r'(hello|hi|greet)\s*(me|my name is)?\s*(\w+)?', request, re.IGNORECASE)
            name = name_match.group(3) if name_match and name_match.group(3) else "User"
            print(f"Agent decided to use the 'greet' tool for '{name}'.")
            # --- ACTION ---
            return self.tools["greet"](name)

        else:
            print("Agent couldn't find a suitable tool for the request.")
            return "I'm sorry, I don't understand that request."

# --- Example Usage ---
if __name__ == "__main__":
    agent = SimpleAIAgent()

    # Demonstrate agent processing various requests
    print(agent.process_request("Please add 5 and 3"))
    print(agent.process_request("Subtract 10 from 4"))
    print(agent.process_request("15 - 7"))
    print(agent.process_request("Hello there!"))
    print(agent.process_request("Greet John"))
    print(agent.process_request("Can you add 10 and 20?"))
    print(agent.process_request("What is the weather like?"))
