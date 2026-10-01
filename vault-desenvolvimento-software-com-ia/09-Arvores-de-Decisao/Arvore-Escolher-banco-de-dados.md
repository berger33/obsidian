---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Escolher banco de dados"]
---
# Escolher banco de dados

## Pergunta inicial
Escolher banco de dados?

## Versão em texto
- **Relacional** → [[PostgreSQL]]
- **Documento** → [[MongoDB]]
- **Cache** → [[Redis]]
- **Vetorial** → [[Vector-database]]

## Diagrama
```mermaid
flowchart TD
    A[Escolher banco de dados]
    A --> B1[Relacional]
    B1 --> L1[[PostgreSQL]]
    A --> B2[Documento]
    B2 --> L2[[MongoDB]]
    A --> B3[Cache]
    B3 --> L3[[Redis]]
    A --> B4[Vetorial]
    B4 --> L4[[Vector-database]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
