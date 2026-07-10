<h1 align="center">Christian H. Cooper</h1>

<p align="center">
  <em>Quant trader · visual reasoning · modified GRPO · languages from single historical books</em>
</p>

<p align="center">
  <a href="https://github.com/HarleyCoops"><img src="https://img.shields.io/badge/GitHub-HarleyCoops-181717?style=for-the-badge&logo=github" alt="GitHub"></a>
  <a href="https://huggingface.co/HarleyCooper"><img src="https://img.shields.io/badge/HuggingFace-@HarleyCooper-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black" alt="Hugging Face"></a>
  <a href="https://x.com/christiancooper"><img src="https://img.shields.io/badge/𝕏-@christiancooper-000000?style=for-the-badge" alt="X"></a>
  <a href="https://wandb.ai/christian-cooper-us"><img src="https://img.shields.io/badge/W%26B-experiments-FFBE00?style=for-the-badge&logo=weightsandbiases&logoColor=black" alt="Weights & Biases"></a>
</p>

<p align="center">
  <img src="./profile-3d-contrib/profile-night-green.svg" alt="3D Contribution Chart" width="100%"/>
</p>

<p align="center">
  <sub>I train small models to do hard reasoning — and to speak from books that almost no one still reads aloud.</sub>
</p>

---

## Now

<table>
<tr>
<td width="33%" valign="top">

**Modified GRPO → languages**  
Dakota1890 → Cree1865 → AutoScientist loops. One public-domain volume becomes grammar rules, verifiable rewards, and a community-correctable model.

</td>
<td width="33%" valign="top">

**Visual reasoning**  
[Math-To-Manim](https://github.com/HarleyCoops/Math-To-Manim) (2.4k★) — if a model can render a recursive Archimedean solid, it can probably think.

</td>
<td width="33%" valign="top">

**Place & archive**  
Fortress · MONOLITH · Alberta LiDAR · Hector’s hand · Warre & Vavasour journals — terrain and ink as first-class data.

</td>
</tr>
</table>

---

# Visual Reasoning

<p align="center">
  <a href="https://github.com/HarleyCoops/Math-To-Manim">
    <img src="https://raw.githubusercontent.com/HarleyCoops/Math-To-Manim/main/docs/assets/r1-pythagorean-tweet.gif" alt="Math-To-Manim Pythagorean animation" width="88%"/>
  </a>
</p>

<p align="center">
  <b><a href="https://github.com/HarleyCoops/Math-To-Manim">Math-To-Manim</a></b> — text & images → epic math/physics animations & study notes<br/>
  <sub><code>Manim</code> · <code>visual eval</code> · <code>code-gen reasoning</code> · <a href="https://github.com/HarleyCoops/KimiK2Manim">KimiK2Manim</a></sub>
</p>

<table>
<tr>
<td width="50%" align="center" valign="top">

<a href="https://github.com/HarleyCoops/Math-To-Manim">
  <img src="https://raw.githubusercontent.com/HarleyCoops/Math-To-Manim/main/docs/assets/mythos-qft-vertex.png" alt="Mythos QFT vertex diagram" width="100%"/>
</a>

**Recursive geometry as eval**  
The [62-face recursive rhombicosidodecahedron](https://github.com/HarleyCoops/Math-To-Manim) is the stress test: nested polyhedra, exact coordinates, render-or-fail. Most LLMs die on the math alone.

</td>
<td width="50%" align="center" valign="top">

<a href="https://github.com/HarleyCoops/Math-To-Manim">
  <img src="https://media.githubusercontent.com/media/HarleyCoops/HarleyCoops/main/Public/volatility_surface.gif" alt="Black-Scholes volatility surface" width="100%"/>
</a>

**Black-Scholes volatility surface**  
The smile exotic desks actually trade against — CFA intuition rendered as motion, not a static chart.

</td>
</tr>
</table>

<p align="center">
  <img src="https://raw.githubusercontent.com/HarleyCoops/Math-To-Manim/main/docs/assets/mythos-learns-math-to-manim.png" alt="Mythos learns Math-To-Manim" width="72%"/>
</p>

<p align="center">
  <sub>Animation as a <b>reasoning eval</b>: the model must plan geometry, write Manim, and survive the render-repair loop.</sub>
</p>

---

# Generalized Learning via Modified GRPO

The bet: **deterministic, compositional rewards** beat vague LLM-as-judge loops for qualitative tasks — especially when the “ground truth” is a single historical book.

```text
one public-domain volume
   → VLM extraction (preserve orthography exactly)
   → executable grammar / dictionary rules
   → thousands of verifiable RL tasks
   → modified GRPO (no LLM judge)
   → published adapter
   → community correction (the real second stage)
```

### Dakota1890 — the template

<p align="center">
  <a href="https://github.com/HarleyCoops/Dakota1890"><b>Dakota1890</b></a>
  · Riggs 1890 grammar & dictionary
  · reward = orthography + affixes + semantics
</p>

| Model | Scale | Method | Link |
|---|---|---|---|
| Qwen3-0.6B-Dakota-Grammar-RL | 0.6B | GRPO proof | [HF](https://huggingface.co/HarleyCooper/Qwen3-0.6B-Dakota-Grammar-RL) |
| Qwen3-0.6B-Dakota-Grammar-RL-400 | 0.6B | +150% reward | [HF](https://huggingface.co/HarleyCooper/Qwen3-0.6B-Dakota-Grammar-RL-400) |
| Qwen3-30B-Dakota1890 | 30B MoE | Tinker LoRA | [HF](https://huggingface.co/HarleyCooper/Qwen3-30B-Dakota1890) |
| **Qwen3.6-35B-A3B-Dakota1890-GRPO** | **35B** | **latest GRPO** | [HF](https://huggingface.co/HarleyCooper/Qwen3.6-35B-A3B-Dakota1890-GRPO) |

The model is not always right. That is not the point. It has read the 1890 book cover to cover. Descendants of Dakota speakers teach it the rest — the StoneyNakoda community-in-the-loop stage.

### Cree1865 — the generalization test

<table>
<tr>
<td width="42%" align="center" valign="top">

<a href="https://github.com/HarleyCoops/Cree1865">
  <img src="https://raw.githubusercontent.com/HarleyCoops/Cree1865/main/docs/story/title_page.png" alt="Watkins 1865 Cree dictionary title page" width="100%"/>
</a>

<sub>Watkins 1865 — *A Dictionary of the Cree Language*</sub>

</td>
<td width="58%" valign="top">

<a href="https://github.com/HarleyCoops/Cree1865">
  <img src="https://raw.githubusercontent.com/HarleyCoops/Cree1865/main/docs/story/source_contact_sheet.png" alt="Contact sheet of Watkins 1865 pages" width="100%"/>
</a>

**Hypothesis:** one historical volume is enough to bootstrap a correctable low-resource model.

- Base: `Qwen3-30B-A3B` + LoRA  
- ~19.5k dictionary entries → ~38k RL tasks  
- Deterministic Cree reward ledger (exact / containment / orthography / F1 / length)  
- Live run: [W&B `hda2wqhl`](https://wandb.ai/christian-cooper-us/thinking-machines-qwen3-30b/runs/hda2wqhl)  
- Artifacts: [model](https://huggingface.co/HarleyCooper/Cree1865) · [Space](https://huggingface.co/spaces/HarleyCooper/Cree1865-Tinker-Inference)

</td>
</tr>
</table>

### AutoScientist loops

Recursive data ↔ model cycles on the Dakota seed (private contest workspace).  
Seed → Adaption upload → cycle manifest → deterministic QA harness → public release artifacts — show the **loop**, not only a chatbot.

Also in the GRPO family: [StoneyNakoda](https://github.com/HarleyCoops/StoneyNakoda) · [smolThinker-.5B](https://github.com/HarleyCoops/smolThinker-.5B) · [OneShotAquaRAT](https://github.com/HarleyCoops/OneShotAquaRAT) · [Qwen3-RailroadEngineer1959-RL](https://github.com/HarleyCoops/Qwen3-RailroadEngineer1959-RL)

---

# Place, Terrain & Handwriting

Archival intelligence for the Canadian Rockies — maps that fly, journals that speak, places that reveal their people.

<table>
<tr>
<td width="50%" align="center" valign="top">

### Alberta LiDAR
<a href="https://lidar-eight.vercel.app"><img src="https://img.shields.io/badge/Live_Demo-lidar--eight.vercel.app-22c55e?style=for-the-badge" alt="LiDAR demo"></a>

Map-driven LiDAR / DEM visualizer — pick a region, pull OpenTopography elevation, render multi-layer 3D terrain.

[Live demo](https://lidar-eight.vercel.app) · [lidar2](https://github.com/HarleyCoops/lidar2) · [contour](https://github.com/HarleyCoops/contour)

<sub><code>Three.js</code> · <code>OpenTopography</code> · <code>flyable topo</code></sub>

</td>
<td width="50%" align="center" valign="top">

### Warre & Vavasour
<a href="https://harleycoops.github.io/wv-archival/"><img src="https://img.shields.io/badge/Live-wv--archival-0ea5e9?style=for-the-badge" alt="WV archival"></a>

Archival transcription dossiers and flyable map films for the Warre & Vavasour journals.

[Live site](https://harleycoops.github.io/wv-archival/) · [wv-archival](https://github.com/HarleyCoops/wv-archival)

<sub><code>archival dossiers</code> · <code>map films</code></sub>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### MONOLITH + FORTRESS
Private research line: **MONOLITH** is a real-DEM terrain engine (Emerald Lake default, 1902/1921 historic sheet overlays, align-by-click georef). **FORTRESS** is the place-first Whyte Museum pipeline for Fortress Mountain / Kananaskis — location → archives → artifacts → people → story clusters.

<sub>Repos are private today — no public Pages deploy yet.</sub>

</td>
<td width="50%" valign="top">

### Hector’s handwriting
Private HTR line on Sir James Hector’s **1858 Kicking Horse** field journals (Palliser / MS-0443): VLM draft → human gold → TrOCR / Qwen3-VL LoRA → CER/WER. Public companion is the Warre & Vavasour site above.

<sub>Hector1858 + GenericOCR remain private while rights/gold-set work continues.</sub>

</td>
</tr>
</table>

---

# Hugging Face

<p align="center">
  <a href="https://huggingface.co/HarleyCooper"><img alt="Hugging Face" src="https://img.shields.io/badge/HuggingFace-17_models_·_8_datasets_·_Spaces-FFD21E?logo=huggingface&logoColor=black&style=for-the-badge"></a>
</p>

| Artifact | What it is |
|---|---|
| [`Qwen3.6-35B-A3B-Dakota1890-GRPO`](https://huggingface.co/HarleyCooper/Qwen3.6-35B-A3B-Dakota1890-GRPO) | Latest Dakota GRPO endpoint |
| [`Cree1865`](https://huggingface.co/HarleyCooper/Cree1865) | Watkins 1865 Cree adapter |
| [`Qwen3-0.6B-Dakota-Grammar-RL`](https://huggingface.co/HarleyCooper/Qwen3-0.6B-Dakota-Grammar-RL) | Tiny-model grammar proof |
| [`nanochat-AquaRat`](https://huggingface.co/HarleyCooper/nanochat-AquaRat) | Algebraic reasoning RL |
| [`Qwen.5B-OpenR1Math`](https://huggingface.co/HarleyCooper/Qwen.5B-OpenR1Math) | Open-R1 style math, 0.5B |
| [`dakota-bilingual-qa`](https://huggingface.co/datasets/HarleyCooper/dakota-bilingual-qa) | Dakota–English QA seed |
| [`synthetic_stoney_data`](https://huggingface.co/datasets/HarleyCooper/synthetic_stoney_data) | 68.8k Stoney rows |
| [`Cree1865-Tinker-Inference`](https://huggingface.co/spaces/HarleyCooper/Cree1865-Tinker-Inference) | Live Cree sampler Space |

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

base = "Qwen/Qwen3-30B-A3B-Instruct-2507"
adapter = "HarleyCooper/Cree1865"

model = AutoModelForCausalLM.from_pretrained(base, device_map="auto", torch_dtype="auto")
tok = AutoTokenizer.from_pretrained(base)
model = PeftModel.from_pretrained(model, adapter)
```

---

# Tape

<!-- NEWS:START -->
| Category | Date | Headline |
|----------|------|----------|
| Market | Jul 09, 2026 | [Kevin Warsh names members of his Federal Reserve task forces, including Marc Andreessen, Doug McM...](https://www.cnbc.com/2026/07/09/kevin-warsh-names-members-of-his-federal-reserve-task-forces-including-marc-andreessen-doug-mcmillon.html) |
| Market | Jul 10, 2026 | [Prediction markets spark insider trading concerns. Here's how Goldman and other companies are res...](https://www.cnbc.com/2026/07/09/prediction-markets-spark-insider-trading-fears-how-firms-are-responding.html) |
| Market | Jul 09, 2026 | [Kalshi traders think gas prices will stay higher for longer as U.S.-Iran tensions heat back up](https://www.cnbc.com/2026/07/09/kalshi-traders-see-higher-gas-prices-lasting-through-election-day.html) |
| Market | Jul 09, 2026 | [Goldman Sachs wins $70 billion in asset management deals with Verizon, Lockheed Martin](https://www.cnbc.com/2026/07/09/goldman-sachs-asset-management-deals-verizon-lockheed-martin.html) |
| Market | Jul 08, 2026 | [Michael Burry bets on sportsbooks DraftKings and Flutter, sees prediction markets curbed by regul...](https://www.cnbc.com/2026/07/08/michael-burry-bets-on-sportsbooks-draftkings-flutter.html) |
| Finance | Jul 10, 2026 | [Investors sell longer-dated AI debt amid Big Tech borrowing spree](https://www.ft.com/content/28380abc-72f9-4287-8d36-2823c73358ce) |
| Finance | Jul 10, 2026 | [SK Hynix’s US shares jump 14% on Nasdaq debut](https://www.ft.com/content/33133a86-925e-4395-9f60-35e2a4052500) |
| Finance | Jul 10, 2026 | [All you never wanted to know about corporate bond market issuance](https://www.ft.com/content/47a66129-548e-45c6-8855-0691616e92da) |
| Finance | Jul 10, 2026 | [Classicist Emily Wilson: ‘Odysseus is a different kind of conman’](https://www.ft.com/content/3edbfdf4-cb20-4393-9d5d-ffc1dd241ca4) |
| Finance | Jul 10, 2026 | [How an ex-Democrat became the face of Trump’s retribution agenda](https://www.ft.com/content/8f24f3a4-2c7c-4288-8e11-711500be427b) |

<!-- NEWS:END -->

---

<p align="center">
  <img src="./Public/reply.jpg" alt="Karpathy reply" height="120"/>
  &nbsp;&nbsp;
  <img src="./Public/HubleGoogleScholar.jpg" alt="Google Scholar citation" height="120"/>
</p>

<p align="center">
  <sub>
    <a href="https://x.com/christiancooper">𝕏</a> ·
    <a href="https://huggingface.co/HarleyCooper">Hugging Face</a> ·
    <a href="https://wandb.ai/christian-cooper-us">W&B</a> ·
    <a href="https://github.com/HarleyCoops/Math-To-Manim">Math-To-Manim</a> ·
    <a href="https://github.com/HarleyCoops/Dakota1890">Dakota1890</a> ·
    <a href="https://github.com/HarleyCoops/Cree1865">Cree1865</a>
  </sub>
</p>
