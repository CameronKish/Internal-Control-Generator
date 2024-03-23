def generate_output(selected_options):
    output = ""
    
    category_options = {
        "Nature of Control": {
            "Manual": "Output for Manual control",
            "ITDM": "Output for ITDM control"
        },
        "IPE": {
            "Yes": "What IPE is used? Enter the names of each:",
            "No": None  # No output needed for "No" option
        },
        "Frequency": {
            "Annual": "Performed Annually",
            "Quarterly": "Performed Quarterly frequency",
            "Monthly": "Performed Monthly",
            "Weekly": "Performed Weekly",
            "Daily": "Performed Daily",
            "Recurring": "Recurring Frequency",
            "Ad Hoc": "Performed Ad Hoc"
        },
        "Judgement Involved": {
            "Yes": "What types of judgments are involved? Describe judgments made:",
            "No": None  # No output needed for "No" option
        },
        "Quantitative Thresholds": {
            "Yes": "What are the quantitative thresholds? Enter the values:",
            "No": None  # No output needed for "No" option
        },
        "Qualitative Thresholds": {
            "Yes": "What are the qualitative thresholds? Describe thresholds:",
            "No": None  # No output needed for "No" option
        },
        "Investigation and Resolution Process": {
            "Yes": "Describe the investigation and resolution process:",
            "No": None  # No output needed for "No" option
        }
    }
    
    # Generate output for each category
    for category, options in category_options.items():
        selected_option = selected_options.get(category)
        if selected_option is not None and selected_option == "No":
            continue  # Skip printing this category
        output += f"{category}: "
        if selected_option is not None:
            if selected_option == "Yes":
                user_input = input(f"{options[selected_option]}")
                output += f"{user_input}\n"
            elif options[selected_option] is not None:
                output += options[selected_option] + "\n"
        else:
            output += "No option selected\n"
    
    # Generic line
    output += "Below are now examples of layouts for this type of control.\n"

    # Add additional static lines
    if selected_options.get("Nature of Control") == "Manual":
        output += "Additional line for Manual control\n"
    elif selected_options.get("Nature of Control") == "ITDM":
        output += "Additional line for ITDM control\n"
    
    if selected_options.get("IPE") == "Yes":
        output += (
            "Below are 3 templates for examples of what different IPE attributes look like:\n"
            "IPE 1: **Data Generation and Review:** These control attributes involve generating substantiating reports or data lists (primarily using SAP or Blackline), subsequent review for accuracy and completeness, and usage of this data in subsequent steps.\n" 
            "IPE Template 1: [Role] prepares the [Report Name] from the [System Name] using [Process/Method]. The prepared data/report is then reviewed by [Reviewer Role] for completeness and accuracy. [Reviewer Role] also validates the parameters/data such as [List of parameters] that are used.\n"
            "IPE 2: **Data Analysis and Adjustment:** These attributes involve applying specific adjustments or manipulations to the data or report generated in previous steps (like application of VLOOKUP, filters, pivot tables, cutoff adjustments etc.), and then reviewing these adjustments for accuracy and completeness.\n"
            "IPE Template 2: The [Role] applies necessary adjustments on the [Report Name/Data] using [Method like VLOOKUPS, filters etc.]. The adjusted data is then reviewed by [Reviewer Role] to ensure that the proper adjustments are made and the resulting data/report is accurate.\n"
            "IPE 3: **Data Validation and Approval:** These attributes primarily involve final validation or reconciliation of data or numbers, and obtaining necessary approvals on journal entries or adjustments.\n"
            "IPE Template 3: The [Role] validates the [data/report] and ensures that the totals or specific numbers reconcile/match with [comparison reference]. Journal Entries (if applicable) are reviewed and approved by a competent [Reviewer Role] before being posted into [System Name].\n"
            "In general, all IPE attributes primarily involve some form of data/report generation, analysis or manipulation, and final validation/approval. These categories are not entirely mutually exclusive and a single attribute can fall into multiple of these categories depending on the specifics. Lastly, all these control activities contribute towards ensuring completeness, accuracy, validity and appropriateness of financial reporting.\n"
        )
    if selected_options.get("Judgement Involved") == "Yes":
        output += (
            "Below are 4 templates for examples of what different design attributes look like:\n"
            "Design 1. Report Generation & Review: These attributes involve generating various financial reports, databases, or summaries, followed by detailed reviews to ensure correctness and completeness.\n"
            "Design Template 1: [Frequency], the [Role] will generate the [Report Name]. The [Role] will retain [Evidence] to ensure the report was generated correctly. The [Review Role] will reperform the [Role]'s procedures to ensure all steps were executed correctly.\n"
            "Design 2. Reconciliation & Validation: These attributes mainly deal with cross-checking data from multiple sources or reports to ensure accuracy and consistency, frequently performing manual or systemic reconciliations.\n"
            "Design Template 2: [Role] will reconcile [Data Point 1] to [Data Point 2] for completeness/accuracy on a [Frequency] basis. Any discrepancy above [Threshold] would be investigated and adjusted accordingly."
            "Design 3. Approval & Confirmation: These attributes deal with acquiring approval from senior management or confirming changes to various financial elements, to ensure accuracy and appropriateness.\n"
            "Design Template 3: Any changes to [Financial Element] will be confirmed/approved by [Role]. Evidence of the approval/confirmation will be retained per audit trail requirements.\n" 
            "Design 4. Analysis & Assessment: These attributes involve deep analysis and assessment of financial data to identify potential risks, trends or discrepancies.\n"
            "Design Template 4: The [Role] conducts thorough analysis/assessment on a [Frequency] basis. If any part of the [Data Set] exceeds/anomalies are identified, further examination will be conducted. Any discrepancies over [Threshold] will be reported and addressed.\n"
        )
    elif selected_options.get("Judgement Involved") == "No":
        output += (
            "Below are 5 templates for examples of what different design attributes look like:\n"
            "Design 1: Review and approval – This involves the assessment of documents, values and parameters by an authority for correctness, completeness and accuracy. Often, the status of the review and approval is evidenced by sign-offs.\n"
            "Design Template 1: [Position] conducts review of [Data/Document/Procedure] to ensure [Specific Criteria]. Completion of review is evidenced by [Evidence].\n"
            "Design 2: Data extraction and manipulation – Procedures involving extraction of data from systems and further processing, categorizing or modifying this data for various purposes.\n"
            "Design Template 2: Using [Tool/System], [Execute position] extracts [Data] and performs [Specific Procedures]. The result is then used for [Specific Purpose].\n"
            "Design 3: Reconciliation - Processes to ensure two sets of records are in agreement and correct. The reconciliation process ensures that the money leaving an account matches the actual amount spent and that the two are balanced at the end of the recording period.\n"
            "Design Template 3: [Position] performs reconciliation of [GL balance/Subledger balance] to [Supporting Documents]. Any discrepancies greater than [$Threshold] are investigated for proper explanation/documentation.\n"
            "Design 4: Control Procedures in Event of Anomalies – Steps to be taken when discrepancies, errors or mismatches are identified, which typically involve investigative procedures and corrective actions.\n"
            "Design Template 4: In event of [Specific Anomaly], [Position] performs [Specific Investigative Procedures]. Following investigation, [Corrective Procedures] are implemented.\n"
            "Design 5: Sampling and Testing Methods - Different methods of taking representative samples from a population and performing specific tests or checks.\n"
            "Design Template 5: [Position] uses [Specific Method/Tool] to select samples for testing. Samples are then tested for [Specific Criteria/Conditions].\n"
        )
    
    return output

# Example usage
selected_options = {
    "Nature of Control": "Manual",
    "IPE": "Yes",
    "Frequency": "Monthly",
    "Judgement Involved": "Yes",
    "Quantitative Thresholds": "Yes",
    "Qualitative Thresholds": "No",
    "Investigation and Resolution Process": "No"
}

output_text = generate_output(selected_options)
Post_prompt= input(f"Please provide a detailed description of all activity occuring to achieve the objective of this control:\n\n ")


print(output_text + "Using the above detail as examples, here is a description of the control being performed. Please draft attributes using the control details above in addition to the following control description: " + Post_prompt)
