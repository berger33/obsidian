---
id: software.testes.tranche22.001588
tipo: tecnica
dominio: software
subdominio: testes
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://github.com/reqnroll/Reqnroll/blob/main/README.md", "https://github.com/reqnroll/Reqnroll/blob/main/LICENSE"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Reqnroll: licença, patrocínio e linhagem

## Em uma frase
A linha de licença separa as peças: o Reqnroll para Visual Studio é licenciado sob BSD 3-Clause (copyright 2024-2026 Reqnroll), o projeto declara basear-se no framework SpecFlow e lista patrocinadores — Spec Solutions, Info Support e TestMu AI — com página própria de sponsorship.

## Por que importa
Adoção corporativa exige clareza de licença por artefato (extensão VS versus runtime NuGet) e um vetor de manutenção financiado; o README responde as duas perguntas sem rodeios.

## Como funciona
Antes de embutir o Reqnroll numa imagem interna, confira no repositório a LICENSE da versão exata que você consome e registre os termos da extensão separadamente.

## Exemplo
O badge de versão NuGet e o workflow de CI aparecem no topo do README, forma rápida de checar vitalidade antes de adotar.

## Limites e trade-offs
A numeração de copyright (2024-2026) indica o período do projeto próprio, não o do codebase herdado do SpecFlow; ao auditar proveniência, considere o histórico do fork.

## Como verificar
Abra a página de sponsorship linkada pelo README e confirme a lista de apoiadores vigente na data da sua verificação.

## Conexões
- [[reqnroll-mstest-outline]] — Veja também: Reqnroll: Scenario Outlines sob MsTest geram testes data-driven.
- [[reqnroll-setup-guides]] — Veja também: Reqnroll: por onde começar segundo o próprio projeto.

## Fontes
- [Reqnroll — README oficial](https://github.com/reqnroll/Reqnroll/blob/main/README.md) — proposta, plataformas, executores e instalação NuGet; consultado em 2026-10-03.
- [Reqnroll — arquivo LICENSE](https://github.com/reqnroll/Reqnroll/blob/main/LICENSE) — texto BSD 3-Clause citado pelo README; consultado em 2026-10-03.
