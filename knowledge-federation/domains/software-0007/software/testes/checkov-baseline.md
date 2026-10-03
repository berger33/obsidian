---
id: software.testes.tranche19.001311
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-19.md"
fontes: ["https://github.com/bridgecrewio/checkov/blob/master/README.md", "https://github.com/bridgecrewio/checkov"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Checkov: separar passivo antigo de achados novos

## Em uma frase
A criação de linha de base registra os achados existentes em arquivo, e as execuções seguintes comparam contra esse registro.

## Por que importa
A linha de base permite bloquear apenas regressões em código legado sem exigir correção imediata de todo o passivo.

## Como funciona
Gere a linha de base uma única vez em execução deliberada, versione o arquivo e proíba sua atualização automática na esteira.

## Exemplo
Um repositório legado pode registrar o estado atual e passar a bloquear somente achados introduzidos por novas mudanças.

## Limites e trade-offs
Atualizar a linha de base em toda execução aceita silenciosamente novos riscos, e arquivos gerados por máquina em revisão automática perdem valor.

## Como verificar
Introduza um achado novo e confirme que a execução com linha de base falha apenas por causa dele.

## Conexões
- [[checkov-suppressions]] — Veja também: Checkov: registrar supressões com justificativa.
- [[checkov-secrets]] — Veja também: Checkov: detectar segredos em arquivos de infraestrutura.

## Fontes
- [Checkov — Guia de uso](https://github.com/bridgecrewio/checkov/blob/master/README.md) — execução, seleção de verificações, supressões, linha de base e segredos; consultado em 2026-10-03.
- [Checkov — repositório oficial](https://github.com/bridgecrewio/checkov) — código-fonte, verificações e documentação do projeto; consultado em 2026-10-03.
