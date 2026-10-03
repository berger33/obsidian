---
id: software.devops.tranche02.000104
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/crossplane/crossplane/main/README.md", "https://github.com/crossplane/crossplane"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Tabela de versões mantidas e cronograma de End-of-Life (EOL)

## Em uma frase
A seção `Releases` do README lista as versões mantidas e próximas com suas datas de lançamento e fim de vida (EOL): `v1.20` (21 de maio de 2025, EOL em novembro de 2026), `v2.2` (18 de fevereiro de 2026, EOL em novembro de 2026), `v2.3` (21 de maio de 2026, EOL em fevereiro de 2027), `v2.4` (20 de agosto de 2026, EOL em maio de 2027), `v2.5` (novembro de 2026, EOL em agosto de 2027), `v2.6` (fevereiro de 2027, EOL em novembro de 2027) e `v2.7` (maio de 2027, EOL em fevereiro de 2028).

## Por que importa
Como o Crossplane opera continuamente no cluster reconciliando infraestrutura crítica, acompanhar a janela de manutenção trimestral evita permanecer em versões sem correções de segurança.

## Como funciona
Consulte a tabela de releases e a documentação do ciclo de lançamento (`docs.crossplane.io/knowledge-base/guides/release-cycle`) ao planejar upgrades dos clusters de control plane.

## Exemplo
Uma organização rodando `v2.2` agenda o upgrade para `v2.4` ou `v2.5` antes da janela de EOL de novembro de 2026.

## Limites e trade-offs
O processo completo de release é documentado separadamente no repositório `crossplane/release`; valide sempre as notas de versão antes de atualizar CRDs em produção.

## Como verificar
Conferi a seção Releases e a tabela de versões no README oficial de `crossplane/crossplane`.

## Conexões
- [[crossplane-get-started-and-composition-docs]] — Veja também: Ponto de partida oficial e guia de início com Composition.
- [[crossplane-v1-20-eol-and-v2-migration]] — Veja também: Fim de suporte da série v1.20 e transição para o Crossplane v2.

## Fontes
- [Crossplane — GitHub README](https://raw.githubusercontent.com/crossplane/crossplane/main/README.md) — Visão geral do Crossplane como framework de control planes cloud-native na CNCF, tabela de releases e EOL (v1.20 e v2.2–v2.7), roadmap, reuniões e 14 SIGs.; consultado em 2026-10-03.
- [Crossplane — Repositório Oficial no GitHub](https://github.com/crossplane/crossplane) — Repositório oficial do Crossplane com código-fonte, ADOPTERS.md, contributing/README.md e notas de release.; consultado em 2026-10-03.
