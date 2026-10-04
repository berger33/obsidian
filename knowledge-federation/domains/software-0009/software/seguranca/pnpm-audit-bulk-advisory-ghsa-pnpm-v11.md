---
id: software.seguranca.tranche17.001651
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://pnpm.io/cli/audit", "https://github.com/pnpm/pnpm/blob/main/pnpm/docs/cli/audit.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `pnpm audit` v11+: Bulk Advisory e uso de IDs GHSA

## Em uma frase
A documentação atual informa que, desde pnpm 11, `pnpm audit` consulta o endpoint Bulk Advisory e filtra advisories por identificador GHSA.

## Por que importa
Pipelines que migraram de versões antigas podem ainda armazenar CVEs na configuração, produzindo exceções que não correspondem ao formato esperado pelo client atual.

## Como funciona
Confira a versão do pnpm e substitua identificadores legados conforme o resultado atual, mantendo a URL do advisory e a justificativa junto ao ignore.

## Exemplo
Após atualizar o package manager, execute auditoria em branch e compare `More info` e a lista `audit.ignore` antes de aceitar mudanças de IDs.

## Limites e trade-offs
A ausência de CVE no payload do endpoint descrito não significa que o advisory não tenha CVE em outras bases; IDs dependem da interface consultada.

## Como verificar
Teste um advisory controlado, confirme o GHSA exibido no relatório e compare com o identificador versionado em `pnpm-workspace.yaml`.

## Conexões
- [[pnpm-audit-prod-dev-optional-dependencies-escopo]] — Delimitar `pnpm audit` por produção, desenvolvimento e dependências opcionais.

## Fontes
- [pnpm — `pnpm audit`](https://pnpm.io/cli/audit) — endpoint Bulk Advisory usado desde v11 e IDs GHSA exibidos pelo CLI; consultado em 2026-10-04.
- [pnpm — documentação versionada de `pnpm audit`](https://github.com/pnpm/pnpm/blob/main/pnpm/docs/cli/audit.md) — fonte versionada pelo projeto para o comportamento Bulk Advisory e os identificadores GHSA do CLI; consultado em 2026-10-04.
