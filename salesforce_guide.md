# Salesforce User Guide

**Generated from:** Excel workflow documentation
**Date:** 2026-05-26

---

# Module: End 2 End


## 1.0


### Lead

**Screenshot:** Figure 1 (see screenshots Excel)

- New Lead Form
  - *System: Form  - Company Info, Source, Contact person, Currency*
- Lead page - To add -Country
- Task created - First connect
  - *System:  - Mark as contacted
 - Working contacted*
- Convert Lead Form- 
-Account - New / Existing
-Contact - New / Exiting
  - *System: Converted Status -
Converted / Closed- Not converted*
- Converted -
-Account creation in SF - Entity
-Contact created in SF

## 2.0


### Account

**Screenshot:** Figure 2 (see screenshots Excel)

- New Branch Form
  - *System: Account Name, Type (Direct / Distributor), Partner function (Only Ship to, Only Bill to, Sold to/ship to/ Bill to), currency
 -  Select Country
SAP Code -  Will be blank*
- Account heirarchy:-
Entity - ABC PVT LTD
Branch - ABC Gujarat
  - *System: Status - Prospect*
- Status - Data Enrichment
  - *System: Tax details, Bank details, Address, credit info etc*
- Status- Data verification & Sales Recommendation
- Submit for approval - Form
- Select Approver
  - *System: Status - Under Apporval*
- Approver
- Approve account form
- Approved
  - *System: Status - Activation Pending*
- Account SYNC
- Account Info pushed to SAP
  - *System: SAP Account created
- SAP Business Partner Code generated
- SAP Code received in SF*
- SAP
- Mail triggered to Owner - Creator & data guardian
  - *System: To add-
-Sales Area view - Org, Div, distribution, Sales district
-Financial View -  Tax condition*
- Account Status -  Active

## 3.0


### Opportunity

**Screenshot:** Figure 3 (see screenshots Excel)

- Accounts> Opportunities > New
  - *System:  - Existing product
 - New Product Development*
- New Opportunities  -  Existing Product
- Opportunities form
  - *System: Header Data-
a) Opportunity Detail
- Opportunity name, LOB,
- Purchase order type - ( Standard / Contract) 
- Order type - (domestic / export)
- currency
b) Sales & Distributions -
-Sales Org, Division, Distributor channel
c)  Requirements - Payment terms, Inco terms, Inco location, packaging, storage terms 
d) Additional Details - close date etc*
- Opportunity created
  - *System: Status  - Prospect
Probability - 20 %*
- Opportunity page -  Add Partner Info
- Sold to party, Bill to party, Ship to party
- Oppo > Relationships > Contact roles
  - *System: Contact person 
Contact person role*
- Add Products
- Search Product via name / code
-Add - Plant, shipping point, Quantity, line
  - *System: Add multiple products, or similar product multiple times as per requirement*
- Stage Change-
 - Select Stage >Quote
- Status > costing/  Pricing
  - *System: Stage :- Quote, Probability - 50 %
Quote Number created*

## 4.0


### Quote

**Screenshot:** Figure 4 (see screenshots Excel)

- Stage - Draft
  - *System: Data - Opportunity inputs*
- Quote Line Item:
- Referential Price
- Quoted price
  - *System: Make 1 line item as primary*
- Fetch Quote Price
  - *System: Quote sync response from SAP*
- SAP-
Scale wise pricing to be maintained
- Referential Price -  Base , FOB, Freight Cost
  - *System:  - Amendment in the quotation pricing
- Get Net price as per quantity*
- Stage Change-
Select - Approval Reqired
  - *System: Stage -  Approval Required*
- Submit for approval
- Submit for approval form
- Select Approver
  - *System: Stage - Under Review*
- Quote Approval-
- Approve Quote
  - *System: Stage - Cost pricing approval*
- Create PDF
  - *System: Quotation PDF review*
- Presented to customer - Outside
  - *System: Stage - Presentated to Customer - Mark as complete*
- Opportunity level
- Stage - Quote
- Status - Quote submitted
- Quote - Stage Change - 
Customer Accepted
  - *System: Mark as complete*
- Opportunity level
- Stage -Negotiation
  - *System: Probability- 80 %*
- PO Received
  - *System: Add-
- PO Date, PO Number, PO Order Type*
- Marking Opportunity closed
- Po Status - Received
- Stage - Closed Won
  - *System: Opportunity - Stage- Closed Won
Order Created*

## 5.0


### Sales Order

**Screenshot:** Figure 5 (see screenshots Excel)

- Status- Open
SO Ref ID- Blank
  - *System: Order >> Related >> Add PO

- Upload PO files*
- Sync Order-
- Opportunity number send to SAP
-SAP Response - Order data sent to SAP
  - *System: Status - Sales Order creation in progress*
- SAP 
Opportunity (cw) detail --> Staging table (ZGSD401)
  - *System: 2 Approaches
a) SAP process -  create SO & Delivery, Add PO
b) Create SO via staging table, PO auto add*
- SAP -
Create SO via staging table, PO auto add
-Opp won date 
-opp pending for SO creation
- select opp & domestic & export orde
  - *System: Marked as New order in SF*
- Create subsequent orders - SAP process
  - *System: Marked as repeat order in SF*
- DMS document-- QCC documents type added
- SO Creation in SAP
- Organizational Data
- Pricing data
-SO number generated
  - *System: SO number transferred to SF*
- SAP SO also reflect 2 key no -
- SF opportunity number 
- Ref Sales document
- SO number received
  - *System: SO Status - Completely process*
- Delivery Created in SAP
- Dispatch created in SF
  - *System: Delivery No - As per SAP delivery no*
- Invoice created in SAP
- Invoice detail in SF
- Invoice Status - Generated
  - *System:  - Invoice no, date, Invoice Amount,
*
- Payment received in SAP
- Invoice detail in SF
-  Collection status - Collected
  - *System:  - Date, amount*

## 6.0


### Integrations

**Screenshot:** Figure 6 (see screenshots Excel)


### Material Master Syncing

**Screenshot:** Figure 7 (see screenshots Excel)

- ZGBSD407 - Material master data pushed to SFDC
- a )Retrigger to SFDC
- To manually re-push material data from SAP to Salesforce
- Users can provide Material Number(s) or a Date Range
  - *System:  -  Restricted to IT Team via authorization objects*
- b) Log report
 - Useful for auditing, tracking data flows, and troubleshooting.
-ilter logs based on criteria such as date, material 
number, or status.
- IT & User
  - *System:   -  IT & User*
- c) Incremental Data Push to SFDC
-Captures and pushes new or updated material records on an hourly basis
- Used primarily in automated or scheduled background jobs
  - *System:  - Restricted to IT team only*

### Sales Order Syncing

**Screenshot:** Figure 8 (see screenshots Excel)

- ZGBSD410 - to monitor sales order-related data 
being transmitted from SAP to SFDC
- a) Log report
- visibility into the end-to-end sales order flow, including associated delivery  and invoice creation details.
  - *System:   -  IT & User*
- b)Retrigger to SFDC
 - used for repushing the data
  - *System:  - Restricted to IT team only*

###  BP update Log and Repush

**Screenshot:** Figure 9 (see screenshots Excel)

- ZGBSD411 – To maintain a log of updates made to 
SFDC Business Partner (BP) customer records
- a) Log Report - Created status
  - *System:   -  IT & User*
- b) Retrigger - Retriggering in customer if needed ,
  - *System:  - Restricted to IT team only*

### Customer List Sync

**Screenshot:** Figure 10 (see screenshots Excel)

- ZSD14N -  better visibility of customer data integration between Salesforce and SAP
- a) Draft Customer List
-  list of customers that have been pushed from Salesforce to SAP but are still in the draft stage ( identify records that are pending completion)
-  draft customers have only the general data maintained in SAP
-  also get the Email ID and the ME User ID : for mail triggering

### Collection Sync

**Screenshot:** Figure 11 (see screenshots Excel)

- ZGBSD409 - Collection Amount sync
- a) Retrigger to SFDC - Customer  / Billing document based
  - *System:  - Restricted to IT team only*
- b) Incremental data push to SFDC-
Background job based on Date
  - *System:  - Restricted to IT team only*

### Customer Master Update

**Screenshot:** Figure 12 (see screenshots Excel)

- Key fields in the General Data may include information such as:
 - Customer name
 -  Address details (street, city, postal code, country, etc.)
 - Contact information (phone number, email address, etc.)
 - Credit Limit of the customer
  - *System: When the business updates any key fields in the Customer Master General Data within SAP,
these changes are automatically captured and transmitted to Salesforce (SFDC) in real
time.*
- If a Central Block is applied, the status in Salesforce is reflected as "Blocked."

### Customer Master: Denied Party Check from Thomas Reuters

**Screenshot:** Figure 13 (see screenshots Excel)

- In the Customer Master (KNA1), If both fields (SPERR and SPERZ) are populated with a block, this indicates that the customer is restricted from both central and sales-related activities.
  - *System: This status should be communicated as "Denied Party" in downstream systems, such as Salesforce (SFDC)
- "DPS_BLOCK": "" in the above Payload signifies this check.*

###  Customer master Attachments Document Upload

**Screenshot:** Figure 14 (see screenshots Excel)

- Customer's documents such as tax documents, including
PAN and GST certificates. 
- These documents are uploaded and stored in the Document
Management System (DMS)
- The documents are uploaded under the QCC document type

### Customer master Data extractor

**Screenshot:** Figure 15 (see screenshots Excel)

- ZGBSD402 Customer master Data extractor :- 
- ZGBSD402 is a custom transaction developed for the initial extraction of Customer Master Data from SAP
 - This extraction process was executed as a one-time batch job, primarily during the initial data migration phas

### Email trigger for Business Partner creation

**Screenshot:** Figure 16 (see screenshots Excel)

- ZTVARVC configuration table-
 - Once a Business Partner is created, a notification should be sent to the ME (Market Executive), Account Owner, or Data Guardian regarding the new customer created in
Salesforce (SFDC).

### Material Master extract for initial Upload

**Screenshot:** Figure 17 (see screenshots Excel)

- ZGBSD403 Material Master extract for initial Upload.
This transaction code was created for fetching the initial Material master upload in the API
format. This was executed in the background

### Quotation Creation and Pricing ( Price Simulation ) 

**Screenshot:** Figure 18 (see screenshots Excel)

- The price, already available in
SAP, will be calculated and sent to Salesforce for display as a reference
 -  Quote data (Material, Quantity),is provided and sent out to SAP. SAP share the Selling Price and the Cost Price 
• Cost Price – Based on the Pricing control, either the standard Price or the moving average
price maintained in the material master will be shared by SAP to Sales force.
• Selling Price – Based on the data received from the Sales force, SAP will run the Pricing API
which basically simulates the price based on the condition records maintained and the
access sequence maintained for various pricing conditions.
  - *System: Ref--1.12*

### Invoice Data extractor

**Screenshot:** Figure 19 (see screenshots Excel)

- ZGBSD406 – Invoice Data Extractor is a custom program designed to extract Sales Order (SO) lifecycle data from SAP  
- The program was primarily used for the initial data load during the implementation of the Customer 360 view in SFDC
 - The extraction was performed using a batch job
  - *System: Ref 1.14*

### Old reference field correction Program

**Screenshot:** Figure 20 (see screenshots Excel)

- ZGBSD408 has been developed to correct and update existing Sales Orders by populating the newly introduced field “Old Reference Sales Order” in Additional Data Tab B at the line-item level.
  - *System: Ref 1.15*

### Old reference Sales Order Enhancement

**Screenshot:** Figure 21 (see screenshots Excel)

- A new field has been introduced under the Additional Data Tab B at the line item level in the Sales Order. This field is designed to store the reference of a previously created
Sales Order.
  - *System: Ref 1.18*

### SO life cycle – Sales Order / Delivery / Invoice status

**Screenshot:** Figure 22 (see screenshots Excel)

- The Sales Order Lifecycle API has been developed to send real-time data from SAP to
Salesforce (SFDC). As soon as a Sales Order is created in SAP, a batch job is triggered to
transmit the relevant data to SFDC.
This integration covers the entire Sales Order lifecycle, and data is sent at each key stage:
1. Sales Order Creation
2. Delivery Creation
3. Post Goods Issue (PGI)
4. Invoice Creation
  - *System: Ref 1.19*

### On demand Invoice Print

**Screenshot:** Figure 23 (see screenshots Excel)

- This API has been developed to facilitate the transfer of invoices from SAP to Salesforce (SFDC). The process involves converting the invoice document from PDF format to Base64 encoding, after which it is transmitted via the API to SFDC.
  - *System: Ref 1.21*

---



---

