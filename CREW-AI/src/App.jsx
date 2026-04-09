import { useState } from 'react'
import { Activity, Beaker, FileText, Send, Loader2, HeartPulse } from 'lucide-react'

function App() {
  const [topic, setTopic] = useState('')
  const [loading, setLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)

  const generateContent = async (e) => {
    e.preventDefault()
    if (!topic.trim()) return

    setLoading(true)
    setError(null)
    setResult(null)

    try {
      const apiUrl = import.meta.env.VITE_API_URL || '';
      const response = await fetch(`${apiUrl}/api/generate`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ topic }),
      })

      if (!response.ok) {
        throw new Error('Failed to generate content')
      }

      const data = await response.json()
      setResult(data.content)
    } catch (err) {
      setError(err.message || 'Something went wrong while generating content.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="app-container">
      <div className="background-glow"></div>
      
      <header className="header">
        <div className="logo-container">
          <HeartPulse className="logo-icon" />
          <h1>MediWriters AI</h1>
        </div>
        <p className="subtitle">High-quality, verifiable healthcare content powered by CrewAI</p>
      </header>

      <main className="main-content">
        <div className="hero-card">
          <div className="card-glass">
            <h2>Generate Medical Blog</h2>
            <p>Our multi-agent system will research, write, and safely edit a comprehensive article on any healthcare topic you choose.</p>
            
            <form onSubmit={generateContent} className="input-group">
              <input
                type="text"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
                placeholder="e.g. Diabetes Management, Keto Diet, Heart Health..."
                className="topic-input"
                disabled={loading}
              />
              <button type="submit" className="generate-btn" disabled={loading || !topic.trim()}>
                {loading ? <Loader2 className="spin-icon" /> : <Send className="send-icon" />}
                {loading ? 'Generating...' : 'Generate'}
              </button>
            </form>
            
            <div className="agent-indicators">
              <div className={`agent ${loading ? 'active' : ''}`}>
                <Beaker className="agent-icon" />
                <span>Researcher</span>
              </div>
              <div className={`agent ${loading ? 'active' : ''}`}>
                <FileText className="agent-icon" />
                <span>Writer</span>
              </div>
              <div className={`agent ${loading ? 'active' : ''}`}>
                <Activity className="agent-icon" />
                <span>Editor</span>
              </div>
            </div>
          </div>
        </div>

        {error && (
          <div className="error-message">
            <p>{error}</p>
          </div>
        )}

        {result && (
          <div className="result-container">
            <div className="result-header">
              <h3>Generated Article:</h3>
              <div className="badge success">Verified Safe</div>
            </div>
            <div className="result-content markdown-body" dangerouslySetInnerHTML={{ __html: result.replace(/\n\n/g, '<br/><br/>').replace(/\n/g, '<br/>') }}>
            </div>
          </div>
        )}
      </main>
    </div>
  )
}

export default App
