## Prompt 1: Technical Variables

**Objective:** Extract key insights from the customer testimonial about [Company Name]'s Business Intelligence (BI) adoption and implementation process.

**Guiding Questions:**
**1. Adoption Drivers:** What were the primary drivers behind [Company Name]'s BI adoption? (e.g., [adoption driver 1], [adoption driver 2], etc.)
**2. Implementation Strategies:** Which strategies did [Company Name] employ to successfully deploy its BI capabilities? (e.g., [implementation strategy 1], [implementation strategy 2], etc.)
3. **Challenges and Solutions:** What were the most common challenges faced by [Company Name] during its BI implementation process, and how were they addressed? (e.g., [common challenge 1], [common challenge 2], etc.)
**4. Monetization:** How did [Company Name] monetize its BI capabilities? (e.g., [monetization approach 1], [monetization approach 2], etc.)
**5. Collaboration and Culture:** What strategies did [Company Name] use to promote team collaboration and data-driven decision-making within its organization as a result of implementing BI?
**6. Mobile Accessibility:** Does [Company Name] display their dashboard in mobile apps?
**7. Ease of Use:** How intuitive and user-friendly is the platform? Consider feedback related to the learning curve and user interface.
**8. Functionality:** What features are available (e.g., data visualization, report generation, analytics)? Assess whether the platform meets the diverse needs of users.
**9. Integration Capabilities:** How easily can the platform integrate with other tools and systems in the users’ environments?
**10. Scalability:** Can the platform scale according to the organization’s needs? Consider feedback on its performance as the amount of data grows.
**11. Cost Effectiveness:** Assess perceptions regarding the platform’s pricing relative to its features and capabilities.
**12. Customer Support:** How effective is the customer support? Review comments about the responsiveness and helpfulness of the support team.
**13. Data Security:** How well does the platform secure user data? Include feedback on any security features and users’ trust in the platform.
**14. Customization Options:** How adaptable is the platform to specific business needs? Consider how users feel about the customization capabilities.
**15. Training and Resources:** Review the availability and quality of training materials and resources to help users maximize their use of the platform.

**Instructions to the Model:**
**1. Prioritize Accuracy:** Extract information directly from the text. Do not fabricate or "hallucinate" details.
**2. Handle Missing Information:** If a topic is not mentioned in the testimonial, indicate "Information not found" in the corresponding JSON field.
**3. Output Format:** Provide a JSON object with the following keys: `drivers`, `imp_strategies`, `challenges`, `monetization`, `collaboration`, `mobile`, `ease_of_use`,  `functionality`, `integration`, `scalability`, `cost_effectiveness`, `customer_support`, `data_security`, `customization`, `training`.

## Prompt 2: Deep Insights

**Objective:** Extract key insights from the customer testimonial about [Company Name]'s Business Intelligence (BI) adoption and implementation process.

**Guiding Questions:**

**1. Feedback Integration:** How is customer feedback, through direct input or satisfaction surveys, integrated and analyzed within the BI platform to continually improve the training experience?
**2. Social Responsibility Support:** How does the BI platform assist in promoting social responsibility, including features or analyses related to community engagement, diversity and inclusion, and ethical business practices?
**3. Data Balance (Secondary Datasets):** Identify and categorize any mentions of external data, secondary data, or data sources beyond the company's primary dataset. How is the BI tool used to merge, blend, or relate internal and external datasets?
**4. Dynamic Stakeholder Interests:** How do users discuss responding to changes in business questions, evolving stakeholder requests, or the need for new visualizations?
**5. Societal Impact:** How does the platform demonstrate societal impact to stakeholders, including public funders?
**6. Strategic Planning:** How does the platform help in building evidence to support bidding for future contracts?
**7. Targeting Interventions/Campaigns:** How does the platform aid in building evidence for targeting interventions or campaigns?
**8. Business Expansion:** How does the platform enable the company to expand its offering from service to service + information/insight (vertical integration)?
**9. Stakeholder Engagement:** What evidence is there of becoming a more attractive partner for clients/collaborators by being able to share insights or be transparent?
**10. Performance Tracking:** How does the BI system capture and analyze data on staff/users performance?
**11. Behavioral Change:** How does the BI platform contribute to facilitating behavioral change among users/clients?
**12. Financial Insights:** How does the platform provide insights into revenue and other financial metrics?

**Instructions to the Model:**

**1. Prioritize Accuracy:** Extract information directly from the text. Do not fabricate or "hallucinate" details.
**2. Handle Missing Information:** If a topic is not mentioned in the testimonial, indicate "Information not found" in the corresponding JSON field.
**3. Output:** Summarize the extracted information into JSON format with keys:

- `feedback_integration`
- `social_responsibility`
- `data_balance`
- `dynamic_stakeholders`
- `societal_impact`
- `strategic_planning`
- `targeting_interventions`
- `business_expansion`
- `stakeholder_engagement`
- `performance_tracking`
- `behavioral_change`
- `financial_insights`