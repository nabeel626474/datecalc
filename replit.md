# DateCalc - Date Difference & Age Calculator

## Overview
DateCalc is a static website that provides date calculation tools including date difference calculation and age calculation. It was originally built with Next.js and exported as static HTML/CSS/JS files.

## Project Architecture
- **Type**: Static website (pre-built Next.js export)
- **Server**: Python `http.server` for local development (`server.py`)
- **Port**: 5000 (bound to 0.0.0.0)
- **Deployment**: Static deployment serving the root directory

## Project Structure
- `index.html` - Home page with date calculator tools
- `about.html` - About page
- `contact.html` - Contact page
- `privacy.html` - Privacy policy
- `terms.html` - Terms of service
- `_next/` - Next.js static assets (JS, CSS, fonts)
- `favicon.ico` - Site favicon
- `server.py` - Development static file server with clean URL support

## Development
The development server (`server.py`) handles:
- Serving static files
- Clean URL routing (e.g., `/about` serves `about.html`)
- Cache-control headers for development
- RSC request handling

## Recent Changes
- 2026-02-19: Initial import and Replit environment setup
