STRUCTURE_PROFILE_PROMPT = """
You are an expert resume parser. Extract and structure the following resume text into a JSON format.

IMPORTANT: Only extract information that is explicitly stated in the text. Do NOT make assumptions or add information that isn't clearly present.

Resume Text:
{raw_text}

Please return a JSON object with the following structure:

{{
  "profile": {{
    "contact_info": {{
      "full_name": "string or null",
      "email": "string or null", 
      "phone": "string or null",
      "location": "string or null",
      "linkedin": "string or null",
      "github": "string or null",
      "portfolio": "string or null"
    }},
    "professional_summary": "string or null",
    "experience": [
      {{
        "job_title": "string or null",
        "company": "string or null", 
        "location": "string or null",
        "start_date": "string or null",
        "end_date": "string or null",
        "is_current": false,
        "bullets": ["list of achievement bullets"]
      }}
    ],
    "education": [
      {{
        "degree": "string or null",
        "institution": "string or null",
        "location": "string or null", 
        "graduation_date": "string or null",
        "gpa": "string or null",
        "relevant_coursework": ["list of courses"]
      }}
    ],
    "technical_skills": ["list of technical skills"],
    "certifications": ["list of certifications"],
    "languages": ["list of languages"]
  }},
  "missing_fields": ["list of fields that are missing or unclear"]
}}

Focus on:
- Contact information from headers
- Work experience with quantified achievements
- Education details
- Technical skills and tools
- Certifications and languages

Mark fields as missing if they are incomplete, unclear, or would benefit from clarification.
"""

GENERATE_QUESTIONS_PROMPT = """
Based on the missing fields identified in the resume, generate 3-5 concise clarification questions to fill gaps.

Missing fields: {missing_fields}

Current profile summary:
{profile_summary}

Generate questions that will help create a complete, ATS-friendly resume. Focus on:
- Missing contact information
- Unclear employment dates
- Vague job responsibilities or achievements 
- Missing technical skills
- Incomplete education details

Return as a JSON list of strings:
["Question 1?", "Question 2?", "Question 3?"]

Keep questions specific and actionable. Avoid asking about information that's already clear.
"""

JD_ADAPTATION_PROMPT = """
You are an expert resume optimizer. Adapt the following resume profile to better match the target job description.

Current Profile:
{profile}

Target Job Description:
{job_description}

RULES:
- Do NOT fabricate experience, skills, or achievements
- Only reorder, emphasize, or rephrase existing content
- Prioritize relevant skills and experiences
- Adjust professional summary to highlight relevant qualifications
- Reorder bullet points to lead with most relevant achievements
- Ensure all claims remain truthful and verifiable

Return the adapted profile in the same JSON structure as provided, with optimized content for ATS systems and human reviewers.

Focus on:
- Keywords from the job description (when truthfully applicable)
- Relevant technical skills ordering
- Achievement bullets that demonstrate required competencies
- Professional summary alignment with role requirements
"""

HITL_INSTRUCTION_PROMPT = """
Please answer the following questions to complete your resume profile:

{questions}

Provide clear, specific answers. For dates, use MM/YYYY format. For achievements, include numbers when possible.
"""