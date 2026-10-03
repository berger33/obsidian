---
id: software.seguranca.tranche01.000096
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md", "https://raw.githubusercontent.com/ossf/scorecard/main/README.md", "https://github.com/ossf/scorecard"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# OpenSSF Scorecard `Signed-Releases` e `Packaging`: assinatura de artefatos, atestados de proveniência SLSA e pacotes oficiais

## Em uma frase
Os checks **`Signed-Releases`** (`Risk: High`) e **`Packaging`** (`Risk: Medium`) avaliam como o projeto constrói, empacota e publica suas versões para os usuários finais: se os pacotes são publicados a partir de workflows automatizados de CI e se as releases possuem **assinaturas criptográficas** (PGP, Minisign, Sigstore Cosign) ou **atestados de proveniência SLSA (`*.intoto.jsonl`)**.

## Por que importa
Se um mantenedor compila o binário na sua própria estação de trabalho local e faz upload manual na aba *Releases* do GitHub sem assinatura nem proveniência SLSA, não há garantia criptográfica de que aquele binário corresponde ao código-fonte público revisado.

## Como funciona
Ao integrar o gerador oficial **`slsa-framework/slsa-github-generator`** ou assinar os artefatos e imagens com **Sigstore Cosign** no workflow de release, o Scorecard verifica a presença dos arquivos `.sig`, `.pem` ou `.intoto.jsonl` nas últimas releases e atribui pontuação máxima.

## Exemplo
```bash
# Verificando os checks Signed-Releases e Packaging em um repositório:
scorecard --repo=github.com/ossf/scorecard \
  --checks=Signed-Releases,Packaging \
  --show-details
```

## Limites e trade-offs
Para alcançar SLSA Build Level 3 no GitHub Actions e nota `10/10` em `Signed-Releases`, utilize os workflows reutilizáveis isolados do projeto `slsa-framework/slsa-github-generator`.

## Como verificar
Consulte a saída de `--checks=Signed-Releases --show-details` para verificar quais releases recentes foram auditadas.

## Conexões
- [[scorecard-check-pinned-dependencies-hash-sha-imutavel-containers-actions]] — Veja também: OpenSSF Scorecard `Pinned-Dependencies`: fixação de GitHub Actions, imagens Docker e downloads por hash criptográfico SHA.
- [[scorecard-checks-sast-fuzzing-vulnerabilities-dependency-update-tool]] — Veja também: OpenSSF Scorecard Código Seguro: checks `SAST`, `Fuzzing`, `Vulnerabilities` (OSV) e `Dependency-Update-Tool`.

## Fontes
- [OpenSSF Scorecard GitHub — README.md (Automated Security Assessment for Open Source, CLI & GitHub Action, Structured Results Probes & BigQuery Dataset)](https://raw.githubusercontent.com/ossf/scorecard/main/docs/checks.md) — README oficial do ossf/scorecard cobrindo objetivos do projeto, execução via CLI/Docker/GitHub Action, sistema de Probes V5 e dataset público semanal no BigQuery; consultado em 2026-10-03.
- [OpenSSF Scorecard Official Documentation — Checks Reference (docs/checks.md: Branch-Protection 5 Tiers, Binary-Artifacts, Token-Permissions, Pinned-Dependencies & Signed-Releases)](https://raw.githubusercontent.com/ossf/scorecard/main/README.md) — Catálogo técnico oficial docs/checks.md detalhando risco, critérios de pontuação e passos de remediação de cada check do OpenSSF Scorecard; consultado em 2026-10-03.
- [OpenSSF Scorecard — Official GitHub Repository](https://github.com/ossf/scorecard) — Repositório oficial Apache-2.0 do OpenSSF Scorecard; consultado em 2026-10-03.
