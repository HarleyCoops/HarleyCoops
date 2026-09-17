# Profile strategy: industrial clients and deployment partners

Reviewed 2026-09-16 (America/Edmonton). This is the editorial plan behind the local README rewrite. No profile settings, repository pins, remote repositories, or Hub cards were changed.

## The positioning

**AI for the people who build things.**

The first screen should answer: who do you help, what can you put to work, and how does someone begin? The strongest story is the connection between onsite deployment, supported tools, reviewed harness improvements, and inspectable training research.

Suggested GitHub bio:

> Building AI workspaces for Canadian industry. Onsite terminals, custom agent harnesses, and verifiable model training. WorkspaceAlberta / Warre & Vavasour.

Suggested professional headline:

> Applied AI engineer | Industrial deployments, agent harnesses & RL | WorkspaceAlberta / Warre & Vavasour

Keep the family-doctor model of engineering support and the “Wouldn't it be great if…” invitation. Explain the concrete service before the philosophy.

## What changed in the draft

- WorkspaceAlberta now leads the page, with the procurement, harness, and setup repositories shown together.
- Business questions lead to observable outputs: an opportunity shortlist, a bid brief, a document review, or a scoped working artifact.
- The harness section explains reviewed procedure improvement separately from model-weight training.
- RailroadHarness connects the industrial direction to actual agent-training research without claiming deployment results.
- The research section uses the current railroad release and its evaluation scope, plus a compact selection of language work.
- Two animations preserve the visual identity without making a visitor scroll past a movie wall to find the business.
- Removed hardcoded repository/Hub counts, profile-view counters, duplicated badges, generic tool walls, and the financial news feed. The news workflow is manual-only in this local change.
- Contribution history remains in a collapsed section, compatible with the existing theme rotator.
- The industrial collage is copied from the existing WorkspaceAlberta checkout, credited, and explicitly historical.

## What the evidence supports

| Evidence | Source | Presentation decision |
|---|---|---|
| Procurement tools and hosted/local deployment documentation | [WorkspaceAlberta](https://github.com/HarleyCoops/WorkspaceAlberta), [deployment guide](https://github.com/HarleyCoops/WorkspaceAlberta/blob/main/docs/deployment.md) | Lead with the concrete procurement workflow. This review did not run a live customer transaction or verify production uptime. |
| Onsite terminal setup and support procedures | [Setup](https://github.com/HarleyCoops/workspaceAlbertaSetup), [support runbook](https://github.com/HarleyCoops/workspaceAlbertaSetup/blob/main/docs/tailscale-pi-remote-support.md) | Show the deployment capability. Avoid an independently verified fleet-size or customer-results claim. |
| Separate task and improvement procedures, with human review | [Harness deployment](https://github.com/HarleyCoops/workspacealberta-harness/blob/workspace-alberta/WORKSPACE_ALBERTA.md) | Describe the documented mechanism. Publishing a skill is not proof that a scheduler or fleet rollout is active. |
| Proposed training export and evaluation design | [Harness learning](https://github.com/HarleyCoops/WorkspaceAlberta/blob/main/docs/harness-learning.md) | Label further RL from authorized work traces as research. |
| OpenCode + TRL/OpenEnv training scaffold | [RailroadHarness](https://github.com/HarleyCoops/RailroadHarness) | Link as the harness-training experiment, separately from Tinker results. |
| 2,708 railroad tasks, 2,438 train / 270 test | [Dataset](https://huggingface.co/datasets/HarleyCooper/volume2gym-railroad-1959) | Replace the stale seven-row fixture description. Rule-linkage audit still has unresolved labels; do not claim complete citation coverage. |
| Held-out similarity reward 0.2493 → 0.3753; tokens/turn 255.86 → 90.08 | [Model card](https://huggingface.co/HarleyCooper/Qwen3-4B-RailRoadEngineer1959), [machine-readable summary](https://huggingface.co/HarleyCooper/Qwen3-4B-RailRoadEngineer1959/blob/main/analysis/run-summary.json) | State 270 repeated held-out scenarios, four gates, final gate at step 60. These are lexical/format measures, not industrial safety or business-outcome measures. |
| Dakota 35B adapter and 82.05M training tokens | [Model card](https://huggingface.co/HarleyCooper/Qwen3.6-35B-A3B-Dakota1890-GRPO) | Evidence of training and reward instrumentation; disclose zero exact match. |
| Laguna completed run with public metrics | [Run card](https://huggingface.co/HarleyCooper/Laguna-XS.2-Adaption-Dakota-QA-GRPO) | Describe as a run card, not downloadable adapter weights. Training reward is not held-out linguistic accuracy. |

## The biggest improvement still to make

Publish **one real, permission-cleared deployment case study**. The present public evidence is much stronger on implementation and research than on independently inspectable customer outcomes.

Use this structure:

1. **The business task:** who performs it, how often, and what makes it difficult.
2. **The previous workflow:** tools, elapsed time, human effort, and common failure.
3. **The installed workflow:** terminal, model route, connected sources, and operator handoff.
4. **A visible artifact:** a redacted brief, source links, requirements, unknowns, and the operator's decision.
5. **A measured comparison:** number of tasks, dates, baseline method, median time, correction rate, and cost per accepted artifact.
6. **What failed:** one real failure and the change that addressed it.
7. **What happened commercially:** attributable new work only when documented and permitted for publication; distinguish an opportunity from a bid, award, or paid invoice.

Do not fill these fields with projections. Choose one repeatable task and measure it before generalizing.

## Visual direction and asset plan

Use a restrained industrial palette: warm paper, charcoal, steel blue, and a small copper accent. Preserve readable text and source captions. Prefer one image per claim over many decorative images.

| Placement | Asset | Status / next action |
|---|---|---|
| Opening | Existing Foothills foundry triptych | Included as historical brand imagery, with attribution. Replace or follow with a real terminal photograph when available. |
| WorkspaceAlberta | 30–60 second terminal walkthrough | Capture a public or sanitized task from company capabilities to sources, brief, and operator correction. Label a staged example as a demonstration. |
| Deployment | Actual terminal on a desk, with clear caption | Needed. The existing hardware renders are concepts; do not present them as customer installation photographs. |
| Harness | Task → evidence → artifact → correction → review → terminal update | Included as a compact Mermaid diagram. A later demo should show a real reviewed change. |
| Research | Railroad held-out evaluation chart | Embedded from the published model card and linked to the full run. |
| Visual engineering | Two Math-To-Manim animations | Reused existing local GIFs. More films remain one click away. |

A GitHub profile should remain understandable when images fail to load. The headline, business outputs, repository map, results, and contact links are text. Keep wide research tables out of the opening screen.

## GitHub and Hugging Face cleanup

- Use the new bio and the six repositories in [PIN_PROJECTS_GUIDE.md](PIN_PROJECTS_GUIDE.md).
- Add concise About descriptions to the harness and setup repositories; their public pages currently lack them.
- On Hugging Face, curate a small industrial/procedural learning collection: railroad dataset → published Tinker adapter → RailroadHarness code. Keep language experiments in a separate collection with cross-links.
- The current Hub API returned 20 model repositories, 7 datasets, and 8 Spaces. Those are repository counts, not trained-model or working-demo counts; omit them from the headline.
- `railroad-judge-grpo-4b` currently contains only `.gitattributes`. Do not feature it as a released trained model.
- `railroad-judge-grpo-4b-smoke` has adapter files but an unfilled autogenerated model card. Add base model, method, dataset/split, run identifier, actual outcome, and limitations before featuring it.
- The current public listing does not include the old `StoneyNakoda45k` dataset or `StoneyApp` Space links. Use verified current artifacts instead.
- The checked Cree, Dakota, STONEY-1, and AskAboutCIL Spaces reported `SLEEPING`. Do not label the collection “live demos” without checking startup and performing a representative request.
- Inspect weights, documentation, and outcomes individually. A new repository or a successful upload does not prove a completed training experiment.

These settings and remote edits are recommendations; they were not applied.

## Measure whether the profile works

Use qualified deployment conversations as the main outcome. Ask incoming contacts which project or demonstration brought them in. Maintain a simple monthly record of relevant inquiries, walkthroughs, scoped pilots, and completed deployments.

For the technical case study, use task completion, evidence correctness, human corrections, median time to an accepted artifact, and cost. Report the sample size and dates. Repository activity and training-token volume belong in the supporting evidence.
