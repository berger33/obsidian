---
tipo: arvore-decisao
dominio: fundamentos
nivel: iniciante
confianca: media
ultima_verificacao: 2026-09-30
validade: volatil
fontes: []
tags: [tipo/arvore-decisao, dominio/fundamentos]
aliases: ["Controlar custos de IA"]
---
# Controlar custos de IA

## Pergunta inicial
Controlar custos de IA?

## Versão em texto
- **Muitos prompts** → [[Custos-de-tokens]]
- **Agentes cloud** → [[Custos-escondidos-de-cloud-agents]]
- **Modelos caros** → [[Model-router]]
- **RAG** → [[RAG-app]]

## Diagrama
```mermaid
flowchart TD
    A[Controlar custos de IA]
    A --> B1[Muitos prompts]
    B1 --> L1[[Custos-de-tokens]]
    A --> B2[Agentes cloud]
    B2 --> L2[[Custos-escondidos-de-cloud-agents]]
    A --> B3[Modelos caros]
    B3 --> L3[[Model-router]]
    A --> B4[RAG]
    B4 --> L4[[RAG-app]]
```

## Como usar com IA
Peça ao agente para escolher uma folha, justificar a escolha, listar premissas e apontar quais notas do vault devem ser estudadas antes de implementar.

## Conexões
- [[Home]] — voltar ao mapa geral.
- [[MOC-Fundamentos]] — conceitos transversais.
- [[Validacao-de-codigo-gerado-por-IA]] — validar qualquer caminho escolhido.
- [[Contrato-de-tarefa-para-agentes]] — transformar a decisão em tarefa.
