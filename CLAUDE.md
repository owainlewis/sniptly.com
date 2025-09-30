# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Niva is a plain text writing tool designed to run in the browser with a minimalist UX. The goal is to provide a frustration-free plain text editing experience (avoiding issues like auto-indented bullets common in modern editors).

## Architecture

### UI Layout
- **Left Sidebar**: File list for managing documents
- **Center Panel**: Large, clean writing area with focus on typography
- **Right Sidebar**: Reserved for AI assistant (planned for v2)

### Core Features
- Simple plain text editor
- In-memory document storage
- Browser-based (no backend required initially)
- Minimal, beautiful UX with typography focus

## Development Status

This is a greenfield project. The PRD is defined in `docs/PRD.md` but implementation has not yet begun. When starting development, consider:

1. **Technology Stack**: Choose a modern web framework suitable for a text editor (e.g., React, Vue, or vanilla JS with a minimal bundle size)
2. **Storage**: Start with localStorage or IndexedDB for in-memory persistence
3. **Editor Component**: Consider using a lightweight plain text editor library or building custom to ensure true plain-text behavior without auto-formatting
4. **Typography**: Focus on readable fonts and proper spacing to create a pleasant writing experience