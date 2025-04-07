from src.translator import translate_content
import unittest
from unittest.mock import patch, MagicMock


def test_chinese():
    is_english, translated_content = translate_content("这是一条中文消息")
    assert is_english == False
    assert translated_content == "This is a Chinese message."

def test_spanish():
    is_english, translated_content = translate_content("Este es un mensaje en español.")
    assert is_english == False
    assert translated_content == "This is a message in Spanish."

@patch('src.translator.client.chat.completions.create')
def test_llm_normal_response(mock_completions):
    lang_response = MagicMock()
    lang_response.choices = [MagicMock()]
    lang_response.choices[0].message.content = "english"
    
    # Set up mock to return the language response
    mock_completions.return_value = lang_response
    
    is_english, translated_content = translate_content("This is an English message.")
 
    assert is_english == True
    assert translated_content == "This is an English message."

    # Verify that the API was called once for language detection
    mock_completions.assert_called_once()

@patch('src.translator.client.chat.completions.create')
def test_llm_gibberish_response(mock_completions):
    lang_response = MagicMock()
    lang_response.choices = [MagicMock()]
    lang_response.choices[0].message.content = "unknown"
    
    translation_response = MagicMock()
    translation_response.choices = [MagicMock()]
    translation_response.choices[0].message.content = "Unintelligible text"
    
    # Set up mock to return different responses on consecutive calls
    mock_completions.side_effect = [lang_response, translation_response]
    
    is_english, translated_content = translate_content("ejwfbgio@$uehf werifuh$*@)weoiuf ewuf$%we")
    
    # Verify the response
    assert is_english == False
    assert translated_content == "Unintelligible text"


    # Set up mock to return different responses on consecutive calls
    mock_completions.side_effect = [lang_response, translation_response]
    
    is_english, translated_content = translate_content(" ") # Empty string
    
    # Verify the response
    assert is_english == False
    assert translated_content == "Unintelligible text"
    
    # Verify that the API was called 4 times (twice for language detection, twice for translation)
    assert mock_completions.call_count == 4