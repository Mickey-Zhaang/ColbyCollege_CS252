# NumPy Practice

GitHub (code): https://github.com/Mickey-Zhaang/NumPy_Practice
Web: https://numpied.onrender.com

A browser game where you write one-line NumPy-style indexing (e.g. `arr[1,:]`, `arr[:, 2]`) to match a highlighted row, column, or submatrix. Code runs in the browser via [Pyodide](https://pyodide.org/); correctness is checked by comparing your output to the expected result.

## How it works

1. A random integer matrix is generated and a challenge region is chosen (row, column, or submatrix).
2. The highlighted region is shown; you type an expression using `arr` that would print that region.
3. You hit **Run**. Your code is executed in Pyodide with `arr` set to the matrix; the result is compared to the expected output (with normalization and numeric tolerance).
4. On success, a new round starts; a leaderboard (Supabase) tracks completed rounds.

## Tech stack

- **React 19** + **TypeScript** + **Vite**
- **Pyodide** (CDN) for in-browser Python/NumPy
- **Supabase** for anonymous play-count leaderboard
- **TanStack Query** for leaderboard fetching
- **styled-components** for UI

## Getting started

### Prerequisites

- Node.js 18+
- pnpm (or npm/yarn)

### Install and run

```bash
git clone <repository-url>
cd NumPy_Practice
pnpm install
pnpm serve
```

Open `http://localhost:5173`. Pyodide loads on first visit (first run may take a few seconds).

## Scripts

| Command                | Description                         |
| ---------------------- | ----------------------------------- |
| `pnpm serve`           | Start dev server (Vite)             |
| `pnpm build`           | TypeScript check + production build |
| `pnpm preview`         | Preview production build            |
| `pnpm lint`            | Run ESLint                          |
| `pnpm lint:fix`        | ESLint with auto-fix                |
| `pnpm format`          | Format with Prettier                |
| `pnpm format:check`    | Check formatting (CI)               |
| `pnpm storybook`       | Start Storybook on port 6006        |
| `pnpm build-storybook` | Build static Storybook              |

## Project structure

```
src/
├── components/
│   └── CodeRunner/           # Main game UI and logic
│       ├── CodeRunner.tsx    # Layout, pulses, input, output
│       ├── useCodeRunner.ts  # Matrix/challenge state, run, compare
│       ├── CodeRunner.utils.ts   # Challenge types, matrix/challenge generation
│       ├── CodeRunner.constants.ts
│       └── CodeRunnerComponents/ # Input, button, matrix display, leaderboard
├── lib/
│   ├── supabase.ts           # Supabase client
│   └── playCount.ts          # Record rounds, anonymous ID
├── App.tsx
├── main.tsx
└── index.css
```

## License

MIT — see [LICENSE](LICENSE).
