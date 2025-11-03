# Polly

## **Amazon Polly - Key Concepts**

Amazon Polly is an AWS service that uses deep learning to convert text into lifelike speech, enabling applications to "talk."

## **Key Features**

- **Pronunciation Lexicons:** Allow customization of word pronunciation. This is useful for:
    - Stylized words with non-standard spellings.
    - Acronyms (e.g., ensuring "AWS" is pronounced "Amazon Web Services").
    - Lexicons are uploaded and used with the `SynthesizeSpeech` operation.
- **Speech Synthesis Markup Language (SSML):** Provides granular control over speech output, including:
    - Emphasis on specific words or phrases.
    - Phonetic pronunciation.
    - Inclusion of effects like breathing sounds or whispering.
    - Different speaking styles (e.g., Newscaster).

## **Demonstration Highlights**

- **Neural Text-to-Speech (NTTS):** Produces highly natural and human-like speech.
- **Voice Selection:** Offers a variety of voices to choose from.
- **SSML Implementation:** Demonstrates how to use SSML tags to:
    - Insert pauses (`<break>`).
    - Control emphasis (not explicitly shown but mentioned as a capability).
- **Lexicon Application:** Shows where to apply a custom lexicon to modify the pronunciation of specific terms like "AWS." A lexicon file needs to be created and uploaded for this functionality.