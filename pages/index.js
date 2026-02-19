import React from 'react';

export default function Home() {
  return (
    <div style={{ padding: '20px', fontFamily: 'sans-serif' }}>
      <h1>Welcome to Date Calculator</h1>
      <p>This is a Next.js application.</p>
      <nav>
        <ul style={{ listStyle: 'none', padding: 0 }}>
          <li><a href="/about">About</a></li>
          <li><a href="/contact">Contact</a></li>
          <li><a href="/privacy">Privacy Policy</a></li>
          <li><a href="/terms">Terms of Service</a></li>
        </ul>
      </nav>
    </div>
  );
}
