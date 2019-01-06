# Survey-Sentiment-Analysis
Batch Sentiment Analysis for survey data in Excel Speadsheets. Uses VADER for sentiment analysis.

## Pre-Requisites
The script uses VADER for sentiment analysis and Pandas. Both are automatically installed when the script is run.

## Analysis
When complete, it generates 4 metrics - neg, neu, pos, and compound. For example:

| Neg  | Neu  | Pos | Compound |
|------|------|-----|----------|
| 0.13 | 0.67 | 0.2 | 0.71     |

| VALUE    | DESCRIPTION                                                                                  |
|----------|----------------------------------------------------------------------------------------------|
| Neg      | As a %, how negative the text was                                                            |
| Neu      | As a %, how neutral the text was                                                             |
| Pos      | As a %, how positive the text was                                                            |
| Compound | An overall sentiment for the text, ranging from -1 (highly negative) to +1 (highly positive) |

## Issues
At present, this script runs without fail on Python 3.X, however, encounters an encoding error on Python 2.X.
