{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "04dc8838-5daf-46c9-bd3b-b5733bd77f1b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: openai in c:\\users\\admin\\anaconda3\\lib\\site-packages (0.28.0)\n",
      "Requirement already satisfied: requests>=2.20 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from openai) (2.32.2)\n",
      "Requirement already satisfied: tqdm in c:\\users\\admin\\anaconda3\\lib\\site-packages (from openai) (4.66.4)\n",
      "Requirement already satisfied: aiohttp in c:\\users\\admin\\anaconda3\\lib\\site-packages (from openai) (3.9.5)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (2.2.2)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from requests>=2.20->openai) (2024.8.30)\n",
      "Requirement already satisfied: aiosignal>=1.1.2 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from aiohttp->openai) (1.2.0)\n",
      "Requirement already satisfied: attrs>=17.3.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from aiohttp->openai) (23.1.0)\n",
      "Requirement already satisfied: frozenlist>=1.1.1 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from aiohttp->openai) (1.4.0)\n",
      "Requirement already satisfied: multidict<7.0,>=4.5 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from aiohttp->openai) (6.0.4)\n",
      "Requirement already satisfied: yarl<2.0,>=1.0 in c:\\users\\admin\\anaconda3\\lib\\site-packages (from aiohttp->openai) (1.9.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\admin\\anaconda3\\lib\\site-packages (from tqdm->openai) (0.4.6)\n"
     ]
    }
   ],
   "source": [
    "!pip install openai"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5a4c7e74-1109-4ef7-8f13-589cdc07e907",
   "metadata": {},
   "outputs": [],
   "source": [
    "import openai\n",
    "\n",
    "def get_embeddings_oai(texts):\n",
    "    \"\"\" Get text embeddings using OpenAI's model. \"\"\"\n",
    "    response = openai.Embedding.create(\n",
    "        model=\"text-embedding-ada-002\",\n",
    "        input=texts\n",
    "    )\n",
    "    return [embedding[\"embedding\"] for embedding in response[\"data\"]]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2556fedf-3aa1-4167-ac9d-fba60b8caf6e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
