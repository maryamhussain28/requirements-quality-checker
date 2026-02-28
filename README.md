# Requirements Quality Checker

A lightweight automated tool for assessing the quality of natural language software requirements based on common requirements engineering best practices.

## Overview

Poorly written requirements often contain ambiguity, weak modal verbs, lack measurable criteria, or use vague terminology. This tool performs automated static analysis of a requirement statement and provides structured feedback along with a quality score.

The goal is to support early-stage requirements validation and improve specification clarity.

## Features

The tool analyzes a requirement statement and checks for:

- Ambiguous terms (e.g., fast, efficient, user-friendly, robust)
- Weak modal verbs (e.g., should, may, might, could)
- Excessive length (>25 words)
- Lack of measurable criteria (no numeric values detected)
- Possible passive voice usage
- Quality score out of 10

## Example

Input:
The system should be fast and user-friendly.

Output:
⚠ Ambiguous terms detected: fast, user-friendly  
⚠ Weak modal verbs detected: should  
⚠ No measurable criteria found (no numbers detected)  

Quality Score: 4/10

## Installation

1. Clone the repository:

2. Navigate to the project folder:

3. Run the program:

## Project Structure
requirements-quality-checker/
├── checker.py
├── main.py
├── requirements.txt
└── README.md


## How It Works

The system applies rule-based checks using:

- Predefined ambiguity dictionaries
- Regular expressions for pattern detection
- Basic linguistic heuristics
- Scoring mechanism based on detected issues

This lightweight approach ensures fast execution and ease of extensibility.

## Future Extensions

Potential improvements include:

- NLP-based syntactic parsing
- Machine learning-based ambiguity detection
- Integration with Large Language Models (LLMs)
- IEEE/ISO 29148 compliance validation
- Web-based interface

## Academic Relevance

This project demonstrates:

- Automated requirements quality analysis
- Rule-based natural language processing
- Practical application of software requirements engineering principles
- Foundation for AI-driven requirements validation research

## License

MIT License