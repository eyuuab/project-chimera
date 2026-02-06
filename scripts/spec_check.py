# scripts/spec_check.py
import os
import sys
import re

def parse_spec_models(spec_path="specs/technical.md"):
    """Extracts expected class names from the Technical Spec."""
    if not os.path.exists(spec_path):
        print(f"❌ Critical: Spec file not found at {spec_path}")
        return []
    
    with open(spec_path, "r") as f:
        content = f.read()
    
    # Heuristic: Looks for headers like "### 1.1 The Agent Task (`Task`)"
    # Regex captures the text inside the (`...`)
    models = re.findall(r"\(`([a-zA-Z0-9_]+)`\)", content)
    return set(models)

def scan_codebase_for_classes(src_path="src"):
    """Scans python files in src/ to find class definitions."""
    found_classes = set()
    for root, _, files in os.walk(src_path):
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    content = f.read()
                    # Regex to find 'class Task(BaseModel):' or just 'class Task:'
                    classes = re.findall(r"class\s+([a-zA-Z0-9_]+)", content)
                    found_classes.update(classes)
    return found_classes

def main():
    print("🔍 Running Spec Alignment Check...")
    
    expected_models = parse_spec_models()
    if not expected_models:
        print("⚠️  Warning: No models found in spec (Check regex formatting).")
        sys.exit(0) # Not a failure, just a warning
        
    found_classes = scan_codebase_for_classes()
    
    missing = expected_models - found_classes
    
    print(f"📄 Expected Models from Spec: {expected_models}")
    print(f"💻 Found Classes in Code: {found_classes}")
    
    if missing:
        print(f"\n❌ Spec Alignment FAILURE: The following models are defined in specs but missing in code:")
        for m in missing:
            print(f"   - {m}")
        print("\nAction: Implement these Pydantic models in src/core/models.py")
        sys.exit(1)
    
    print("\n✅ Spec Alignment SUCCESS: All specified models exist in code.")
    sys.exit(0)

if __name__ == "__main__":
    main()