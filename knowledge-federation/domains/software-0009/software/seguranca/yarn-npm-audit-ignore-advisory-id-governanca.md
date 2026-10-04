---
id: software.seguranca.tranche17.001668
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
fontes: ["https://yarnpkg.com/cli/npm/audit#details", "https://yarnpkg.com/configuration/yarnrc#npmAuditIgnoreAdvisories"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `--ignore` no Yarn: suprimir advisory específico com revisão recorrente

## Em uma frase
Yarn permite ignorar IDs de advisories por linha de comando ou configuração persistente, além de excluir pacotes inteiros da auditoria.

## Por que importa
Uma exceção por ID tende a ser mais estreita que ignorar pacote, mas ainda precisa de motivo e retorno para não virar supressão invisível.

## Como funciona
Use somente o identificador confirmado no relatório, registre a análise de aplicabilidade e reavalie a exceção quando a árvore ou advisory mudar.

## Exemplo
Abra um pull request que adicione um ID à configuração e inclua dono, escopo, racional técnico e data prevista para remoção.

```text
yarn npm audit --ignore 1234567
```

## Limites e trade-offs
A documentação não transforma o ignore em correção; pacotes relacionados podem continuar vulneráveis em outros advisories ou versões.

## Como verificar
Compare auditoria com e sem ignore, confirme o ID e rode uma checagem de configuração para detectar exceções sem owner.

## Conexões
- [[yarn-npm-audit-exclude-packages-false-positive-policy]] — `--exclude` no Yarn: reduzir ruído com escopo de pacote documentado.
- [[yarn-why-triagem-pacote-transitivo-origem]] — `yarn why` depois do audit: localizar quem introduziu uma dependência transitiva.

## Fontes
- [Yarn — opção `--ignore`](https://yarnpkg.com/cli/npm/audit#details) — ignorados por ID de advisory e diferença em relação a excluir pacotes; consultado em 2026-10-04.
- [Yarn — `npmAuditIgnoreAdvisories`](https://yarnpkg.com/configuration/yarnrc#npmAuditIgnoreAdvisories) — allowlist persistente de IDs de advisory; consultado em 2026-10-04.
