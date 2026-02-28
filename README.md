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
Ambiguous terms detected: fast, user-friendly  
Weak modal verbs detected: should  
No measurable criteria found (no numbers detected)  

Quality Score: 4/10

## Installation

1. Clone the repository:

2. Navigate to the project folder:

3. Run the program:

## Project Structure
requirements-quality-checker/
├── checker.py
├── main.py
├── ai_module.py
├── requirements.txt
└── README.md


## How It Works

The system applies rule-based checks using:

- Predefined ambiguity dictionaries
- Regular expressions for pattern detection
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

# Requirements Quality Checker

An AI-based analytical system for automated quality evaluation of natural language software requirements.

Requirements Quality Checker is a web-based NLP system that performs structured quality assessment of software requirement statements. The system integrates transformer-based contextual embeddings with modular evaluation logic to analyze clarity, ambiguity, consistency, and semantic similarity.

The project demonstrates modular backend architecture, ML inference integration, and reproducible scoring design suitable for research-oriented extension.

## Motivation

Poorly written requirements introduce ambiguity, inconsistency, and implementation risk in software projects. This system explores automated quality assessment using semantic representations and structured evaluation layers.

The goal is to provide:

- Automated semantic similarity analysis
- Constraint detection and ambiguity analysis
- Multi-dimensional quality scoring
- Structured feedback generation

## System Architecture

The implementation follows a layered architecture:

1. **Input Processing Layer**
   - Requirement parsing
   - Text normalization
   - Preprocessing

2. **Embedding & Semantic Analysis Layer**
   - Transformer-based contextual embeddings
   - Semantic similarity computation
   - Clustering and relatedness detection

3. **Evaluation & Scoring Layer**
   - Rule-based validation mechanisms
   - Multi-dimensional scoring logic
   - Reproducible metric computation

4. **Feedback Synthesis Layer**
   - Structured diagnostic output
   - Human-readable feedback generation

5. **Presentation Layer**
   - Streamlit-based interactive interface
   - Decoupled backend inference pipeline

The architecture is designed for extensibility, enabling integration of additional evaluation models without restructuring core components.

## Tech Stack

- Python
- Streamlit
- Transformer-based NLP models
- Sentence embeddings
- NumPy / Pandas
- Scikit-learn (if applicable)

## Key Features

- Modular backend pipeline
- Real-time inference execution
- Deterministic scoring mechanisms
- Separation of computation and presentation layers
- Clean, maintainable code structure

## Installation

Clone the repository:

```bash
git clone https://github.com/maryamhussain28/requirements-quality-checker.git
cd requirements-quality-checker