from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough


def generation(retriever, question, openai_api_key):
    """
    Generate responses based on prompts and embeddings.

    Parameters:
        retriever (object): Object for retrieving relevant information.
        question (str): User question.
        openai_api_key (str): API key for OpenAI service.

    Returns:
        str: Generated response to the user question.
    """

    try:
        # Prompt template
        template = """Answer the question based only on the following context, which can include text and tables:
        {context}
        Question: {question}
        """
        prompt = ChatPromptTemplate.from_template(template)

        # LLM
        model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", openai_api_key=openai_api_key)

        # RAG pipeline
        chain = (
                {"context": retriever, "question": RunnablePassthrough()}
                | prompt
                | model
                | StrOutputParser()
        )
        output = chain.invoke(question)

        return output

    except Exception as e:
        print(f"Error generating response: {e}")
        return None
