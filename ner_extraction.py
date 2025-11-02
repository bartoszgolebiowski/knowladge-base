import os
import json
import re
import spacy
from pathlib import Path
from spacy.pipeline import EntityRuler
from spacy.lang.en.stop_words import STOP_WORDS
from collections import Counter

# Ścieżka do folderu z dokumentami
DOCS_DIR = Path("knowladge/sa-prof")


ADDITIONAL_STOPWORDS = {
    "account",
    "accounts",
    "application",
    "applications",
    "automation",
    "availability",
    "backup",
    "benefits",
    "budget",
    "budgets",
    "capacity",
    "central",
    "centrally",
    "cloud",
    "compute",
    "configuration",
    "connectivity",
    "console",
    "cost",
    "customers",
    "data",
    "default",
    "deployment",
    "deployment options",
    "design",
    "development",
    "devices",
    "environment",
    "environments",
    "example",
    "feature",
    "features",
    "function",
    "goals",
    "guidance",
    "implementation",
    "improvements",
    "infrastructure",
    "integration",
    "introduction",
    "latency",
    "library",
    "logging",
    "management",
    "migration",
    "network",
    "networks",
    "overview",
    "performance",
    "platform",
    "portfolio",
    "presentation",
    "pricing",
    "process",
    "recommendations",
    "reference",
    "requirements",
    "resources",
    "scalability",
    "security",
    "solution",
    "solutions",
    "support",
    "testing",
    "usage",
    "use case",
    "workflow",
}

UPPERCASE_TOKENS = {
    "aws",
    "iam",
    "sns",
    "sqs",
    "kms",
    "efs",
    "vpn",
    "waf",
    "sso",
}

ACRONYM_MAP = {
    # Pełne nazwy -> akronimy
    "amazon ec2": "ec2",
    "aws ec2": "ec2",
    "amazon s3": "s3",
    "aws s3": "s3",
    "amazon rds": "rds",
    "aws rds": "rds",
    "amazon eks": "eks",
    "aws eks": "eks",
    "amazon ecs": "ecs",
    "aws ecs": "ecs",
    "aws identity and access management": "iam",
    "aws key management service": "kms",
    "amazon sns": "sns",
    "aws sns": "sns",
    "amazon sqs": "sqs",
    "aws sqs": "sqs",
    "amazon vpc": "vpc",
    "aws vpc": "vpc",
    "aws cloudformation": "cloudformation",
    "auto scaling": "auto scaling",
    "application load balancer": "alb",
    "network load balancer": "nlb",
    "elastic load balancing": "elb",
    "amazon efs": "efs",
    "aws efs": "efs",
    "amazon emr": "emr",
    "aws emr": "emr",
    "aws glue": "glue",
    "amazon ebs": "ebs",
    "aws ebs": "ebs",
    "aws systems manager": "ssm",
    "aws resource access manager": "ram",
    "aws waf": "waf",
    "aws vpn": "vpn",
    "aws elastic network interfaces": "eni",
    "amazon elastic network interfaces": "eni",
    "elastic network interfaces": "eni",
    "amazon cloudfront": "cloudfront",
    "aws cloudfront": "cloudfront",
    "amazon lambda": "lambda",
    "aws lambda": "lambda",
    "amazon dynamodb": "dynamodb",
    "aws dynamodb": "dynamodb",
    "amazon aurora": "aurora",
    "aws aurora": "aurora",
    "amazon redshift": "redshift",
    "aws redshift": "redshift",
    "aws athena": "athena",
    "amazon athena": "athena",
    "aws sagemaker": "sagemaker",
    "amazon sagemaker": "sagemaker",
    "aws rekognition": "rekognition",
    "amazon rekognition": "rekognition",
    "aws comprehend": "comprehend",
    "amazon comprehend": "comprehend",
    "aws kinesis": "kinesis",
    "amazon kinesis": "kinesis",
    "aws route 53": "route 53",
    "amazon route 53": "route 53",
    "aws guardduty": "guardduty",
    "amazon guardduty": "guardduty",
    "aws config": "config",
    "amazon config": "config",
    "aws organizations": "organizations",
    "amazon organizations": "organizations",
    "aws budgets": "budgets",
    "amazon budgets": "budgets",
    "aws cost explorer": "cost explorer",
    "amazon cost explorer": "cost explorer",
}


def normalize_entity(entity: str) -> str:
    """Normalizuje encję do formy kanonicznej w lower-case."""
    text = re.sub(r"[\*\`\"\(\)\[\]\{\}:;,]+", " ", entity.lower())
    text = re.sub(r"[^a-z0-9\-\+/&\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    # Usuń "amazon" jeśli występuje w encji
    text = re.sub(r"\bamazon\b", "", text).strip()
    text = re.sub(r"\baws\b", "", text).strip()
    return text


def clean_entities(entities, content):
    """Czyści i normalizuje listę encji."""
    content_lower = content.lower()
    cleaned = {}

    for raw_entity in entities:
        normalized = normalize_entity(raw_entity)
        if not normalized:
            continue

        if len(normalized) < 3:
            continue

        tokens = normalized.split()
        if any(len(token) == 1 for token in tokens):
            continue

        if normalized in STOP_WORDS or normalized in ADDITIONAL_STOPWORDS:
            continue

        if len(tokens) == 1 and tokens[0].endswith(("ing", "ly")):
            continue

        canonical_key = ACRONYM_MAP.get(normalized, normalized)
        formatted = canonical_key

        if normalized not in content_lower and canonical_key not in content_lower:
            continue

        cleaned[canonical_key] = formatted

    return sorted(cleaned.values())


def extract_entities(text, nlp):
    """Ekstrakcja encji z tekstu za pomocą spaCy."""
    doc = nlp(text)
    entities = []
    for ent in doc.ents:
        print(f"Znaleziono encję: {ent.text} o typie {ent.label_}")
        if ent.label_ in ["ORG", "PRODUCT", "GPE"] and len(ent.text) > 2:
            entities.append(ent.text.lower())
    return list(set(entities))


def process_documents():
    """Przetwarzanie wszystkich dokumentów markdown."""
    nlp = spacy.load("en_core_web_sm")

    results = {}

    # Iteracja po plikach .md
    for file_path in DOCS_DIR.glob("*.md"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Ekstrakcja encji
            entities = extract_entities(content, nlp)
            cleaned_entities = clean_entities(entities, content)
            results[file_path.name] = cleaned_entities
            print(
                f"Przetworzono: {file_path.name} - surowe {len(entities)}, po czyszczeniu {len(cleaned_entities)} encji"
            )
        except Exception as e:
            print(f"Błąd przetwarzania {file_path.name}: {e}")

    # Filtruj rzadkie encje (mniej niż 3 wystąpienia)
    entity_count = Counter()
    for entities in results.values():
        for entity in entities:
            entity_count[entity] += 1

    filtered_results = {}
    for doc, entities in results.items():
        filtered_entities = [ent for ent in entities if entity_count[ent] >= 3]
        if filtered_entities:
            filtered_results[doc] = filtered_entities

    print(
        f"Po filtracji rzadkich encji: {sum(len(entities) for entities in filtered_results.values())} encji w {len(filtered_results)} dokumentach."
    )

    output_file = Path("ner_results.json")
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(filtered_results, f, indent=4, ensure_ascii=False)
    print(f"Wyniki zapisane do {output_file}")


if __name__ == "__main__":
    process_documents()
