# AI Analytics Assistant

**Status:** Planned project. Implementation has not started yet.

## Project Goal

Build an AI assisted analytics application that allows a user to ask business questions in natural language and turn those questions into a structured SQL based analysis workflow.

## Planned Workflow

1. Accept a business question from the user.
2. Provide the application with database schema and business context.
3. Use an LLM to propose SQL for the question.
4. Validate joins, filters, aggregations, dates, and business rules before accepting the query.
5. Run the validated query against a relational database.
6. Use Python and Pandas to analyze the result.
7. Present useful summaries and visualizations.
8. Test the system with a repeatable set of business questions and document failure cases.

## Planned Technologies

- Python
- SQL
- Pandas
- LLM API
- Relational database
- Streamlit or FastAPI

## Engineering Focus

- Natural language to SQL
- Schema aware prompting
- Query validation
- Human review of AI generated output
- Error handling
- Evaluation and failure analysis
- Clear application architecture

## Current State

This repository folder currently contains the project plan only. Code, tests, evaluation results, architecture documentation, and implementation details will be added as the project is built and verified.
