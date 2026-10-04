---
id: software.seguranca.tranche17.001648
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
fontes: ["https://docs.npmjs.com/cli/v11/commands/npm-audit#calculating-meta-vulnerabilities-and-remediations", "https://github.com/npm/metavuln-calculator"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Metavulnerabilidades no npm: quando uma dependência pai só resolve para versão vulnerável

## Em uma frase
O npm calcula metavulnerabilidades quando a faixa aceita por um pacote intermediário só pode instalar versões vulneráveis de uma dependência inferior.

## Por que importa
O pacote diretamente citado pelo advisory pode não aparecer no manifest raiz, então o caminho transitivo é essencial para encontrar o dono da atualização.

## Como funciona
Leia a cadeia do relatório e descubra qual dependência pai limita a correção; atualize o pai ou aplique uma intervenção testada na resolução.

## Exemplo
Use `npm ls pacote` para encontrar quem introduz a versão vulnerável e abra uma atualização no pacote superior antes de forçar override amplo.

```text
npm audit
```

## Limites e trade-offs
A presença transitiva não prova que a funcionalidade vulnerável seja chamada, e correções podem exigir atualização coordenada de vários pais.

## Como verificar
Compare a árvore instalada antes e depois, confirme a faixa corrigida no advisory e execute testes que cubram a integração alterada.

## Conexões
- [[npm-audit-json-sarif-automacao-relatorio]] — `npm audit --json`: preservar dados estruturados para triagem automatizada.
- [[npm-audit-signatures-provenance-attestations-distincao]] — `npm audit signatures`: verificação separada de assinatura e proveniência do registry.

## Fontes
- [npm CLI v11 — metavulnerabilities](https://docs.npmjs.com/cli/v11/commands/npm-audit#calculating-meta-vulnerabilities-and-remediations) — cálculo de dependências vulneráveis por dependência transitiva vulnerável; consultado em 2026-10-04.
- [npm CLI — `@npmcli/metavuln-calculator`](https://github.com/npm/metavuln-calculator) — cálculo das metavulnerabilidades e remediações usadas pelo npm; consultado em 2026-10-04.
