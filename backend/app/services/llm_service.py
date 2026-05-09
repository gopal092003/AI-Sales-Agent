"""
LLM service layer.

Supports:
- Groq
- Ollama
"""

from groq import AsyncGroq

from app.core.config import settings
from app.core.logger import setup_logger

logger = setup_logger()


class LLMService:
    """
    Unified LLM provider service.
    """

    def __init__(self):
        self.groq_client = None

        # Initialize Groq
        if settings.GROQ_API_KEY:
            self.groq_client = AsyncGroq(
                api_key=settings.GROQ_API_KEY
            )

            logger.info(
                "Groq client initialized."
            )

        else:
            logger.warning(
                "Groq API key missing."
            )

    # =====================================================
    # GENERATE
    # =====================================================

    async def generate(
        self,
        prompt: str,
        provider: str = "groq",
        temperature: float = 0.3,
    ) -> str:
        """
        Generate LLM response.
        """

        if provider == "groq":
            return await self._generate_groq(
                prompt=prompt,
                temperature=temperature,
            )

        raise ValueError(
            f"Unsupported provider: {provider}"
        )

    # =====================================================
    # GROQ
    # =====================================================

    async def _generate_groq(
        self,
        prompt: str,
        temperature: float = 0.3,
    ) -> str:
        """
        Generate using Groq API.
        """

        if not self.groq_client:
            raise ValueError(
                "Groq client is not configured."
            )

        response = (
            await self.groq_client.chat.completions.create(
                model=settings.DEFAULT_LLM_MODEL,
                temperature=temperature,
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
            )
        )

        return (
            response.choices[0]
            .message.content.strip()
        )


# Singleton instance
llm_service = LLMService()