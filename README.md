# smartcity-park-ux-planning-cbr

# SmartCity Park UX Planning — CBR System
A Smart City CBR system that analyzes park user behavior and recommends optimized Tech UX (TUX), Space UX (SUX), and Behavior UX (BUX) solutions. The system retrieves similar past cases, generates and ranks UX design interventions, and supports data-driven planning for urban service, spatial, and technology design.


---

# 📌 Table of Contents
- [About The Project](#about-the-project)
- [CBR Workflow](#cbr-workflow)
- [Case Features](#case-features)
- [Case Base Summary](#case-base-summary)
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


___
# Case Features

The CBR system evaluates Smart City park waste-related behaviors using a structured feature schema that includes **User Basic Information**, **Problem (Behavior + Context)**, and **Evaluation Outcome**.  
These features are encoded consistently for similarity matching and solution recommendation.

---

## **1. User Basic Information**

### **1-1. User Interaction Type (User_Interaction_Type)**

| Code | Type | Description |
|------|------|-------------|
| **RU** | Recreational Users | Individuals/groups engaging in leisure activities (walking, sports, picnics, relaxation) |
| **SIU** | Special Interest Users | Visitors with specific interests (pet owners, bird watchers, fitness users, etc.) |
| **EP** | Event Participants | Visitors attending scheduled events (public or private) |
| **CEU** | Cultural & Educational Users | School groups, tourists, or visitors engaging in learning activities |
| **OS** | Operational Staff | Park workers (maintenance, safety, administration, event organizers) |
| **SS** | Support Services | External vendors (food trucks, rental services, tour guides) |

---

### **1-2. Scenario (Scenario)**  
Represents the activity context in which the behavior occurs.

| Code | Scenario | Description |
|------|----------|-------------|
| **ET** | Exploring Trails | Walking, hiking, jogging; movement-based exploration |
| **EP** | Enjoying Picnics | Eating outdoors, group socializing, finding picnic spots |
| **EIP** | Engaging in Play | Children/family play and interactive installations |
| **PS** | Participating in Sports | Sports participation (organized or casual) |
| **AE** | Attending Events | Concerts, festivals, community or private gatherings |
| **ON** | Observing Nature | Bird-watching, photography, nature appreciation |
| **RS** | Relaxing in Solitude | Meditation, reading, resting in quiet areas |

---

## **2. Problem (Behavior + Context)**

The system encodes both **Disposal Behavior** and **Context** to understand why a certain waste-related action occurred.

---

### **2-1. Disposal Behavior (Disposal_Behavior)**

#### **Positive Behavior (PO)**  
| Code | Behavior | Meaning |
|------|----------|---------|
| **PO-PD** | Proper Disposal | Trash disposed correctly |
| **PO-RC** | Recycling Correctly | User sorts recyclables correctly |
| **PO-PULPD** | Picking Up Litter | User picks up litter & disposes properly |

#### **Neutral Behavior (NT)**  
| Code | Behavior | Meaning |
|------|----------|---------|
| **NT-DNRO** | Disposing Non-recyclables Only | Does not sort recyclables; disposes only general waste |
| **NT-POT** | Packing Out Trash | User carries trash out (take-out behavior) |

#### **Negative Behavior (NG)**  
| Code | Behavior | Meaning |
|------|----------|---------|
| **NG-IRBU** | Incorrect Recycling Bin Use | Wrong sorting / misuse of recycling bins |
| **NG-DTPR** | Trash in Public Restrooms | Discards waste in restroom bins |
| **NG-LOG** | Littering on the Ground | Leaves trash in open areas |

---

### **2-2. Context (Context)**  
Conditions influencing the user’s behavior.

#### **Bad Context**

##### **Personal Factors**
| Code | Meaning |
|------|---------|
| **PF-LPA** | Lack of Public Awareness |
| **PF-CRG** | Confusing Recycling Guidelines |

##### **Environmental Factors**
| Code | Meaning |
|------|---------|
| **EF-OTB** | Overflowing Trash Bin |
| **EF-SWS** | Seasonal Waste Spike |
| **EF-DFTC** | Difficulty Finding Trash Can (Lack of signage / visibility) |
| **EF-INOB** | Insufficient Number of Bins |

#### **Good Context**
| Code | Meaning |
|------|---------|
| **EF-SPB** | Strategically Placed Bins (picnic areas, sports fields, walking paths) |

---

## **3. Evaluation Outcome (Evaluation_Outcome)**  
Represents whether the user behavior was appropriate given the context and environment.

| Code | Meaning |
|------|---------|
| **A** | Appropriate |
| **PA** | Partially Appropriate |
| **IA** | Inappropriate |

---

# Case Base Summary
The system currently includes **11 curated cases** representing diverse user behaviors, contexts, and Smart City UX/Service/Spatial interventions within park environments.  
These cases support CBR similarity matching, evaluation, and multi-dimensional UX solution generation.

| Case ID | User Type | Scenario | Behavior | Context | Eval | UX Solution | Smart City Solution |
| Case ID | User Type | Scenario | Disposal Behavior | Context | Evaluation | UX Solution | Smart City Design Solution |
|--------|-----------|----------|-------------------|---------|------------|-------------|-----------------------------|
| **01** | Visitor | Picnic | Littering | Difficulty finding trash can (No signage) | IA | Add trashcans + signage | Integrated Waste Mgmt System + Smart Recycling Stations |
| **02** | Family | Picnic | Trash in restroom | Overflowing bin | IA | Deploy mobile waste bins | Adaptive Waste Collection Schedule |
| **03** | Children | Playground | Trash in restroom | Unclear sorting guidelines | IA | Clear recycling guidelines | Educational & Interactive Waste Disposal |
| **04** | Visitor | Picnic | Proper disposal | Strategically placed bins | A | Maintain bin placement | Expanded Smart Bin System |
| **05** | Visitor | Playground | Recycling | Walking path context | A | Maintain & promote recycling | Smart Recycling Stations |
| **06** | Visitor | Sports | Trash but not recycle | Lack of public awareness | IA | Waste disposal campaign | Sports-themed engagement program |
| **07** | Visitor | Walking | Packing out trash | Jogging route (normal) | A | Incentives for pack-out | Accessible waste point design |
| **08** | Visitor | Picnic | Packing out trash | Seasonal waste fluctuations | A | Add bins & staffing in peaks | Predictive seasonal waste scheduling |
| **09** | Visitor | Event Participation | Trash but not recycle | Overflowing bin | IA | Temporary event waste stations | Educational/Interactive waste engagement during events |
| **10** | Vendor | Event Selling | Trash in restroom | Difficulty finding trashcan | IA | Increase bins for vendors | Waste location wayfinding (Vendor App) |
| **11** | RU | ET (Trails) | Mixed: PO-PD + NT-POT | EF-DFTC | PA | Signage + extra bins on trails | TUX-IWMS + BUX-PEAP |

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
HCI Research · UX Planning · Interaction Design · Smart City





