# Financial Literacy Framework

**An open-source framework of plain-language financial education modules for community financial institutions**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CFPB Aligned](https://img.shields.io/badge/CFPB-Aligned-blue)](https://www.consumerfinance.gov/consumer-tools/educator-tools/)

---

## The Problem This Framework Solves

Financial products are not complicated because they have to be. They are complicated because nobody has required them to be explained simply.

A credit card agreement runs to dozens of pages. A mortgage disclosure is dense with regulatory language that most people cannot parse. An investment account opening form includes risk disclosures written for lawyers, not for the first-time investor trying to save for retirement. And yet the people who most need to understand these documents — people opening their first bank account, people applying for their first loan, people navigating financial products for the first time — are exactly the people least equipped to read them.

The FINRA 2024 National Financial Capability Study found that only 48% of American adults could answer four out of five basic financial literacy questions correctly. The gap is not randomly distributed. It is concentrated among the populations that community financial institutions exist to serve.

This framework gives those institutions a starting point for closing that gap — not through one-size-fits-all campaigns but through modular, customisable, plain-language education that any institution can adopt, adapt, and deploy.

---

## What This Framework Contains

### Education Modules

Five topic modules, each independently usable:

| Module | What It Covers |
|---|---|
| [Banking Basics](modules/banking-basics/) | Accounts, fees, deposits, FDIC insurance, how banking works |
| [Credit and Loans](modules/credit-and-loans/) | Credit scores, interest rates, types of loans, rights when borrowing |
| [Investing Basics](modules/investing-basics/) | How investing works, risk vs return, retirement accounts, common products |
| [AI in Finance](modules/ai-in-finance/) | How AI makes decisions about your money, your rights, what to ask |
| [Understanding Your Rights](modules/understanding-your-rights/) | ECOA, FCRA, Reg E, TILA, CFPB complaint process |

Each module contains:
- A plain-language concept guide for educators to use in workshops, onboarding, or digital content
- A glossary defining every term in language accessible to someone with no financial background
- Customisation notes so each institution can adapt the content to their specific member population

### Python Tools

Two analytical tools that support financial literacy programme design:

**Tool 1 — Plain Language Converter** (`tools/plain-language-converter.py`)
Scans any financial document or text for complex terms and produces a plain-language explanation alongside each one. Useful for auditing existing member communications, loan documents, account disclosures, or onboarding materials.

**Tool 2 — Financial Literacy Gap Analyzer** (`tools/literacy-gap-analyzer.py`)
Uses publicly available FINRA National Financial Capability Study data to map financial literacy gaps by state, income level, and demographic group — helping institutions identify which modules are most needed for their specific member population.

### Adoption Guides

- [Institution Adoption Guide](docs/institution-adoption-guide.md) — step-by-step for implementing modules at a credit union, community bank, or CDFI
- [Customisation Guide](docs/customization-guide.md) — how to adapt content for specific populations including first-generation bankers, immigrant communities, and young adults

---

## Who This Is Built For

- **Credit unions and CDFIs** serving first-generation banking customers, underserved communities, and thin-file members
- **Community banks** building financial wellness programmes for their service areas
- **Fintech onboarding teams** wanting to explain their products clearly rather than bury members in disclosure language
- **Financial educators and counsellors** who want modular, adaptable content they can deploy across multiple topics

---

## How It Connects to the KYC API Framework

The [KYC API Framework for Financial Inclusion](https://github.com/sujiyer/kyc-api-framework) solves the technical onboarding problem — how to build systems that let more people through the door. This framework solves the comprehension problem — whether people understand what they are walking into.

An institution that implements both has a complete picture: an onboarding system designed for inclusion, and education materials that help members understand what they have just signed up for.

---

## How It Connects to the AI Governance Framework

The AI in Finance module directly prepares members to engage with AI-assisted financial decisions — understanding what it means when an AI helped decide their loan application, what they can ask for, and what their rights are. The [Fintech AI Governance Framework](https://github.com/sujiyer/fintech-ai-governance-framework) governs how those AI systems are built. This framework ensures members understand how those decisions affect them.

---

## National Importance

The FINRA 2024 National Financial Capability Study found that only 48% of American adults can answer four out of five basic financial literacy questions. Financial literacy gaps are concentrated among lower-income households, younger adults, and communities with historically limited access to financial services — the same populations CDFI credit unions and community banks exist to serve.

Institutions that adopt standardised, high-quality financial education reduce member confusion, reduce support costs, improve product uptake among underserved members, and build the trust that keeps members engaged with the formal financial system rather than returning to costly nonbank alternatives.

---

## Contributing

Contributions from financial educators, compliance professionals, community institution practitioners, and financial technology professionals are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

Contributions that address specific populations — immigrant communities, agricultural workers, elderly members, first-generation bankers — are especially valuable.

---

## License

MIT License. See [LICENSE](LICENSE).

---

## Author

**Sujatha Gopalakrishnan Iyer**
Financial Technology Product Professional | AI Governance | Financial Inclusion

*Published independently and outside of employment. This framework represents generalised educational knowledge for broad institutional use.*
