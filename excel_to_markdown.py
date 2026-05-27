import pandas as pd
import os

def excel_to_markdown(excel_file_path, output_file='salesforce_guide.md'):
    """
    Converts multi-sheet Excel to RAG-ready Markdown
    
    Args:
        excel_file_path: Path to your Excel file with steps
        output_file: Output markdown file name
    """
    
    print(f"📖 Reading Excel file: {excel_file_path}")
    
    # Read all sheets from Excel
    try:
        sheets_dict = pd.read_excel(excel_file_path, sheet_name=None)
        print(f"✅ Found {len(sheets_dict)} sheets")
    except Exception as e:
        print(f"❌ Error reading Excel: {e}")
        return
    
    # Open output markdown file
    with open(output_file, 'w', encoding='utf-8') as md_file:
        
        # Write document header
        md_file.write("# Salesforce User Guide\n\n")
        md_file.write("**Generated from:** Excel workflow documentation\n")
        md_file.write(f"**Date:** {pd.Timestamp.now().strftime('%Y-%m-%d')}\n\n")
        md_file.write("---\n\n")
        
        # Process each sheet
        for sheet_name, df in sheets_dict.items():
            print(f"\n📄 Processing sheet: {sheet_name}")
            
            # Sheet header
            md_file.write(f"# Module: {sheet_name}\n\n")
            
            # Get column names
            columns = df.columns.tolist()
            print(f"   Columns found: {columns}")
            
            # Assume structure: L1, L2, L3, System (based on your screenshot)
            # Adjust column names based on YOUR actual Excel
            l1_col = columns[0] if len(columns) > 0 else None
            l2_col = columns[1] if len(columns) > 1 else None
            l3_col = columns[2] if len(columns) > 2 else None
            system_col = columns[3] if len(columns) > 3 else None
            
            current_l1 = None
            current_l2 = None
            figure_counter = 1
            
            # Process each row
            for index, row in df.iterrows():
                
                # Get values (handle NaN)
                l1_val = str(row[l1_col]) if pd.notna(row[l1_col]) else None
                l2_val = str(row[l2_col]) if pd.notna(row[l2_col]) else None
                l3_val = str(row[l3_col]) if pd.notna(row[l3_col]) else None
                system_val = str(row[system_col]) if pd.notna(row[system_col]) else None
                
                # L1 - Main section (e.g., "Lead", "Account")
                if l1_val and l1_val != current_l1 and l1_val != 'nan':
                    current_l1 = l1_val
                    md_file.write(f"\n## {l1_val}\n\n")
                
                # L2 - Sub-section (e.g., "New Lead Form", "Convert Lead Form")
                if l2_val and l2_val != current_l2 and l2_val != 'nan':
                    current_l2 = l2_val
                    md_file.write(f"\n### {l2_val}\n\n")
                    
                    # Add screenshot reference
                    md_file.write(f"**Screenshot:** Figure {figure_counter} (see screenshots Excel)\n\n")
                    figure_counter += 1
                
                # L3 - Details
                if l3_val and l3_val != 'nan':
                    # Clean up the text
                    l3_val = l3_val.strip()
                    
                    # If it looks like a list item, add bullet
                    if l3_val.startswith('-'):
                        md_file.write(f"{l3_val}\n")
                    else:
                        md_file.write(f"- {l3_val}\n")
                
                # System column (if exists)
                if system_val and system_val != 'nan' and system_val.strip():
                    md_file.write(f"  - *System: {system_val}*\n")
            
            # End of sheet
            md_file.write("\n---\n\n")
        
        # Add appendix for screenshot descriptions
        md_file.write("\n# Appendix: Screenshot Descriptions\n\n")
        md_file.write("*TODO: Add descriptions for each screenshot from your screenshots Excel file*\n\n")
        
        for i in range(1, figure_counter):
            md_file.write(f"## Figure {i}\n")
            md_file.write("**Screen:** [Name from screenshots file]\n\n")
            md_file.write("**Description:** [Describe what's visible in screenshot]\n\n")
            md_file.write("**Key Fields:**\n")
            md_file.write("- Field 1: [description]\n")
            md_file.write("- Field 2: [description]\n\n")
            md_file.write("**How to reach this screen:** [Navigation path]\n\n")
            md_file.write("---\n\n")
    
    print(f"\n✅ Conversion complete!")
    print(f"📄 Output file: {output_file}")
    print(f"📊 Total figures referenced: {figure_counter - 1}")


# ============================================
# USAGE
# ============================================

if __name__ == "__main__":
    
    # STEP 1: Update this path to YOUR Excel file
    excel_file = "salesforce_steps.xlsx"  # Change to your actual filename
    
    # STEP 2: Run the conversion
    excel_to_markdown(excel_file, output_file="salesforce_guide.md")
    
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    print("1. Open salesforce_guide.md")
    print("2. Review the auto-generated content")
    print("3. Fill in screenshot descriptions in Appendix")
    print("4. Use this file with your RAG system (replace knowledge.txt)")
    print("="*60)