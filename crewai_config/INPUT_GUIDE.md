# Input Guide - How to Provide Project Requirements

## 🎯 Overview

The Elite Development Crew needs structured input to build your application. You can provide requirements in **two ways**:

1. **Interactive Mode** - Answer prompts in terminal (easiest for first-time users)
2. **File Mode** - Create a requirements file and pass it as argument (best for reusability)

---

## 🖥️ Method 1: Interactive Mode (Recommended for Beginners)

### How to Use

Simply run without arguments:

```bash
python main.py
```

The system will prompt you for each section:

```
================================================================================
ELITE SOFTWARE DEVELOPMENT CREW - PROJECT REQUIREMENTS
================================================================================

Let's define your project requirements in a structured format.
This ensures the crew has all the information needed for success.

📍 PROJECT NAME:
Enter project name: Task Management App

🎯 PURPOSE / WHY THIS EXISTS:
Describe the main goal — the outcome, not the solution.
(Enter your text. Press Enter twice when done)

Enable small teams to collaborate on projects with clear task ownership
<press Enter twice>

👤 TARGET USERS:
Who will use this? Roles, demographics, needs.
(Enter your text. Press Enter twice when done)

Project managers, software engineers, and team leads who need simple task tracking
<press Enter twice>

... and so on
```

### Interactive Mode Features

- ✅ Step-by-step guided input
- ✅ Examples provided for each section
- ✅ Default values for common settings
- ✅ Option to save your inputs to a file for reuse
- ✅ Confirmation before running (with cost estimate)

### Tips for Interactive Mode

1. **Press Enter twice** to finish multiline sections
2. **For lists**, enter one item per line, then press Enter twice
3. **Skip optional sections** by pressing Enter twice immediately
4. **Save your brief** when prompted (you can reuse it later)

---

## 📄 Method 2: File Mode (Recommended for Experienced Users)

### How to Use

Create a text file with your requirements and pass it as an argument:

```bash
python main.py my_project_brief.txt
```

### File Format

Your file should follow this structure:

```markdown
# [PROJECT NAME]

## 🎯 Purpose / Why This Exists
[Your text here]

## 👤 Target Users
[Your text here]

## 🤲 User Problem
[Your text here]

## 🏆 Success Metrics / KPIs
- Metric 1
- Metric 2
- Metric 3

## 💡 Functional Requirements
- Requirement 1
- Requirement 2
- Requirement 3

## 💭 Nice-to-Haves (Not Mandatory)
- Optional feature 1
- Optional feature 2

## ⚙ System Constraints
- Must use Next.js + Node + Prisma + PostgreSQL
- Must use secure authentication (NextAuth)
- Must support local hosting
- [Add your custom constraints]

## 🔐 Security Requirements
- Hashed passwords
- Role-based access control
- [Add more requirements]

## 🧪 Testing & Quality Requirements
- 100% critical-path coverage
- E2E tests via Playwright
- Must meet WCAG 2.1 AA
- Test coverage >80%

## 📦 Output Expectations
The crew should deliver:
- Complete project structure
- Full code implementation
- Comprehensive documentation
- Test coverage
- Quality reports
- Deployment configuration

## ❓ Open Questions (Crew Should Resolve)
- Question 1
- Question 2

## 🛠️ Technical Stack (Pre-defined)
- Frontend: Next.js 14+ (App Router, React Server Components)
- Backend: Node.js (API Routes, Server Actions)
- Database: PostgreSQL
- ORM: Prisma
- Authentication: NextAuth.js
- Testing: Jest + Playwright
- Styling: Tailwind CSS
```

### Using the Template

We've provided a complete template with examples:

```bash
# Copy the template
cp project_brief_template.txt my_project.txt

# Edit it with your favorite editor
nano my_project.txt  # or vim, code, etc.

# Run with your brief
python main.py my_project.txt
```

---

## 📋 Required Sections Explained

### 📍 PROJECT NAME
**What it is**: The name of your application

**Example**:
```
Task Management Platform
```

---

### 🎯 PURPOSE / WHY THIS EXISTS
**What it is**: The main goal and outcome (not the solution)

**Good Example**:
```
Enable small remote teams to coordinate work asynchronously without
meeting overhead, reducing confusion about task ownership and priorities.
```

**Bad Example**:
```
Build a web app for task management with React
```

**Why it matters**: Helps the Product Strategist understand the real problem to solve, not just features to build.

---

### 👤 TARGET USERS
**What it is**: Who will use this and what they need

**Good Example**:
```
- Project Managers: Need visibility into team capacity and progress
- Software Engineers: Need clear assignments without admin overhead
- Team Leads: Need to distribute work fairly and track velocity

Demographics: Remote software teams, 5-15 people per team, tech-savvy
```

**Bad Example**:
```
People who need to manage tasks
```

**Why it matters**: Shapes UX decisions, accessibility needs, and feature priorities.

---

### 🤲 USER PROBLEM
**What it is**: What users struggle with today (pain points)

**Good Example**:
```
Teams currently use multiple disconnected tools (Slack, email, spreadsheets)
to track work. This creates:
- Confusion about what's highest priority
- Duplicated effort when tasks aren't visible
- Lost context when switching between tools
- No audit trail of decisions
```

**Bad Example**:
```
They don't have a task manager
```

**Why it matters**: Ensures solutions address real pain, not imagined needs.

---

### 🏆 SUCCESS METRICS / KPIs
**What it is**: Specific, measurable goals

**Good Examples**:
```
- New users can create first task in <2 minutes
- Task completion rate increases 20% within 30 days
- Lighthouse accessibility score ≥95
- Lighthouse performance score ≥90
- 80%+ user satisfaction (NPS score)
- Zero critical security vulnerabilities
```

**Bad Examples**:
```
- Fast and easy to use
- Good performance
- Secure
```

**Why it matters**: Provides clear targets for quality gates and success measurement.

---

### 💡 FUNCTIONAL REQUIREMENTS
**What it is**: List of capabilities the system must have

**Good Examples**:
```
- User authentication via email/password and Google OAuth
- Create, edit, delete, and archive tasks
- Assign tasks to one or more team members
- Set due dates and priority levels (high/medium/low)
- Add comments to tasks with @mentions
- Attach files up to 10MB per task
- Real-time updates when tasks change
- Search tasks by text, assignee, or status
- Dashboard showing my tasks and team overview
- Email notifications for assignments and mentions
```

**Bad Examples**:
```
- Use React hooks
- Have a nice UI
- Be fast
```

**Why it matters**: Becomes the checklist for implementation and testing.

---

### 💭 NICE-TO-HAVES (Not Mandatory)
**What it is**: Optional enhancements that add value but aren't critical

**Good Examples**:
```
- Recurring task templates
- Time tracking per task
- Calendar view of due dates
- Slack integration for notifications
- Bulk edit operations
- Mobile app (PWA)
- Custom fields per workspace
- Export data to CSV
```

**Why it matters**: Helps prioritize MVP vs future enhancements. Crew may include some if time allows.

---

### ⚙ SYSTEM CONSTRAINTS
**What it is**: Technical or operational limitations

**Default (always included)**:
```
- Must use Next.js + Node + Prisma + PostgreSQL
- Must use secure authentication (NextAuth)
- Must support local hosting
```

**Additional Examples**:
```
- Must work offline for viewing cached data
- Must support 1000+ concurrent users
- Must integrate with existing LDAP for SSO
- Data must stay in EU for GDPR compliance
- Must deploy to AWS (not Azure/GCP)
- Maximum API response time: 200ms
- Mobile-first design required
```

**Why it matters**: Guides architecture decisions and technology choices.

---

### 🔐 SECURITY REQUIREMENTS
**What it is**: Security specifications beyond defaults

**Good Examples**:
```
- Passwords hashed with bcrypt (cost factor 12)
- Role-based access control (Admin, Team Lead, Member, Guest)
- Multi-factor authentication via TOTP
- Session timeout after 30 min inactivity
- Audit log for admin actions
- Rate limiting: 100 req/min per user
- Input sanitization on all endpoints
- CSRF tokens on state-changing requests
- Secure password reset with email verification
- PII data encrypted at rest (AES-256)
```

**Bad Examples**:
```
- Make it secure
- Use HTTPS
```

**Why it matters**: Ensures compliance and reduces vulnerabilities.

---

### 🧪 TESTING & QUALITY REQUIREMENTS
**What it is**: Testing standards and quality thresholds

**Default (always included)**:
```
- 100% critical-path coverage
- E2E tests via Playwright
- Must meet WCAG 2.1 AA
- Test coverage >80%
```

**Additional Examples**:
```
- Load testing for 500 concurrent users
- API performance tests (p95 < 200ms)
- Browser compatibility: Chrome, Firefox, Safari, Edge (last 2 versions)
- Mobile testing on iOS and Android
- Penetration testing checklist (OWASP)
- Code quality score >B (SonarQube)
```

**Why it matters**: Sets quality bar and ensures comprehensive testing.

---

### 📦 OUTPUT EXPECTATIONS
**What it is**: What deliverables you expect

**Default (always included)**:
```
- Complete project structure following Next.js best practices
- Full code implementation with TypeScript
- Comprehensive documentation (README, API docs, setup guides)
- Test coverage (unit, integration, E2E)
- Quality reports (accessibility, performance, security)
- Deployment configuration (Docker, CI/CD)
- Report on architectural decisions and tradeoffs
```

**Additional if needed**:
```
- Deployment scripts for AWS
- User onboarding guide
- API client library for third-party integrations
- Database migration strategy document
```

**Why it matters**: Ensures you get everything needed for production deployment.

---

### ❓ OPEN QUESTIONS (Crew Should Resolve)
**What it is**: Genuine uncertainties for the crew to decide

**Good Examples**:
```
- Should we support multiple workspaces per user account?
- What's the maximum file attachment size?
- Should task history be immutable or allow editing?
- Should we use WebSockets or polling for real-time updates?
- What's the data retention policy (keep deleted tasks?)
- Should we support guest users (view-only access)?
```

**Bad Examples**:
```
- Should we use TypeScript? (already decided in stack)
- Should we test? (already in quality requirements)
```

**Why it matters**: Crew documents decisions in ADRs, creating a knowledge trail.

---

## 🎨 Examples by Project Type

### Example 1: Simple Blog

```markdown
# Personal Tech Blog

## 🎯 Purpose / Why This Exists
Enable developers to share technical knowledge through well-formatted
articles without dealing with complex CMS platforms.

## 👤 Target Users
- Blog Author: Solo developer who wants to write and publish quickly
- Readers: Other developers looking for tutorials and insights

## 🤲 User Problem
Existing platforms (Medium, WordPress) are too heavy, have poor
markdown support, or lock in content. Developers want simple,
fast, markdown-based blogging.

## 🏆 Success Metrics / KPIs
- Author can publish new post in <5 minutes
- Page load time <1.5 seconds
- Lighthouse performance >90
- Lighthouse accessibility >95

## 💡 Functional Requirements
- Write articles in markdown with live preview
- Publish and unpublish articles
- Tag articles with categories
- Code syntax highlighting
- RSS feed generation
- SEO meta tags
- Article search

## 💭 Nice-to-Haves (Not Mandatory)
- Comment system
- Social media share buttons
- Newsletter subscription
- Analytics dashboard

## 🔐 Security Requirements
- Single admin login
- Protected admin routes
- CSRF protection

## ❓ Open Questions (Crew Should Resolve)
- Should drafts auto-save?
- Should we support series/collections of posts?
```

---

### Example 2: E-commerce Store

```markdown
# Artisan Marketplace

## 🎯 Purpose / Why This Exists
Enable small artisan businesses to sell handmade goods online
without expensive Shopify subscriptions or complex setups.

## 👤 Target Users
- Shop Owner: Small business owner, limited tech skills
- Shoppers: Consumers looking for unique handmade items

## 🤲 User Problem
Shopify costs $29-79/month. Etsy takes 6.5% fees. Both lock
in sellers and own the customer relationship.

## 🏆 Success Metrics / KPIs
- Shop owner can list first product in <10 minutes
- Checkout completion rate >70%
- Mobile conversion rate >50%
- Lighthouse performance >90
- Payment processing <3 seconds

## 💡 Functional Requirements
- Product catalog with images
- Shopping cart
- Stripe payment integration
- Order management
- Inventory tracking
- Customer accounts
- Order history
- Email receipts
- Search and filter products
- Product reviews

## 💭 Nice-to-Haves (Not Mandatory)
- Discount codes
- Abandoned cart recovery
- Gift cards
- Multi-vendor support

## 🔐 Security Requirements
- PCI compliance via Stripe
- Customer data encryption
- Secure checkout flow
- Password hashing

## ❓ Open Questions (Crew Should Resolve)
- Should we support digital products?
- What's the refund/return policy flow?
- Should shipping be calculated or flat rate?
```

---

## 💡 Pro Tips

### 1. Be Specific, Not Prescriptive

**Good**: "Users need to see real-time updates when tasks change"
**Bad**: "Use WebSockets with Socket.io for real-time"

Let the crew decide implementation. You specify the outcome.

---

### 2. Focus on Outcomes, Not Solutions

**Good**: "Reduce time to find relevant tasks from 5 minutes to 30 seconds"
**Bad**: "Add a search bar with autocomplete"

The crew might find a better solution than you imagined.

---

### 3. Include the "Why" for Requirements

**Good**: "Support offline viewing because field workers have spotty connectivity"
**Bad**: "Must work offline"

Context helps the crew make better tradeoff decisions.

---

### 4. Make Success Metrics Measurable

**Good**: "Lighthouse accessibility score ≥95"
**Bad**: "Very accessible"

Measurable metrics enable validation.

---

### 5. Don't Overspecify Nice-to-Haves

**Good**: "Email notifications for task assignments"
**Bad**: "Use SendGrid with custom templates for beautiful HTML emails with retries..."

Nice-to-haves should be simple descriptions. Crew handles the details.

---

### 6. List Real Open Questions

These should be genuine uncertainties where you'd value the crew's expertise:

**Good**:
```
- Should we allow task reassignment or require original assigner approval?
- What happens to tasks when a user is removed from the team?
- Should task comments be editable or immutable for audit purposes?
```

**Bad**:
```
- Should we use React? (already decided)
- Should we test? (always yes)
```

---

## ⚡ Quick Start Checklist

Before running the crew, ensure you have:

- [ ] Clear understanding of the user problem
- [ ] Specific success metrics (not vague goals)
- [ ] List of required functionality (not implementation)
- [ ] Security requirements identified
- [ ] Known constraints documented
- [ ] Open questions listed

---

## 🚀 Running the Crew

### Interactive Mode
```bash
python main.py
# Follow prompts, press Enter twice to finish each section
```

### File Mode
```bash
# Use the template
cp project_brief_template.txt my_project.txt
# Edit my_project.txt
python main.py my_project.txt
```

### With Custom Model
```bash
# Use GPT-3.5 for cost savings
python main.py my_project.txt --model gpt-3.5-turbo

# Use GPT-4 Turbo for better quality
python main.py my_project.txt --model gpt-4-turbo-preview
```

---

## 📞 Need Help?

If you're unsure how to fill out any section:

1. Check [project_brief_template.txt](project_brief_template.txt) for detailed examples
2. Use interactive mode - it provides guidance for each section
3. Start with the examples in this guide and adapt them
4. Remember: The crew can resolve ambiguities, so don't overthink it!

---

**Ready to build? Start with interactive mode: `python main.py`** 🚀
