# Requirement ID: FR_hybrid_1

- Description: The system shall provide an emotionally distressed user with an immediate supportive response and at least one relevant coping option when the user reports anxiety, stress, or emotional overload.
- Source Persona: Anxious Student Seeking Immediate Emotional Support
- Traceability: Derived from review group H1
- Acceptance Criteria: Given the user reports anxiety, stress, or emotional overload When the support request is submitted Then the application must display a supportive response and at least one relevant coping option in the same interaction.
- Notes: Refined from the automated requirement by broadening the trigger condition beyond anxiety alone while keeping the response testable.

# Requirement ID: FR_hybrid_2

- Description: The system shall maintain a non-judgmental and emotionally appropriate conversational tone during emotional support interactions.
- Source Persona: Anxious Student Seeking Immediate Emotional Support
- Traceability: Derived from review group H1
- Acceptance Criteria: Given the user is discussing emotional distress When the chatbot responds Then the response must remain supportive, non-judgmental, and aligned with the user’s emotional context.
- Notes: Refined from the automated requirement by making the tone expectation more concise and directly testable.

# Requirement ID: FR_hybrid_3

- Description: The system shall provide bedtime users with direct access to calming sleep and relaxation content.
- Source Persona: Sleep-Deprived User Looking for Low-Effort Relaxation
- Traceability: Derived from review group H2
- Acceptance Criteria: Given the user is seeking sleep or relaxation support at bedtime When the user opens the relevant feature Then the application must provide calming content such as guided exercises, soothing audio, or relaxation activities.
- Notes: Refined from the automated requirement by making the bedtime context explicit.

# Requirement ID: FR_hybrid_4

- Description: The system shall allow a user to reach sleep-support content from the main interface in no more than three user actions.
- Source Persona: Sleep-Deprived User Looking for Low-Effort Relaxation
- Traceability: Derived from review group H2
- Acceptance Criteria: Given the user starts from the home screen When the user attempts to access sleep-support content Then the selected sleep-support feature must be reachable in no more than three user actions.
- Notes: Refined from the automated requirement by converting minimal navigation into a measurable usability constraint.

# Requirement ID: FR_hybrid_5

- Description: The system shall provide users with structured journaling prompts or guided reflection spaces for emotional self-reflection.
- Source Persona: Reflective User Practicing Journaling and CBT
- Traceability: Derived from review group H3
- Acceptance Criteria: Given the user opens the journaling or reflection feature When the session begins Then the application must present a structured prompt, guided reflection space, or equivalent journaling support.
- Notes: Refined from the automated requirement by simplifying the wording while keeping the feature expectation clear.

# Requirement ID: FR_hybrid_6

- Description: The system shall guide users through at least one structured CBT step for identifying, examining, or reframing negative thoughts.
- Source Persona: Reflective User Practicing Journaling and CBT
- Traceability: Derived from review group H3
- Acceptance Criteria: Given the user starts a CBT-related exercise When the activity begins Then the application must guide the user through at least one structured step for identifying, examining, or reframing negative thoughts.
- Notes: Refined from the automated requirement by making the CBT behavior more explicit and educationally grounded.

# Requirement ID: FR_hybrid_7

- Description: The system shall label premium-only features before the user attempts to open or use them.
- Source Persona: Cost-Conscious User Evaluating Whether Premium Is Worth It
- Traceability: Derived from review group H4
- Acceptance Criteria: Given the user browses application features When a premium-only feature is displayed Then the feature must be visibly labeled as premium before the user selects it.
- Notes: Refined from the automated requirement by specifying that the label must appear before attempted use, not after.

# Requirement ID: FR_hybrid_8

- Description: The system shall display subscription cost, billing model, and premium access information together on the premium information screen.
- Source Persona: Cost-Conscious User Evaluating Whether Premium Is Worth It
- Traceability: Derived from review group H4
- Acceptance Criteria: Given the user opens a premium feature or subscription screen When pricing information is presented Then the application must display the subscription cost, billing model, and premium access details together on that screen.
- Notes: Refined from the automated requirement by making the information-location requirement more explicit.

# Requirement ID: FR_hybrid_9

- Description: The system shall allow users to complete interactions with core features without crashing, freezing, or terminating unexpectedly.
- Source Persona: User Whose Trust Depends on Technical Reliability
- Traceability: Derived from review group H5
- Acceptance Criteria: Given the user is actively using a core feature When the interaction is completed Then the application must remain responsive and must not crash, freeze, or terminate unexpectedly.
- Notes: Refined from the automated requirement by focusing on completion of the interaction rather than general use.

# Requirement ID: FR_hybrid_10

- Description: The system shall authenticate a user with valid credentials and load the main interface without error.
- Source Persona: User Whose Trust Depends on Technical Reliability
- Traceability: Derived from review group H5
- Acceptance Criteria: Given the user enters valid login credentials When the login request is submitted Then the application must authenticate the user successfully and load the main interface without error.
- Notes: Retained the automated structure because it was already specific and testable.
