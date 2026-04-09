# Healthcare Multi-Agent Blog Generator

A full-stack application leveraging CrewAI and the Groq LLM API to automatically research, write, and safely edit high-quality healthcare blog posts.

## Architecture
- **Frontend**: React (Vite) styled with premium vanilla CSS for a "wow" aesthetic.
- **Backend**: Python Serverless Functions (FastAPI) inside the `api/` directory.
- **AI Framework**: CrewAI with 3 specialized agents: Researcher, Writer, and Editor.
- **LLM**: Groq (`mixtral-8x7b-32768`).

## Local Setup

### Frontend
1. Make sure Node.js is installed.
2. Run `npm install`
3. Run `npm run dev` to start the frontend.

### Backend
1. Ensure Python 3.9+ is installed.
2. Create a virtual environment: `python -m venv venv`
3. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
4. Install requirements: `pip install -r api/requirements.txt`
5. Start the backend locally with Uvicorn (make sure you install uvicorn: `pip install uvicorn`):
   ```bash
   uvicorn api.index:app --reload --port 8000
   ```
*(Note: If running frontend and backend locally simultaneously without Vercel CLI, you may need to configure Vite proxy in vite.config.js to point `/api` to `http://localhost:8000/api`)*

## Vercel Deployment (via GitHub)

This repository is structured optimally for **1-click Vercel Deployment**.

1. Commit and push this entire repository to GitHub.
2. Go to [Vercel](https://vercel.com/) and create a "New Project".
3. Import your GitHub repository.
4. **Important**: In the Vercel deployment settings, expand **Environment Variables** and add:
   - Name: `GROQ_API_KEY`
   - Value: `your-groq-api-key`
5. Click **Deploy**. Vercel will automatically:
   - Install Node.js dependencies and build the React app.
   - Detect the `api/` folder and install Python dependencies from `api/requirements.txt`.
   - Setup serverless functions to handle all `/api` requests correctly due to `vercel.json`.

## Testing the App
Once deployed, open the Vercel URL, type a topic like "Diabetes Management", and watch the AI multi-agent workflow generate your polished blog post!
