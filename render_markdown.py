from models import ProfessionalProfile


def create_resume_markdown(profile: ProfessionalProfile, output_path: str) -> str:
    """
    Create a clean, ATS-friendly resume in Markdown format.
    
    Args:
        profile: CanonicalProfile object with structured resume data
        output_path: Path where to save the output Markdown file
        
    Returns:
        str: Path to the created Markdown file
    """
    lines = []

    print(profile)
    
    # Header with contact information
    if profile.contact_info.full_name:
        lines.append(f"# {profile.contact_info.full_name}")
        lines.append("")
    
    # Contact details
    contact_parts = []
    if profile.contact_info.email:
        contact_parts.append(f"📧 {profile.contact_info.email}")
    if profile.contact_info.location:
        contact_parts.append(f"📍 {profile.contact_info.location}")
    if profile.contact_info.linkedin:
        contact_parts.append(f"💼 [LinkedIn]({profile.contact_info.linkedin})")
    
    if contact_parts:
        lines.append(" | ".join(contact_parts))
        lines.append("")
    
    lines.append("---")
    lines.append("")
    
    # Professional summary
    if profile.professional_summary:
        lines.append("## Professional Summary")
        lines.append("")
        lines.append(profile.professional_summary)
        lines.append("")
    
    # Experience section
    if profile.experience:
        lines.append("## Professional Experience")
        lines.append("")
        
        # Limit to max 4 most recent roles
        recent_experiences = profile.experience[:4]
        
        for exp in recent_experiences:
            if exp.job_title and exp.company_or_product:
                lines.append(f"### {exp.job_title}")
                lines.append(f"**{exp.company_or_product}**")
                
                # Dates
                if exp.start_date:
                    date_text = exp.start_date
                    if exp.end_date:
                        date_text += f" - {exp.end_date}"
                    elif exp.is_current:
                        date_text += " - Present"
                    lines.append(f"*{date_text}*")
                
                lines.append("")
                
                # Bullets (max 6)
                bullets = exp.bullets[:6] if exp.bullets else []
                for bullet in bullets:
                    lines.append(f"- {bullet}")
                
                lines.append("")
    
    # Education section
    if profile.education:
        lines.append("## Education")
        lines.append("")
        
        for edu in profile.education:
            if edu.degree and edu.institution:
                lines.append(f"### {edu.degree}")
                lines.append(f"**{edu.institution}**")
                
                if edu.graduation_date:
                    lines.append(f"*{edu.graduation_date}*")
                
                lines.append("")
    
    # Technical skills section
    if profile.technical_skills:
        lines.append("## Technical Skills")
        lines.append("")
        lines.append(" • ".join(profile.technical_skills))
        lines.append("")
    
    # Certifications
    if profile.certifications:
        lines.append("## Certifications")
        lines.append("")
        for cert in profile.certifications:
            lines.append(f"- {cert}")
        lines.append("")
    
    # Languages
    if profile.languages:
        lines.append("## Languages")
        lines.append("")
        lines.append(" • ".join(profile.languages))
        lines.append("")
    
    # Write to file
    content = "\n".join(lines)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return output_path