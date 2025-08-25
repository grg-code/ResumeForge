import json
from typing import Dict, Any

from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage


def _ok(data: Any) -> Dict[str, Any]:
    return {"ok": True, "data": data, "error": None}


def _err(msg: str) -> Dict[str, Any]:
    return {"ok": False, "data": None, "error": msg}



@tool
def ask_question(question: str) -> Dict[str, Any]:
    """
    Ask a clarification question to the human user.
    
    Args:
        question: The specific question to ask the human
        
    Returns:
        Dict with success/error status and the user's answer
    """
    try:
        # Ask the human directly
        print(f"\n🤔 Clarification needed:")
        print(f"Question: {question}")
        
        answer = input("Your answer: ").strip()
        
        if answer:
            return _ok(answer)
        else:
            return _err("No answer provided")

    except Exception as e:
        return _err(f"Error asking question: {str(e)}")





