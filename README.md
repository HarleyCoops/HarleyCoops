<!-- Badges + counters (kept at top) -->
<p align="center">
  <a href="https://github.com/HarleyCoops"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-HarleyCoops-111827?logo=github&logoColor=white"></a>
  <a href="https://huggingface.co/HarleyCooper"><img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-HarleyCooper-ffcc4d?logo=huggingface&logoColor=111827"></a>
  <a href="https://wandb.ai/christian-cooper-us"><img alt="Weights & Biases" src="https://img.shields.io/badge/Weights%20%26%20Biases-christian--cooper--us-FFBE00?logo=weightsandbiases&logoColor=111827"></a>
  <a href="https://linkedin.com/in/christianhcooperus"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Christian%20H.%20Cooper-0a66c2?logo=linkedin&logoColor=white"></a>
  <a href="https://twitter.com/christiancooper"><img alt="X / Twitter" src="https://img.shields.io/badge/X-christiancooper-111827?logo=x&logoColor=white"></a>
  <a href="https://kaggle.com/christianhcooper"><img alt="Kaggle" src="https://img.shields.io/badge/Kaggle-christianhcooper-20BEFF?logo=kaggle&logoColor=111827"></a>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=harleycoops&label=Profile%20views&color=d97757&style=flat" alt="Profile views" />
  <img src="https://img.shields.io/github/followers/HarleyCoops?label=Followers&style=flat&color=111827&logo=github" alt="GitHub followers" />
  <img src="https://img.shields.io/github/stars/HarleyCoops?label=Total%20stars&style=flat&color=111827&logo=github" alt="Total GitHub stars" />
  <img src="https://img.shields.io/badge/Public%20repos-700%2B-d97757" alt="More than 700 public repos" />
</p>

<p align="center">
  <img src="./profile-3d-contrib/profile-season.svg" alt="3D contribution chart for HarleyCoops" width="100%" />
</p>

---

## The Short Version

I'm Christian H. Cooper, an **ML engineer working on low-resource language models, reinforcement learning, and agent harnesses**. My main research line is **Dakota and Cree**: turning historical grammars and dictionaries into extracted data, verifiable tasks, reward functions, and models that can be evaluated and corrected.

I also build **[Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim)**, where a mathematical question becomes a visual explanation, and **WorkspaceAlberta Harness**, which connects AI tools to practical work for Canadian businesses and skilled trades. Across these projects, I work on the whole loop: prepare the data, build the system, inspect its failures, and measure what improves.

<table>
  <tr>
    <td align="center" width="20%"><strong>700+</strong><br/>public repos</td>
    <td align="center" width="20%"><strong>2,400+</strong><br/>stars on Math-To-Manim</td>
    <td align="center" width="20%"><strong>17 / 7 / 8</strong><br/>HF models, datasets, Spaces</td>
    <td align="center" width="20%"><strong>82M+</strong><br/>tokens through one GRPO run</td>
    <td align="center" width="20%"><strong>Dakota + Cree</strong><br/>low-resource language research</td>
  </tr>
</table>

**The engineering behind the projects:**

- **Model training & fine-tuning** — GRPO post-training and LoRA experiments on Tinker and Prime Intellect, with model cards, checkpoints, and training logs on Hugging Face and W&B.
- **Data labeling & dataset engineering** — VLM extraction from archival scans, orthography-preserving labeling, synthetic Q&A expansion, structural holdouts, hash-addressed dataset artifacts with citations intact.
- **Reward/verifier design** — grammar-derived checks with separate orthography, morphology, and reference-matching scores, so a change in reward can be traced to the scoring code.
- **Visualization that explains** — Manim render pipelines, RL training-curve dashboards, LiDAR terrain viewers.

---

## The Movie Wall — Math-To-Manim

**Ask a question → get a visual explanation.** Math-To-Manim works backward through prerequisites, builds a teaching sequence, checks the mathematics, and turns it into a Manim scene for rendering and review.

I started it on the morning of **January 20, 2025**, the day DeepSeek-R1 was released. The [first project commit](https://github.com/HarleyCoops/Math-To-Manim/commit/09a2f22ec02b0374d38373d28f76c5764a1e9a2e) records 04:24 Mountain Time. GRPO made me think about recursive self-reasoning: could a system check intermediate results and use that feedback to improve its next attempt? Math-To-Manim gave me something concrete to test. [R1's release record](https://huggingface.co/deepseek-ai/DeepSeek-R1/commit/5a56bdbde75a16bdfbf3a8e9c852be3dfcfb8eef) marks the same day.

<table>
  <tr>
    <td width="33%">
      <a href="https://github.com/HarleyCoops/Math-To-Manim">
        <img src="./Public/mtm-traitor-axis.gif" alt="The Traitor Axis — Dzhanibekov T-handle tumbling, RK4-integrated Euler equations, polhode loops on the angular-momentum sphere" width="100%" />
      </a>
      <p align="center"><strong>The Traitor Axis</strong><br/>Rigid-body chaos from RK4 integration — predicted flip at 3.4 s, simulated at 3.5 s.</p>
    </td>
    <td width="33%">
      <a href="https://github.com/HarleyCoops/Math-To-Manim/tree/main/docs/showcase">
        <img src="./Public/mtm-last-day.gif" alt="The Last Day — one continuous 3D take from eigenmodes through torus, helicoid, catenoid, to a Lorenz attractor" width="100%" />
      </a>
      <p align="center"><strong>The Last Day</strong><br/>One continuous 3D take: sphere → torus → helicoid → catenoid → Lorenz.</p>
    </td>
    <td width="33%">
      <a href="https://github.com/HarleyCoops/Math-To-Manim/tree/main/docs/showcase">
        <img src="./Public/mtm-vortex.gif" alt="Vortex Leapfrog — two vortex rings leapfrogging, simulated live by Biot-Savart integration" width="100%" />
      </a>
      <p align="center"><strong>Vortex Leapfrog</strong><br/>Two rings leapfrogging, simulated live by Biot-Savart integration.</p>
    </td>
  </tr>
  <tr>
    <td width="33%">
      <img src="./Public/mtm-rhombi.gif" alt="Rhombicosidodecahedron rotating" width="100%" />
      <p align="center"><strong>Archimedean solids</strong></p>
    </td>
    <td width="33%">
      <img src="./Public/mtm-lorenz.gif" alt="Lorenz attractor drawing itself" width="100%" />
      <p align="center"><strong>Lorenz attractor</strong></p>
    </td>
    <td width="33%">
      <img src="./Public/vol-surface.gif" alt="Animated options volatility surface" width="100%" />
      <p align="center"><strong>Volatility surface</strong> — options intuition in motion</p>
    </td>
  </tr>
</table>

<p align="center">
  <a href="https://github.com/HarleyCoops/Math-To-Manim"><img alt="Math-To-Manim" src="https://img.shields.io/badge/Math--To--Manim-2.4k%20stars-d97757?logo=github&logoColor=white"></a>
  <a href="https://github.com/HarleyCoops/KimiK3Manim"><img alt="KimiK3Manim" src="https://img.shields.io/badge/KimiK3Manim-agent%20swarm%20renders-111827"></a>
  <a href="https://github.com/HarleyCoops/Math-To-Manim/tree/main/docs/showcase"><img alt="Full showcase" src="https://img.shields.io/badge/Full%20motion%20showcase-30%2B%20films-0ea5e9"></a>
</p>

**Still in progress:** I am using Math-To-Manim as an RL experiment, turning failed scenes and repair attempts into training tasks. Cheap code checks guide rollouts; rendered frames provide slower evaluation. Inference-time revision and RL weight updates are separate steps, and I am still working on the connection between them. [Read the experiment notes](https://github.com/HarleyCoops/Math-To-Manim/blob/main/docs/PRIME_INTELLECT_RL.md).

---

## The Training Lab — Dakota, Cree, and GRPO

**Can a historical language volume provide enough structure to start a useful training loop?**

[**Dakota1890**](https://github.com/HarleyCoops/Dakota1890) starts with Riggs' 1890 grammar and dictionary: preserve the orthography, extract rules, generate tasks, and score outputs against explicit constraints. The experiments have progressed from a 0.6B model to a 35B GRPO adapter.

[**Cree1865**](https://github.com/HarleyCoops/Cree1865) tests the approach on Watkins' 1865 dictionary, with synthetic bilingual Q&A, a Cree-specific verifier, and LoRA training through Tinker. Its 800-step run, model card, and inference demo are linked below.

The shared idea is **grammar as a reward function**. I log the scoring components separately to see what the model is learning and where the verifier falls short. A higher score on source-derived tasks does not establish fluency; speaker-led evaluation and correction remain the next stage I want to develop.

**Now building:** [Baguettotron-Dakota1890](https://github.com/HarleyCoops/Baguettotron-Dakota1890) connects the Dakota1890 morphology gym to a GRPO fine-tuning stack for PleIAs/Baguettotron.

One Dakota reward formulation illustrates the component breakdown; the Cree verifier uses its own rubric.

```python
reward = (
    0.4 * character_preservation +   # orthography: ŋ š ć ḣ preserved?
    0.4 * affix_accuracy +           # morphology: correct affixes applied?
    0.2 * semantic_correctness       # semantics: meaning vs. ground truth
) * difficulty_multiplier            # curriculum weight, 1.0x → 2.0x
```

<table>
  <tr>
    <td width="50%">
      <a href="https://huggingface.co/HarleyCooper/Qwen3.6-35B-A3B-Dakota1890-GRPO"><img src="./Public/wandb-qwen36-dashboard.png" alt="W&B dashboard — Dakota1890 Qwen3.6-35B GRPO run, reward channels restored" width="100%" /></a>
      <p align="center"><strong>Qwen3.6-35B Dakota GRPO</strong> — 82.05M tokens, composite reward climbing, ledger audit flat at zero.</p>
    </td>
    <td width="50%">
      <a href="https://wandb.ai/christian-cooper-us"><img src="./Public/wandb-qwen36-reward.png" alt="Composite reward progression across the 35B Dakota run" width="100%" /></a>
      <p align="center"><strong>Reward progression</strong> — every channel logged per step on Weights &amp; Biases.</p>
    </td>
  </tr>
  <tr>
    <td width="50%">
      <a href="https://github.com/HarleyCoops/Qwen3-RailroadEngineer1959-RL"><img src="./Public/wandb-rr-dashboard.png" alt="Railroad Engineer 1959 RL training dashboard" width="100%" /></a>
      <p align="center"><strong>Railroad Engineer 1959</strong> — a rulebook becomes a training environment.</p>
    </td>
    <td width="50%">
      <a href="https://github.com/HarleyCoops/nanochatAquaRat"><img src="./Public/aquarat-training.png" alt="nanochat AQuA-RAT algebra reasoning training curves" width="100%" /></a>
      <p align="center"><strong>nanochat × AQuA-RAT</strong> — small-model algebra reasoning, end-to-end RL.</p>
    </td>
  </tr>
</table>

### Published model runs

| Model | Params | Method | Reported run result |
|---|---:|---|---|
| [Laguna-XS.2-Adaption-Dakota-QA-GRPO](https://huggingface.co/HarleyCooper/Laguna-XS.2-Adaption-Dakota-QA-GRPO) | XS | GRPO, Prime Hosted Training | Reward **0.283 → 0.433**, char-F1 **0.327 → 0.635** |
| [Qwen3.6-35B-A3B-Dakota1890-GRPO](https://huggingface.co/HarleyCooper/Qwen3.6-35B-A3B-Dakota1890-GRPO) | 35B | GRPO, Tinker | **82.05M tokens**, audited reward channels |
| [Cree1865](https://huggingface.co/HarleyCooper/Cree1865) | 30B-A3B | Modified GRPO, Tinker | 800-step synthetic-expansion run, [live W&B](https://wandb.ai/christian-cooper-us/thinking-machines-qwen3-30b/runs/hda2wqhl) |
| [Qwen3-4B-RailRoadEngineer1959](https://huggingface.co/HarleyCooper/Qwen3-4B-RailRoadEngineer1959) | 4B | LoRA, volume2gym lineage | Rulebook-compiled task families |
| [Qwen3-0.6B-Dakota-Grammar-RL-400](https://huggingface.co/HarleyCooper/Qwen3-0.6B-Dakota-Grammar-RL-400) | 0.6B | GRPO, Prime Intellect | 400 steps, **+150% reward**, 97.9% morphology accuracy |
| [nanochat-AquaRat](https://huggingface.co/HarleyCooper/nanochat-AquaRat) | nano | RL, AQuA-RAT | GSM8K-style → multiple-choice algebra |

<p align="center">
  <a href="https://github.com/HarleyCoops/Math-To-Manim"><img src="https://github-readme-stats.vercel.app/api/pin/?username=harleycoops&repo=Math-To-Manim&theme=react&hide_border=true" alt="Math-To-Manim GitHub card" /></a>
  <a href="https://github.com/HarleyCoops/Dakota1890"><img src="https://github-readme-stats.vercel.app/api/pin/?username=harleycoops&repo=Dakota1890&theme=react&hide_border=true" alt="Dakota1890 GitHub card" /></a>
</p>
<p align="center">
  <a href="https://github.com/HarleyCoops/volume2gym"><img src="https://github-readme-stats.vercel.app/api/pin/?username=harleycoops&repo=volume2gym&theme=react&hide_border=true" alt="volume2gym GitHub card" /></a>
  <a href="https://github.com/HarleyCoops/Cree1865"><img src="https://github-readme-stats.vercel.app/api/pin/?username=harleycoops&repo=Cree1865&theme=react&hide_border=true" alt="Cree1865 GitHub card" /></a>
</p>

---

## Data Labeling & Dataset Engineering — Book → Gym → Model

[**volume2gym**](https://github.com/HarleyCoops/volume2gym) develops the broader engineering idea: turn structured source material into cited knowledge units, training tasks, and executable checks. It supports six task families, grouped holdouts, reward ledgers, and SFT/GRPO exports, with hashes that make changes to artifacts detectable.

| Task family the compiler emits | What it tests |
|---|---|
| `standard_operation` | Correct ordinary application |
| `edge_case` | Boundary conditions and missing facts |
| `conflict_resolution` | Compatible resolution of constraints |
| `exception_handling` | Exception triggers vs. normal boundaries |
| `violation_check` | Missing requirements, forbidden actions, bad order |
| `adversarial_distractor` | Rejection of plausible but unsupported instructions |

The 1959 *Consolidated Code of Operating Rules* lineage: **536 extracted rules → 2,708 scenarios** → gym → [Qwen3-4B adapter](https://huggingface.co/HarleyCooper/Qwen3-4B-RailRoadEngineer1959) → [Rule 99 contract fixture](https://huggingface.co/datasets/HarleyCooper/volume2gym-railroad-1959) on Hugging Face.

### Labeled datasets on the Hub

| Dataset | What it is | Shape |
|---|---|---|
| [adaption-dakota-english-qa](https://huggingface.co/datasets/HarleyCooper/adaption-dakota-english-qa) | Remastered Dakota–English QA for instruction tuning & GRPO | 1,953 examples |
| [dakota-bilingual-qa](https://huggingface.co/datasets/HarleyCooper/dakota-bilingual-qa) | Bilingual QA pairs from the 1890 dictionary | 2,445 examples, train/val |
| [volume2gym-railroad-1959](https://huggingface.co/datasets/HarleyCooper/volume2gym-railroad-1959) | Rule 99 artifact-contract fixture with ledgers | 6 train / 1 held-out |

<p align="center">
  <img src="./Public/research-map.svg" alt="Research and build map connecting sources, datasets, model runs, and public demos" width="100%" />
</p>

---

## The Archive — The Sources Behind Dakota and Cree

The scans are part of the engineering problem. Diacritics, variant spellings, and dictionary direction matter when text becomes training data. I use VLM extraction and synthetic Q&A to create more tasks from the relationships recorded in each source, while keeping the distinction between extracted material and generated examples.

These historical books are starting points. They cannot capture a living language on their own. The correction loop I want to build retains the prompt, the model's answer, and a speaker's correction with the context that explains the mistake.

<table>
  <tr>
    <td width="33%">
      <a href="https://github.com/HarleyCoops/Cree1865"><img src="./Public/cree-title.jpg" alt="Title page of Watkins' 1865 Dictionary of the Cree Language" width="100%" /></a>
      <p align="center"><strong>Cree1865</strong> — Watkins' 1865 dictionary, 98 pages sampled</p>
    </td>
    <td width="33%">
      <a href="https://github.com/HarleyCoops/Cree1865"><img src="./Public/cree-orthography.jpg" alt="Macro of Cree diacritical marks in 1865 letterpress" width="100%" /></a>
      <p align="center"><strong>The marks that make it Cree</strong> — diacritics as verifiable signal</p>
    </td>
    <td width="33%">
      <a href="https://github.com/HarleyCoops/Cree1865"><img src="./Public/cree-two-directions.jpg" alt="Diptych: English-to-Cree and Cree-to-English dictionary directions" width="100%" /></a>
      <p align="center"><strong>Two directions</strong> — English→Cree and Cree→English</p>
    </td>
  </tr>
  <tr>
    <td colspan="3" align="center">
      <a href="https://github.com/HarleyCoops/Dakota1890"><img src="./Public/dakota-grammar.jpg" alt="Riggs 1890 Grammar and Dictionary of the Dakota Language scan" width="50%" /></a>
      <p align="center"><strong>Dakota1890</strong> — Riggs' 1890 grammar: 1,497 rules → 10,576 verifiable tasks</p>
    </td>
  </tr>
</table>

| Project | Source volume | Public artifacts |
|---|---|---|
| [Dakota1890](https://github.com/HarleyCoops/Dakota1890) | Riggs 1890 *Grammar & Dictionary of the Dakota Language* | [Baguettotron GRPO stack](https://github.com/HarleyCoops/Baguettotron-Dakota1890) · [35B adapter](https://huggingface.co/HarleyCooper/Qwen3.6-35B-A3B-Dakota1890-GRPO) · [Laguna run card](https://huggingface.co/HarleyCooper/Laguna-XS.2-Adaption-Dakota-QA-GRPO) |
| [Cree1865](https://github.com/HarleyCoops/Cree1865) | Watkins 1865 *Dictionary of the Cree Language* | [HF model](https://huggingface.co/HarleyCooper/Cree1865) · [W&B run](https://wandb.ai/christian-cooper-us/thinking-machines-qwen3-30b/runs/hda2wqhl) · [explained dashboard](https://wandb.ai/christian-cooper-us/thinking-machines-qwen3-30b/reports/Cree1865-Synthetic-Expansion-V1-Explained-Dashboard--VmlldzoxNzM1MDY2MQ==) · [inference Space](https://huggingface.co/spaces/HarleyCooper/Cree1865-Tinker-Inference) |
| [Railroad Engineer 1959](https://github.com/HarleyCoops/Qwen3-RailroadEngineer1959-RL) | 1959 *Consolidated Code of Operating Rules* | [Qwen3-4B LoRA](https://huggingface.co/HarleyCooper/Qwen3-4B-RailRoadEngineer1959) · [dataset fixture](https://huggingface.co/datasets/HarleyCooper/volume2gym-railroad-1959) |

Handwriting and OCR lineage runs through the repo list too — [PyLaia](https://github.com/HarleyCoops/PyLaia) (handwritten document analysis), [deepseek-ocr](https://github.com/HarleyCoops/deepseek-ocr), [olmocr](https://github.com/HarleyCoops/olmocr) (PDF linearization for training data), and a reproduction of [LeCun 1989 handwritten zip-code recognition](https://github.com/HarleyCoops/lecun1989-repro) — the ancestor of all of this.

---

## WorkspaceAlberta Harness — AI for Businesses and Skilled Trades

I design **WorkspaceAlberta Harness**, a custom AI terminal that connects business context with procurement evidence from CanadaBuys and Alberta Purchasing Connection. The aim is practical: help an operator assess an opportunity and produce a useful bid brief, document, or working tool.

My work covers connectors, tool routing, persistent task state, and agent procedures that can be improved through reviewed corrections. It applies the same discipline as the training work: keep the evidence visible, distinguish missing information from a confirmed answer, and measure whether the result helps the person doing the job.

---

## Alberta Geospatial & Agent Tooling

| Project | What it shows |
|---|---|
| [lidar2](https://github.com/HarleyCoops/lidar2) | Map-driven LiDAR visualizer — OpenTopography DEM → multi-layer 3D terrain point clouds (React, Three.js, custom GLSL elevation shaders) |
| [maplibre-gl-lidar](https://github.com/HarleyCoops/maplibre-gl-lidar) | MapLibre plugin for visualizing LiDAR point clouds |
| [openArchive](https://github.com/HarleyCoops/openArchive) | Research UX over BC & Alberta archive collections |
| [AlbertaWorkspaceAgent](https://github.com/HarleyCoops/AlbertaWorkspaceAgent) | Agent-native workspace experiments for Alberta research workflows |

---

## Hugging Face Hub

<p>
  <a href="https://huggingface.co/HarleyCooper"><img alt="Hugging Face profile" src="https://img.shields.io/badge/Hugging%20Face-HarleyCooper-ffcc4d?logo=huggingface&logoColor=111827"></a>
  <a href="https://huggingface.co/models?author=HarleyCooper"><img alt="Models" src="https://img.shields.io/badge/models-17-16a34a"></a>
  <a href="https://huggingface.co/datasets?author=HarleyCooper"><img alt="Datasets" src="https://img.shields.io/badge/datasets-7-f59e0b"></a>
  <a href="https://huggingface.co/spaces?author=HarleyCooper"><img alt="Spaces" src="https://img.shields.io/badge/spaces-8-0ea5e9"></a>
</p>

| Live demos (Spaces) | Try it |
|---|---|
| [Cree1865-Tinker-Inference](https://huggingface.co/spaces/HarleyCooper/Cree1865-Tinker-Inference) | Sample from the Cree1865 training run |
| [Dakota-.6B](https://huggingface.co/spaces/HarleyCooper/Dakota-.6B) | Dakota grammar RL demo |
| [AskAboutCIL](https://huggingface.co/spaces/HarleyCooper/AskAboutCIL) | Community-in-the-loop method explainer |

## Weights & Biases

The linked training runs expose reward curves and component metrics. I use these logs to investigate failures and check whether the recorded rewards agree with the verifier.

<p>
  <a href="https://wandb.ai/christian-cooper-us"><img alt="W&B profile" src="https://img.shields.io/badge/W%26B-christian--cooper--us-FFBE00?logo=weightsandbiases&logoColor=111827"></a>
  <a href="https://wandb.ai/christian-cooper-us/thinking-machines-qwen3-30b/runs/hda2wqhl"><img alt="Cree1865 run" src="https://img.shields.io/badge/Cree1865%20run-hda2wqhl-111827"></a>
  <a href="https://wandb.ai/christian-cooper-us/dakota-rl-grammar/runs/7nikv4vp"><img alt="Dakota trainer run" src="https://img.shields.io/badge/Dakota%20trainer-7nikv4vp-111827"></a>
  <a href="https://wandb.ai/christian-cooper-us/thinking-machines-qwen3-30b/reports/Cree1865-Synthetic-Expansion-V1-Explained-Dashboard--VmlldzoxNzM1MDY2MQ=="><img alt="Explained dashboard" src="https://img.shields.io/badge/W%26B%20report-Cree1865%20explained-7c3aed"></a>
</p>

---

## Stack

<p>
  <img src="https://skillicons.dev/icons?i=python,pytorch,ts,react,threejs,docker,gcp,git&theme=dark" alt="Python, PyTorch, TypeScript, React, Three.js, Docker, GCP, Git" />
</p>
<p>
  <img src="https://img.shields.io/badge/GRPO%20%2F%20RL%20post--training-111827" alt="GRPO and RL post-training" />
  <img src="https://img.shields.io/badge/Transformers%20%2F%20PEFT%20%2F%20LoRA-ffcc4d?logo=huggingface&logoColor=111827" alt="Transformers, PEFT, LoRA" />
  <img src="https://img.shields.io/badge/Tinker%20%2F%20Prime%20Intellect-7c3aed" alt="Tinker and Prime Intellect training infra" />
  <img src="https://img.shields.io/badge/Weights%20%26%20Biases-FFBE00?logo=weightsandbiases&logoColor=111827" alt="Weights and Biases" />
  <img src="https://img.shields.io/badge/Manim-0ea5e9" alt="Manim" />
  <img src="https://img.shields.io/badge/VLM%20extraction%20%2F%20OCR-d97757" alt="VLM extraction and OCR" />
  <img src="https://img.shields.io/badge/Gradio-f97316" alt="Gradio" />
  <img src="https://img.shields.io/badge/LangChain%20%2F%20MCP-1f2937" alt="LangChain and MCP" />
  <img src="https://img.shields.io/badge/Quant%20Finance-0f766e" alt="Quantitative finance" />
</p>

---

## Market Wire

*Live — refreshed every 6 hours by a GitHub Action from CNBC, Reuters, and FT feeds.*

<!-- NEWS:START -->
| Category | Date | Headline |
|----------|------|----------|
| Market | Sep 25, 2026 | [Appeals court rules that states can regulate Kalshi’s sports prediction markets, dealing another ...](https://www.cnbc.com/2026/09/25/appeals-court-rules-states-can-regulate-sports-prediction-markets.html) |
| Market | Sep 25, 2026 | [Crypto platform Bitget suspects North Korea is responsible for $352 million hack](https://www.cnbc.com/2026/09/25/crypto-platform-bitget-suspects-north-korea-in-352-million-hack.html) |
| Market | Sep 25, 2026 | [China's Xi urges U.S. to cooperate on AI](https://www.cnbc.com/2026/09/25/chinas-xi-urges-us-to-cooperate-on-ai.html) |
| Market | Sep 25, 2026 | [Here's who attended the Trump-Xi state dinner](https://www.cnbc.com/2026/09/25/heres-who-is-attending-the-trump-xi-state-dinner.html) |
| Market | Sep 24, 2026 | [Philadelphia Fed's Anna Paulson says 'modest' rate moves likely ahead to tame inflation](https://www.cnbc.com/2026/09/24/philadelphia-feds-anna-paulson-says-modest-rate-moves-likely-ahead-to-tame-inflation.html) |
| Finance | Sep 25, 2026 | [Soaring bond yields ‘not even close’ to cooling red-hot US economy, investors say](https://www.ft.com/content/bcf0715b-4292-428e-80ec-e6702d430aa4?syn-25a6b1a6=1) |
| Finance | Sep 25, 2026 | [US bond sell-off pushes long-term yields to highest since 2004](https://www.ft.com/content/c5af4151-2c14-481b-8145-f5ec1f43a3f4?syn-25a6b1a6=1) |
| Finance | Sep 25, 2026 | [Bond ructions point to new danger zone in markets](https://www.ft.com/content/4acbdc1f-d898-4966-b865-924470de0066?syn-25a6b1a6=1) |
| Finance | Sep 25, 2026 | [Maga base recoils as Trump goes all-in on AI](https://www.ft.com/content/e8a815e6-a105-42ea-938e-352b8c8d5c3b?syn-25a6b1a6=1) |
| Finance | Sep 25, 2026 | [Pomp prevails over substance as Trump hosts Xi](https://www.ft.com/content/cdff194b-8106-4f71-b5b8-d0dbaf2c4d79?syn-25a6b1a6=1) |

<!-- NEWS:END -->

---

## GitHub Analytics

<details open>
  <summary><strong>Open stats dashboards</strong></summary>

  <p align="center">
    <img src="https://github-readme-streak-stats.herokuapp.com/?user=harleycoops&theme=react&hide_border=true&date_format=M%20j%5B%2C%20Y%5D" alt="GitHub streak stats" />
  </p>

  <p align="center">
    <img src="https://github-readme-stats.vercel.app/api?username=harleycoops&show_icons=true&theme=react&hide_border=true&count_private=true&include_all_commits=true" alt="GitHub stats" />
    <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=harleycoops&layout=compact&theme=react&hide_border=true&langs_count=8" alt="Top languages" />
  </p>

  <p align="center">
    <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=harleycoops&theme=github_dark" alt="GitHub profile summary card" />
  </p>

  <p align="center">
    <img src="https://github-readme-activity-graph.vercel.app/graph?username=harleycoops&theme=react-dark&hide_border=true&area=true" alt="GitHub activity graph" />
  </p>
</details>

<details>
  <summary><strong>Star history — Math-To-Manim</strong></summary>
  <p align="center">
    <a href="https://www.star-history.com/?repos=HarleyCoops%2FMath-To-Manim&type=date&legend=top-left">
      <img src="https://api.star-history.com/chart?repos=HarleyCoops/Math-To-Manim&type=date&legend=top-left" alt="Math-To-Manim star history chart" width="80%" />
    </a>
  </p>
</details>

---

## Receipts

<details>
  <summary>Small artifacts I keep around</summary>

  <p align="center">
    <img src="./Public/reply.jpg" alt="Karpathy comment screenshot" width="80%" />
  </p>

  <p align="center">
    <img src="./Public/HubleGoogleScholar.jpg" alt="Google Scholar screenshot" width="80%" />
  </p>
</details>

---

## Connect

<p align="center">
  <a href="https://github.com/HarleyCoops">GitHub</a> ·
  <a href="https://huggingface.co/HarleyCooper">Hugging Face</a> ·
  <a href="https://wandb.ai/christian-cooper-us">Weights &amp; Biases</a> ·
  <a href="https://linkedin.com/in/christianhcooperus">LinkedIn</a> ·
  <a href="https://twitter.com/christiancooper">X</a> ·
  <a href="https://kaggle.com/christianhcooper">Kaggle</a>
</p>

<p align="center"><em>Interested in low-resource language modeling, RL environments, or agent harnesses? The repos and run cards above show how I work. Get in touch if you are building in the same direction.</em></p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:d97757,50:7f1d1d,100:111827&height=120&section=footer" alt="Footer banner" width="100%" />
</p>
