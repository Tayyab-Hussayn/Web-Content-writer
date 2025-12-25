# Frontend Instructions & Requirements

## Core Vision
Build a highly advanced, modern, and engaging frontend using Next.js. The design must be "wow" inducing, premium, and state-of-the-art.

## Technology Stack
- **Framework**: Next.js
- **Styling**: Vanilla CSS (preferred per user prompt) or TailwindCSS (check user preference if needed, but defaults to high-end custom CSS for "wow" factor).
- **State Management**: React Context or similar.

## Design Aesthetics
- **Theme**: Modern, vibrant, dark modes, glassmorphism.
- **Interactivity**: Smooth gradients, micro-animations, dynamic transitions.
- **Premium Feel**: Avoid generic bootstrap-like looks. Use curated color palettes and typography (Inter, Roboto, Outfit).

## Workflows & UI Requirements

### 1. Landing / Auth
- **Login/Register**:
  - Google OAuth 2.0 (One-click)
  - Email/Password
  - "Magic Link" optional
- **Hero**: Compelling introduction to the AI Content Writer.

### 2. Main Dashboard (Content Generation Flow)
- **Step 1: Image Upload**:
  - Drag & Drop zone for webpage screenshots.
  - Preview of uploaded image.
- **Step 2: Analysis Loading State**:
  - Visual feedback while "Visual Analysis" is happening (Gemini Vision).
- **Step 3: Business Context Questions**:
  - Form with 4-5 questions (Business Identity, Page Purpose, Audience, Tone).
  - Tone selector: [Professional, Friendly, Authoritative, Conversational, Inspirational].
  - Optional "Local Instructions" field.
- **Step 4: Model Selection (Paid Feature)**:
  - Dropdown to select model (Gemini vs Claude/GPT-4).
  - Show quotas/limits (Free vs Pro).
- **Step 5: Generation & Result**:
  - Display generated content in a structured format (likely editable cards or a preview of the page structure).
  - Options to Regenerate or Save.

### 3. User Settings
- **AI Instructions**:
  - Global text area (500 chars) for paid users.
- **Subscription Management**:
  - View current tier (Free/Pro).
  - Upgrade/Downgrade buttons.
  - Link to Stripe Billing Portal.

### 4. Admin Dashboard
- **Analytics**:
  - Total users, DAU, Generations count, etc.

## Technical Constraints
- **Backend API**: The frontend will consume the FastAPI backend at `/api/v1`.
- **Auth**: JWT stored in HTTP-only cookies (need proxy or BFF pattern or careful CORS handling).
- **Real-time**: Potential need for polling or WebSockets for long-running generation tasks.

## Design Directives
- **Optimization**: Fast load times, SEO optimized.
- **Responsive**: Mobile and Desktop fully supported.
