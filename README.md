# smartcity-park-ux-planning-cbr

# SmartCity Park UX Planning — CBR System
A Smart City CBR system that analyzes park user behavior and recommends optimized Tech UX (TUX), Space UX (SUX), and Behavior UX (BUX) solutions. The system retrieves similar past cases, generates and ranks UX design interventions, and supports data-driven planning for urban service, spatial, and technology design.


---

# 📌 Table of Contents
- [About The Project](#about-the-project)
- [CBR Workflow](#cbr-workflow)
- [Case Structure](#case-structure)
- [Similarity Model](#similarity-model)
- [Repository Structure](#repository-structure)
- [How to Run](#how-to-run)
- [Example Output](#example-output)
- [Future Work](#future-work)
- [License](#license)

---

# About The Project

Smart City parks generate diverse user behaviors driven by environmental factors, population density, waste bin placement, signage clarity, and UX system interactions.  
This project aims to **analyze these behaviors through Case-Based Reasoning (CBR)** and provide **data-driven UX planning recommendations**.

The system identifies:
- What type of behavior problem occurred  
- Under what environmental context  
- Which UX intervention (TUX/SUX/BUX) is most effective  

Ultimately, it acts as a **decision-support engine** for urban UX planners and Smart City designers.

---

# CBR Workflow
Input → A new case consisting of observed behaviors & context

1. Case Matching  
   - Weighted similarity calculation  
   - Behavior + Context + User Type matching  

2. Solution Generation  
   - Retrieve solutions from similar past cases  
   - Generate an initial solution set  

3. Solution Optimization  
   - Filter by context  
   - Adjust using domain rules / heuristics  
   - (Optional future extension: ML-based effectiveness scoring)  

4. Solution Ranking  
   - Evaluate feasibility, impact, relevance  
   - Return sorted recommendation list  

Output →  
  - Recommended UX solutions (TUX, SUX, BUX)  
  - Implementation guidelines  
  - Expected impact  

Feedback Loop →  
  - Monitor real-world performance  
  - Update case base with new outcomes
  - Improve system accuracy over time  


---

# Case Structure

Each case consists of:

### 1. User Basic Information**
```json
"User_Basic_Information": {
  "User_Interaction_Type": "RU",
  "Scenario": "ET"
}
```

### 2. Disposal Behavior (Problem Features)
```json
  "Problem": {
  "Disposal_Behavior": {
    "PO-PD": 1,
    "PO-RC": 0,
    "PO-PULPD": 0,
    "NT-DNRO": 0,
    "NT-POT": 0,
    "NG-IRBU": 1,
    "NG-DTPR": 0,
    "NG-LOG": 0
  }
}
```

### 3. Context
```json
  "Context": {
  "PF-LPA": 1,
  "PF-CRG": 1,
  "EF-OTB": 0,
  "EF-SWS": 0,
  "EF-DFTC": 1,
  "EF-INOB": 1,
  "EF-SPB": 0
}
```

### 4. Evaluation Outcome
```json
  "Evaluation_Outcome": "IA"
```

### 5. Solutions
```json
  "Solutions": [
  { "Category": "TUX", "Type": "TUX-SRS" },
  { "Category": "BUX", "Type": "BUX-CRG" },
  { "Category": "SUX", "Type": "SUX-TCS" }
]
```

```
Similarity score is computed as:
Total Similarity =
    w_user * Sim(User Info)
  + w_behavior * Sim(Disposal Behavior)
  + w_context * Sim(Context)
  + w_solutions * Sim(Solutions)
```

### 6. Example group weights:
```python
Group_Weights = {
    "User_Info": 0.15,
    "Disposal_Behavior": 0.45,
    "Context": 0.30,
    "Solutions": 0.10
}
```

# Repository Structure
```
smartcity-park-ux-planning-cbr/
│
├── data/
│   └── case_base.json
│
├── cbr/
│   ├── main.py
│   ├── similarity.py
│   ├── case_loader.py
│   ├── evaluation.py
│   └── solution_engine.py
│
└── README.md
```

# How to Run
```bash
python cbr/main.py
```

# Example Output
  Most Similar Case: C014 (similarity 0.82)

# Evaluation Outcome:
  Inappropriate — high-risk disposal behavior detected.

  Recommended Solutions:
  1. TUX-SRS — Smart Recycling Station
  2. SUX-TCS — Clear signage guides
  3. BUX-CRG — Recycling guideline improvements

# Future Work
  - Add ML optimization for similarity weights
  - Implement FastAPI web UI
  - IoT integration with Smart City 
  - Reinforcement learning for solution effectiveness prediction

# License
MIT License

# Author
Gyuri Sim (심규리)
HCI Research · UX Planning · Smart City Interaction Design





