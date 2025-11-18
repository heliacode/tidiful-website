# Using TidiFul Welcome Email Templates in n8n

This guide explains how to use the TidiFul welcome email templates with n8n's Email node.

## 📧 n8n Email Node Setup

### Option 1: Using HTML Email Node (Recommended)

1. **Add Email Node** to your workflow
2. **Select "Send Email"** action
3. **Configure Email Settings:**
   - **To:** `{{ $json.email }}` (or your user email field)
   - **Subject:** `Welcome to TidiFul - Let's Get Started!`
   - **Email Type:** HTML
   - **HTML:** Copy the entire HTML from `welcome-email.html` or `welcome-email-compact.html`

### Option 2: Using HTML Template with Variables

For better personalization, you can use n8n's expression syntax:

#### Subject Line
```
Welcome to TidiFul, {{ $json.firstName }}! 🚀
```

#### HTML Body with Variables
Replace in the template:
- `Hi there,` → `Hi {{ $json.firstName }},`
- Add dynamic content based on user data

## 🔧 Template Variables for n8n

### Available Variables
- `{{ $json.email }}` - User's email address
- `{{ $json.firstName }}` - User's first name
- `{{ $json.lastName }}` - User's last name
- `{{ $json.accountType }}` - Plan type (Starter, Professional, Enterprise)
- `{{ $json.signupDate }}` - Date they signed up

### Example Personalization

In the HTML template, replace:
```html
<p style="margin: 0 0 20px 0; font-size: 16px; color: #333333;">Hi there,</p>
```

With:
```html
<p style="margin: 0 0 20px 0; font-size: 16px; color: #333333;">Hi {{ $json.firstName }},</p>
```

## 📋 Complete n8n Workflow Example

### Workflow Structure
```
1. Trigger (Webhook/Manual/Cron)
   ↓
2. Get User Data (Database/API)
   ↓
3. Set Template Variables (Set Node)
   ↓
4. Send Welcome Email (Email Node)
   ↓
5. Log Success (Optional)
```

### Set Node Configuration
Create a Set node before the Email node to prepare data:

```json
{
  "firstName": "{{ $json.first_name }}",
  "email": "{{ $json.email }}",
  "accountType": "{{ $json.plan }}",
  "signupDate": "{{ $json.created_at }}"
}
```

### Email Node Configuration

**Basic Settings:**
- **Connection:** Your SMTP/Email service connection
- **From Email:** `noreply@tidiful.com` or `hello@tidiful.com`
- **From Name:** `TidiFul Team`
- **To Email:** `{{ $json.email }}`
- **Subject:** `Welcome to TidiFul, {{ $json.firstName }}! 🚀`

**HTML Content:**
- Copy the entire HTML from `welcome-email.html`
- Replace static text with n8n expressions where needed

## 🎯 Recommended n8n Workflow

### Trigger: New User Signup
```javascript
// When a new user signs up, trigger this workflow
{
  "userId": "123",
  "email": "user@example.com",
  "firstName": "John",
  "lastName": "Doe",
  "plan": "Starter"
}
```

### Email Node HTML (with n8n expressions)
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f5f5f5;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f5f5f5; padding: 20px 0;">
        <tr>
            <td align="center">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="max-width: 600px; background-color: #ffffff; border-radius: 8px;">
                    <tr>
                        <td style="background-color: #10b981; padding: 30px 20px; text-align: center;">
                            <h1 style="margin: 0; color: #ffffff; font-size: 28px; font-weight: bold;">Welcome to TidiFul, {{ $json.firstName }}!</h1>
                            <p style="margin: 10px 0 0 0; color: #d1fae5; font-size: 16px;">You're all set to transform your document processing</p>
                        </td>
                    </tr>
                    <tr>
                        <td style="padding: 30px 20px;">
                            <p style="margin: 0 0 15px 0; font-size: 16px; color: #333333;">Hi {{ $json.firstName }},</p>
                            <!-- Rest of template... -->
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```

## 🔌 n8n Email Service Configuration

### SMTP Settings (if using SMTP)
- **Host:** Your SMTP server (e.g., `smtp.gmail.com`, `smtp.sendgrid.net`)
- **Port:** 587 (TLS) or 465 (SSL)
- **User:** Your SMTP username
- **Password:** Your SMTP password
- **Secure:** true

### Recommended Email Services for n8n
1. **SendGrid** - Great deliverability, easy setup
2. **Mailgun** - Developer-friendly, good analytics
3. **AWS SES** - Cost-effective for high volume
4. **Gmail SMTP** - Simple for testing (not recommended for production)

## 📝 Template Customization for n8n

### Dynamic Account Type Message
Add conditional content based on plan:

```html
{{#if (eq $json.accountType "Enterprise")}}
<p style="margin: 0 0 15px 0; font-size: 16px; color: #333333;">
    As an Enterprise customer, you have access to priority support and unlimited processing!
</p>
{{/if}}
```

Note: n8n uses JavaScript expressions, not Handlebars. Use:
```javascript
{{ $json.accountType === "Enterprise" ? "You have priority support!" : "Welcome to TidiFul!" }}
```

### Conditional Content with n8n Expressions
Use n8n's expression syntax for conditionals:

```html
<p style="margin: 0 0 15px 0; font-size: 16px; color: #333333;">
    {{ $json.accountType === "Enterprise" ? "As an Enterprise customer, you have access to priority support!" : "Welcome to TidiFul!" }}
</p>
```

## 🚀 Quick Start Checklist

- [ ] Set up email service connection in n8n
- [ ] Copy HTML template to Email node
- [ ] Configure recipient email field
- [ ] Add personalization variables
- [ ] Test with sample data
- [ ] Verify email delivery
- [ ] Check email rendering in multiple clients
- [ ] Set up error handling
- [ ] Add logging/monitoring

## 🧪 Testing in n8n

1. **Manual Test:**
   - Use "Execute Workflow" button
   - Provide test data in JSON format
   - Check execution log for errors

2. **Test Data:**
```json
{
  "email": "test@example.com",
  "firstName": "Test",
  "lastName": "User",
  "accountType": "Starter",
  "signupDate": "2025-01-15"
}
```

3. **Verify:**
   - Email is sent successfully
   - HTML renders correctly
   - Links work properly
   - Images load (if using)

## 🔄 Workflow Automation Ideas

### Delayed Welcome Email
- Trigger: User signup
- Wait: 1 hour (let them explore first)
- Action: Send welcome email

### Follow-up Sequence
- Day 1: Welcome email
- Day 3: Feature highlights email
- Day 7: Success tips email

### Conditional Sending
- Only send if user hasn't logged in after 24 hours
- Skip if user already received welcome email
- Different templates for different plan types

## 📊 Monitoring & Analytics

### Track Email Events
- Add tracking pixels (if needed)
- Monitor open rates
- Track click-through rates
- Log email delivery status

### Error Handling
- Catch email sending failures
- Retry logic for failed sends
- Alert on repeated failures
- Log errors for debugging

## 🎨 Template Files for n8n

Use these templates:
- **`welcome-email-compact.html`** - Recommended for n8n (simpler, more reliable)
- **`welcome-email.html`** - Full-featured version (if you need richer formatting)

## 💡 Tips for n8n

1. **Store templates in n8n's Code node** for easier management
2. **Use n8n's HTML node** to inject variables into templates
3. **Test with Execute Workflow** before activating
4. **Use n8n's error workflow** to handle failures
5. **Monitor execution history** for debugging

## 🔗 Related Resources

- [n8n Email Node Documentation](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.email/)
- [n8n Expression Syntax](https://docs.n8n.io/code/expressions/)
- [n8n Workflow Examples](https://n8n.io/workflows/)

---

**Need Help?** Check n8n's documentation or contact TidiFul support for template customization assistance.

