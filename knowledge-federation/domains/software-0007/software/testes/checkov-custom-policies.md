---
id: software.testes.tranche19.001313
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
fontes: ["https://github.com/bridgecrewio/checkov", "https://github.com/bridgecrewio/checkov/blob/master/README.md"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Checkov: escrever políticas próprias

## Em uma frase
Políticas próprias podem ser escritas em linguagem de programação ou em formato declarativo e mantidas junto ao projeto.

## Por que importa
Convenções internas de nomenclatura, rede e criptografia não são cobertas pelas verificações genéricas e precisam de política local.

## Como funciona
Coloque as políticas em diretório versionado, aponte a execução para ele e teste cada política com casos positivos e negativos.

## Exemplo
Uma política interna pode exigir que todo recurso de armazenamento declare política de retenção conforme a regra da organização.

## Limites e trade-offs
Políticas sem teste passam a acusar configurações legítimas após mudanças no provedor, e a duplicação de verificações genéricas gera ruído.

## Como verificar
Altere um caso de teste para a forma proibida e confirme que a política própria acusa exatamente o recurso modificado.

## Conexões
- [[checkov-secrets]] — Veja também: Checkov: detectar segredos em arquivos de infraestrutura.
- [[checkov-output-and-ci]] — Veja também: Checkov: publicar o resultado na esteira.

## Fontes
- [Checkov — repositório oficial](https://github.com/bridgecrewio/checkov) — código-fonte, verificações e documentação do projeto; consultado em 2026-10-03.
- [Checkov — Guia de uso](https://github.com/bridgecrewio/checkov/blob/master/README.md) — execução, seleção de verificações, supressões, linha de base e segredos; consultado em 2026-10-03.
