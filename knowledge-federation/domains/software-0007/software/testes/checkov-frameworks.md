---
id: software.testes.tranche19.001308
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

# Checkov: escolher a estrutura de infraestrutura analisada

## Em uma frase
A ferramenta identifica o tipo de configuração pelo conteúdo e oferece verificações específicas para cada estrutura suportada.

## Por que importa
Limitar a análise à estrutura usada reduz ruído e evita conclusões de verificações que não se aplicam ao projeto.

## Como funciona
Declare a estrutura quando ela não for óbvia, aponte para o diretório correto e revise as verificações aplicáveis antes de adotar a ferramenta.

## Exemplo
Uma análise pode cobrir apenas os arquivos de infraestrutura declarada e ignorar os manifestos de orquestração, tratados em execução própria.

## Limites e trade-offs
Analisar diretórios que contêm dependências baixadas gera achados irrelevantes, e restringir demais deixa arquivos fora da cobertura.

## Como verificar
Liste as estruturas reconhecidas no diretório e confirme que todas as que o projeto usa estão cobertas.

## Conexões
- [[checkov-running-checks]] — Veja também: Checkov: selecionar e excluir verificações.

## Fontes
- [Checkov — repositório oficial](https://github.com/bridgecrewio/checkov) — código-fonte, verificações e documentação do projeto; consultado em 2026-10-03.
- [Checkov — Guia de uso](https://github.com/bridgecrewio/checkov/blob/master/README.md) — execução, seleção de verificações, supressões, linha de base e segredos; consultado em 2026-10-03.
