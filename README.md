# 🚀 Azure Logic Apps – Ready to Deploy

This repository contains production-ready Azure Logic App ARM templates.  
Click the **Deploy to Azure** button below to deploy directly into your Azure tenant.

---

## 📧 1) Send Incident Email

Automatically sends email notifications when an incident is triggered.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fabhipatidar343343%2FLogic_apps%2Frefs%2Fheads%2Fmain%2Fsend_incident_email.json)

---

## 🔄 2) Incident Ingestion from Izoolab to Log Analytics Workspace

Fetches incidents from Izoolab API, enriches them, checks for duplicates, and ingests them into a Log Analytics Workspace.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fabhipatidar343343%2FLogic_apps%2Frefs%2Fheads%2Fmain%2Fincident_ingestion_izoolab.json)

---

## 🛠 Deployment Steps

1. Click the **Deploy to Azure** button.
2. Sign in to your Azure tenant.
3. Enter the required parameters.
4. Review and click **Create**.

---

⚡ Ensure the required permissions are assigned before deployment (Logic App managed identity access, workspace roles, etc.).
