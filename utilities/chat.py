async def format_agent_response(agent, messages):
    """Stream response from agent and return the final content (no Langfuse)."""

    response_text = ""
    async for chunk in agent.astream(
        {"messages": messages},
        # keep thread_id if you like, just drop callbacks
        config={"configurable": {"thread_id": "main_session"}},
        stream_mode="values",
    ):
        if "messages" in chunk and chunk["messages"]:
            latest_message = chunk["messages"][-1]
            if hasattr(latest_message, "content"):
                response_text = latest_message.content

    return response_text


