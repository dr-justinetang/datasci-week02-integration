#!/bin/bash
# setup_project.sh - project scaffold script

echo "Setting up project structure..."

# Create dirs
mkdir -p src data output

# .gitignore
cat > .gitignore << 'EOF'
__pycache__/
output/
*.pyc
EOF

# requirements.txt
echo "pandas" > requirements.txt

# Sample students.csv
cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,88,Math
Bob,21,92,Science
Charlie,22,76,Math
Diana,20,85,History
Evan,23,90,Science
Fiona,21,67,Math
George,22,73,History
Hannah,20,95,Math
EOF

# Python templates
cat > src/data_analysis.py << 'EOF'
# Basic student data analysis script
# TODO: Implement functions and main()
EOF

cat > src/data_analysis_functions.py << 'EOF'
# Advanced modular data analysis
# TODO: Implement reusable functions
EOF

echo "Project scaffold created successfully."


