# Backend Development with Python & Django — A 12-Week Course

This repository contains a complete, practical backend development course
built around Python, Django, PostgreSQL, and REST APIs.

The course is designed to be **taught live**, three sessions a week, over
12 weeks, and to leave students able to build and deploy a real backend
application on their own.

## Who this is for

Beginner-to-intermediate programmers who want a structured path into
professional backend development. See `COURSE_SPEC.md` for the full
target-learner profile and prerequisites.

## How the repository is organized

```
backend-course/
├── README.md                  ← you are here
├── COURSE_SPEC.md              ← what the course is, in one place
├── LEARNING_OUTCOMES.md        ← measurable outcomes, grouped by topic
├── COURSE_ROADMAP.md           ← week-by-week plan and progression
├── TEACHING_GUIDE.md           ← how an instructor should run a session
├── ASSESSMENT.md               ← how student ability is checked
├── AI_USAGE_POLICY.md          ← how AI tools fit into the course
├── STYLE_GUIDE.md              ← how all course docs must be written
├── CONTRIBUTING.md             ← how to add or edit course content
├── docs/
│   └── audits/                 ← workload and difficulty progression reviews
├── weeks/
│   ├── 01-python-foundations/
│   │   ├── README.md           ← weekly blueprint
│   │   ├── lesson-1.md
│   │   ├── lesson-2.md
│   │   ├── lesson-3.md
│   │   └── project/            ← that week's project, spec + code
│   ├── 02-web-http-fundamentals/
│   └── ... through 12-capstone/
├── capstone/                   ← final capstone project specification
└── resources/                  ← shared reference material used across weeks
```

Each week folder is self-contained: its `README.md` explains what the week
covers and why, its three `lesson-*.md` files hold the actual teaching
content (explanations, examples, tasks, checkpoints), and its `project/`
folder holds that week's hands-on build.

There are no separate "examples" or "assignments" folders anywhere in this
repository. Exercises, demonstrations, and practice tasks live inside the
lesson files themselves, next to the concept they belong to.

## Current status

- ✅ Repository architecture and course blueprint — complete
- ✅ Weeks 1–11 — fully written: lessons, working project code, and (for
  each project involving one) an automated test pass confirming it
  actually runs, including edge cases
- ✅ Week 12 (Capstone) — specification complete by design; no lessons
  or reference solution, since the week measures independent,
  unassisted work (see `AI_USAGE_POLICY.md`, Stage 3)

## Where to start

- **Instructors**: read `COURSE_SPEC.md`, then `TEACHING_GUIDE.md`, then
  `weeks/01-python-foundations/README.md`.
- **Students**: start at `weeks/01-python-foundations/README.md`.
