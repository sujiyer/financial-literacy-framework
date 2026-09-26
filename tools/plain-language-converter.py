"""
Plain Language Financial Terms Converter
==========================================
Scans any financial document or text for complex financial terms
and produces plain-language explanations alongside each one.

Use this tool to audit your institution's member communications,
loan documents, account disclosures, and onboarding materials
for language that may be unclear to first-time banking customers.

Part of the Financial Literacy Framework
github.com/sujiyer/financial-literacy-framework

Author: Sujatha Gopalakrishnan Iyer
"""

import os
import re
from datetime import datetime

# ============================================================
# WHAT YOU ARE LEARNING:
# - Dictionaries: storing key-value pairs (term: explanation)
# - String methods: searching and manipulating text
# - File reading: opening and reading a text file
# - Loops: going through items one at a time
# ============================================================

# Step 1: The Plain Language Dictionary
# This DICTIONARY maps financial jargon to plain language
# Key = the complex term, Value = the plain explanation
# Any institution can expand this dictionary for their context

FINANCIAL_TERMS = {

    # --- BANKING BASICS ---
    "APY": (
        "Annual Percentage Yield",
        "The actual interest rate your savings earns in a year, "
        "including the effect of interest being added to your balance "
        "over time. Higher APY means more money earned on savings."
    ),
    "APR": (
        "Annual Percentage Rate",
        "The yearly cost of borrowing money, expressed as a percentage. "
        "It includes the interest rate plus most fees. Lower APR means "
        "less money paid on a loan."
    ),
    "FDIC": (
        "Federal Deposit Insurance Corporation",
        "A US government agency that protects your money in the bank. "
        "If a bank fails, the FDIC insures your deposits up to $250,000 "
        "per account category. Your money is safe up to that limit."
    ),
    "NCUA": (
        "National Credit Union Administration",
        "The US government agency that insures deposits at credit unions, "
        "similar to how the FDIC protects bank deposits. Coverage is also "
        "up to $250,000 per account category."
    ),
    "overdraft": (
        "Overdraft",
        "When you spend more money than you have in your account. The bank "
        "may cover the payment but charge you a fee, often $25 to $35. "
        "Some accounts have overdraft protection that transfers money from "
        "another account instead."
    ),
    "minimum balance": (
        "Minimum Balance",
        "The least amount of money you must keep in your account to avoid "
        "a monthly fee or to earn interest. If your balance falls below "
        "this amount, you may be charged a fee."
    ),
    "routing number": (
        "Routing Number",
        "A 9-digit number that identifies your bank. You need this number, "
        "along with your account number, to set up direct deposit or to "
        "transfer money between banks."
    ),
    "ACH": (
        "Automated Clearing House",
        "The electronic network that moves money between bank accounts in "
        "the United States. Direct deposit, online bill payments, and "
        "peer-to-peer transfers like Venmo all use ACH."
    ),

    # --- CREDIT AND LOANS ---
    "credit score": (
        "Credit Score",
        "A number between 300 and 850 that tells lenders how likely you "
        "are to repay borrowed money on time. Higher is better. A score "
        "above 700 is generally considered good. It is calculated from "
        "your payment history, debt amounts, and length of credit history."
    ),
    "credit bureau": (
        "Credit Bureau",
        "A company that collects information about how people borrow and "
        "repay money. The three main bureaus in the US are Equifax, "
        "Experian, and TransUnion. Lenders check your credit report from "
        "these bureaus before deciding whether to give you a loan."
    ),
    "hard inquiry": (
        "Hard Inquiry",
        "When a lender checks your credit report because you applied for "
        "credit. Hard inquiries can lower your credit score by a few "
        "points and stay on your report for two years. Multiple "
        "applications in a short period can have more impact."
    ),
    "soft inquiry": (
        "Soft Inquiry",
        "When someone checks your credit report in a way that does not "
        "affect your score. Checking your own credit, pre-approval "
        "screenings, and employer background checks are soft inquiries."
    ),
    "debt-to-income ratio": (
        "Debt-to-Income Ratio (DTI)",
        "The percentage of your monthly income that goes toward paying "
        "debts. Lenders use this to decide if you can afford a new loan. "
        "A DTI below 36% is generally considered healthy. To calculate "
        "it, divide your monthly debt payments by your monthly income."
    ),
    "collateral": (
        "Collateral",
        "Property or assets you pledge as security for a loan. If you "
        "cannot repay the loan, the lender can take the collateral. "
        "A mortgage uses your home as collateral. A car loan uses "
        "your car."
    ),
    "amortization": (
        "Amortization",
        "The process of paying off a loan through regular monthly "
        "payments over time. Early payments go mostly toward interest; "
        "later payments go mostly toward the principal (the original "
        "amount borrowed)."
    ),
    "principal": (
        "Principal",
        "The original amount of money you borrowed, not including "
        "interest. As you make payments, the principal goes down. "
        "Interest is calculated on the remaining principal."
    ),
    "FICO": (
        "FICO Score",
        "A specific type of credit score created by the Fair Isaac "
        "Corporation. It is the most widely used credit scoring model "
        "in the United States. Lenders use it to evaluate credit "
        "applications."
    ),
    "subprime": (
        "Subprime",
        "A category for borrowers with lower credit scores, typically "
        "below 620. Subprime loans often come with higher interest rates "
        "because lenders see them as higher risk. If you have a subprime "
        "score, working to improve it can save significant money on "
        "future loans."
    ),

    # --- INVESTING ---
    "401(k)": (
        "401(k)",
        "A retirement savings account offered through your employer. "
        "You contribute pre-tax money, which reduces your taxable income "
        "now. The money grows tax-deferred until you withdraw it in "
        "retirement. Many employers match a portion of your contributions "
        "— that is free money you should not leave on the table."
    ),
    "IRA": (
        "Individual Retirement Account",
        "A personal retirement savings account you open yourself, "
        "independent of your employer. A Traditional IRA lets you "
        "contribute pre-tax money. A Roth IRA uses after-tax money but "
        "grows tax-free. Both have annual contribution limits."
    ),
    "diversification": (
        "Diversification",
        "Spreading your investments across different types of assets "
        "so that if one goes down, others may hold steady or go up. "
        "The idea is not to put all your eggs in one basket. A "
        "diversified portfolio typically includes stocks, bonds, "
        "and other assets."
    ),
    "volatility": (
        "Volatility",
        "How much an investment's price goes up and down over time. "
        "High volatility means the price can change a lot in a short "
        "period — both up and down. Stocks are generally more volatile "
        "than bonds. Higher volatility usually means higher potential "
        "return, but also higher potential loss."
    ),
    "ETF": (
        "Exchange-Traded Fund",
        "A type of investment that holds a collection of stocks, bonds, "
        "or other assets and trades on a stock exchange like a single "
        "stock. ETFs are often lower cost than mutual funds and let you "
        "invest in many companies at once through a single purchase."
    ),
    "mutual fund": (
        "Mutual Fund",
        "A pool of money from many investors that is managed by a "
        "professional and invested in a collection of stocks, bonds, "
        "or other securities. You buy shares of the fund. The value "
        "of your shares goes up or down based on how the underlying "
        "investments perform."
    ),

    # --- AI IN FINANCE ---
    "algorithmic decision": (
        "Algorithmic Decision",
        "A decision made automatically by a computer program using "
        "rules and data, rather than a human making the judgment. "
        "Banks and lenders increasingly use algorithms to decide "
        "loan applications, set interest rates, and flag fraud. "
        "You have the right to know when a significant decision "
        "was made by an algorithm and to request an explanation."
    ),
    "adverse action": (
        "Adverse Action",
        "When a lender denies your application, offers you less "
        "favorable terms, or takes a negative action on your account. "
        "Under federal law, lenders must tell you specifically why "
        "an adverse action was taken — including when AI or algorithms "
        "were used in the decision."
    ),
    "black box": (
        "Black Box",
        "An AI system whose decision-making process cannot be easily "
        "explained — you can see the inputs and outputs but not how "
        "it arrived at the decision. Black-box AI in financial decisions "
        "is a growing regulatory concern because it can hide bias and "
        "makes it hard to give consumers specific explanations."
    ),

    # --- YOUR RIGHTS ---
    "ECOA": (
        "Equal Credit Opportunity Act",
        "A federal law that prohibits lenders from discriminating "
        "against credit applicants based on race, color, religion, "
        "national origin, sex, marital status, age, or because you "
        "receive public assistance. If you are denied credit, you have "
        "the right to know why."
    ),
    "FCRA": (
        "Fair Credit Reporting Act",
        "A federal law that gives you the right to see your credit "
        "reports, dispute inaccurate information, and limit who can "
        "access your credit information. You are entitled to one free "
        "credit report from each bureau annually at "
        "annualcreditreport.com."
    ),
    "TILA": (
        "Truth in Lending Act",
        "A federal law that requires lenders to clearly disclose the "
        "terms and costs of a loan before you sign. This includes the "
        "APR, total amount you will pay, and all fees. This is why "
        "you receive those disclosure forms when you apply for credit."
    ),
    "Reg E": (
        "Regulation E",
        "The federal regulation that protects consumers when using "
        "electronic banking services — debit cards, ATMs, and electronic "
        "transfers. It limits your liability for unauthorized transactions "
        "if you report them promptly. Report within 2 days: max $50 "
        "liability. Report within 60 days: max $500."
    ),
    "CFPB": (
        "Consumer Financial Protection Bureau",
        "The US government agency responsible for protecting consumers "
        "in the financial marketplace. If you have a problem with a bank, "
        "lender, credit card company, or other financial institution, "
        "you can file a complaint at consumerfinance.gov/complaint. "
        "The CFPB contacts the company on your behalf."
    ),
}


def scan_text_for_terms(text):
    """
    FUNCTION: Scans a block of text for known financial terms.
    Returns a list of terms found and their plain-language explanations.
    """
    found_terms = []

    for term, (full_name, explanation) in FINANCIAL_TERMS.items():
        # Search case-insensitively using REGEX
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        if pattern.search(text):
            found_terms.append({
                "term": term,
                "full_name": full_name,
                "explanation": explanation
            })

    return found_terms


def convert_document(input_text, title="Document"):
    """
    Takes a financial document's text and produces a plain-language
    companion glossary for all terms found.
    """
    print(f"\nScanning: {title}")
    print("-" * 50)

    found = scan_text_for_terms(input_text)

    if not found:
        print("No complex financial terms detected.")
        return ""

    print(f"Found {len(found)} financial term(s) that may need plain-language explanation.\n")

    output = f"PLAIN LANGUAGE GUIDE FOR: {title}\n"
    output += f"Generated: {datetime.now().strftime('%B %d, %Y')}\n"
    output += "=" * 60 + "\n\n"
    output += "The following terms were found in this document.\n"
    output += "Plain-language explanations are provided below.\n\n"
    output += "=" * 60 + "\n\n"

    for item in found:
        output += f"TERM: {item['term']}"
        if item['full_name'] != item['term']:
            output += f" ({item['full_name']})"
        output += "\n"
        output += f"WHAT IT MEANS: {item['explanation']}\n"
        output += "\n" + "-" * 40 + "\n\n"

    return output


def run_demo():
    """
    Demonstrates the converter on sample financial documents.
    """
    os.makedirs("output", exist_ok=True)

    # DEMO 1: Credit card agreement excerpt
    credit_card_text = """
    Your APR for purchases is 22.99%. This is a variable APR.
    We calculate the interest charge on your account by applying
    the daily periodic rate to the daily balance, including
    current transactions. Your credit score will be checked via
    a hard inquiry when you apply. We report to all three major
    credit bureaus. Minimum balance requirements do not apply to
    this account. You may be subject to an overdraft fee of $35
    if you exceed your credit limit.
    """

    # DEMO 2: Loan disclosure excerpt
    loan_text = """
    Your debt-to-income ratio must be below 43% to qualify.
    This loan is secured by collateral in the form of your
    vehicle. The principal amount is $15,000. Your FICO score
    of 680 qualifies you for our standard rate. Please review
    your TILA disclosure carefully. Under ECOA, you have the
    right to know if your application is denied and the
    specific reasons for the adverse action.
    """

    # DEMO 3: Investment account opening
    investment_text = """
    This account allows contributions to a traditional IRA
    or Roth IRA up to the annual limit. Investments in ETF
    products carry market risk including volatility. We
    recommend diversification across asset classes. Your
    401(k) rollover can be processed within 3 to 5 business days.
    All investment decisions involving algorithmic decision
    systems are subject to our AI governance policy.
    """

    # Run the converter on each demo document
    demos = [
        ("Credit Card Agreement Excerpt", credit_card_text),
        ("Loan Disclosure Excerpt", loan_text),
        ("Investment Account Opening Excerpt", investment_text),
    ]

    all_output = ""
    for title, text in demos:
        result = convert_document(text, title)
        all_output += result + "\n\n"

    # Save combined output
    output_path = os.path.join("output", "plain_language_guide.txt")
    with open(output_path, "w") as f:
        f.write(all_output)

    print(f"\nFull plain-language guide saved to: {output_path}")
    print("\nPreview of output:")
    print(all_output[:600] + "...")

    return all_output


def convert_your_document(file_path):
    """
    HOW TO USE THIS WITH YOUR OWN DOCUMENTS:

    1. Save your financial document as a .txt file
    2. Run this function with the path to your file
    3. The converter will produce a plain-language glossary

    Example:
        convert_your_document("my_loan_agreement.txt")
    """
    try:
        with open(file_path, "r") as f:
            text = f.read()
        result = convert_document(text, os.path.basename(file_path))
        output_path = os.path.join("output", "plain_language_" + os.path.basename(file_path))
        with open(output_path, "w") as f:
            f.write(result)
        print(f"Output saved to: {output_path}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        print("Make sure the file path is correct.")


# ============================================================
# RUN THE DEMO
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("PLAIN LANGUAGE FINANCIAL TERMS CONVERTER")
    print("Financial Literacy Framework")
    print("github.com/sujiyer/financial-literacy-framework")
    print("=" * 60)

    print("\nRunning demo on three sample financial documents...")
    print("(To convert your own document, use convert_your_document())")

    run_demo()

    print("\n" + "=" * 60)
    print("CONVERSION COMPLETE")
    print("=" * 60)
    print("\nThis tool contains plain-language definitions for")
    print(f"{len(FINANCIAL_TERMS)} financial terms across 5 categories:")
    print("  Banking Basics, Credit and Loans, Investing,")
    print("  AI in Finance, and Consumer Rights")
    print("\nTo add terms for your institution, edit the")
    print("FINANCIAL_TERMS dictionary at the top of this file.")
