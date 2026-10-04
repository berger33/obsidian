---
id: software.seguranca.tranche17.001641
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#description", "https://docs.npmjs.com/cli/v11/using-npm/config#registry"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `npm audit`: envio da descrição de dependências ao registry configurado

## Em uma frase
`npm audit` envia ao registry padrão uma descrição das dependências configuradas no projeto e solicita um relatório de vulnerabilidades conhecidas.

## Por que importa
O dado enviado e o registry escolhido são relevantes em workspaces com nomes privados ou políticas de saída de rede, além do resultado de segurança.

## Como funciona
Avalie a política do registry, o conteúdo do lockfile e o fluxo de autenticação antes de integrar a chamada em ambientes com dependências internas.

## Exemplo
Em CI corporativa, configure um registry aprovado e registre quais manifestos e lockfiles o job entrega, sem imprimir credenciais ou nomes sensíveis nos logs.

```text
npm audit
```

## Limites e trade-offs
A consulta cobre advisories conhecidos pelo serviço consultado; o resultado não detecta toda dependência maliciosa nem vulnerabilidade ainda sem advisory.

## Como verificar
Inspecione a configuração de registry do job e compare o conjunto de pacotes resolvidos com o lockfile versionado antes de compartilhar o relatório.

## Conexões
- [[npm-audit-lockfile-reprodutibilidade-package-lock]] — `package-lock.json` como entrada do `npm audit`: consistência e reprodutibilidade.

## Fontes
- [npm CLI v11 — `npm audit`](https://docs.npmjs.com/cli/v11/commands/npm-audit#description) — descrição do envio dos dados de dependências ao registry padrão; consultado em 2026-10-04.
- [npm CLI v11 — configuração `registry`](https://docs.npmjs.com/cli/v11/using-npm/config#registry) — seleção do registry padrão e configuração de autenticação/escopo; consultado em 2026-10-04.
