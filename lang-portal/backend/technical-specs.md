# Backend server technical specs

## Business Goal:
    A language learning school wants o build a prototype of language portal which serves as "
    1. Inventory of possible vocabulary that can be learned.
    2. Acts as learning Record store. Providing correct or wrong score on learning vocabulary.
    3. A unified launchpad to launch different launching apps.

## Technical Requirements:
    - Backend will be build using python and flask.
    - Database will SQLite3
    - API will always return JSON.

## Database Schema:
    We have following tables
    1. words
        - id | integer
        - japanese | string
        - romaji | string
        - english | string
        - parts | string
    2. word_groups - join table for words and groups.
        - id|integer
        - word_id|integer
        - group_id|integer

    3. groups - thematic groups of words
        - id|integer
        - name|string
    4. study_sessions - records of study sessions that group word_review_items
        - id
        - study_activity_id
        - word_id
        - created_at - datetime
    5. study_activities - a study activity that links study session to group.
        - id
        - study_session_id
        - group_id - integer
        - created_at - datetime
    6. word_review_items - a record of word practice, determining word is correct or not.
        - word_id - integer
        - study_session_id - integer
        - correct -boolean
        - created_at - datetime

## API Endpoints:
    - GET /words
    - GET /words/:id
    - GET /groups
    - GET /groups/:id
    - GET /groups/:id/words