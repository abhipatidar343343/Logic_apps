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

# 🛠 Deployment Steps

1. Click the **Deploy to Azure** button.
2. Sign in to your Azure tenant.
3. Enter the required parameters.
4. Review and click **Create**.

---

# 🔐 Managed Identity (Important)

If the Logic App uses Azure Monitor Logs or Log Analytics:

- Ensure **System Assigned Managed Identity** is enabled.
- After deployment, go to:
  - Logic App → Identity → Turn **On** (if not already enabled).
- Assign required roles on the target Log Analytics Workspace:
  - `Log Analytics Contributor` OR
  - `Log Analytics Data Sender` (minimum required)

Without proper RBAC permissions, ingestion or query actions may fail.

---

# 🔄 Post-Deployment Actions (Required)

After deployment:

### 1️⃣ Re-authenticate Connectors
Some connectors require manual authentication after deployment:
- Open Logic App → API Connections
- Edit each connection
- Authenticate using your account

### 2️⃣ Update API Keys & Secrets
Any API keys or secrets included in the template are placeholders.

You MUST:
- Open the HTTP authentication action
- Replace:
  - `INSERT API KEY HERE`
  - `INSERT SECRET KEY HERE`
- Save the Logic App

ARM deployments reset these values to default placeholders.

---

# ⚠️ Basic Troubleshooting

### ❌ “Unauthorized” or 403 Errors
- Check Managed Identity role assignments
- Ensure workspace permissions are granted

### ❌ Connector Not Working
- Re-authenticate the connection
- Verify correct subscription & tenant

### ❌ No Data Ingested
- Verify Workspace Name & Resource Group parameters
- Confirm table exists in Log Analytics
- Check Run History for failed actions

### ❌ Deployment Succeeds but Fails at Runtime
- Validate API keys
- Check that required connectors are properly authenticated
- Confirm networking/firewall settings (if applicable)

---

# ✅ Recommended Best Practices

- Use Managed Identity instead of workspace keys wherever possible
- Avoid hardcoding secrets
- Assign least-privilege RBAC roles
- Test in a non-production resource group first

---

⚡ Always review the Logic App run history after first deployment to confirm successful execution.
