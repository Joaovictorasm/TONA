
import Link from 'next/link'

export default function Home() {
  return (
    <main style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>FitNut Platform</h1>
      <p>Plataforma de acompanhamento físico e nutricional para profissionais.</p>
      <div style={{ marginTop: '2rem' }}>
        <Link href="/protocols">
          <a style={{ padding: '0.5rem 1rem', backgroundColor: '#0070f3', color: 'white', textDecoration: 'none', borderRadius: '4px' }}>
            Gerenciar Protocolos
          </a>
        </Link>
      </div>
    </main>
  )
}
