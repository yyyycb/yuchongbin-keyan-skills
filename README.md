# yuchongbin-keyan-skills

余崇斌的个人科研 Skills 合集。该仓库以 Codex Plugin 的形式组织，重点沉淀可复用、证据驱动的科研工作流。

## 当前 Skills

### `discover-research-ideas`

中文名：**有 Taste 的科研 Idea 发掘**

从获奖、高引用、高 Star 且开源的高质量工作出发，学习优秀论文背后的“研究动作”，复现并验证真实缺陷，诊断因果瓶颈，推导或迁移解决原理，最终形成可证伪、可实现、具有领域意义和论文叙事空间的候选 Idea。

显式调用：

```text
$discover-research-ideas
```

## 仓库结构

```text
.
├── .codex-plugin/
│   └── plugin.json
└── skills/
    └── discover-research-ideas/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/
        └── scripts/
```

## 本地使用

将仓库作为 Codex Plugin 安装，或把需要使用的 Skill 目录链接到本机 Codex Skills 目录。修改仓库中的 Skill 后，符号链接方式会直接使用最新源码。

本仓库用于个人科研工作流沉淀，未经许可请勿公开传播。
