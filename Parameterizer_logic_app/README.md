# Azure Logic App ARM Template Parameterizer

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Azure](https://img.shields.io/badge/Azure-Logic%20Apps-blue)
![Automation](https://img.shields.io/badge/Automation-ARM%20Templates-green)
![Status](https://img.shields.io/badge/status-active-success)

A utility for converting exported **Azure Logic App JSON definitions** into **environment-agnostic, parameterized ARM templates** suitable for deployment across multiple Azure environments.

This repository provides a CLI wrapper that executes a transformation notebook to automatically parameterize Logic App templates.

---

# Overview

Exported Logic Apps from Azure typically contain **hard-coded environment values**, such as:

- Subscription IDs  
- Resource Group names  
- Connection IDs  
- Managed API references  

This makes them difficult to redeploy across environments.

This tool converts exported Logic App definitions into **reusable ARM templates** by:

- Detecting environment-specific values
- Converting them into parameters
- Rebuilding the Logic App template structure
- Producing a deployable ARM template

---

# Repository Structure

```
.
├── converter.ipynb
└── parameterizer.py
```

| File | Description |
|-----|-------------|
| `converter.ipynb` | Notebook containing the Logic App parameterization logic |
| `parameterizer.py` | CLI wrapper used to execute the notebook against JSON files |

---

# Requirements

Python **3.8+**

Install required dependencies:

```
pip install nbconvert nbformat
```

---

# Usage

Run the CLI tool and provide a folder containing exported Logic App JSON files.

```
python3 parameterizer.py <input-folder>
```

Example:

```
python3 parameterizer.py Desktop/Input
```

---

# Example

### Input Folder

```
Desktop/Input
    incident_ingestion.json
    alert_enrichment.json
```

### After Running the Tool

```
Desktop/Input
    incident_ingestion.json
    alert_enrichment.json
    incident_ingestion_template.json
    alert_enrichment_template.json
```

Each Logic App file is converted into a **parameterized ARM template**.

---

# Transformation Example

### Original Export (Simplified)

```json
"connectionId": "/subscriptions/abc123/resourceGroups/rg/providers/Microsoft.Web/connections/azuremonitorlogs"
```

### Generated ARM Template

```json
"connectionId": "[resourceId('Microsoft.Web/connections', variables('azuremonitorlogsConnectionName'))]"
```

Environment-specific values are converted into **ARM expressions and parameters**, allowing the template to be deployed across multiple environments.

---

# How It Works

1. The CLI scans the specified directory for `.json` files.
2. Files ending with `_template.json` are skipped.
3. For each Logic App file:
   - `converter.ipynb` is executed programmatically
   - Environment-specific values are detected
   - The Logic App definition is parameterized
4. A deployable ARM template is generated and saved alongside the original file.

---

# Deployment Workflow

```
Logic App Export
        │
        ▼
Logic App JSON Definition
        │
        ▼
Parameterizer CLI
        │
        ▼
converter.ipynb Execution
        │
        ▼
Parameterized ARM Template
        │
        ▼
Reusable Cross-Environment Deployment
```

---

# Limitations

## Custom Connectors

⚠️ **Custom connectors are currently not supported.**

Logic Apps that rely on **Azure Custom Connectors (`Microsoft.Web/customApis`)** cannot be fully parameterized by this tool.

Custom connectors require:

- Existing `customApis` resources
- Correct `join/action` permissions
- Pre-configured API connections

Because of this, the tool does **not automatically handle**:

- `Microsoft.Web/customApis`
- Custom connector API IDs
- Custom connector authorization bindings

### Recommended Workflow for Custom Connectors

If your Logic App uses custom connectors:

1. Deploy the custom connector manually.
2. Create the required API connection in the target environment.
3. Update the generated ARM template to reference the existing connection.

---

# Notes

- All `.json` files in the specified directory are processed.
- Files ending with `_template.json` are skipped.
- Each Logic App file is processed independently.

---

# Troubleshooting

### Python Not Found

Verify Python installation:

```
python3 --version
```

---

### Missing Dependencies

Install required packages:

```
pip install nbconvert nbformat
```

---

### Notebook Execution Errors

Ensure the following files exist in the same directory:

```
converter.ipynb
parameterizer.py
```

---

# Future Improvements

Potential enhancements include:

- Parallel processing for large batches of Logic Apps
- Support for custom connector parameterization
- Automated ARM template validation
- Packaging as an installable Python CLI tool
- GitHub Action integration for CI deployments

---

# License

This project is provided as-is for automation and deployment tooling purposes.
