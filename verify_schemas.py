#!/usr/bin/env python3
"""Quick schema verification"""

import json
import re
from pathlib import Path

def verify_schemas(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all JSON-LD scripts
    matches = re.findall(r'<script type=["\']application/ld\+json["\']>(.*?)</script>', content, re.DOTALL | re.IGNORECASE)
    
    print(f"\n{file_path.name}:")
    print(f"Found {len(matches)} JSON-LD schema blocks")
    
    schemas_found = {
        'BlogPosting': False,
        'FAQPage': False,
        'HowTo': False,
        'Organization': False
    }
    
    for i, match in enumerate(matches, 1):
        try:
            schema = json.loads(match.strip())
            schema_type = schema.get('@type', '')
            print(f"  Schema {i}: {schema_type} - Valid JSON")
            
            if schema_type == 'BlogPosting':
                schemas_found['BlogPosting'] = True
            elif schema_type == 'FAQPage':
                schemas_found['FAQPage'] = True
            elif schema_type == 'HowTo':
                schemas_found['HowTo'] = True
            
            # Check for nested Organization
            if 'author' in schema and schema['author'].get('@type') == 'Organization':
                schemas_found['Organization'] = True
            if 'publisher' in schema and schema['publisher'].get('@type') == 'Organization':
                schemas_found['Organization'] = True
                
        except json.JSONDecodeError as e:
            print(f"  Schema {i}: INVALID JSON - {e}")
    
    print("\nSchemas Found:")
    for schema_type, found in schemas_found.items():
        status = "[OK]" if found else "[MISSING]"
        print(f"  {status} {schema_type}")
    
    return schemas_found

# Verify both new posts
verify_schemas(Path("blog/posts/invoice-to-pdf-complete-guide.html"))
verify_schemas(Path("blog/posts/image-to-csv-complete-guide.html"))

